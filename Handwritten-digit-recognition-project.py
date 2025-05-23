# -*- coding: utf-8 -*-
"""Day5_GDGC

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EK7396s_-FgLKLSQOTbFKGrq1OE-4d5r
"""

# Commented out IPython magic to ensure Python compatibility.
import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
# %matplotlib inline

(x_train,y_train),(x_test,y_test) = keras.datasets.mnist.load_data()  #mnist dataset for handwritten digits

len(x_train)

y_train

x_train

x_test

x_train[0].shape  #black and white image size=> (28 * 28)

x_train[5]

plt.matshow(x_train[5])     #To see image at this index

y_train[5]

x_train = x_train/255
x_test = x_test/255    #dividing by 255 as max_size of image pixel is 255 => To normalize the datapoints

"""ANN Model without hidden layer"""

model = keras.Sequential([keras.layers.Flatten(input_shape=(28,28)),keras.layers.Dense(10,activation='sigmoid')])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

model.fit(x_train,y_train,epochs=5)

model.evaluate(x_test,y_test)

plt.matshow(x_test[0])

x_test[0]

y_test[0]

y_predict = model.predict(x_test)

np.argmax(y_predict[0])

y_pred_lables=[np.argmax(i) for i in y_predict]
y_pred_lables

cm = tf.math.confusion_matrix(labels=y_test,predictions=y_pred_lables)
cm

import pandas as pd
import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True,fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')

"""ANN with hidden layer"""

model = keras.Sequential([keras.layers.Flatten(input_shape=(28,28)),
                          keras.layers.Dense(100,activation='relu'),
                          keras.layers.Dense(10,activation='sigmoid')
                          ])

model.compile(
    optimizer = 'adam',
    loss = "sparse_categorical_crossentropy",
    metrics = ['accuracy']
)

model.fit(x_train,y_train,epochs=5)

y_predict = model.predict(x_test)

y_pred_lables=[np.argmax(i) for i in y_predict]
y_pred_lables

cm=tf.math.confusion_matrix(labels=y_test,predictions=y_pred_lables)

import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True,fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')

loss, accuracy = model.evaluate(x_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")