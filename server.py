import re
import nltk
from flask import Flask, request
from flask_cors import cross_origin

app = Flask(__name__)


# TODO: Clean up
def summarize(article_text):
    article_text = re.sub(r"\[[0-9]*\]", " ", article_text)
    article_text = re.sub(r"\s+", " ", article_text)

    formatted_article_text = re.sub("[^a-zA-Z]", " ", article_text)
    formatted_article_text = re.sub(r"\s+", " ", formatted_article_text)

    sentence_list = nltk.sent_tokenize(article_text)
    stopwords = nltk.corpus.stopwords.words("english")

    word_frequencies = {}

    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
        maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maximum_frequncy
        sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(" ")) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    import heapq

    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    return " ".join(summary_sentences)


def check_nltk_resources():
    try:
        nltk.data.find("tokenizers/punkt")
        nltk.data.find("corpora/stopwords")
    except LookupError:
        nltk.download("punkt")
        nltk.download("stopwords")


@app.route("/summarize", methods=["POST"])
@cross_origin(origins=["*"])
def text_summarize():
    article_text = request.get_json()

    check_nltk_resources()

    summary = summarize(article_text)

    return dict(data=summary)
