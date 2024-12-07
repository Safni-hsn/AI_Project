import re
from indicnlp.tokenize import indic_tokenize
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator


# Load a Tamil word list (you need a word list for spell checking)
def load_tamil_words():
    tamil_words = set()
    try:
        with open("tamil_words.txt", "r", encoding="utf-8") as f:
            for line in f:
                tamil_words.add(line.strip())  # Add each word from the word list
    except FileNotFoundError:
        print("Error: tamil_words.txt file not found.")
    return tamil_words


# Basic spell correction function using a dictionary
def correct_spelling(tamil_text, tamil_words_set):
    corrected_text = []
    tokens = indic_tokenize.trivial_tokenize(tamil_text)  # Tokenize the Tamil text

    for token in tokens:
        if token not in tamil_words_set:  # If the word is not in the word list
            corrected_token = find_closest_match(token, tamil_words_set)
            corrected_text.append(corrected_token)
        else:
            corrected_text.append(token)

    return " ".join(corrected_text)


# Function to find the closest matching word from the dictionary (basic edit distance approach)
def find_closest_match(word, word_list):
    closest_word = word  # Default is the word itself
    min_distance = float('inf')

    for dict_word in word_list:
        distance = levenshtein_distance(word, dict_word)  # Compute edit distance
        if distance < min_distance:
            min_distance = distance
            closest_word = dict_word

    return closest_word


# Levenshtein distance (edit distance) function
def levenshtein_distance(a, b):
    if len(a) < len(b):
        return levenshtein_distance(b, a)
    if len(b) == 0:
        return len(a)
    a, b = list(a), list(b)
    while len(a) > len(b):
        b.append("")
    d = []
    for i in range(len(a) + 1):
        d.append([0] * (len(b) + 1))
    for i in range(len(a) + 1):
        d[i][0] = i
    for j in range(len(b) + 1):
        d[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)
    return d[len(a)][len(b)]


# Example of correcting Tamil text
tamil_text = "நான் ஒரு பள்ளி கறறல் நடந்து விடு. இது அறிவியல் ஆரா்ச்சி வினா ஆகும்."
tamil_words_set = load_tamil_words()  # Load the Tamil word list

# If the word list is successfully loaded
if tamil_words_set:
    corrected_text = correct_spelling(tamil_text, tamil_words_set)
    print("Original Text: ", tamil_text)
    print("Corrected Text: ", corrected_text)
else:
    print("No word list available for spell checking.")
