import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer

dataset = pd.read_csv('dataset-rough.csv')

#x is the list of datapoints
#y is the index
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#converts the data to binary
l = LabelBinarizer()
y = l.fit_transform(y)

#Define the neural network
#42 input nodes
#relu activation function
#softmax for output layer
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1536, input_shape=(21,)))
model.add(tf.keras.layers.Activation("relu"))
model.add(tf.keras.layers.Dense(768))
model.add(tf.keras.layers.Activation("relu"))
model.add(tf.keras.layers.Dense(384))
model.add(tf.keras.layers.Activation("relu"))
model.add(tf.keras.layers.Dense(128))
model.add(tf.keras.layers.Activation("relu"))
model.add(tf.keras.layers.Dense(y.shape[1]))
model.add(tf.keras.layers.Activation("softmax"))

opt = tf.keras.optimizers.SGD(learning_rate=0.01)
model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])
model.fit(x, y, batch_size=1, epochs=100)
model.save("model.h5")