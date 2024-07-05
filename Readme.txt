Image Encryption Tool
Overview
The Image Encryption Tool is a Python script that combines visual cryptography (image splitting) and basic pixel manipulation to enhance image security. It splits an image into two shares using visual cryptography and then encrypts one of the shares using a simple mathematical operation (addition).

Features
Split an image into two shares (share1 and share2).
Encrypt share1 using a user-defined integer key.
Save the encrypted share1 as “encrypted_share.png.”
Requirements
Python 3.x
Pillow (PIL fork) library for image processing
Usage
Install Pillow (if not already installed):
pip install Pillow

Run the script:
python image_encryption.py

Follow the prompts:
Enter the path to your input image.
Enter an integer encryption key.
The tool will split the image, create share1 and share2, and save the encrypted share1.
Example
Suppose you have an image named “my_image.png.” After running the script, you’ll get:

share1.png (original pixel values)
share2.png (inverted pixel values)
encrypted_share.png (share1 with added encryption key)
Notes
Customize the code or explore more advanced encryption techniques for stronger security.
Remember to keep the encryption key secure