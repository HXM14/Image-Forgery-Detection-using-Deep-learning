# Image-Forgery-Detection-using-Deep-learning
image processing with convolutional neural network to Detect tampring in image 
## Project Description
This Project Compine Different Deep learning techniques and image processing techniques to detect image tampring "Copy Move and Splicing" Forgery in Different image Formats either lossy or lossless formats we implement two different techniques to detect tampring i build my own Model with  ELA preprocessing and use fine tuning with two different pretraind Models (VGG19 , VGG15) those Models traind using [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true),Image Forgery Detection Application give user the ability to test images with Application trained Models **OR** Train the Application Model with New Dataset and Test images with this New Trained Mode.

You Can watch Application Demo From [Youtube](https://www.youtube.com/watch?v=8les9jfMM-U&t=111s)

### Models
1. Error Level Analysis"ELA"[1][2] top Accuracy **(94.54% , epoc12)** You Can read More about ELA Frome [Here!](https://fotoforensics.com/tutorial-ela.php).
2. VGG16 Pretraind Model.
3. VGG19 Pretraind Model.

### Datasets
Those Models traind on Many Datasets to Achive Highest Accuracy 
1. MICCF2000 copyMove Dataset :contains 2000 images (1300 authentic-700 tampered ) color images 2048x1536 pixels.
2. CASIAV2 splicing Dataset :contains 12,614 image (7491 authentic -5123 tampered) color images 384x265 pixels.

### Application Description[libraries , Python version , IDE]

Application coded using GUI library PyQt5 , tensorflow Keras API , Numpy ,......etc .IDE used Pycharm community edition and Anaconda Enviroment with python 3.5.4.

#### References

**[1]** Agus Gunawan[1], Holy Lovenia[2], Adrian Hartarto Pramudita[3] "Detection og Image tampering  With ELA and Deep learning" Informatics Engineering School of Electrical and Informatics Engineering, Bandung Institute of Technology
**[2]** Nor Bakiah A. W.[1], Mohd. Yamani I. I. [2], Ainuddin Wahid A. W. [3], Rosli Salleh [4] "An Evaluation of Error Level Analysis in Image Forensics" in IEEE 5th International Conference on System Engineering and Technology, Aug 2015. 10 - 11, UiTM, Shah Alam, Malaysia.

