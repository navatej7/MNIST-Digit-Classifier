# MNIST-digit-recognizer-app
A deep learning model trained on the MNIST dataset to recognize handwritten digits (0–9). This project demonstrates image classification using neural networks in Python, with preprocessing, model training, and evaluation included. Useful as a beginner-friendly introduction to computer vision and deep learning concepts.


This project implements a handwritten digit recognition application using deep learning and interactive GUI components. The core functionality involves training a convolutional neural network (CNN) on the MNIST dataset and deploying it using a Pygame window that allows users to draw digits with mouse input for real-time prediction.

Features: 
MNIST Dataset Training; 
The CNN model is built using Keras and trained on the MNIST handwritten digit dataset. The dataset consists of 60,000 training images and 10,000 testing images of handwritten digits (0-9). 

Preprocessing;  
Images are normalized for pixel intensity, reshaped to fit the CNN input shape, and labels are one-hot encoded to match output classes. 

CNN Architecture; 
The model includes convolutional layers, max pooling, dropout for regularization, and fully connected dense layers with a softmax output for 10-class classification. 

Model Training and Validation; 
Training uses the Adam optimizer, categorical crossentropy loss, and includes callbacks for early stopping and model checkpoints to save the best model based on validation accuracy. 

Model Saving and Loading, 
The trained model is saved as bestmodel.h5 and reloaded for inference in the Pygame application. 

Pygame Drawing Interface, 
Users can write digits with the mouse in a Pygame window. The app tracks drawing input to create an image region containing the digit. 

Image Processing for Prediction, 
The drawn digit is resized and normalized to fit the CNN input requirements before prediction. 

Real-time Prediction; 
After completing a digit drawing, the app predicts the digit and displays the predicted class label on the Pygame window. 

Restart Button; 
A button allows users to clear the drawing surface and draw a new digit for fresh predictions. 

Installation and Setup: 
Install required Python packages; 
pip install numpy matplotlib keras tensorflow pygame opencv-python, 
Run the training notebook or script to generate the trained model file (bestmodel.h5), 
Run the Pygame script to launch the interactive digit recognizer. 

Usage: 
Use the mouse in the Pygame window to draw a digit (0-9), 
Release the mouse button to trigger prediction, 
View the predicted digit label on the screen, 
Press the "Restart" button to clear the canvas and draw again, 
Close the Pygame window or press Esc to exit.

File Structure: 
train_model.ipynb or equivalent: Jupyter notebook for training the CNN model, 
bestmodel.h5: Saved Keras model after training, 
digit_recognizer.py: Pygame application that allows interactive digit drawing and prediction. 



