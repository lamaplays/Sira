
from jinja2 import FileSystemLoader, Environment


def md_cv(json_cv):
    
    env = Environment(
    loader=FileSystemLoader("."),
    comment_start_string='{=',
    comment_end_string='=}',
    block_start_string="((*",
    block_end_string="*))",
    variable_start_string="(((",
    variable_end_string=")))",
    autoescape=False,  
    )
    
    template = env.get_template("generators/cv_template.md")
    tex_output = template.render(**json_cv)
    
    with open("new_cv.md","w",encoding="utf-8") as f:
        f.write(tex_output)
        print("markdown CV generated")    
    
    







    



    