from langchain.agents import initialize_agent,Tool
from langchain.chat_models import ChatOpenAI
from langchain import LLMMathChain, SerpAPIWrapper

llm = ChatOpenAI(model_name="gpt-3.5-turbo-0301",temperature=0)

def fib(n):
  if n<=1:
    return n
  else:
    return fib(n-1) + fib(n-2)

search = SerpAPIWrapper()
llm_math_chain = LLMMathChain(llm=llm, verbose=True)
tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    ),
    Tool(
        name="Fibonacci",
        func=lambda n: str(fib(int(n))),
        description="use when you want to calculate the nth fibonacci number. The input of function must be arabic numeral without any string."
    )
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

