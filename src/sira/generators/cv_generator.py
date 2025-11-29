
from jinja2 import PackageLoader, Environment



def md_cv(json_cv: dict):
    
    env = Environment(
    loader=PackageLoader("sira", "generators"),
    comment_start_string='{=',
    comment_end_string='=}',
    block_start_string="((*",
    block_end_string="*))",
    variable_start_string="(((",
    variable_end_string=")))",
    autoescape=False,  
    )
    
    template = env.get_template("cv_template.md")
    md_output = template.render(**json_cv)

    print("Tailored markdown CV generated\nPreview")    
        
    return md_output
    









    



    