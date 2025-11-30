<h1 style="text-align:center;">SIRA: CV tailoring AI Tool</h1>

### Installation
tool made available from the releases page as either a .whl file
'''
pip install sira-0.1.0-py3-none-any.whl
'''
or source zip.
### usage
 - This tool uses ollama to talk to your local LLMs, make sure you have ollama and the desired LLM installaed on your machine.
 - Make sure that ur input cv follow this specific JSON format:
 ```
{
  "personal_statement": "",
  "education": {},
  "experience": [],
  "skills": {},
  "projects": []
}
```
[see the data.json for reference]()

 - run `sira` or `sira-h` to display available arguments
### features
- leaverages local open LLMs capibilities to tailor you cv through ollama API.
- digest JSON CV and output formated md file.
- cli based.

  ### future plans
  -  introduce huggingface models
  -  wider range of templates
  -  less restrictive input


### made with ❤️ 
### any feedback would be appreciated


  

  

  

  




