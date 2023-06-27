import OpenEXR
import numpy as np
from PIL import Image


def read_exr_file(file_path):
    # Open the EXR file
    exr_file = OpenEXR.InputFile(file_path)

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
        channel_data_type = data_types[str(
            header['channels'][channel_name].type)]
        channel_data[channel_name] = np.frombuffer(
            exr_file.channel(channel_name), dtype=channel_data_type)

    # Close the EXR file
    exr_file.close()

    return channel_data


def save_as_jpeg(channel_data, channel_name, output_path):
    # Get the channel data
    data = channel_data[channel_name]

    # Normalize the data to the range [0, 1]
    data_normalized = (data - data.min()) / (data.max() - data.min())

    # Rescale the data to the range [0, 255]
    data_rescaled = (data_normalized * 255).astype(np.uint8)

    # Create a PIL Image from the channel data
    image = Image.fromarray(data_rescaled)

    # Save the image as a JPEG file
    image.save(output_path)


# Specify the path to your EXR file
exr_file_path = './input.exr'

# Read the EXR file
channel_data = read_exr_file(exr_file_path)

# Specify the channels you want to save as JPEG
channels_to_save = ['R', 'G', 'B']  # Example: saving the R, G, and B channels

# Save each channel as a JPEG
for channel_name in channels_to_save:
    # Specify the output path for each channel
    output_path = f'./{channel_name}.jpg'
    save_as_jpeg(channel_data, channel_name, output_path)
