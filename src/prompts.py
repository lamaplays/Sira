

def prompt(cv_data:dict, job_desc: str):
    return f"""
        You MUST respond with ONLY a valid python dictionary.
        Given this CV:
        {cv_data}

        Tailor it for this job:
        {job_desc}
        
        Instructions:
        - Personal Statement: Rewrite to highlight skills matching the job
        - Experience: Select and emphasize ONLY relevant experiences/projects
        - Skills: List ONLY skills mentioned in the job description first, then add others
        
        Example transformation:
        Original Skills: "Java, Python, C++, Unity"
        Job needs: "Python, Docker"
        Tailored Skills: "Python, Docker, Java, C++"
        (Prioritized Python and Docker, kept others)
        
        Note: use passive first person pronouns.
        
         
        """
    