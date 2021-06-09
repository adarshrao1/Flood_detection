# Importing Libraries
from fastai.vision.all import *
import os
import pathlib
from PIL import Image
import numpy
import cv2


# Prediction function
def predict(image_path):
    # Set file paths and output file names
    out_path = os.path.split(os.path.split(image_path)[0])[0] + "/output/"
    image_name = os.path.basename(image_path)
    est_image_url = out_path + image_name[:-4] + "_est" + ".jpg"
    bin_image_url = out_path + image_name[:-4] + "_bin" + ".jpg"

    # create output file dictionary
    output = dict()

    # Linux pickle file path to windows path
    if os.name == 'nt':
        pathlib.PosixPath = pathlib.WindowsPath

    # Load export file
    learn = load_learner("./model_data/export.pkl")

    # Generate prediction
    predictions = learn.predict(image_path)

    # Convert prediction to array
    numpy_data = predictions[1].numpy()
    numpy_data2 = predictions[2].numpy()

    # Calculate Binary data
    count0 = numpy.count_nonzero(numpy_data == 0)
    count1 = numpy.count_nonzero(numpy_data == 1)

    # Calculate Estimation data
    image_cal = (numpy_data2[1] * 255).astype(numpy.uint8)
    threshold = 128
    water = 0
    for n in range(0, 255):
        if n < threshold:
            water += numpy.count_nonzero(image_cal == n) * n / 255
        else:
            water += numpy.count_nonzero(image_cal == n)

    # Convert binary image to blue and save it
    est_img = (numpy_data2[1] * 255).astype(numpy.float32)
    est_image = numpy.empty(numpy_data2[1].shape + (3,)).astype(numpy.float32)
    est_image[:, :, 0] = est_img
    # est_image = Image.fromarray(est_image)
    # est_image.save(est_image_url)
    cv2.imwrite(est_image_url,est_image)

    # Convert estimated image to blue and save it
    bin_img = (numpy_data * 255).astype(numpy.float32)
    bin_image = numpy.empty(numpy_data.shape + (3,)).astype(numpy.float32)
    bin_image[:, :, 0] = bin_img
    # bin_image = Image.fromarray(bin_image)
    # bin_image.save(bin_image_url)
    cv2.imwrite(bin_image_url,bin_image)

    # Save output to dictionary
    output['est_water'] = round(water * 100 / image_cal.size, 2)
    output['est_land'] = round((image_cal.size - water) * 100 / image_cal.size, 2)
    output['bin_water'] = round(count1 * 100 / numpy_data.size, 2)
    output['bin_land'] = round(count0 * 100 / numpy_data.size, 2)
    output['est'] = est_image_url[1:]
    output['bin'] = bin_image_url[1:]
    output['height'] = numpy_data.shape[0]
    output['width'] = numpy_data.shape[1]

    return output
