import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()

os.environ["LANGSMITH_TRACING"] = "true"

model = init_chat_model("gpt-4o-mini", model_provider="openai", api_key=os.environ["OPENAI_API_KEY"])
messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

response = model.invoke(messages)
print(response.content)

# for token in model.stream(messages):
#     print(token.content)