# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 22:01
# @Author  : Bruce
# @Email   : daishaobing@outlook.com
# @File    : train_char
# @Project: 模仿丘吉尔人物自传写作生成模型

import numpy as np
import tensorflow as tf
import tensorflow.keras as k


gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)

raw_text = open('data/Winston_Churchil.txt', 'r', encoding='utf-8').read()
raw_text = raw_text.lower()

# 统计字符总数
chars = sorted(list(set(raw_text)))
print(len(raw_text))
print(len(chars))

char_to_index = dict((c, i) for i, c in enumerate(chars))
index_to_char = dict((i, c) for i, c in enumerate(chars))


# 以输入字符长度为50构建训练集
seq_length = 50

x = []
y = []
for i in range(len(raw_text) - seq_length):
    input = raw_text[i:i + seq_length]
    target = raw_text[i+seq_length]
    x.append([char_to_index[char] for char in input])
    y.append(char_to_index[target])

# print(x[:3])
# print(y[:3])

n_patterns = len(x)
n_vocab = len(chars)

x = np.reshape(x, (n_patterns, seq_length, 1))
x = x /  float(n_vocab)
y = k.utils.to_categorical(y)  # one-hot

# print(x[10][:10])
# print(y[10])
# print(y.shape)


# 构建模型并训练
model = k.Sequential([
    k.layers.Bidirectional(k.layers.LSTM(256, input_shape=(x.shape[1], x.shape[2]))),
    k.layers.Dropout(0.2),
    k.layers.Dense(y.shape[1], activation='softmax'),
])
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(x,y, epochs=50, batch_size=1024)

# save model and dict
model.save('./model/model_char.h5')
with open('./data/char_to_index.txt', 'w') as fp:
    fp.write(str(char_to_index))
with open('./data/index_to_char.txt', 'w') as fp:
    fp.write(str(index_to_char))
