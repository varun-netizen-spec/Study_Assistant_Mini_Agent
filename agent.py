from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory

# Load free open-source LLM
llm = Ollama(model="llama3")

# Tool 1: Calculator
def calculator(expression: str) -> str:
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation"

# Tool 2: Text Summarizer
def summarizer(text: str) -> str:
    prompt = f"Summarize this text in simple words:\n{text}"
    return llm(prompt)

tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Useful for solving math problems"
    ),
    Tool(
        name="Summarizer",
        func=summarizer,
        description="Summarizes long text"
    )
]

# Memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Create Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

print("🤖 AI Study Assistant Ready (type 'exit' to quit)\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    response = agent.run(query)
    print("Assistant:", response)
