import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.initializers import RandomNormal
import numpy
#input?
X = []

# fix random seed for reproducibility
numpy.random.seed(7)

model = Sequential()
model.add(Dense(11*11*2, input_dim=11*11, activation='relu'))
model.add(Dense(11*11, activation='relu'))
model.add(Dense(4, activation='sigmoid'))


model.fit(X,
          Y,
          epochs=10,
         
         shuffle=True)

model.predict(X)