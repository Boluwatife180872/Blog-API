import uuid  # generates unique filenames so uploaded images don't overwrite one another
from io import BytesIO  # lets Python read image bytes as if they were a file.
from pathlib import Path  # makes it easier to create and work with file paths.

from PIL import Image, ImageOps  # for image processing & operations
# Image - opens and saves images using Pillow
# ImageOps - provides image operations such as correcting orientation and resizing/cropping.

# directory to store profile pictures
PROFILE_PICS_DIR = Path("media/profile_pics")

# Process Image Function


def process_profile_image(content: bytes) -> str:
    with Image.open(BytesIO(content)) as original:
        img = ImageOps.exif_transpose(original)

        img = ImageOps.fit(img, (300, 300), method=Image.Resampling.LANCZOS)

        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB")

        filename = f"{uuid.uuid4().hex}.jpg"
        filepath = PROFILE_PICS_DIR / filename

        PROFILE_PICS_DIR.mkdir(parents=True, exist_ok=True)

        img.save(filepath, "JPEG", quality=85, optimize=True)

    return filename

# Delete Profile Image Function

def delete_profile_image(filename: str | None) -> None:
    if filename is None:
        return

    filepath = PROFILE_PICS_DIR / filename
    if filepath.exists():
        filepath.unlink()
