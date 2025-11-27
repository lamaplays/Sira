from sira.models import outputCV


def get_llm(model_name: str | None = None):

    try:
        if model_name is None:
            raise ValueError("No local model specified")

        from langchain_ollama import ChatOllama

        model = ChatOllama(
            model=model_name,
            format="json",
            temperature=0.7,
            
        )
        return model.with_structured_output(outputCV)

    except Exception as e:
        print(f"[sira] Could not load Ollama model '{model_name}': {e}")
        raise SystemExit("[sira] Exiting due to model loading failure.")