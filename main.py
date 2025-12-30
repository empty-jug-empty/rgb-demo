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

def load_image_to_array(filepath):
    """
    Load an image, resize to 64x64, and convert to 0x00RRGGBB uint32 numpy array.
    """
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return np.zeros((DISPLAY_HEIGHT, DISPLAY_WIDTH), dtype=np.uint32)

    try:
        img = Image.open(filepath)
        img = img.convert("RGB")
        img = img.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        
        # Convert to numpy array
        arr = np.array(img, dtype=np.uint32)
        
        # Pack RGB into uint32: 0x00RRGGBB
        r = arr[:, :, 0]
        g = arr[:, :, 1]
        b = arr[:, :, 2]
        
        packed_arr = (r << 16) | (g << 8) | b
        return packed_arr
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return np.zeros((DISPLAY_HEIGHT, DISPLAY_WIDTH), dtype=np.uint32)

def main():
    print("Initializing Single 64x64 RGB Matrix...")
    
    # Initialize the matrix
    matrix = piomatter.RGBMatrix(
        width=DISPLAY_WIDTH,
        height=DISPLAY_HEIGHT,
        n_addr_lines=5,
        pinout=piomatter.Pinout.AdafruitMatrixBonnet,
        colorspace=piomatter.Colorspace.RGB888Packed
    )

    # Load Bowser image
    image_path = os.path.join("images", "Bowser.png")
    print(f"Loading {image_path}...")
    
    framebuffer = load_image_to_array(image_path)

    print("Displaying image. Press Ctrl+C to stop.")
    
    try:
        while True:
            matrix.show(framebuffer)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nShutdown signal received. Exiting.")
        matrix.show(np.zeros((DISPLAY_HEIGHT, DISPLAY_WIDTH), dtype=np.uint32))

if __name__ == "__main__":
    main()
# filepath: /Users/cloud/Projects/ocean-wave/demo2/main.py
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

def load_image_to_array(filepath):
    """
    Load an image, resize to 64x64, and convert to 0x00RRGGBB uint32 numpy array.
    """
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return np.zeros((DISPLAY_HEIGHT, DISPLAY_WIDTH), dtype=np.uint32)

    try:
        img = Image.open(filepath)
        img = img.convert("RGB")
        img = img.resize((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        
        # Convert to numpy array
        arr = np.array(img, dtype=np.uint32)
        
        # Pack RGB into uint32: 0x00RRGGBB
        r = arr[:, :, 0]
        g = arr[:, :, 1]
        b = arr[:, :, 2]
        
        packed_arr = (r << 16) | (g << 8) | b
        return packed_arr
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return np.zeros((DISPLAY_HEIGHT, DISPLAY_WIDTH), dtype=np.uint32)

def main():
    print("Initializing Single 64x64 RGB Matrix...")
    
    # Initialize the matrix
    matrix = piomatter.RGBMatrix(
        width=DISPLAY_WIDTH,
        height=DISPLAY_HEIGHT,
        n_addr_lines=5,
        pinout=piomatter.Pinout.AdafruitMatrixBonnet,
        colorspace=piomatter.Colorspace.RGB888Packed
    )

    # Load Bowser image
    image_path = os.path.join("images", "Bowser.png")
    print(f"Loading {image_path}...")
    
    framebuffer = load_image_to_array(image_path)

    print("Displaying image. Press Ctrl+C to stop.")
    
    try:
        while True:
            matrix.show(framebuffer)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nShutdown signal received. Exiting.")
        matrix.show(np.zeros((DISPLAY_HEIGHT, DISPLAY_WIDTH), dtype=np.uint32))

if __name__ == "__main__":
    main()