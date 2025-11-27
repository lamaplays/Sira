from sira.models import outputCV
import json
from pathlib import Path


def load_validate(cv_path:Path) -> outputCV:
    with cv_path.open('r',encoding='utf-8') as f:
        cv_json = json.load(f)
        
    return outputCV(**cv_json)  # validation  
 
    
    