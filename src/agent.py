#TODO:
#    if model.name == "ollama":
#     #parser = PydanticOutputParser(pydantic_object=outputCV)
   # we could add {parser.get_format_instructions()} to the above prompt if needed
   # # Use Ollama with format="json" PS idotn what doesnt that mean
    # tailored = parser.parse(response) i think no need forthis line
#    else:
#         pass   
#from langchain_core.output_parsers import PydanticOutputParser

        





from pydantic import BaseModel, Field
from typing import TypedDict, Optional
from langgraph.graph import StateGraph
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import json
from langchain_openai import ChatOpenAI
import pprint



    
load_dotenv()


class outputCV(BaseModel):
    personal_statement: str = Field(...,description="a Rewritten personal statement to match job requirements.  ")
    experience: str = Field(...,description=" experiences/achievements relevant to the job. ")
    relevant_skills: str = Field(..., description="skills relevant to the job description") 
    
class siraState(TypedDict):
    cv_data: dict #input
    job_desc: str #input
    output_cv : Optional[outputCV] # output
 
with open("mock_data.json",'r') as f:
    mock_data = json.load(f)
    valid_cv = outputCV(**mock_data)  # validation  

   
def tailor_node(state: siraState):
    model = ChatOllama(
       model="deepseek-r1:8b",
       format="json",
       temperature=0.7,
       reasoning=False
       
   )   
    # chat = ChatOpenAI(model="gpt-5-mini",)    
    structured_llm = model.with_structured_output(outputCV)
   
    #pprint.pp(f'state of the cv data:\n{state["cv_data"]}')

    prompt = f"""
        You MUST respond with ONLY a valid python dictionary.
        Given this CV:
        {state["cv_data"]}

        Tailor it for this job:
        {state["job_desc"]}
        
        Instructions:
        - Personal Statement: Rewrite to highlight skills matching the job
        - Experience: Select and emphasize ONLY relevant experiences/projects
        - Skills: List ONLY skills mentioned in the job description first, then add others
        
        Example transformation:
        Original Skills: "Java, Python, C++, Unity"
        Job needs: "Python, Docker"
        Tailored Skills: "Python, Docker, Java, C++"
        (Prioritized Python and Docker, kept others)
        
        Note: use passive third person pronouns.
        
         
        """
 
    
    response = structured_llm.invoke(prompt) 
    return {"output_cv":response}

#graph
builder = StateGraph(siraState)
builder.add_node("tailor",tailor_node)
builder.set_entry_point("tailor")
builder.set_finish_point("tailor")

graph = builder.compile()


#pprint.pp(f"valid cv\n{valid_cv}")

result = graph.invoke({
    "cv_data":valid_cv.model_dump(), #make it a dict
    "job_desc":"""
        Frontend Developer Intern - E-commerce Platform
        Looking for someone with React.js, TypeScript, CSS/Sass, 
        and experience with payment gateway integration.
        No ML/AI experience needed.
        
    """,
    }) # add ur job desc inside the parantheses


pprint.pp(result["output_cv"])

outputcv_result = result["output_cv"]

json_output_cv = outputcv_result.model_dump_json(indent=2)
        
import json2latex

with open("new_cv.tex","w") as r:
    json2latex.dump("latexCv",json_output_cv,r)
    
    
    
    