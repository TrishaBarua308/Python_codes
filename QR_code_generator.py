'''import qrcode

text=input("Input text to convert it into a qr code:")
filename=input("Input a filename to save the qr code image:")

def generate_qr_code(text,filename):
    img_qrcode=qrcode.make(text)
    img_qrcode.save(filename)

generate_qr_code(text,filename)'''

# import qrcode
#
# def generate_qr(filepath):
#     with open(filepath, 'r') as f:
#         lines = f.readlines()
#     text = lines[0].strip()
#     filename = lines[1].strip()
#
#     img_qr = qrcode.make(text)
#     img_qr.save(filename)
#
# generate_qr('input.txt')

















