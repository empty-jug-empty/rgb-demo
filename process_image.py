from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
import os
import numpy as np

# Register HEIC opener with Pillow
register_heif_opener()

def process_image(input_path, output_path, target_size=(64, 64)):
    """
    Load an HEIC (or other) image, resize/crop to fit target dimensions,
    and save as PNG.
    """
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found")
        return

    print(f"Processing {input_path}...")
    try:
        img = Image.open(input_path)
        
        # Convert to RGB
        img = img.convert("RGB")
        
        # Replace white background with black
        # Assuming "white based" means pixels close to white
        data = np.array(img)
        # Threshold for white (adjust as needed, e.g., > 200)
        threshold = 200
        red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
        mask = (red > threshold) & (green > threshold) & (blue > threshold)
        data[mask] = [0, 0, 0]
        img = Image.fromarray(data)

        # Resize and pad to fill the target size with black background
        # This preserves aspect ratio and adds black bars if needed
        processed_img = ImageOps.pad(img, target_size, method=Image.Resampling.LANCZOS, color=(0, 0, 0))
        
        print(f"Saving to {output_path} with size {target_size}")
        processed_img.save(output_path, "PNG")
        print("Done.")
    except Exception as e:
        print(f"Failed to process image: {e}")

if __name__ == "__main__":
    # Target resolution based on project context (2x 64x64 panels)
    TARGET_WIDTH = 64
    TARGET_HEIGHT = 64
    
    process_image("images/peach.jpeg", "images/peach.png", (TARGET_WIDTH, TARGET_HEIGHT))
