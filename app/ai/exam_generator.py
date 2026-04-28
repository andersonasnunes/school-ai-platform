# app/ai/exam_generator.py

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def build_exam_prompt(data):
    return f"""
    Você é um professor especialista em elaborar avaliações escolares.

    Crie uma prova com as seguintes características:

    Matéria: {data['subject']}
    Série: {data['grade']}
    Nível: {data['level']}

    Tema: {data['topic']}
    Subtópicos: {data['subtopics']}

    Dificuldade: {data['difficulty']}
    Quantidade de questões: {data['questions']}

    Requisitos:

    - Questões claras e objetivas
    - Misturar questões de cálculo e interpretação
    - Contextualizar com situações do dia a dia
    - Incluir gabarito ao final
    - Separar bem: QUESTÕES e GABARITO

    Formato:

    QUESTÕES:
    1.
    2.
    ...

    GABARITO:
    1.
    2.
    ...
    """


def generate_exam(data):
    prompt = build_exam_prompt(data)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Você é um especialista em avaliação educacional."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content