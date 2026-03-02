from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent

# Modular Imports
from tools.tools import search_tool, wiki_tool, save_tool
from agents.models import ResearchResponse
from prompts.research_prompt import research_prompt

# Load env file
load_dotenv()

# Setup
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)
tools = [search_tool, wiki_tool, save_tool]

# Build agent
prompt = research_prompt.partial(format_instructions=parser.get_format_instructions())
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__":
    query = input("Hey there!, What can I help you research?\n")
    raw_response = agent_executor.invoke({"query": query})

    try:
        structured_response = parser.parse(raw_response.get("output")[0]["text"])
        print(structured_response)
    except Exception as e:
        print("Error parsing...") 