import OpenEXR
import numpy as np

# Specify the path to your OpenEXR file
file_path = './dwsample-exr-640.exr'

exr_file = OpenEXR.InputFile(file_path)

# Get the image header information
header = exr_file.header()

print(header)