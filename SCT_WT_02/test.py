from PIL import Image

def print_welcome_pattern():
    print("Welcome to the Image Encryption Tool!")
    print("Enjoy securing your images with pixel manipulation.")

def split_image(image_path):
    try:
        # Open the image
        original_image = Image.open(image_path)
        width, height = original_image.size

        # Create two blank images (shares)
        share1 = Image.new("L", (width, height))
        share2 = Image.new("L", (width, height))

        # Split each pixel into two shares
        for i in range(width):
            for j in range(height):
                pixel_value = original_image.getpixel((i, j))
                share1.putpixel((i, j), pixel_value)
                share2.putpixel((i, j), 255 - pixel_value)  # Invert the pixel value

        # Save the shares
        share1.save("share1.png")
        share2.save("share2.png")
        print("Image split into two shares: share1.png and share2.png")
    except FileNotFoundError:
        print(f"Error: Image path '{image_path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

def encrypt_image(image_path, key):
    try:
        # Open the image
        share1 = Image.open(image_path)
        pixels = share1.load()

        # Apply a basic mathematical operation (e.g., addition) to each pixel
        for i in range(share1.width):
            for j in range(share1.height):
                pixel_value = pixels[i, j]
                # Example: Add the key to each pixel value
                pixels[i, j] = pixel_value + key

        # Save the encrypted share
        encrypted_share_path = "encrypted_share.png"
        share1.save(encrypted_share_path)
        print(f"Share 1 encrypted and saved as {encrypted_share_path}")
    except FileNotFoundError:
        print(f"Error: Share 1 path '{image_path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

# Get user inputs
image_path = input("Enter the path to your image: ")
encryption_key = int(input("Enter an integer encryption key: "))

# Print the welcome pattern
print_welcome_pattern()

# Split the image
split_image(image_path)

# Encrypt the share
encrypt_image("share1.png", encryption_key)
