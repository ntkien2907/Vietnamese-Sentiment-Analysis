import pickle
import numpy as np
from tensorflow.keras.preprocessing import sequence as sq
from config import *
from preprocess import *

with open(WORD2ID_PKL, 'rb') as f:
  word2id = pickle.load(f)

def indexing(sentence, word2id):
  words = sentence.split()
  ids = [word2id[word] for word in words]
  return np.array(ids)

def LSTM_CNN_predict(text, model):
  text = preprocess_sentence(text)
  x = indexing(text, word2id)
  x = sq.pad_sequences([x], maxlen=SEQUENCE_LENGTH)
  result = model.predict(x)
  return np.argmax(result)