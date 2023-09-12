import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
question = "Write a select query to find top 10 entries in table Employee "

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

repo_id = "defog/sqlcoder"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
)
llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.run(question))