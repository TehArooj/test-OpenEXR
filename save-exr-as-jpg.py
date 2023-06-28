import OpenEXR
import numpy as np
from PIL import Image

def convert_exr_to_jpg(exr_file_path, jpg_file_path):
    # Open the EXR file
    exr_file = OpenEXR.InputFile(exr_file_path)

    # Get the image header information
    header = exr_file.header()

    # Extract the channels' names and data types
    channels = header['channels']
    data_types = {
        'HALF': np.float16,
        'FLOAT': np.float32,
    }

    # Prepare an empty dictionary to store channel data
    channel_data = {}

    # Read each channel and store its data
    for channel_name in channels:
        channel_data_type = data_types[str(header['channels'][channel_name].type)]
        channel_data[channel_name] = np.frombuffer(exr_file.channel(channel_name), dtype=channel_data_type)

    # Close the EXR file
    exr_file.close()

    # Extract the RGB channels
    red_channel = channel_data['R']
    green_channel = channel_data['G']
    blue_channel = channel_data['B']

    # Stack the channels together
    image_data = np.stack((red_channel, green_channel, blue_channel), axis=-1)

    # Normalize the data to the range [0, 1]
    image_data_normalized = (image_data - image_data.min()) / (image_data.max() - image_data.min())

    # Rescale the data to the range [0, 255]
    image_data_rescaled = (image_data_normalized * 255).astype(np.uint8)

    # Create a PIL Image from the channel data
    image = Image.fromarray(image_data_rescaled)

    # Save the image as a jpg file
    image.save(jpg_file_path)

# Specify the path to your EXR file
exr_file_path = './dwsample-exr-640.exr'

# Specify the path to save the jpg file
jpg_file_path = './newImage.jpg'

# Convert the EXR file to jpg
convert_exr_to_jpg(exr_file_path, jpg_file_path)
