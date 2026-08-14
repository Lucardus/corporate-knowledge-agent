from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from ...tools.rag_retrieval import search_corporate_documents

faq_agent = Agent(
    model='gemini-2.5-flash',
    name='faq_agent',
    description='Answers questions about company policies, manuals and internal documents using RAG on the AlloyDB knowledge base.',
    instruction=(
        'You are the FAQ Agent of the Corporate Knowledge Agent. ' 
        'Use the search_corporate_documents tool to search for relevant information' 
        'on the basis of internal policies before answering any questions about ' 
        'policies, procedures, security, privacy or business rules. ' 
        'Base your answers exclusively on the content returned by the search. ' 
        'If the search does not return relevant information (high distance or unrelated content), ' 
        'Clearly state that you have not found an authorized internal source for that question,' 
        'instead of inventing an answer. ' 
        'Always cite the source document (title, document_id, version) in your response.'
    ),
    tools=[FunctionTool(search_corporate_documents)],
)
