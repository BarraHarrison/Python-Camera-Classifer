## Python Camera Classifier

This is a desktop application that uses a live camera feed to train and classify images into two user-defined categories.
The app leverages Support Vector Machines (SVM) from scikit-learn and provides a simple graphical user interface (GUI) built with Tkinter.
It allows users to collect image data, train a model, and predict live camera feed inputs in real time.


## Dependencies

- opencv-python (OpenCV for image processing)
- Pillow (Image processing)
- scikit-learn (Machine learning model)
- tkinter (Built-in for GUI creation)

## How It Works

- The app opens a camera window and prompts you to define two class names.
- Collect images for both classes by clicking the respective buttons.
- Train the model using the collected images.
- Use the Predict button or enable Auto Prediction to classify live camera frames.
- Reset the app at any time to clear data and restart.
