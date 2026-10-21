import config
import init_model
from smolagents import CodeAgent
from retriever import RetrieverTool
import time
import pandas as pd
import indexing

start_time = time.perf_counter()

base,key = config.initialize_config()
vectorestore = indexing.build_store()
retrieval_tool = RetrieverTool(vectorestore)
llm = init_model.initialize_model(base,key)
agent = CodeAgent(
    tools=[retrieval_tool],
    model=llm,
    max_steps=6,
    verbosity_level=2
)

# print(agent.run('What are the key aspects of an Agentic AI system?'))
# print(agent.run("List down the authors of the research paper - `Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions` "))
# print(agent.run("What can be the evaluation metrics for the Agentic AI systems?"))
print(agent.run("Give me the abstract for the paper - `Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions`"))

end_time = time.perf_counter()
elapsed = end_time - start_time
print(f'Elapsed time: {elapsed}')
