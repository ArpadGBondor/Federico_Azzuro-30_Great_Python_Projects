from difflib import get_close_matches


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
    return text.lower().strip()


def chat_bot(knowledge: dict):
    while True:
        user_input: str = clean_text(input("You: "))

        if user_input in ("quit", "exit", "bye", "goodbye"):
            print("Bot: Goodbye!")
            break

        best_match: str | None = get_best_match(
            user_question=user_input, questions=knowledge
        )

        if answer := knowledge.get(best_match):
            print(f"Bot: {answer}")
        else:
            print("Bot: Sorry, I don't know.")


if __name__ == "__main__":
    brain = {
        "hello": "Hey there!",
        "hi": "Hello!",
        "hey": "Hi there!",
        "how are you": "I'm doing great!",
        "what is your name": "I'm a Python bot!",
        "who made you": "A cool programmer 😎",
        "what time is it": "I don't have a watch!",
        "what day is it": "Every day is coding day!",
        "where are you from": "From the digital world!",
        "what is python": "Python is a programming language.",
        "what is ai": "AI means Artificial Intelligence.",
        "tell me a joke": "Why do programmers love Python? Because it's easy!",
        "help": "Try asking me simple questions.",
        "thanks": "You're welcome!",
        "thank you": "No problem!",
        "bye": "Goodbye!",
        "goodbye": "See you later!",
        "what can you do": "I can chat with you.",
        "are you real": "As real as code can be!",
        "favorite color": "I like blue (like Python)!",
        "favorite food": "Electricity ⚡",
        "how old are you": "I was born today!",
        "what is coding": "Coding is telling computers what to do.",
        "tell me something": "Learning Python is awesome!",
        "are you smart": "I'm learning every day!",
        "do you sleep": "Never 😄",
        "where do you live": "Inside this program.",
        "what is life": "42 😉",
        "who am i": "A future programmer!",
    }

    chat_bot(knowledge=brain)
