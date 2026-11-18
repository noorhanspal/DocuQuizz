
from django.conf import settings
from openai import OpenAI


def generate_mcqs(text, num_questions=5, difficulty="medium"):

    if not settings.OPENAI_API_KEY or settings.OPENAI_API_KEY == "your_api_key_here":
        return []

    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    prompt = f"""
    Generate {num_questions} multiple-choice questions
    using ONLY the document text provided below.

    Difficulty: {difficulty}

    Each question must have:
    - One question
    - Four options (A, B, C, D)
    - One correct answer

    Document text:
    {text}
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions="You are an educational MCQ generator.",
        input=prompt
    )

    return response.output_text
