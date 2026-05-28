import qrcode

def generate_qr_code(filepath):
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
        if len(lines) < 2:
            print("Error: File must have at least 2 lines")
            return
        text = lines[0].strip()
        filename = lines[1].strip()
        image_qrcode = qrcode.make(text)
        image_qrcode.save(filename)
        print(f"QR Code saved successfully as '{filename}'")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
    except Exception as e:
        print(f"Unexpected error: {e}")

generate_qr_code("image_input.txt")