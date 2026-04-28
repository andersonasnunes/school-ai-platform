# app/ai/tutor.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# 🔥 carrega variáveis do .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY não encontrada. Verifique seu .env")

client = OpenAI(api_key=api_key)


def build_prompt(data):
    return f"""
    Você é um professor experiente de {data['subject']}.

    Público:
    - Série: {data['grade']}
    - Nível: {data['level']}

    Conteúdo:
    - Tema: {data['topic']}
    - Subtópicos: {data['subtopics']}

    Gere:

    - Explicação didática
    - Exemplos
    - Dicas pedagógicas
    - 3 exercícios

    Linguagem simples e clara.
    """


def generate_lesson(data):
    try:
        prompt = build_prompt(data)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente educacional especialista."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("ERRO IA:", str(e))

        # 👇 fallback inteligente
        return f"""
        ⚠️ Modo offline ativado (sem IA)

        Tema: {data['topic']}

        Resumo básico:
        Este conteúdo aborda {data['topic']} com foco em {data['subtopics']}.
        O professor pode trabalhar exemplos práticos e exercícios para reforço.

        (Erro técnico: {str(e)})
        """

    return response.choices[0].message.content