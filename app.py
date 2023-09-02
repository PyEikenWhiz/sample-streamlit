import qrcode  # Import the QR code library
import streamlit as st  # Import Streamlit
import io  # Import a library for handling data as bytes

# Create a Streamlit web app
st.title("QR Code Generator")  # Set the web app title
url = st.text_input("Enter URL Here")  # Create a text input for the URL

# Define a function to generate a QR code
def generate_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)  # Set QR code settings
    qr.add_data(url)  # Add the URL data
    qr.make(fit=True)  # Generate the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")  # Customize QR code colors

    # Convert QR code image to bytes-like object
    img_bytes = io.BytesIO()  # Prepare for image conversion
    qr_image.save(img_bytes, format="PNG")  # Save as PNG format
    return img_bytes

# Check if the "Generate QR Code" button is clicked
if st.button("Generate QR Code"):
    st.write("Entered URL!:", url)  # Display the entered URL
    qr_image_bytes = generate_qr_code(url)  # Generate the QR code image
    st.image(qr_image_bytes)  # Display the QR code in the web app

    # Save the QR code image as "saved_image.png" and add a download button
    with open("saved_image.png", "wb") as f:
        f.write(qr_image_bytes.getvalue())
    st.write("QR code image saved as 'saved_image.png'")  # Inform the user
    st.download_button(
        label="Download QR Code",
        data=qr_image_bytes,
        file_name="qr_code.png",
        mime="image/png"
    )
