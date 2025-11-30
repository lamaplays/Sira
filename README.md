<h1 align=center >SIRA: CV tailoring AI Tool</h1>

### Installation
tool made available from the [releases]() page as either a .whl file
```
pip install sira-0.1.0-py3-none-any.whl
```
or source zip.
### Usage
 - This tool uses ollama to talk to your local LLMs, make sure you have ollama and the desired LLM installaed on your machine.
 - Make sure you inpute cv is in JSON format follow this specific nature:
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

 - run `sira` or `sira-h` to display available arguments.
### features
- leverages local open LLMs capabilities to tailor you cv through ollama API.
- digest JSON CV and output formated md file.
- CLI based.

 ### Roadmap
  -  introduce huggingface models
  -  wider range of templates
  -  less restrictive input

<h3 align=center>  made with ❤️ </h3>
<h5 align=center> any feedback would be appreciated!</h5>


  

  

  

  






