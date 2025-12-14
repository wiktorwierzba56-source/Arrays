def word_count(text):
    words = text.split()  # Dzielimy tekst na słowa
    return len(words)

def longest_to_shortest(text):
    words = text.split()
    words_sorted = sorted(words, key=len, reverse=True)  # Sortujemy według długości
    return words_sorted


def alphabetically_sorted(text):
    words = text.split()
    words_sorted = sorted(words)  #alfabetycznie
    return words_sorted

text = "An apple a day keeps the doctor away"
print("Text:", text)
print("Number of words:", word_count(text))
print("Words from the longest to shortest:", longest_to_shortest(text))
print("Words ordered alphabetically:", alphabetically_sorted(text))
