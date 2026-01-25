import re
from collections import Counter
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file: str) -> list[str]:
    with open(pdf_file, "rb") as pdf:  # read bytes mode
        reader = PdfReader(pdf, strict=False)

        print("Pages:", len(reader.pages))
        print("-" * 10)

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]

        return pdf_text


def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r"\s+|\s*[,;?!.-]\s*", text.lower())
        all_words += [word for word in split_text if word]
    return Counter(all_words)


def main():
    extracted_text: list[str] = extract_text_from_pdf("sample.pdf")
    print(extracted_text)
    print("-" * 10)
    counter: Counter = count_words(text_list=extracted_text)
    for word, mention in counter.most_common(10):
        print(f"{word:15}: {mention} times")


if __name__ == "__main__":
    main()
