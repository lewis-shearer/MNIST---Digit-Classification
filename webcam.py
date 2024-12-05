import cv2
import numpy as np
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('mnist.h5')

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Frame', frame)

    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):  # Capture frame on 'c' key press
        # Convert the frame to grayscale and resize it to 32x32 pixels
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (32, 32))
        normalized = resized / 255.0
        reshaped = np.reshape(normalized, (1, 32, 32, 1))

        # Make a prediction
        prediction = model.predict(reshaped)
        predicted_digit = np.argmax(prediction)

        # Display the prediction on the frame
        cv2.putText(frame, str(predicted_digit), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Frame', frame)
        cv2.waitKey(0)  # Wait for key press to continue

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
#%%

#%%

#%%
