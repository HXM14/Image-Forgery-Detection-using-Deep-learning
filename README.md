<h1 align="center">
 <a href="https://www.linkedin.com/in/hxazem/"><img src="https://user-images.githubusercontent.com/36288517/70856230-91739480-1ee0-11ea-9d85-6acd691642ab.png" alt="IFD"></a>
</h1>


[important Note]  this was my graduation project if you want to reuse it use only training py Files for training Models the whole application will not work as this was for local testing omly and i didn't upload h5 files hich is trained models becuase it was about ~3GB size which is too much you can use kaggle API with colab to train models easily, thanks :) 




# Image-Forgery-Detection-using-Deep-learning
Image processing with convolutional neural network to detect tampering in image 
## Project Description
This project combines different deep learning techniques and image processing techniques to detect image tampering "Copy Move and Splicing" forgery in different image formats (either lossy or lossless formats). We implement two different techniques to detect tampering. I built my own model with  ELA preprocessing and used fine tuning with two different pre-trained Models (VGG19 , VGG15) which are trained using [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true),Image  Forgery detection application gives user the ability to test images with the application trained models **OR** train the application model with new dataset and test images with this new trained model.

You Can watch Application Demo From [Youtube](https://www.youtube.com/watch?v=8les9jfMM-U&t=111s)
### Models
1. Error Level Analysis"ELA" **[1][2]** top Accuracy **(94.54% , epoc12)** You can read More about ELA from [Here!](https://fotoforensics.com/tutorial-ela.php).
2. VGG16 Pretraind Model.
3. VGG19 Pretraind Model.
### Datasets 
Those Models are trained on Many Datasets to Achieve the highest Accuracy 
1. MICCF2000 copyMove Dataset :contains 2000 images (1300 authentic-700 tampered ) color images 2048x1536 pixels.
2. CASIAV2 splicing Dataset :contains 12,614 image (7491 authentic -5123 tampered) color images 384x265 pixels.
### Application Description[libraries , Python version , IDE]
Application coded using GUI library PyQt5, tensorflow Keras API , Numpy ,......etc .IDE used - Pycharm community edition and Anaconda Enviroment with python 3.5.4.
### References
**[1]** Agus Gunawan[1], Holy Lovenia[2], Adrian Hartarto Pramudita[3] "Detection og Image tampering  With ELA and Deep learning" Informatics Engineering School of Electrical and Informatics Engineering, Bandung Institute of Technology.

**[2]** Nor Bakiah A. W.[1], Mohd. Yamani I. I. [2], Ainuddin Wahid A. W. [3], Rosli Salleh [4] "An Evaluation of Error Level Analysis in Image Forensics" in IEEE 5th International Conference on System Engineering and Technology, Aug 2015. 10 - 11, UiTM, Shah Alam, Malaysia.

