from PIL import Image
from spiral import spiral_coords
from bitops import text_to_bits

def encode(image_path, message, output_path):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    W, H = img.size
    bit_stream = list(text_to_bits(message))
    capacity = W * H * 3
    if len(bit_stream) > capacity:
        raise ValueError(f"Message too long: needs {len(bit_stream)} bits, image holds {capacity}.")
    idx = 0
    for (x, y) in spiral_coords(W, H):
        if idx >= len(bit_stream):
            break
        r, g, b = pixels[x, y]
        new_channels = []
        for val in (r, g, b):
            if idx < len(bit_stream):
                new_channels.append((val & ~1) | int(bit_stream[idx]))
                idx += 1
            else:
                new_channels.append(val)
        pixels[x, y] = tuple(new_channels)
    img.save(output_path, format='PNG')
    print(f"[done] Stego image saved → {output_path}")