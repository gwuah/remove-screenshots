import os, subprocess

class cd:
	"""Context manager for changing the current working directory"""
	def __init__(self, newPath):
		self.newPath = os.path.expanduser(newPath)

	def __enter__(self):
		self.savedPath = os.getcwd()
		os.chdir(self.newPath)

	def __exit__(self, etype, value, traceback):
		os.chdir(self.savedPath)


def get_all_images(files) :
    return [file for file in files if file.split(".")[-1] == "png"]
    
def main() :
    files = os.listdir()
    images = get_all_images(files)
    for image in images :
        os.remove(image)

main()