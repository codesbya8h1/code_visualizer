
import os
from langchain.chat_models import ChatOpenAI

# Initialize the LLM with chat model
openai_api_key = os.environ['OPENAI_API_KEY']
openai_llm = ChatOpenAI(
    openai_api_key=openai_api_key,
    model_name="gpt-3.5-turbo",
    temperature=0
)

# Create an LLM chain
# chain = LLMChain(llm=openai_llm, prompt=prompt)
# LLMChain(llm=ChatOpenAI(), prompt=prompt)

# Run the chain
# result = chain.run("artificial intelligence")
# print(result)
