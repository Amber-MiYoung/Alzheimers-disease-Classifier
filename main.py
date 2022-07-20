
"""

The 4 classes of Aalzheimer's disease included in this dataset are:

Non Demented,
Very Mild Demented,
Mild Demented,
Moderate Demented

"""

import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model


verbose_name = {
    0: "Non Demented",
    1: "Very Mild Demented",
    2: "Mild Demented",
    3: "Moderate Demented",
}

# Load model

#model = load_model("alzheimer_model.h5", compile=False)
model = load_model("model/alzheimer_model..h5")

#model.make_predict_function()

def getPrediction(filename):
    
    SIZE = 128
    test_image = Image.open(filename).convert("L")
    test_image = np.asarray(test_image.resize((SIZE,SIZE)))
    test_image = test_image/255.0      #Scale pixel values
    test_image = test_image.reshape(-1, SIZE, SIZE, 1)

    predict_x = model.predict(test_image)
    classes_x = np.argmax(predict_x, axis=1)

    return verbose_name[classes_x[0]]

test_prediction =getPrediction('mild.jpg')
