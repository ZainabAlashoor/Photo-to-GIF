import imageio.v3 as iio

filenames = ['pic1.jpeg', 'pic2.jpeg', 'pic3.jpeg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('result.gif', images, duration = 500, loop = 0)