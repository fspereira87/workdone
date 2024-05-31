
# Dataset Loading and Model Accuracy Issue

## Dataset Loading Issue


While working on a traffic sign classification project, an error was encountered during dataset loading. The addition of the following code snippet revealed that only 5 images were successfully loaded from the dataset:

python
img = cv2.imread(img_path)
if img is None:
    print(f"Error loading image: {img_path}. Skipping...")
    continue

The error was caused by an problem uploading a big amount of data at once. The upload was segmented in smaller parts, and the error solved.


Model Architectures:

1st Model (64 units): Test accuracy: 85%, 87%, 88% for X=1, 2, 3.
2nd Model (128 units): Similar performance to 1st model.
3rd Model (512 units): Test accuracy: 89%, 90%, 87% for X=1, 2, 3. Shows signs of overfitting.

Model (512 units):

Training accuracies around 92-93%, test accuracies 89-91%.
Increasing layers didn't significantly improve results.

Convolutional Layers:

Adding 16 filter, 3x3 convolution to tiny model increased accuracy to 99%.
Increasing filter number didn't drastically improve accuracy but increased training time.
Filter size changes (3x3 to 5x5 or 7x7) had minimal impact.
Pooling Layers:

2x2 Max pooling on tiny model increased accuracy to 99%, switching to Average Pooling slightly decreased accuracy.
Large-1 model with 2x2 Max pooling had 99% accuracy, but larger models didn't see significant improvement.

Multiple Convolution and Pooling Layers:

Better results with higher filter numbers.
Adding more than two layers didn't significantly benefit accuracy.

Dropout:

Adding dropout helped avoid overfitting.
Higher dropout percentages tended to worsen training fit and loss.
Large models may need lower dropout percentages for effective training.

Choosing Best Model:

333/333 - 3s - loss: 0.0950 - accuracy: 0.9751 - 3s/epoch - 9ms/step - two sets of convolutional and max-pooling. No drop out

333/333 - 3s - loss: 0.0632 - accuracy: 0.9863 - 3s/epoch - 10ms/step - two sets of convolutional and max-pooling. 0.5 Drop out

333/333 - 3s - loss: 0.0350 - accuracy: 0.9921 - 3s/epoch - 10ms/step - two sets of convolutional and max-pooling. 0.65 Drop out

333/333 - 3s - loss: 0.0388 - accuracy: 0.9913 - 3s/epoch - 10ms/step - two sets of convolutional and max-pooling. 0.70 Drop out


Result: two sets of convolutional and max-pooling. 0.65 Drop out


Video URL: https://youtu.be/JLNhXufHjWA
