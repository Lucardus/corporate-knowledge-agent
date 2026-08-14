import os
from dotenv import load_dotenv

load_dotenv("src/agents/orchestrator_agent/.env")

from src.agents.orchestrator_agent.tools.rag_retrieval import search_corporate_documents

results = search_corporate_documents("posso cancelar um pedido que já foi enviado?")
for r in results:
    print(f"[{r['distance']:.4f}] {r['title']} — {r['section']}")
