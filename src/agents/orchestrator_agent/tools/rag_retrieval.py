import os

from google.cloud.alloydb.connector import Connector
from google import genai
from google.genai import types
import sqlalchemy

# --- Config (via env vars) ---
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
REGION = os.getenv("ALLOYDB_REGION", "us-central1")
CLUSTER = os.getenv("ALLOYDB_CLUSTER", "corporate-knowledge-cluster")
INSTANCE = os.getenv("ALLOYDB_INSTANCE", "corporate-knowledge-instance")
DB_NAME = os.getenv("ALLOYDB_DATABASE", "postgres")
DB_USER = os.getenv("ALLOYDB_USER", "postgres")
DB_PASSWORD = os.getenv("ALLOYDB_PASSWORD")

INSTANCE_URI = f"projects/{PROJECT_ID}/locations/{REGION}/clusters/{CLUSTER}/instances/{INSTANCE}"
EMBEDDING_MODEL = "text-embedding-005"

_connector = Connector()


def _getconn():
    return _connector.connect(
        INSTANCE_URI,
        "pg8000",
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        ip_type="PUBLIC",
    )


_engine = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=_getconn,
)

_genai_client = genai.Client(vertexai=True, project=PROJECT_ID, location="global")


def _embed_query(text: str) -> list[float]:
    """Generates an embedding for the given text using the same model used to embed the corpus."""
    response = _genai_client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=[text],
    )
    return response.embeddings[0].values


def search_corporate_documents(query: str, top_k: int = 3) -> list[dict]:
    """Searches the internal corporate knowledge base for information relevant to the query.

    Performs semantic search over indexed corporate policy documents stored in AlloyDB,
    returning the most relevant document sections along with their source metadata
    (document ID, department, version, status, effective date) for citation purposes.

    Args:
        query: The user's question or topic to search for.
        top_k: Number of top matching document sections to return (default 3).

    Returns:
        A list of dicts, each containing: title, section, content, document_id,
        department, version, status, effective_date, and distance (lower = more relevant).
    """
    query_embedding = _embed_query(query)

    sql = sqlalchemy.text(
        """
        SELECT
            title,
            section,
            content,
            document_id,
            department,
            version,
            status,
            effective_date,
            embedding <=> (:query_embedding)::vector AS distance
        FROM knowledge_documents
        ORDER BY embedding <=> (:query_embedding)::vector
        LIMIT :top_k
        """
    )

    with _engine.connect() as conn:
        rows = conn.execute(
            sql,
            {"query_embedding": str(query_embedding), "top_k": top_k},
        ).mappings().all()

    results = []
    for row in rows:
        row_dict = dict(row)
        if row_dict.get("effective_date") is not None:
            row_dict["effective_date"] = row_dict["effective_date"].isoformat()
        results.append(row_dict)

    return results
