#1.인공지능 : 사람이 하는 행동을 기계가 가능하게 하는 것
#Machine Learning : 통계적 방법을 사용하여 기계가 경험을 통해 개선할 수 있도록 하는 ai techniuq의 하위 집합
#Deep Learning :  다층 신경망의 계산을 가능하게 하는 ML의 부분집합

#problem solviing procedure
#1. Hypothesis H(x) = Wx+b 
#2. Cost H(x) -y
#3. Minimise Cost Minimise cost(W,b)

#Multi variable Problem Solving Procedure
#1.Hypothesis H(x1,x2,x3...) = W1x1+W2x2+W3x3+...
#2.Cost cost(W,b) = sum(H(x1,x2,x3...)-y)^2   

#perceptron
#퍼셉트론으로 XOR를 해결 못한다. =>다층 퍼셉트론으로 XOR을 해결한다. 
#이렇게 복잡한 것을 Back propagation 으로 가중치를 조정한다. 
#Vanishing Gradient : Layer가 많아지면 가중치가 사라지기도 한다.

#keras -The python Deep Learning, Neural Network library
# model 객체 : 'Sequential' model 사용, linaer로 층을 쌓아간다
            #model summary : 모델에 대한 요약을 보여준다
# Deep Learning에서는 ReLU를 많이 사용한다. Sigmoid는 vanising gradient가 많이 발생




#tensorflow 시작
import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt
import math

print(tf.__version__)

#시각화 하기 위한 helper class
# Helper function to display digit images
def show_sample(images, labels, sample_count=25):
  # Create a square with can fit {sample_count} images
  grid_count = math.ceil(math.ceil(math.sqrt(sample_count)))
  grid_count = min(grid_count, len(images), len(labels))
  
  plt.figure(figsize=(2*grid_count, 2*grid_count))
  for i in range(sample_count):
    plt.subplot(grid_count, grid_count, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(images[i], cmap=plt.cm.gray)
    plt.xlabel(labels[i])
  plt.show()


#show the first 25 images in the training dataset.
show_sample(train_images, ['Label : %s' %label for label in train_labels])

#Define constants
batch_size = 128
epochs = 100
num_classes = 10

#Download MNIST dataset
mnist = keras.datasets.mnist(train_images, train_labels),(test_images,test_labels) = mnist.load_data()

#Normalize the input image so that each pixel value is between 0 to 1
train_images = train_images / 255.0
test_images = test_images / 255.0

#Define the model architecture
model = keras.Sequentail([
    keras.layers.Flatten(imput_shape=(28,28)),
    keras.layers.Dense(128,activation=tf.nn.relu),
    keras.layers.Dense(num_classes,activation='softmax')
])
model.complie(optimizer='adam',
             loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
             metrics=['accuracy'])

histoy = model.fit(train_images,train_labels, epochs=epochs, batch_size = batch_size)

#Evaluate the model using test dataset.
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test Accuracy:', test_acc)
