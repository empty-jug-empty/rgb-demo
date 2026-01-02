import sys
import os
import time
import numpy as np
from PIL import Image

# Try to import the mandatory library
try:
    import adafruit_blinka_raspberry_pi5_piomatter as piomatter
except ImportError:
    print("Error: adafruit_blinka_raspberry_pi5_piomatter library is required.")
    sys.exit(1)

# Configuration for Single Panel
DISPLAY_WIDTH = 64
DISPLAY_HEIGHT = 64
BRIGHTNESS = 1 # 0.0 to 1.0

def load_image_to_array(filepath):
    """
    Load an image, resize to 64x64, and convert to numpy array compatible with RGB888Packed.
    Returns (64, 64, 3) uint8 array.
    """
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return np.zeros((DISPLAY_HEIGHT, DISPLAY_WIDTH, 3), dtype=np.uint8)

    try:
        img = Image.open(filepath)
        img = img.convert("RGB")
        img = img.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        
        # Convert to numpy array (H, W, 3) uint8
        return np.array(img, dtype=np.uint8)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return np.zeros((DISPLAY_HEIGHT, DISPLAY_WIDTH, 3), dtype=np.uint8)

def main():
    print("Initializing Single 64x64 RGB Matrix...")
    
    # Load Bowser image first to use as framebuffer
    image_path = os.path.join("images", "peach.png")
    print(f"Loading {image_path}...")
    framebuffer = load_image_to_array(image_path)

    # Apply brightness
    if BRIGHTNESS < 1.0:
        print(f"Applying brightness: {BRIGHTNESS}")
        framebuffer[:] = (framebuffer.astype(np.float32) * BRIGHTNESS).astype(np.uint8)

    # Initialize the geometry
    geometry = piomatter.Geometry(
        width=DISPLAY_WIDTH,
        height=DISPLAY_HEIGHT,
        n_addr_lines=5,
        rotation=piomatter.Orientation.Normal
    )
    
    # Initialize the matrix with the framebuffer
    matrix = piomatter.PioMatter(
        colorspace=piomatter.Colorspace.RGB888Packed,
        pinout=piomatter.Pinout.AdafruitMatrixBonnet,
        framebuffer=framebuffer,
        geometry=geometry
    )

    print("Displaying image. Press Ctrl+C to stop.")
    
    try:
        while True:
            matrix.show()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nShutdown signal received. Exiting.")
        # Clear framebuffer
        framebuffer.fill(0)
        matrix.show()

if __name__ == "__main__":
    main()
