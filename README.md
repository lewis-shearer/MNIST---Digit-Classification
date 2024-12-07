# 🖍️ Handwritten Digit Classifier
A TensorFlow-based Convolutional Neural Network (CNN) model that achieves <b>99% accuracy</b> in handwritten digit classification. This project also includes interactive applications to test predictions using custom handwritten inputs or webcam data.

<h2>🚀 Features</h2>

<b>CNN Architecture:</b>

  - Convolutional layer with ReLU activation
  - MaxPooling layer
  - Convolutional layer with ReLU activation
  - MaxPooling layer
  - Flattening layer
  - 2 Fully-connected Dense layers<br>
  <br>
<b>Interactive Tools:</b><br>
- <b>'app.py'</b>: Opens a window for users to handwrite their own digits and see predictions in real-time.<br>
- <b>'webcam.py'</b>: Uses the webcam to capture handwritten digits for prediction. (Currently under improvement)
 

<h2>🛠️ Technologies</h2><br>
- <b>TensorFlow<b>: For building and training the CNN model.<br>
- <b>OpenCV<b>: For webcam data capture and image processing.<br>


  
<h2>📦 Installation</h2>
<ol>
  <li><b>Clone the repository:</b></li>


  <code>git clone https://github.com/lewis-shearer/handwritten-digit-classifier.git
   cd handwritten-digit-classifier</code>


<li><b>Install dependencies:</b></li>

Ensure you have Python installed, then run:
<code>pip install -r requirements.txt</code>
<li><b>Prepare the environment:</b></li>

- Ensure TensorFlow is properly installed and supports your hardware (GPU support is recommended for faster training).
- Test OpenCV and Tkinter installations.

</ol>



<h2>📘 Usage</h2>
<b>1. Get the CNN Model</b><br>
Run the training notebook recreate the model:<br>
- <b>'mnist.ipynb'</b><br>
Or use the pre trained one:<br>
- <b>'mnist.h5'</b><br><br>


<b>2. Handwriting Interface</b><br>
Launch the handwriting window:
<code>python app.py</code>
Draw a digit in the window to see the model's prediction.

<b>3. Webcam Digit Capture (*Under Development*)</b><br>
Test the webcam interface:
<code>python webcam.py</code>
- The script will capture frames from your webcam and attempt to predict handwritten digits.
- *Note*: Prediction accuracy needs further enhancement in this module.

  
<h2>🌟 Example Results</h2>
<b>App Interface Example:</b>

- User writes the digit <b>'5'</b>.
- Model predicts: <b>'5'</b>.
  
<b>Training Performance:</b>

- Achieved <b>99% accuracy<b> on the MNIST dataset.



<h2>📝 Future Improvements</h2>

- 🛠️ Improve the accuracy of the **'webcam.py'** predictions.
- 🌟 Add support for multi-digit recognition.
- 🎨 Enhance the UI for better usability.

  
**Enjoy exploring the world of digit recognition! ✨**

