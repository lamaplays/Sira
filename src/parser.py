from agent import siraState
import json

with open("mock_data",'r') as f:
    mock_data = json.load(f)

    
    

def parser_node(state:siraState):
    # TODO: this func is supposed to parse the json object "mock_data"
    cv_data = mock_data.model_dump()
    return cv_data    
    