import textacy 
from textacy import extract
import spacy
import pandas as pd


def extract_direct(text):
    extracted = pd.DataFrame()
    for i in text:
        try:
            doc = nlp(i)
            a = ex.direct_quotations(doc)
            for item in a:
                mined = {'speaker': item.speaker, 'cue': item.cue, 'content': item.content}
                extracted = extracted.append(mined, ignore_index = True)
                break
        except ValueError:
            continue
    contents = news_only['index']
    extracted = pd.concat([extracted, contents], ignore_index=True)
    return(extracted)


extract_direct(dataframe['Body'])