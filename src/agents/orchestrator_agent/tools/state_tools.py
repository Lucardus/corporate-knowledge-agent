from typing import List

from google.adk.tools.tool_context import ToolContext


def save_referenced_documents_to_state(
    tool_context: ToolContext, documents: List[str]
) -> dict[str, str]:
    """Saves the list of referenced documents/sources to state["referenced_documents"].

    Use this after retrieving information from internal documentation (policies,
    manuals, FAQs) so the conversation keeps track of which sources have already
    been consulted. This avoids redundant retrieval and lets the agent reference
    previously cited documents in follow-up questions.

    Args:
        documents: a list of document titles or identifiers to add to the
            session's referenced-documents list.

    Returns:
        A status dict indicating success.
    """
    existing_documents = tool_context.state.get("referenced_documents", [])

    updated_documents = existing_documents + [
        doc for doc in documents if doc not in existing_documents
    ]

    tool_context.state["referenced_documents"] = updated_documents

    return {"status": "success"}