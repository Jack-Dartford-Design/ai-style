import neural_style
import os
import subprocess
import pathlib
import sys
from time import sleep


def clear():
	os.system('cls' if os.name=='nt' else 'clear')

clear()

input_dir = input("Please enter the img sequence location here:")
img_dir_exists = pathlib.Path(input_dir)
if img_dir_exists.exists():
	print("Input directory set to: ", input_dir)
else:
	print("Cannot locate directory for images")
	sys.exit()

sleep(1)
clear()

style_images_video = input("Please enter name of style image:")
print("Style image set to: ", style_images_video)

sleep(1)
clear()

ff_iterations = input("Max iterations (default 1000):")
if ff_iterations == "":
	ff_iterations = 1000
	print("Max iterations set to: 1000")
else:
	print("Max iterations set to: ", ff_iterations)

sleep(1)
clear()

data_size = input("Please enter data size (default 1024):")
if data_size == "":
	data_size = 1024
	print("Data size set to: 1024")
else:
	print("Data Size: ", data_size)

sleep(1)
clear()

#for loop for each image in sequence
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg"):
        os.system(f"python neural_style.py --content_img {filename} --style_imgs {style_images_video} --max_iterations {ff_iterations} --max_size {data_size} --img_name {filename} --verbose")
    else:
            continue