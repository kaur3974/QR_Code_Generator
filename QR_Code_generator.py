import qrcode
import streamlit as st
import base64
import os

def generate_qr_code(data, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">{file_label}</a>'
    return href
if __name__ == "__main__":
    # Example usage
    url = st.text_input("Enter URL to create QR: ")

    if url:
        filename = "example_qr_code1.png"
        generate_qr_code(url, filename)
        if st.button("Show QR"):
            st.image(filename, caption='QR Code', use_column_width=True)
        st.markdown(get_binary_file_downloader_html(filename, 'Download QR Code'), unsafe_allow_html=True)