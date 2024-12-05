import cv2
import numpy as np
import tensorflow as tf

img = np.zeros((280, 280, 3), np.uint8)
drawing = False

def draw(event, x, y, flags, param):
    global ix, iy, drawing, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (ix, iy), (x, y), (255, 255, 255), 15)
            ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # Preprocess the image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (32, 32))
        normalized = resized / 255.0
        reshaped = np.reshape(normalized, (1, 32, 32, 1))

        # Make a prediction
        prediction = model.predict(reshaped)
        predicted_digit = np.argmax(prediction)

        # Clear the image and display the prediction
        img = np.zeros((280, 280, 3), np.uint8)
        cv2.putText(img, str(predicted_digit), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Image', img)

# Load the model
model = tf.keras.models.load_model('mnist.h5')  # Replace with your model path

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 600, 600)  # Adjust dimensions as needed
cv2.setMouseCallback('Image', draw)

while True:
    cv2.imshow('Image', img)

    # If 'q' is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cv2.destroyAllWindows()
#%%
