import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from resizeimage import resizeimage


def reduce_size(path,foo):
	foo=foo.save("%s"%path,optimize=True,quality=80)

def flip(path):
	im = np.fliplr(plt.imread(path))
	plt.imsave("%s"%path,im)

def resize(foo):
	cover = resizeimage.resize_cover(foo, [150, 150])
	cover.save("%s"%path)
	#cover.save("%s-resized"%path,foo.format)

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR,"images")

for root,dirs,files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path=os.path.join(root,file)
			foo=Image.open("%s"%path)
			#reduce_size(path,foo)
			#flip(path)
			resize(foo)

print("done")