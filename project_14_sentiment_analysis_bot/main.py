from textblob import TextBlob
from dataclasses import dataclass


@dataclass
class Mood:
    """
    Represents the emotional state detected from a piece of text.

    This class is a simple data container that stores the result of
    sentiment analysis performed by the bot.

    Attributes:
        emoji (str): A visual representation of the detected mood.
        sentiment (float): Polarity score in the range [-1.0, 1.0],
                           where negative values indicate negative
                           sentiment and positive values indicate
                           positive sentiment.
    """

    emoji: str
    sentiment: float


def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    """
    Analyze the sentiment of input text and classify it as positive,
    negative, or neutral.

    This function uses TextBlob to calculate a polarity score and then
    compares it against configurable sensitivity thresholds to determine
    the user's mood.

    Args:
        input_text (str): The text to analyze.
        sensitivity (float): Minimum absolute polarity required to
            classify text as positive or negative. Must be >= 0.

    Returns:
        Mood: A Mood object containing the detected emoji and
        sentiment polarity score.

    Example:
        >>> get_mood("I love this!", sensitivity=0.3)
        Mood(emoji='😀', sentiment=0.5)
    """
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_treshold: float = sensitivity
    hostile_treshold: float = -sensitivity

    if polarity >= friendly_treshold:
        return Mood("😀", polarity)
    elif polarity <= hostile_treshold:
        return Mood("😠", polarity)
    else:
        return Mood("😐", polarity)


def run_bot():
    print("Enter some text to get a sentiment analysis back:")
    while True:
        user_input: str = input("You: ")
        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f"Bot: {mood.emoji} ({mood.sentiment})")


if __name__ == "__main__":
    run_bot()
