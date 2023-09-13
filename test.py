import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from datetime import datetime

print(datetime.now())
question = "Find the name of services that have been used for more than 2 times in first notification of loss. table:CREATE TABLE services (service_name VARCHAR, service_id VARCHAR); CREATE TABLE first_notification_of_loss (service_id VARCHAR)'
"

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

#tsdocode/text-to-sql
#alibidaran/sql_generator

repo_id = "saikiranmaddukuri/chat_to_sql0.17"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 1.5, "max_length": 64}
)
llm_chain = LLMChain(prompt=prompt, llm=llm)
print(datetime.now())
print(llm_chain.run(question))
print(datetime.now())