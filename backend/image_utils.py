import io
from PIL import Image, UnidentifiedImageError

ALLOWED = {"jpg", "jpeg", "png"}
MAX_MB = 5


def validate(file):
    """Check extension, emptiness and size. Returns raw bytes (kept in memory only)."""
    name = file.filename or ""
    ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
    if ext not in ALLOWED:
        raise ValueError("Invalid file type. Sirf JPG ya PNG upload karein.")
    data = file.read()
    if not data:
        raise ValueError("File empty hai.")
    if len(data) > MAX_MB * 1024 * 1024:
        raise ValueError(f"File too large. Max size {MAX_MB} MB hai.")
    return data


def prepare(data, size=(224, 224)):
    """Open -> RGB -> resize to model input size."""
    try:
        Image.open(io.BytesIO(data)).verify()
        img = Image.open(io.BytesIO(data)).convert("RGB")
    except (UnidentifiedImageError, OSError):
        raise ValueError("Image corrupt hai ya read nahi ho paayi.")
    return img.resize(size)
