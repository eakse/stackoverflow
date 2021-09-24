import nltk
from pprint import pprint


# download data sets
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


dummy_text = '''The European languages are members of the same family.
Their separate existence is a myth.
For science, music, sport, etc, Europe uses the same vocabulary.
The languages only differ in their grammar, their pronunciation and their most common words.
Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators.
To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words.
If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages.
The new common language will be more simple and regular than the existing European languages.
It will be as simple as Occidental; in fact, it will be Occidental.
To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is.
The European languages are members of the same family.
Their separate existence is a myth.
For science, music, sport, etc, Europe uses the same vocabulary.
The languages only differ in their grammar, their pronunciation and their most common words.
Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators.
'''



# use only lowercase in this exception list
my_exceptions = ['a']
ignore_characters = '.,;:'

def create_list(text):
    tokens = nltk.word_tokenize(text)
    # see https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    tagged = nltk.pos_tag(tokens)
    pprint(tagged)

    results = []
    current = ''
    tags = set()
    for word, nltktag in tagged:
        tags.add(nltktag)
        if (
            nltktag == 'DT' or 
            nltktag == 'VB' or
            word.lower() in my_exceptions
        ):
            current = f'{current}{word} '
        elif nltktag not in ignore_characters:
            results.append(f'{current}{word}')
            current = ''
    return results


pprint(create_list(dummy_text))