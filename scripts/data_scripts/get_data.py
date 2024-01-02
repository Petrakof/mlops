#!/usr/bin/python3

from catboost.datasets import rotten_tomatoes

# Загрузка данных
train, test = rotten_tomatoes()

# Сохранение данных
train.to_csv("../../data/raw/train.csv", index=False)
test.to_csv("../../data/raw/test.csv", index=False)
