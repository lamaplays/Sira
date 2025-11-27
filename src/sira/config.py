from pathlib import Path
import json


config_path = Path.home()/ ".sira_config.json"
def load_config():
    if not config_path.exists():
        return {}
    try:
        with config_path.open('r', encoding = 'utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:    
        return {}
    
def save_config(cv_path: str | None = None, model_name: str | None = None)-> None:
    
    cfg = load_config()

    if cv_path is not None:
        cfg["cv_path"] = cv_path    
        
    if model_name is not None:
        cfg["model_name"] = model_name     

    with config_path.open('w', encoding = 'utf-8') as f:
        json.dump(cfg, f, indent=2)    
    