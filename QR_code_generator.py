'''import qrcode

text = input("Input text to convert it into qrcode:")
filename = input("Input filename to save qr code in image :")

def generate_qr_code(text, filename):
    image_qr_code = qrcode.make(text)
    image_qr_code.save(filename)

generate_qr_code(text,filename)


'''

import qrcode
def generate_qr_code(filepath):
    with open(filepath,'r') as f:
        lines = f.readlines()
    text = lines[0].strip()
    filename = lines[1].strip()

    # qr make
    image_qr_code = qrcode.make(text)

    # qr image save
    image_qr_code.save(filename)


generate_qr_code('input.txt')