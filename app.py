import streamlit as st
from model import QRCodeGenerator

def main():
    st.title("QR Code Generator")
    st.write("しんちゃん、URLを入れてみて!")

    url = st.text_input("Enter URL Here")

    if st.button("Generate QR Code"):
        st.write("Entered URL:", url)

        qr_generator = QRCodeGenerator()
        qr_code_image_bytes = qr_generator.generate_qr_code(url)

        st.image(qr_code_image_bytes)

if __name__ == "__main__":
    main()
