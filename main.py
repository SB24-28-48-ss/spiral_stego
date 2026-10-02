import sys
import os
from encoder import encode
from decoder import decode

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Encode: python main.py encode <image_path> <message>")
        print("  Decode: python main.py decode <stego_image_path>")
        sys.exit(1)
    command = sys.argv[1].lower()
    if command == 'encode':
        if len(sys.argv) < 4:
            print("Usage: python main.py encode <image_path> <message>")
            sys.exit(1)
        image_path = sys.argv[2]
        message = sys.argv[3]
        os.makedirs('output', exist_ok=True)
        filename = os.path.splitext(os.path.basename(image_path))[0]
        output_path = os.path.join('output', f'{filename}_stego.png')
        encode(image_path, message, output_path)
    elif command == 'decode':
        if len(sys.argv) < 3:
            print("Usage: python main.py decode <stego_image_path>")
            sys.exit(1)
        stego_path = sys.argv[2]
        message = decode(stego_path)
        print(f"[Done] Hidden message: {message}")
    else:
        print(f"Unknown command: '{command}'. Use 'encode' or 'decode'.")
        sys.exit(1)

if __name__ == '__main__':
    main()