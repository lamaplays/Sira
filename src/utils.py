from models import outputCV
import json

def load_validate():
    with open("mock_data.json",'r') as f:
        mock_data = json.load(f)
        
    return outputCV(**mock_data)  # validation  
 
    
    