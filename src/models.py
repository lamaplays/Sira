from pydantic import BaseModel, Field
from typing import TypedDict, Optional


class outputCV(BaseModel):
    personal_statement: str = Field(...,description="a Rewritten personal statement to match job requirements.  ")
    education: dict = Field(...,description="the recieved collage degrees.") 
    experience: list = Field(...,description=" experiences/achievements relevant to the job. ")
    relevant_skills: dict = Field(..., description="skills relevant to the job description. ") 
    projects : list = Field(...,description="list of Done projects related to the job description.") 


class siraState(TypedDict):
    cv_data: dict #input
    job_desc: str #input
    output_cv : Optional[outputCV] # output