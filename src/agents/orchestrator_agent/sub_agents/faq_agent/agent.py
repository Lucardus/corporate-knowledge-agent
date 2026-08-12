from google.adk.agents import Agent

faq_agent = Agent(
    model='gemini-2.5-flash',
    name='faq_agent',
    description='Answers questions about company policies, manuals, and internal documents using RAG.',
    instruction=(
        'You are the FAQ Agent for the Corporate Knowledge Agent.' 
        'Answer questions about policies and internal documentation.' 
        '[PLACEHOLDER: Retrieval via RAG (AlloyDB/Cloud SQL) will be connected on Day 3.'
        'For now, state that the document database is not yet connected.]'
    ),
)
