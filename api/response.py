import pandas as pd
from nltk import ngrams
from difflib import SequenceMatcher
import datetime

df = pd.read_csv('data.csv')


def calculate_similarity(text1, text2, n):
    ngrams_text1 = set(ngrams(text1, n))
    ngrams_text2 = set(ngrams(text2, n))
    intersection = len(ngrams_text1.intersection(ngrams_text2))
    union = len(ngrams_text1) + len(ngrams_text2) - intersection
    similarity_score = intersection / union
    return similarity_score


def answer(q):
    text1 = q
    n = 3
    score = 0
    index = 0

    for i in df['questions']:
        similarity_score = calculate_similarity(text1.lower(), i.lower(), n)
        if score < similarity_score:
            score = similarity_score
            index = df['questions'].tolist().index(i)
            if score > 0.85:
                print(0)
                break
    if score < 0.15:
        return None
    return df['answers'][index]


    