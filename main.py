import os

os.environ["OPENAI_API_KEY"] = "sk-fsdfs"
os.environ["SERPAPI_API_KEY"] = "fssdf"

from tools import agent
from prompt_template import prompt

agent.agent.llm_chain.prompt.template = prompt

if __name__ == '__main__':
    agent.run("上海市长和副市长是谁？今年分别几岁了？把他们岁数求和")