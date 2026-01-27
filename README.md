# Federico Azzuro - 30 Great Python Projects

## Udemy - [Federico Azzuro - 30 Great Python Projects](https://www.udemy.com/course/great-python-projects/)

### Section 2: Starter projects

- Project 01 - Mad Libs
  - A fun text-based game where the user provides words (nouns, verbs,
    adjectives) to fill in a story template.
  - This project teaches basic input handling, string formatting, and working
    with f-strings in Python.
- Project 02 - Number guessing game
  - A simple number guessing game where the computer generates a random number
    within a given range, and the player tries to guess it.
  - This project teaches input validation, loops, conditionals, and working with
    the `random` module.
- Project 03 - Dice simulator
  - A dice rolling simulator where the user can roll one or more dice and see
    the results along with their total.
  - This project teaches working with functions, loops, type hints, exception
    handling, and the `random` module.
- Project 04 - Hangman
  - A simple text-based Hangman game where the player guesses letters to reveal
    a hidden word within a limited number of tries.
  - This project teaches string manipulation, loops, conditionals, input
    validation, and using the `random` module to select words.
- Project 05 - Rock, Paper, Scissors
  - A text-based Rock-Paper-Scissors game where the player competes against a
    simple AI.
  - This project teaches object-oriented programming, loops, conditionals, input
    validation, dictionaries, and using the `random` module.
- Project 06 - Password generator
  - Generates secure, customizable passwords based on user-specified criteria,
    including length, inclusion of uppercase letters, numbers, and symbols.
  - This project teaches working with strings, the `secrets` module for
    cryptographically secure randomization, and basic input/output logic.
- Project 07 - QR code generator
  - A tool to generate QR codes from user-provided text, allowing customization
    of size, padding, foreground, and background colors.
  - This project teaches working with third-party libraries (`qrcode`), classes,
    file handling, and basic user input in Python.
- Project 08 - Website checker
  - Reads a list of websites from a CSV file and checks their HTTP status codes,
    displaying a human-readable description for each.
  - This project teaches working with CSV files, HTTP requests using `requests`,
    dynamic user-agent handling with `fake_useragent`, and using the `http`
    module for status codes.
- Project 09 - Common password checker
  - Checks whether a user-provided password is commonly used by comparing it
    against a list of known passwords.
  - This project teaches file handling with context managers, loops, string
    comparison, and basic function scoping in Python.
- Project 10 - Brute force
  - Simulates cracking a password using two approaches: checking against a list
    of common passwords and brute-forcing all possible combinations up to a
    certain length.
  - This project teaches file handling, tuples for fast comparisons, itertools
    for generating combinations, loops, and performance measurement with
    `time.perf_counter()`.
- Project 11 - Image downloader
  - Downloads an image from a user-provided URL and saves it locally with a
    specified name and optional folder.
  - This project teaches working with file paths, checking for file existence,
    HTTP requests using `requests`, basic exception handling, and string
    manipulation to handle file extensions.
- Project 12 - Tax calculator
  - A simple graphical tax calculator that allows users to input income and tax
    rate, then calculates and displays the tax amount.
  - This project teaches creating GUIs in Python using `customtkinter`, working
    with widgets, handling user input, and updating the interface dynamically.

### Section 3: Intermediate Projects

- Project 13 - File sorter
  - Organizes files in a directory by moving them into folders based on their
    file extensions (e.g., `.jpg` → `jpg/`).
  - This project teaches working with the filesystem using `os` and `shutil`,
    walking directory trees with `os.walk`, creating folders dynamically, and
    cleaning up empty directories.
- Project 14 - Sentiment analysis bot
  - Analyzes user-input text and determines its emotional tone (positive,
    negative, or neutral) using natural language processing.
  - This project teaches using third-party libraries (`TextBlob`), dataclasses,
    sentiment polarity, and building interactive command-line applications.
- Project 15 - URL shortener
  - Shortens long URLs using the Cuttly API and returns a shortened link.
  - This project teaches working with environment variables via `dotenv`, HTTP
    requests using `requests`, error handling, and interacting with external
    APIs.
- Project 16 - PDF reader
  - Extracts text from a PDF file and counts the frequency of each word,
    displaying the most common words.
  - This project teaches working with PDFs using `PyPDF2`, regular expressions
    for text processing, `collections.Counter` for counting, and handling text
    data in Python.
- Project 17 - Chat bot
  - A simple command-line chatbot that responds to user questions by finding the
    closest matching phrase from a predefined knowledge base.
  - This project teaches text preprocessing, string similarity matching using
    `difflib`, dictionary lookups, and building interactive conversational
    programs.
- Project 18/1 - Install selenium
  - Automates a web browser to open and close websites using Selenium and
    ChromeDriver.
  - This project teaches browser automation, working with WebDriver, managing
    external executables, and controlling web sessions programmatically.
- Project 18/2 - Email scraper
  - Automatically visits a website and extracts email addresses from the page
    source using browser automation and regular expressions.
  - This project teaches headless browser automation with Selenium, page loading
    synchronization, regex pattern matching, and basic web scraping techniques.
