from google.adk.agents import Agent

data_query_agent = Agent(
    model='gemini-2.5-flash',
    name='data_query_agent',
    description='Queries structured business data (metrics, status, reports) via MCP tools.',
    instruction=(
        'You are the Data Query Agent for the Corporate Knowledge Agent.' 
        'Answer questions about operational data (status, metrics, reports).' 
        '[PLACEHOLDER: Connection via MCP Toolbox will be added on Day 4.'
        'For now, state that access to structured data is not yet connected.]'
    ),
)
