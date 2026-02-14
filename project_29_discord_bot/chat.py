from difflib import get_close_matches
import json
import random
from typing import Dict, Optional, Union, List

KnowledgeType = Dict[str, Union[str, List[str]]]


def get_best_match(user_question: str, questions: dict) -> str | None:
    """Compares the user message similarity to the ones in the dictionary"""

    question_list: list[str] = [q for q in questions]
    # turns keys of dictionary to a list. Something like this
    # question_list: list[str] = list(questions.keys())

    matches: list = get_close_matches(
        user_question,  # user's message
        question_list,  # options from dictionary keys
        n=1,  # only return the first best one
        cutoff=0.6,
    )  # only 60% match will be recognised

    # Return the first best match, else return None
    if matches:
        return matches[0]
    return None


def clean_text(text: str) -> str:
    """Normalize user input for matching."""
    return text.lower().strip()


def load_knowledge(file: str) -> dict:
    """Load knowledge from JSON file."""
    with open("knowledge.json", "r", encoding="utf-8") as f:
        return json.load(f)


def get_response(match: Optional[str], knowledge: KnowledgeType) -> str:
    """Return response from knowledge (supports list or string)."""

    if not match:
        return "Sorry, I don't know… yet ❤️"

    answer = knowledge.get(match)

    if isinstance(answer, list):
        return random.choice(answer)

    if isinstance(answer, str):
        return answer

    return "Hmm… I’m confused 😅"


def chat_bot(user_input: str) -> str:
    knowledge = load_knowledge("./knowledge.json")
    clean_input: str = clean_text(user_input)
    best_match: str | None = get_best_match(
        user_question=clean_input, questions=knowledge
    )

    return get_response(best_match, knowledge)


if __name__ == "__main__":
    print(chat_bot("bye"))
