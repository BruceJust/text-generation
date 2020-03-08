# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 20:02
# @Author  : Bruce
# @Email   : daishaobing@outlook.com
# @File    : test
# @Project: 模仿丘吉尔人物自传写作生成模型

import tensorflow.keras as k
import nltk
import numpy as np
import argparse




def test():
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('-m', '--mode', default='word')
    parser.add_argument('-i', '--input', default=None)
    args = parser.parse_args()
    mode = args.mode
    input = args.input
    print(mode)
    print(type(mode))
    if input:
        init = input
    else:
        init = 'His object in coming to New York was to engage officers for'
    print('Input sentence: ', init)
    if mode == 'word':
        to_index_file = './data/word_to_index.txt'
        index_to_file = './data/index_to_word.txt'
        model_file = './model/model_word.h5'
        seq_length = 10
    elif mode == 'char':
        to_index_file = './data/char_to_index.txt'
        index_to_file = './data/index_to_char.txt'
        model_file = './model/model_char.h5'
        seq_length = 50
        print('char_ty')
    else:
        return "Wrong mode!"
    with open(to_index_file, 'r') as fp:
        str_to_index = eval(fp.read())
    with open(index_to_file, 'r') as fp:
        index_to_str = eval(fp.read())
    model = k.models.load_model(model_file)

    init = init.lower()
    rounds = 200
    for i in range(rounds):
        new = predict_next(string_to_index(init, str_to_index, seq_length, mode), model, index_to_str)
        if mode == 'word':
            init = init + ' ' + new
        else:
            init += new
    print('Output sentence: ', init)


# 预测
def predict_next(input_array, model, index_to_str):
    y = model.predict(input_array)
    index = y.argmax()
    str = index_to_str[index]
    return str

# 输入文本预处理
def string_to_index(raw_input, str_to_index,seq_length, mode='word'):
    if mode == 'word':
        raw_input = nltk.word_tokenize(raw_input)
        res = []
        for word in raw_input[len(raw_input) - seq_length:]:
            res.append(str_to_index[word])
        res = np.reshape(res, (-1, seq_length))
        return res
    if mode == 'char':
        res = []
        for c in raw_input[len(raw_input) - seq_length:]:
            res.append(str_to_index[c])
        res = np.reshape(res, (1, seq_length, 1))
        res = res / float(len(str_to_index.keys()))
        return res

if __name__ == '__main__':
    test()