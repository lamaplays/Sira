from models import outputCV

def get_llm():
    try:
       from langchain_ollama import ChatOllama
       model = ChatOllama(
            model="deepseek-r1:8b",
            format="json",
            temperature=0.7,
            reasoning= False,
            )   
       structured_llm = model.with_structured_output(outputCV)
 
       return structured_llm

    
    except:
      from dotenv import load_dotenv
      load_dotenv()
      from langchain_openai import ChatOpenAI
      model = ChatOpenAI(model="gpt-5-mini",)
      structured_llm = model.with_structured_output(outputCV)
      return structured_llm


