#TODO:
# check your notes

from langgraph.graph import StateGraph
from models import outputCV, siraState
from prompts import user_prompt, system_prompt
from langchain.messages import SystemMessage, HumanMessage

 


def build_graph(structured_llm):
    
    def tailor_node(state: siraState):
   
        
        user = user_prompt(
            cv_data = state["cv_data"],
            job_desc = state["job_desc"]
        )

        response = structured_llm.invoke([SystemMessage(content=system_prompt()),
                                        HumanMessage(content=user)]) 
        return {"output_cv":response}
    
    
    
    
    builder = StateGraph(siraState)
    builder.add_node("tailor",tailor_node)
    builder.set_entry_point("tailor")
    builder.set_finish_point("tailor")

    graph = builder.compile()
    return graph






        

    
    
    