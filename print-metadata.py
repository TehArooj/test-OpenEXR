import OpenEXR

def print_exr_metadata(file_path):
    # Open the EXR file
    exr_file = OpenEXR.InputFile(file_path)

    # Get the image header information
    header = exr_file.header()

    # Print the metadata
    print("EXR Metadata:")
    for key, value in header.items():
        print(f"{key}: {value}")

    # Close the EXR file
    exr_file.close()

# Specify the path to your EXR file
exr_file_path = './Camera_14.exr'

# Print the metadata from the EXR file
print_exr_metadata(exr_file_path)
