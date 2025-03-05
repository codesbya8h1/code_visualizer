from langchain.chat_models import init_chat_model
from dotenv import load_dotenv


# Load environment variables
from dotenv import load_dotenv
load_dotenv()

LLM_GPT_3_POINT_5_TURBO = init_chat_model(model="gpt-3.5-turbo", temperature=0)