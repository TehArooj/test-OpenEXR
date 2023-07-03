import os
import OpenEXR
import numpy as np
from PIL import Image


def extract_cryptomatte_images(file_path, output_dir):
    # Open the EXR file
    exr_file = OpenEXR.InputFile(file_path)

    # Get the image header information
    header = exr_file.header()

    # Extract the Cryptomatte data
    cryptomatte_data = exr_file.get('cryptomatte')

    # Close the EXR file
    exr_file.close()

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Extract the matte names and IDs
    matte_names = cryptomatte_data['cryptomatte/mattename']
    matte_ids = cryptomatte_data['cryptomatte/']

    # Iterate over the matte names
    for i, matte_name in enumerate(matte_names):
        # Get the matte ID for the current matte name
        matte_id = matte_ids[matte_name]

        # Create an empty image with the size of the matte ID data
        image_data = np.zeros_like(matte_id, dtype=np.float32)

        # Assign the matte ID values to the image data
        image_data[:, :] = matte_id

        # Create a PIL Image from the matte ID data
        image = Image.fromarray(image_data)

        # Save the image as a JPEG file
        output_path = os.path.join(output_dir, f'matte_{i}.jpg')
        image.save(output_path)


# Specify the path to your EXR file
exr_file_path = './Camera_14.exr'

# Specify the output directory to save the extracted images
output_directory = './outputs'

# Extract Cryptomatte data and save as images
extract_cryptomatte_images(exr_file_path, output_directory)
