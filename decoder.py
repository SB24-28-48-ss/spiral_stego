from PIL import Image
from spiral import spiral_coords
from bitops import bits_to_text, DELIMITER

def decode(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    W, H = img.size
    bits = []
    delimiter_len = len(DELIMITER)
    for (x, y) in spiral_coords(W, H):
        for val in pixels[x, y]:
            bits.append(str(val & 1))
        if len(bits) >= delimiter_len + 8:
            joined = ''.join(bits)
            if DELIMITER in joined:
                return bits_to_text(joined)
    raise ValueError("No hidden message found.")