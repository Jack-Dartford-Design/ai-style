Style Transfer AI

Pre-requisites:

Tensorflow 1.14.0
Tensorflow-gpu 1.14.0
Numpy 1.18.1
Scipy 1.4.1
PIL or Pillow
CV2 3.4.2
CUDA 10.0.130
CUDNN 7.6.5

Python 3+
After effects (or any software that can frame blend)

How to use

1. Install pre requisites
2. In cmd.exe cd to the directory of 'ai'
2. Run 'python neural_style.py --content_img test01 --style_img test01 --max_iterations 100 --max_size --verbose
3. Once complete this will output a directory in 'image_output'
4. If everything has functioned correctly then move on to video
5. Convert video file to jpg sequence and render to the image input directory. be sure to empty this directory after each run
6. Run 'neural_style_video.py' and follow instructions on how to proceed
7. This will train on each image and render the output to the 'image_output' directory
8. Once this is done put into video editing software andchange frame blending mode for extra smoothness


