'''
Author: Hivan Du
mail: doo@hivan.me
LastEditors: Hivan Du
LastEditTime: 2023-10-13 13:46:14

Linear Regression:
Use boston house price dataset.
'''

import random
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt

dataset = fetch_openml(name='boston', version=1, as_frame=True, return_X_y=False, parser='pandas')

data = dataset['data']
target = dataset['target']
columns = dataset['feature_names']

dataframe = pd.DataFrame(data)
dataframe['price'] = target

# dataframe.head()

# dfcorr = dataframe.corr()
# import seaborn as sns
# sns.heatmap(dfcorr)

rm = dataframe['RM']
lstat = dataframe['LSTAT']

def linear(x, w, b):
    # vectorized model
    return np.dot(x, w.T) + b

def loss(yhat, y):
    # numpy broadcast numpy 广播方法
    return np.mean((yhat - y) ** 2)

def partial_w(x, y, yhat):
    return np.array([2 * np.mean((yhat - y) * x[0]), 2*np.mean((yhat - y) * x[1])])

def partial_b(x, y, yhat):
    return 2 * np.mean((yhat - y))

def optimize(w, b, x, y, yhat, pw, pb, learning_rate):
    w = w + -1 * pw(x, y, yhat) * learning_rate
    b = b + -1 * pb(x, y, yhat) * learning_rate
    return w, b

def train(model_to_be_train, target, loss, pw, pb):
    w = np.random.random_sample(size=(1, 2))
    b = np.random.random()

    learning_rate=1e-5
    epoch = 200
    losses = []
    batch_size = 10

    for i in range(epoch):
        batch_loss = []
        for batch in range(len(rm)):
            index = random.choice(range(len(rm)))
            rm_x, lstat_x = rm[index], lstat[index]
            x = np.array([rm_x, lstat_x])
            y = target[index]

            yhat = model_to_be_train(x, w, b)
            loss_v = loss(yhat, y)

            batch_loss.append(loss_v)

            w, b = optimize(w, b, x, y, yhat, pw, pb, learning_rate)

            if batch % 100 == 0:
                print('Epoch: {}, Batch: {}, loss: {}'.format(i, batch, loss_v))

        losses.append(np.mean(batch_loss))

    return model_to_be_train, w, b, losses


if __name__ == '__main__':
    model, w, b, losses = train(linear, target, loss, partial_w, partial_b)
    plt.plot(losses)
    predicate = model(np.array([19, 7]), w, b)
    print(predicate)

    plt.show()
