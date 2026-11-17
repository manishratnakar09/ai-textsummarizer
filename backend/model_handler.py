import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2, preprocess_input, decode_predictions)

# Model sirf ek baar server start par load hota hai (first-prediction slowness avoid)
model = MobileNetV2(weights="imagenet")


def predict(img, top=5):
    x = np.expand_dims(np.array(img, dtype="float32"), axis=0)
    x = preprocess_input(x)  # scales pixels to [-1, 1] as MobileNetV2 expects
    preds = model.predict(x, verbose=0)
    results = decode_predictions(preds, top=top)[0]
    return [{"label": name.replace("_", " ").title(),
             "confidence": round(float(p) * 100, 2)} for _, name, p in results]
