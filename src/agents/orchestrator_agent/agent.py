from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.langchain_tool import LangchainTool
from google.adk.tools import exit_loop

from .instructions import ORCHESTRATOR_INSTRUCTIONS
from .tools.custom_functions import get_fx_rate
from .tools.custom_agents import google_search_agent
from .tools.third_party_tools import langchain_wikipedia_tool
from .tools.state_tools import save_referenced_documents_to_state
from .sub_agents.faq_agent.agent import faq_agent
from .sub_agents.data_query_agent.agent import data_query_agent


root_agent = Agent(
    model='gemini-2.5-flash',
    name='orchestrator_agent',
    description='Orchestrates requests among the specialized agents of the Corporate Knowledge Agent.',
    instruction=ORCHESTRATOR_INSTRUCTIONS,
    sub_agents=[faq_agent, data_query_agent],
    tools=[
        FunctionTool(get_fx_rate),
        AgentTool(agent=google_search_agent),
        LangchainTool(langchain_wikipedia_tool),
        FunctionTool(save_referenced_documents_to_state),
    ],
)