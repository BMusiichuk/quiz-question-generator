import json
from pydantic import BaseModel, ValidationError
from openai import OpenAI
from quiz_generator.config import get_openai_api_key

client = OpenAI(api_key=get_openai_api_key())

class QuizQuestion(BaseModel):
    question: str
    options: dict
    answer: str


def generate_quiz_question(learning_objective: str) -> QuizQuestion:
    """
    Generate a multiple-choice quiz question as a structured JSON.

    The output JSON format should be:
    {
      "question": "Question text",
      "options": {
          "A": "Option A",
          "B": "Option B",
          "C": "Option C",
          "D": "Option D"
      },
      "answer": "Letter corresponding to the correct answer"
    }
    """
    prompt = (
        f"Create a multiple-choice quiz question for higher education students on the following topic: "
        f'"{learning_objective}".\n\n'
        "The output must be valid JSON with the following structure:\n"
        "{\n"
        '  "question": "Your question text",\n'
        '  "options": {\n'
        '    "A": "Option A",\n'
        '    "B": "Option B",\n'
        '    "C": "Option C",\n'
        '    "D": "Option D"\n'
        "  },\n"
        '  "answer": "Letter corresponding to the correct answer"\n'
        "}\n\n"
        "Make sure that the correct answer letter matches one of the option keys (A, B, C, D), "
        "and that there is exactly one correct answer. Do not include any additional text."
    )

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a knowledgeable assistant who creates high-quality quiz questions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=300)
        generated_text = response.choices[0].message.content.strip()
        # parse the JSON output
        parsed = json.loads(generated_text)
        quiz_question = QuizQuestion(**parsed)
        # Validate keys A, B, C, D
        if set(quiz_question.options.keys()) != {"A", "B", "C", "D"}:
            raise ValueError("Options must contain exactly the keys A, B, C, and D.")
        if quiz_question.answer not in quiz_question.options:
            raise ValueError("Answer must be one of the option keys.")
        return quiz_question
    except (json.JSONDecodeError, ValidationError) as e:
        raise Exception("Failed to parse quiz question output: " + str(e))
    except Exception as e:
        raise Exception("Failed to generate quiz question: " + str(e))
