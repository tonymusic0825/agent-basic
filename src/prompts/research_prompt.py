from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = "You are a research assistant that will help generate a research paper.\
                Answer the user query and use necessary tools.\
                Wrap the output in this format that provide no other text\n{format_instructions}"

research_prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
])
