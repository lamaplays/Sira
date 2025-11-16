from agent import build_graph
from utils import load_validate
from generators.cv_generater import latex_cv

def main():
    print("Hello from sira!")
    
    graph = build_graph()
    
    cv_data = load_validate()
    job_desc = """Frontend Developer Intern - E-commerce Platform Looking for someone with React.js, TypeScript, CSS/Sass, and experience with payment gateway integration.No ML/AI experience needed."""
    print("tailoring in process: ")
    result = graph.invoke({ "cv_data":cv_data.model_dump(),
                            "job_desc": job_desc  })
   
    json_output_cv = result["output_cv"].model_dump()
    
    
    latex_cv(json_output_cv)
    
    
    
    
    
    

if __name__ == "__main__":
    main()
    print("done")
