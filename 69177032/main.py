import pandas as pd


test_df = pd.DataFrame(
    {
        "_id": ["1a", "2b", "3c", "4d"],
        "column": [
            "und der in zu",
            "Kompliziertereswort something",
            "Lehrerin in zu [Buch]",
            "Buch (Lehrerin) kompliziertereswort",
        ],
    }
)


wordlist = {
    "und": 20,
    "der": 10,
    "in": 40,
    "zu": 10,
    "Kompliziertereswort": 2,
    "Buch": 5,
    "Lehrerin": 5,
}
# convert keys to lowercase
wordlist = {key.lower(): value for key, value in wordlist.items()}


def get_point_average(sentence: str):
    if len(sentence.split()) == 0:
        return 0

    # turn to lowercase and remove everything except letters
    sentence = sentence.lower()
    whitelist = set("abcdefghijklmnopqrstuvwxyz ")
    sentence = "".join(filter(whitelist.__contains__, sentence))

    points = 0
    for word in sentence.split():
        if word in wordlist:
            points += wordlist[word]
    return points / len(sentence.split())


def get_point_average_column(column: list) -> list:
    result = []
    for row in column:
        result.append(get_point_average(row))
    return result


