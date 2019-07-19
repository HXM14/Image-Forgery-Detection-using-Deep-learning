# Image-Forgery-Detection-using-Deep-learning
image processing with convolutional neural network to Detect tampring in image 
## Project Description
This Project Compine Different Deep learning techniques and image processing techniques to detect image tampring "Copy Move and Splicing" Forgery in Different image Formats either lossy or lossless formats we implement two different techniques to detect tampring i build my own Model with  ELA preprocessing and use fine tuning with two different pretraind Models (VGG19 , VGG15) those Models traind using [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true),Image Forgery Detection Application give user the ability to test images with Application trained Models **OR** Train the Application Model with New Dataset and Test images with this New Trained Mode.

You Can watch Application Demo From [Youtube](https://www.youtube.com/watch?v=8les9jfMM-U&t=111s)

**Models**
1. Error Level Analysis"ELA" top Accuracy **(94.54% , epoc12)** You Can read More about ELA Frome [Here!](https://fotoforensics.com/tutorial-ela.php).
2. VGG16 Pretraind Model.
3. VGG19 Pretraind Model.

**Datasets**
Those Models traind on Many Datasets to Achive Highest Accuracy 
1. MICCF2000 copyMove Dataset.
2. CASIAV2 splicing Dataset.

**Application Description[libraries , Python version , IDE]**

Application coded using GUI library PyQt5 , tensorflow Keras API , Numpy ,......etc .IDE used Pycharm community edition and Anaconda Enviroment with python 3.5.4.
