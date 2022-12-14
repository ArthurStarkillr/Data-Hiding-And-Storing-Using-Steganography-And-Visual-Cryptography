import sys
sys.path.insert(0, './src')
import os
import streamlit as UI
from PIL import Image
from src.lsb_stegno import lsb_encode, lsb_decode
from src.n_share import generate_shares, compress_n_join_shares

option = UI.sidebar.radio('Options', ['Encode & Split', 'Merge & Decode'])
# option = UI.sidebar.radio('Options', ['Docs', 'Encode & Split', 'Merge & Decode'])
# if option == 'Docs':
#     UI.title('Documentation')
#     with open('README.md', 'r') as f:
#         docs = f.read()
#     UI.markdown(docs, unsafe_allow_html=True)
if option == 'Encode & Split':
    UI.title('Encoding')
    # Image
    img = UI.file_uploader('Upload Cover Image', type=['jpg', 'png', 'jpeg'])
    if img is not None:
        img = Image.open(img)
        try:
            img.save('C:/Users/ska15/Desktop/PROJECT/images/img.jpg')
        except:
            img.save('C:/Users/ska15/Desktop/PROJECT/images/img.png')
        UI.image(img, caption='Selected image to use for data encoding',use_column_width=True)
        # Data
    txt = UI.text_input('Enter Message to hide')
    print(txt)
    # Encode message
    if UI.button('Encode data and Generate shares'):
    # Checks
        if len(txt) == 0:
            UI.warning('No data to hide')
        elif img is None:
            UI.warning('No image file selected')
        # Generate splits
        else:
            print("In main try: ", txt)
            generate_shares(lsb_encode(txt))
            try:
                os.remove('C:/Users/ska15/Desktop/PROJECT/images/img.jpg')
            except FileNotFoundError:
                os.remove('C:/Users/ska15/Desktop/PROJECT/images/img.png')
            UI.success('Data encoded using Steganography and splitted into twoshares using Visual Cryptography :)!')

elif option == 'Merge & Decode':
    UI.title('Decoding')
# Share 1
#remove below line
    img1 = UI.file_uploader('Upload Share 1', type=['png'])
    if img1 is not None:
        img1 = Image.open(img1)
        img1.save('C:/Users/ska15/Desktop/PROJECT/images/share1.png')
        UI.image(img1, caption='Share 1', use_column_width=True)
        # Share 2
    img2 = UI.file_uploader('Upload Share 2', type=['png'])
    if img2 is not None:
        img2 = Image.open(img2)
        img2.save('C:/Users/ska15/Desktop/PROJECT/images/share2.png')
        UI.image(img2, caption='Share 2', use_column_width=True)
    # Decode message
    if UI.button('Merge Shares into one Combined image and Decode message'):# Check
        if img1 is None or img2 is None:
            UI.warning('Upload both shares')
        # Compress shares
        else:
            compress_n_join_shares()
            os.remove('C:/Users/ska15/Desktop/PROJECT/images/share1.png')
            os.remove('C:/Users/ska15/Desktop/PROJECT/images/share2.png')
            UI.success('Decoded message: ' + lsb_decode('C:/Users/ska15/Desktop/PROJECT/images/compress.png'))