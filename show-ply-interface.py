import sys
sys.path.append("notebook")
from inference import Inference, ready_gaussian_for_video_rendering, render_video, load_image, load_single_mask, display_image, make_scene, interactive_visualizer

# might take a while to load (black screen)
interactive_visualizer(f"splat.ply")