
from jinja2 import FileSystemLoader, Environment


def latex_cv(json_cv):
    
    env = Environment(
    loader=FileSystemLoader("."),
    block_start_string="((*",
    block_end_string="*))",
    variable_start_string="(((",
    variable_end_string=")))",
    autoescape=False,  
    )
    
    
    template = env.get_template("generators/cv_template.tex")
    tex_output = template.render(**json_cv)
    
    with open("new_cv.tex","w",encoding="utf-8") as f:
        f.write(tex_output)
        print("latex cv generated")    
    
    







    



    