# Step 1: Import necessary libraries
import qrcode
from PIL import Image  # For images
import streamlit as st  # For creating web apps
import io  # For handling data as bytes

# Step 2: Set up the web app title
st.title("QR Code Generator")
st.wite("しんちゃん、URLを入れてみて！")
# Step 3: Create a text input widget for the URL
url = st.text_input("Enter URL Here")

# Step 4: Create a button to generate QR code
if st.button("Generate QR Code"):
    # Display the entered URL
    st.write("Entered URL:", url)

    # Step 5: Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)  # Set QR code settings
    qr.add_data(url)  # Add the URL data
    qr.make(fit=True)  # Generate the QR code

    # Step 6: Convert QR code to image
    qr_image = qr.make_image(fill_color="black", back_color="white")  # Customize QR code colors

    # Convert PIL image to bytes-like object
    img_bytes = io.BytesIO()  # Prepare for image conversion
    qr_image.save(img_bytes, format="PNG")  # Save as PNG format

    # Step 7: Display the QR code image
    st.image(img_bytes)  # Display the QR code in the web app
