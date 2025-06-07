import openai
from app.config import Config

openai.api_key = Config.OPENROUTER_API_KEY
openai.api_base = Config.OPENAI_API_BASE

def ask_tutor(question: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model=Config.MODEL,
            messages=[{"role": "user", "content": question}],
            headers={
                # "HTTP-Referer": "https://tutor.ia",
                # "X-Title": "TutorIA"                      
            }
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Erro ao consultar IA: {e}"
