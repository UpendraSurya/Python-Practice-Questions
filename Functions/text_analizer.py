'''Create a function analyze_text(text) that takes a block of text as input.
The function should:
Count the number of words in the text (split by whitespace).
Count the number of characters (excluding whitespaces).
Find the most frequent word (you can assume case-insensitive matching for simplicity).
Return a dictionary containing these counts and the most frequent word.'''

def analyze_text(text):
    wcount = len(text.split())

    count = len(text.replace(" ", ""))

    words = text.lower().split()
    wordf = {}
    for word in words:
        wordf[word] = wordf.get(word, 0) + 1
    most_frequent_word = max(wordf, key=wordf.get)

    result = {
        "word_count": wcount,
        "char_count": count,
        "most_frequent_word": most_frequent_word
    }
    return result


text = "This is a sample text. It contains multiple words and characters."
result = analyze_text(text)
print(result)

#%%
