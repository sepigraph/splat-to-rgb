import sys
import os
import numpy as np
from plyfile import PlyData, PlyElement

def calculate_rgb(f_dc_0, f_dc_1, f_dc_2):
    SH_C0 = 0.28209479177387814
    r = 0.5 + SH_C0 * f_dc_0
    g = 0.5 + SH_C0 * f_dc_1
    b = 0.5 + SH_C0 * f_dc_2
    return r, g, b

def process_ply(input_ply_path, output_ply_path):
    try:
        # Load input PLY file
        ply_data = PlyData.read(input_ply_path)
        vertices = ply_data['vertex']

        # Calculate RGB values for each vertex
        rgb_values = np.array([calculate_rgb(vertex['f_dc_0'], vertex['f_dc_1'], vertex['f_dc_2']) for vertex in vertices])

        # Create new vertex data with RGB values added as attributes
        new_vertex_data = np.zeros(len(vertices), dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('red', 'f4'), ('green', 'f4'), ('blue', 'f4')])
        new_vertex_data['x'] = vertices['x']
        new_vertex_data['y'] = vertices['y']
        new_vertex_data['z'] = vertices['z']
        new_vertex_data['red'], new_vertex_data['green'], new_vertex_data['blue'] = rgb_values[:,0], rgb_values[:,1], rgb_values[:,2]

        # Write the new vertex data to the output PLY file
        new_ply_data = PlyData([PlyElement.describe(new_vertex_data, 'vertex')])
        new_ply_data.write(output_ply_path)

        print("Processed PLY file saved as:", output_ply_path)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python splat_to_rgb.py <input_ply_file>")
        sys.exit(1)

    input_ply_path = sys.argv[1]
    output_ply_path = os.path.splitext(input_ply_path)[0] + "_processed_RGB.ply"

    process_ply(input_ply_path, output_ply_path)
