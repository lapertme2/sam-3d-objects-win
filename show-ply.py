import open3d as o3d
import argparse
import sys

def visualize_point_cloud(ply_path: str) -> None:
    """
    Load and visualize a .ply point cloud file in sky blue color using Open3D.

    Parameters:
        ply_path (str): Path to the input .ply file.
    """
    # Load point cloud from file
    point_cloud = o3d.io.read_point_cloud(ply_path)
    
    # Check if point cloud is empty
    if len(point_cloud.points) == 0:
        print(f"❌ Error: The file '{ply_path}' contains no points.", file=sys.stderr)
        return

    # Assign uniform sky blue color [R=0.53, G=0.81, B=0.98] (values in [0.0, 1.0])
    point_cloud.paint_uniform_color([0.53, 0.81, 0.98])

    # Remove normals (if any) to prevent lighting artifacts
    point_cloud.normals = o3d.utility.Vector3dVector([])

    # Initialize visualizer
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name="Point Cloud Viewer", width=1200, height=800)
    vis.add_geometry(point_cloud)

    # Configure rendering options
    render_opt = vis.get_render_option()
    render_opt.light_on = False      # Critical: disables shading for accurate color
    render_opt.point_size = 2.0      # Adjust point size for visibility
    render_opt.background_color = [0.0, 0.0, 0.0]  # Optional: black background

    # Start interactive visualization
    vis.run()
    vis.destroy_window()


if __name__ == "__main__":
    # Optional: allow passing .ply path via command line
    parser = argparse.ArgumentParser(description="Visualize a .ply point cloud in sky blue.")
    parser.add_argument("ply_file", nargs="?", default="splat.ply",
                        help="Path to the .ply file (default: splat.ply)")
    args = parser.parse_args()

    # Call the visualizer
    visualize_point_cloud(args.ply_file)