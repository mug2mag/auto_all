prompt = """
Answer the following questions as best you can. You have access to the following tools:

Search: useful for when you need to answer questions about current events
Calculator: useful for when you need to answer questions about math
Fibonacci: use when you want to calculate the nth fibonacci number. The input of function must be arabic numeral without any string.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Search, Calculator, Fibonacci]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""
