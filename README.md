# splat-to-rgb
## About
This is a lightweight Python script utility crafted to streamline the processing of Gaussian Splat PLY files. It efficiently transforms the FDC (Foveated Differential Coordinates) color properties of the input PLY file into RGB (Red, Green, Blue) properties, resulting in a new PLY file with accurate color representation and easy readability for use in 3D software applications.

## Installation:
Clone repo and open a Command Prompt in its path, run:
```
pip install -r requirements.txt
```

This will install the modules needed for the file processing.

## Usage

To convert a Gaussian Splat PLY file to a PLY using RGB format color properties with the `splat_to_rgb.py` script, follow these steps:

1. **Navigate to Directory:**
   Open a terminal or command prompt and navigate to the directory containing the `splat_to_rgb.py` script. Get the path to your Gaussian Splat PLY file.

2. **Run the Script:**
   Execute the following command in the terminal, replacing `input_file.ply` with the name of your Gaussian Splat PLY file. Ex:
   ```
   python splat_to_rgb.py <path/input_file.ply>
   ```

Once the script completes execution, you will find the processed PLY file in the same directory as the input file. You can now use this file with 3D software applications for improved point visualization and analysis.

## Notes:
- Currently there's no exception handling yet in the case where a PLY file is supplied without the correct format or gaussian properties, so errors will likely occur in such cases. This has mainly been tested on splat PLY files created from Postshot.

- Please be kind. This is just a small utility I wanted to share for those interested in being able to view point cloud data from Gaussian Splats in DCC software, like Blender. There likely won't be much support.

- The Gaussian Splat properties are pruned in the new file. This is because most DCC viewers do not support viewing Gaussian Splat models. By then once they do this tool won't serve much use other than a utility to reduce splat PLY files to smaller and simpler PLY files.

## Acknowledgements
A huge thanks to David Rhodes who got me deeper into this rabbit hole with Gaussian Splats. He figured out the color conversion formula utilized in this script. I highly recommend viewing his Gaussian Splat tools for Houdini, GSOPs, which you can find here: https://github.com/david-rhodes/GSOPs