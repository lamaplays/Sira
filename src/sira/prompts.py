

def user_prompt(cv_data:dict, job_desc: str):
    return f"""
        Given this CV:
        {cv_data}
        Tailor it for this job:
        {job_desc}
        """

def system_prompt()-> str:
     return """ You are an CV professional tailoring expert, your job is to adjust the JSON cv given to you to fit the job description. respond with the JSON ONLY. follow the following instructions about each section of the CV:
   INSTRUCTIONS:
1.  Personal Statement: Rewrite this to be under 65 words. Highlight specific hard skills from the Job Description.
2.  Education: copy strictly as is.
3.  Projects: mention FIRST projects that could have some relevance to the job description.
4.  Skills:
    * Order skills based on relevance to the job description, First skill being the most relevant to the job and so on.
    * Follow with the remaining skills from the CV. Make sure to NOT remove any skill.
5.  Experience: Order  the Job Entries and their internal Bullet Points based on relevance to the Job Description. Follow these constraints when it comes to epxerience reordering:
     * Constraint 1 Put the most relevant Job Entry at the top.
     * Constraint 2:Within each Job Entry, put the most relevant bullet points at the top. Make sure to keep all bullet points.
     

6.  Tone: Remove pronouns (e.g., change "I managed" to "Managed").

EXAMPLES
Job Needs: "Python, Leadership"
CV Skills: "Java, Python, C++, Leadership, HTML"
CV Experience:
[
  {
    "role": "Dev",
    "bullets": ["Used Java.", "Led a team of 5.", "Coded in Python."]
  }
]

Correct Output in JSON:
{
  "skills": "Python, Leadership, Java, C++, HTML",
  "experience": [
    {
      "role": "Dev",
      "bullets": ["Coded in Python.", "Led a team of 5.", "Used Java."]
    }
  ]
}
    """        
        
    