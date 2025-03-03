import os
from langchain.llms import OpenAI


# Initialize the LLM
openai_api_key = os.environ['OPENAI_API_KEY']
openai_llm = OpenAI(client=None,
                    openai_api_key=openai_api_key,
                    model_name="gpt-3.5-turbo")

# Create an LLM chain
# chain = LLMChain(llm=openai_llm, prompt=prompt)
# LLMChain(llm=OpenAI(), prompt=prompt)

# Run the chain
# result = chain.run("artificial intelligence")
# print(result)
