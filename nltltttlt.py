import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from pprint import pprint


# read the text into a single string.
with open("book1.txt") as infile:
    text = ' '.join(infile.readlines())
words = word_tokenize(text)
words = [word.lower() for word in words if word.isalpha()]


results = []
for word in words:
    # you were using words instead of word below
    token = WordNetLemmatizer().lemmatize(word, "v")
    if token not in results:
        results.append(token)
results.sort()


pprint(results)
print(len(results))
with open("nltk_data.csv", "w") as outfile:
    outfile.writelines(results)
