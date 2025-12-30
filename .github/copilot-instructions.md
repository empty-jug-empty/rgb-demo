# Project Context: Raspberry Pi 5 RGB Matrix POC
- **Hardware:** Raspberry Pi 5 + Adafruit RGB Matrix Bonnet.
- **Display Setup:** Two (2) Waveshare 64x64 RGB Panels chained horizontally (Total resolution: 128x64).
- **Mandatory Library:** Use `adafruit_blinka_raspberry_pi5_piomatter`. 
- **Legacy Ban:** DO NOT suggest or use `rpi-rgb-led-matrix`. It is incompatible with Pi 5 GPIO.

# Hardware Configuration Defaults:
- `n_addr_lines=5` (Required for 64x64 1/32 scan panels).
- `pinout=piomatter.Pinout.AdafruitMatrixBonnet`.
- `colorspace=piomatter.Colorspace.RGB888Packed`.

# Implementation Standards:
- Use `numpy` for all framebuffer operations for performance.
- Pixel format must be 0x00RRGGBB (uint32).
- When loading images, use `Pillow` (PIL) and convert to `numpy` arrays.
- Always include a `try/except KeyboardInterrupt` block to handle clean shutdowns.
- Assume the user is running in a Python virtual environment (venv).