from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the LLM
llm = OpenAI(api_key="your-api-key-here")

# Create a prompt template
prompt = PromptTemplate(input_variables=["topic"],
                        template="Write a short paragraph about {topic}.")

# Create an LLM chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
result = chain.run("artificial intelligence")
print(result)
