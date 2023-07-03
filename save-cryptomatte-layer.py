import OpenEXR
import numpy as np
from PIL import Image

def save_cryptomatte_layer(exr_file_path, cryptomatte_layer_name, output_image_path):
    # Open the EXR file
    exr_file = OpenEXR.InputFile(exr_file_path)

    # Get the image header information
    header = exr_file.header()

    # Extract the Cryptomatte data
    cryptomatte_data = exr_file.get('cryptomatte')

    # Close the EXR file
    exr_file.close()

    # Get the Cryptomatte layer
    cryptomatte_layer = cryptomatte_data[f'cryptomatte/{cryptomatte_layer_name}']

    # Create a numpy array from the Cryptomatte layer
    image_data = np.array(cryptomatte_layer)

    # Create a PIL Image from the Cryptomatte layer
    image = Image.fromarray(image_data)

    # Save the image as a PNG file
    image.save(output_image_path)

# Specify the path to your EXR file
exr_file_path = './Sample.exr'

# Specify the name of the Cryptomatte layer to save
cryptomatte_layer_name = 'R'

# Specify the output image path to save the Cryptomatte layer
output_image_path = './cryptomatte_layer.png'

# Save the Cryptomatte layer as a separate image
save_cryptomatte_layer(exr_file_path, cryptomatte_layer_name, output_image_path)
