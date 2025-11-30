import warnings
warnings.filterwarnings("ignore", message=".*Pydantic V1.*")

from sira.agent import build_graph
from sira.utils import load_validate
from sira.generators.cv_generator import md_cv
from sira.cli import parsing_args
from pathlib import Path
from sira.config import load_config, save_config
from sira.llm_choice import get_llm


def main():
    args = parsing_args()
    cfg = load_config()
    
    # resolve args
    
    cv_path: Path | None = args.cv or cfg.get("cv_path")
    model_name: str | None = args.model or cfg.get("model_name")
   
    if args.store:
        save_config(
            cv_path=str(cv_path) if cv_path is not None else None,
            model_name=model_name,
        )
    
    data_persist = "cv_path" in cfg
    model_choice_persist = "model_name" in cfg

    if cv_path is None and not data_persist:
        raise SystemExit("[sira] No CV file path provided or persisted.")
    if model_name is None and not model_choice_persist:
        raise SystemExit ("[sira] No model name was specified or persisted.")
    
    try:
        cv_data = load_validate(cv_path)
    except Exception as e:
        print(f"[sira] Failed to load or validate CV data from '{cv_path}': {e}")
        raise SystemExit from e
    try:    
        llm = get_llm(model_name)
    except Exception as e:
        print(f"[sira] Failed to initialize LLM '{model_name}': {e}")
        raise SystemExit from e
    try:        
        graph = build_graph(llm)
    except Exception as e:
        print(f"[sira] Failed to build graph with LLM '{model_name}': {e}")
        raise SystemExit from e
    try:    
        job_desc_path = args.job
        with open(job_desc_path, "r", encoding="utf-8") as f:
            job_desc = f.read()
        print(f"using {model_name} from {cv_path}")
    except FileNotFoundError:
        print(f"[sira] Job description file '{job_desc_path}' not found.")
        raise SystemExit from FileNotFoundError 
    except Exception as e:
        print(f"[sira] Failed to read job description from '{job_desc_path}': {e}")
        raise SystemExit from e
    
    
    print("Tailoring in process...\n")
    result = graph.invoke({
            "cv_data": cv_data.model_dump(),
            "job_desc": job_desc,
        })   
    json_output_cv = result["output_cv"].model_dump()
    new_cv = md_cv(json_output_cv) 
    print("="*30)
    print(new_cv)  
    print("="*30)
    

    while True:
        user_input = input("""
Do you want to:
1.rerun tailoring\n
2.save current tailored cv\n
3.change model\n
4.exit\n""").strip()
        if user_input == "1":
            print(f"Using {model_name} with CV from {cv_path}")
            print("Tailoring in process...\n")
            result = graph.invoke({
            "cv_data": cv_data.model_dump(),
            "job_desc": job_desc,
             })   
            json_output_cv = result["output_cv"].model_dump()
            new_cv = md_cv(json_output_cv) 
            print("="*30)
            print(new_cv)  
            print("="*30)         
            continue
        
        
        
        elif user_input == "2":
            with open("tailored_cv.md","w",encoding="utf-8") as f:
                f.write(new_cv)
            print("tailored CV saved as tailored_cv.md")
            continue
                  
    
        elif user_input == "3":
            new_model = input("Enter new model name: ").strip()
            if not new_model:
                print("Model name cannot be empty. Keeping current model.\n")
                continue
                
            try:
                new_llm = get_llm(new_model)
                new_graph = build_graph(new_llm)
                llm = new_llm
                graph = new_graph
                model_name = new_model
                print(f"Model changed to {model_name}\n")
            except Exception as e:
                print(f"[sira] Failed to switch to model '{new_model}': {e}")
                print(f"Keeping current model: {model_name}\n")
            continue


        elif user_input == "4":
            print("goodbye")
            break
        else:
            print("Invalid option.\n")
            continue
            

        
        
        
        


if __name__ == "__main__":
    main()
