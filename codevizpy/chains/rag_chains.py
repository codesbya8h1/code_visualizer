from llm.llm_presets import LLM_GPT_3_POINT_5_TURBO
from prompts.prompt_code_graph import PROMPT_CODE_GRAPH
from graph_response import CodeGraphResponse

def create_code_graph_chain():

    code_graph_chain = PROMPT_CODE_GRAPH | LLM_GPT_3_POINT_5_TURBO
    return code_graph_chain

def create_structured_code_graph_chain():
    
    structure_llm =  LLM_GPT_3_POINT_5_TURBO.with_structured_output(schema=CodeGraphResponse)
    structured_code_graph_chain = PROMPT_CODE_GRAPH | structure_llm
    return structured_code_graph_chain