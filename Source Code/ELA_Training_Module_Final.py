from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.optimizers import RMSprop
from pylab import *
from PIL import Image, ImageChops, ImageEnhance
import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
import os
import random

def train_Ela_Model(csv_file , lr , ep):
    def convert_to_ela_image(path, quality):
        filename = path
        resaved_filename = filename.split('.')[0] + '.resaved.jpg'
        im = Image.open(filename).convert('RGB')
        im.save(resaved_filename, 'JPEG', quality=quality)
        resaved_im = Image.open(resaved_filename)
        ela_im = ImageChops.difference(im, resaved_im)
        extrema = ela_im.getextrema()
        max_diff = max([ex[1] for ex in extrema])
        if max_diff == 0:
            max_diff = 1
        scale = 255.0 / max_diff

        ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
        return ela_im


    dataset = pd.read_csv(csv_file)
    X = []
    Y = []
    for index, row in dataset.iterrows():
        X.append(array(convert_to_ela_image(row[0], 90).resize((128, 128))).flatten() / 255.0)
        Y.append(row[1])

    X = np.array(X)
    Y = to_categorical(Y, 2)
    X = X.reshape(-1, 128, 128, 3)
    X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.1, random_state=5, shuffle=True)

    model = Sequential()

    model.add(Conv2D(filters=32, kernel_size=(5, 5), padding='valid', activation='relu', input_shape=(128, 128, 3)))
    model.add(Conv2D(filters=32, kernel_size=(5, 5), strides=(2, 2), padding='valid', activation='relu'))
    model.add(MaxPool2D(pool_size=2, strides=None, padding='valid', data_format='channels_last'))
    model.add(Dropout(0.25))

    model.add(Flatten())

    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.50))
    model.add(Dense(2, activation="softmax"))
    model.summary()

    optimizer = RMSprop(lr=lr, rho=0.9, epsilon=1e-08, decay=0.0)
    model.compile(optimizer=optimizer, loss="categorical_crossentropy", metrics=["accuracy"])

    #early_stopping = EarlyStopping(monitor='val_acc', min_delta=0, patience=2, verbose=0, mode='auto')

    epochs = ep
    batch_size = 5

    history = model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, validation_data=(X_val, Y_val), verbose=2)

    fig, ax = plt.subplots(3, 1)
    ax[0].plot(history.history['loss'], color='b', label="Training loss")
    ax[0].plot(history.history['val_loss'], color='r', label="validation loss", axes=ax[0])
    legend = ax[0].legend(loc='best', shadow=True)

    ax[1].plot(history.history['acc'], color='b', label="Training accuracy")
    ax[1].plot(history.history['val_acc'], color='r', label="Validation accuracy")
    legend_ = ax[1].legend(loc='best', shadow=True)


    def plot_confusion_matrix(cm_, classes, normalize=False, title_='Confusion matrix', cmap=cm.get_cmap("Spectral")):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        plt.imshow(cm_, interpolation='nearest', cmap=cmap)
        plt.title(title_)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes)
        plt.yticks(tick_marks, classes)

        if normalize:
            cm_ = cm_.astype('float') / cm_.sum(axis=1)[:, np.newaxis]

        thresh = cm_.max() / 2.
        for i, j in itertools.product(range(cm_.shape[0]), range(cm_.shape[1])):
            plt.text(j, i, cm_[i, j],
                     horizontalalignment="center",
                     color="white" if cm_[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')


    Y_pred = model.predict(X_val)
    Y_pred_classes = np.argmax(Y_pred, axis=1)
    Y_true = np.argmax(Y_val, axis=1)

    confusion_mtx = confusion_matrix(Y_true, Y_pred_classes)
    plot_confusion_matrix(confusion_mtx, classes=range(2))

    #plt.show()
    image_path = os.getcwd()+"\\Figures"
    Models_path = os.getcwd()+"\\Re_Traind_Models"
    file_number =random.randint(1, 1000000)
    plot_Name = image_path+"\\ELA_"+str(file_number)+".png"
    Model_Name = Models_path+"\\ELA_"+str(file_number)+".h5"
    plt.savefig(plot_Name , transparent =True , bbox_incehs="tight" , pad_inches = 2 , dpi = 50)
    model.save(Model_Name)
    return plot_Name , Model_Name

