from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from keras import models
from keras import layers
import itertools
from sklearn.metrics import confusion_matrix
from keras import optimizers
from PIL import Image
import pandas as pd
from keras.applications.vgg16 import VGG16
import os
import random

def train_VGG16_Model(csv_file , lr , ep):
    def Read_image(path):
      image = Image.open(path).convert('RGB')
      return image

    X = []
    Y = []
    dataset = pd.read_csv(csv_file)
    for index, row in dataset.iterrows():
        X.append(array(Read_image(row[0]).resize((100, 100))).flatten() / 255.0)
        Y.append(row[1])

    X = np.array(X)
    Y = to_categorical(Y, 2)
    X = X.reshape(-1, 100, 100, 3)

    X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.20, random_state=5)

    vgg_conv = VGG16(weights='imagenet', include_top=False, input_shape=(100, 100, 3))

    model = models.Sequential()
    #Note
    for layer in vgg_conv.layers[:-5]:
        layer.trainable = False

    for layer in vgg_conv.layers:
        print(layer, layer.trainable)

    model.add(vgg_conv)
    model.add(layers.Flatten())
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dropout(0.25))
    model.add(layers.Dense(2, activation='softmax'))

    model.compile(loss='binary_crossentropy',
                  optimizer=optimizers.RMSprop(lr=lr),
                  metrics=['accuracy'])
    epochs = ep
    batch_size = 20

    history = model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, validation_data=(X_val, Y_val),verbose=2)
    fig, ax = plt.subplots(3, 1)
    ax[0].plot(history.history['loss'], color='b', label="Training loss")
    ax[0].plot(history.history['val_loss'], color='r', label="validation loss", axes=ax[0])
    legend = ax[0].legend(loc='best', shadow=True)

    ax[1].plot(history.history['acc'], color='b', label="Training accuracy")
    ax[1].plot(history.history['val_acc'], color='r', label="Validation accuracy")
    legend = ax[1].legend(loc='best', shadow=True)

    def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i, j], horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

    # Predict the values from the validation dataset
    Y_pred = model.predict(X_val)
    # Convert predictions classes to one hot vectors
    Y_pred_classes = np.argmax(Y_pred, axis=1)
    # Convert validation observations to one hot vectors
    Y_true = np.argmax(Y_val, axis=1)
    # compute the confusion matrix
    confusion_mtx = confusion_matrix(Y_true, Y_pred_classes)
    # plot the confusion matrix
    plot_confusion_matrix(confusion_mtx, classes=range(2))

    image_path = os.getcwd()+"\\Figures"
    Models_path = os.getcwd()+"\\Re_Traind_Models"
    file_number =random.randint(1, 1000000)
    plot_Name = image_path+"\\VGG16_"+str(file_number)+".png"
    Model_Name = Models_path+"\\VGG16_"+str(file_number)+".h5"
    plt.savefig(plot_Name , transparent =True , bbox_incehs="tight" , pad_inches = 2 , dpi = 50)
    model.save(Model_Name)
    return plot_Name , Model_Name

