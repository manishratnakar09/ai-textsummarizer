# AI Image Recognition App

Web app jo uploaded image me objects identify karta hai using pretrained **MobileNetV2** (ImageNet, 1000 classes) aur top 5 predictions confidence scores ke saath dikhata hai.

## Features
- JPG/PNG upload (max 5 MB) + preview
- One-click prediction, top 5 labels with % and bars
- Low-confidence warning (< 50%)
- Clear errors for invalid / empty / large files
- Optional webcam capture and TXT download
- Images sirf memory me process hoti hain (privacy)

## Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Structure
```
frontend/  index.html, style.css, script.js
backend/   app.py, model_handler.py, image_utils.py
samples/test_images/   tests/test_results.md
```

## How it works
1. Frontend `fetch()` se image `/predict` par bhejta hai
2. Backend validate -> Pillow RGB -> resize 224x224
3. `preprocess_input` normalise -> MobileNetV2 predict
4. Top-N sort + percentage -> JSON

## Limitations
- Sirf 1000 ImageNet categories (faces, text, most logos nahi)
- Similar classes confuse hoti hain (dog breeds)
- Blur, low light, odd angle, cluttered scene se accuracy girti hai
- Drawings/cartoons par often wrong labels
- High confidence = correct answer, ye guarantee nahi
- Single-label model: multi-object images me mixed results

## Future work
Vision API hybrid (`ai_handler.py`), ResNet50 option, Grad-CAM.

## Screenshots
(Yahan add karein)
