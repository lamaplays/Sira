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
    cv_path: Path | None = args.cv
    if cv_path is None and "cv_path" in cfg:
        cv_path = Path(cfg["cv_path"])
   
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
        llm = get_llm(model_name)
        graph = build_graph(llm)
        print(f"tailoring cv using {model_name} from {cv_path}")
        
    except FileNotFoundError as e:
        print(e)
        raise SystemExit
    
    
    while True:
        
        job_desc = input("Enter your job description\nOr type 'bye' to exit:\n ")
        if job_desc.strip().lower() in {"bye", "goodbye", "exit", "quit"}:
            print("goodbye!")
            break
         
        print("Tailoring in process...\n")
        result = graph.invoke({
            "cv_data": cv_data.model_dump(),
            "job_desc": job_desc,
        })
        json_output_cv = result["output_cv"].model_dump()
        print(json_output_cv)
        md_cv(json_output_cv)


if __name__ == "__main__":
    main()
