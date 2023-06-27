import OpenEXR
import numpy as np


def read_openexr_file(file_path):
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


# Specify the path to your OpenEXR file
file_path = './input.exr'

# Read the OpenEXR file
channel_data = read_openexr_file(file_path)

# Access the pixel data by channel name
for channel_name, data in channel_data.items():
    print(f"Channel: {channel_name}")
    print(f"Data:\n{data}")
