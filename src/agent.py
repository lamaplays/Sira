#TODO:
# check your notes

from langgraph.graph import StateGraph
from models import outputCV, siraState
from prompts import prompt
from llm_choice import get_llm

 
def tailor_node(state: siraState):
   
    structured_llm = get_llm()
    system_prompt = prompt(
        cv_data = state["cv_data"],
        job_desc = state["job_desc"]
    )

    response = structured_llm.invoke(system_prompt) 
    return {"output_cv":response}

def build_graph():
    builder = StateGraph(siraState)
    builder.add_node("tailor",tailor_node)
    builder.set_entry_point("tailor")
    builder.set_finish_point("tailor")

    graph = builder.compile()
    return graph






        

    
    
    