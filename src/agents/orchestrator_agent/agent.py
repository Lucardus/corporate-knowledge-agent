from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='orchestrator_agent',
    description='Orchestrates requests among the specialized agents of the Corporate Knowledge Agent.',
    instruction='You are the orchestrator agent for the Corporate Knowledge Agent. Direct questions regarding policies or documents to the FAQ Agent, and questions regarding data or metrics to the Data Query Agent.',
)
