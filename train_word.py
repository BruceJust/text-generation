# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 23:03
# @Author  : Bruce
# @Email   : daishaobing@outlook.com
# @File    : train_word
# @Project: 模仿丘吉尔人物自传写作生成模型

import numpy as np
import tensorflow as tf
import tensorflow.keras as k
import nltk
import re
import os

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)

raw_text = open('data/Winston_Churchil.txt', 'r', encoding='utf-8').read()
raw_text = raw_text.lower()
raw_text = re.sub('\ufeff', ' ', raw_text)

nltk.download('punkt')
sentensor = nltk.data.load('tokenizers/punkt/english.pickle')

sents = sentensor.tokenize(raw_text)  # 分成句子
# print(sents[:2])

corpus = []
for sen in sents:
    corpus.append(nltk.word_tokenize(sen))  # 分成词

# print(len(corpus))
# print(corpus[:2])

raw_input = [item for sublist in corpus for item in sublist]  # 将多句话汇总用于构建训练集


# 构建词表即字典
vocab = []
for word in raw_input:
    if word not in vocab:
        vocab.append(word)

# print(len(vocab))

word_to_index = dict((w, i) for i, w in enumerate(vocab))
index_to_word = dict((i, w) for i, w in enumerate(vocab))

# 以输入文本长度为10构建训练集
seq_length = 10
x = []
y = []
for i in range(len(raw_input) - seq_length):
    input = raw_input[i:i + seq_length]
    target = raw_input[i + seq_length]
    x.append([word_to_index[word] for word in input])
    y.append(word_to_index[target])
x = np.reshape(x, (-1, seq_length))

y = k.utils.to_categorical(y)  # one-hot

model_dir = 'model'
if not os.path.exists(model_dir):
    os.mkdir(model_dir)

# 构建模型及训练
model = k.Sequential([
    k.layers.Embedding(len(vocab) + 1, 256),
    k.layers.Bidirectional(k.layers.LSTM(256,)),
    k.layers.Dropout(0.2),
    k.layers.Dense(len(vocab), activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam')

model.fit(x, y, batch_size=1024, epochs=50)

# save model and dict
model.save('./model_word.h5')
with open('./data/word_to_index.txt', 'w') as fp:
    fp.write(str(word_to_index))
with open('./data/index_to_word.txt', 'w') as fp:
    fp.write(str(index_to_word))
