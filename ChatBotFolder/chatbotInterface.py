import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read())

words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open('classes.pkl', "rb"))

model = load_model("chatBotModel.h5")


def cleanUpSentence(sentence):
    sentenceWords = nltk.word_tokenize(sentence)
    sentenceWords = [lemmatizer.lemmatize(word) for word in sentenceWords]
    return sentenceWords


def bagOfWords(sentence):
    sentenceWords = cleanUpSentence(sentence)
    bag = [0] * len(words)
    for w in sentenceWords:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bagOfWords(sentence)
    result = model.predict(np.array([bow]))[0]
    errorThreshold = 0.25
    results = [[i, r] for i, r in enumerate(result) if r > errorThreshold]
    results.sort(key=lambda x: x[1], reverse=True)
    returnList = []
    for r in results:
        returnList.append({"intent": classes[r[0]], "probability": str(r[1])})
    return returnList


def getResponse(intentsList, intents_json):
    tag = intentsList[0]["intent"]
    listOfIntents = intents_json["intents"]
    for i in listOfIntents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result


print('bot go brr')

while True:
    message = input("")
    ints = predict_class(message)
    res = getResponse(ints, intents)
    print(res)