import matplotlib.pyplot as plt
from pyntcloud import PyntCloud
 
def show_ply(file_path):
    try:      
        ply = PyntCloud.from_file(file_path)      
        
        points = ply.points
        
        figure = plt.figure()
        axis = figure.add_subplot(111, projection='3d')
        axis.scatter(points['x'], points['y'], points['z'], s=0.1)        
        axis.set_xlabel('X')
        axis.set_ylabel('Y')
        axis.set_zlabel('Z')        
        plt.show()
        
    except Exception as e:
        print(f"read '{file_path}' error: {e}")
 
 
if __name__ == "__main__":	
	file_path="splat.ply"  
	show_ply(file_path)
