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
    bin_data = predictions[1].numpy()
    est_data = predictions[2].numpy()

    # Calculate Binary data
    count0 = numpy.count_nonzero(bin_data == 0)
    count1 = numpy.count_nonzero(bin_data == 1)

    # Calculate Estimation data
    image_cal = (est_data[1] * 255).astype(numpy.uint8)
    threshold = 128
    water = 0
    for n in range(0, 255):
        if n < threshold:
            water += numpy.count_nonzero(image_cal == n) * n / 255
        else:
            water += numpy.count_nonzero(image_cal == n)

    # Convert binary image to blue and save it
    est_img = (est_data[1] * 255).astype(numpy.float32)
    est_image = numpy.empty(est_data[1].shape + (3,)).astype(numpy.float32)
    est_image[:, :, 0] = est_img
    # est_image = Image.fromarray(est_image)
    # est_image.save(est_image_url)
    cv2.imwrite(est_image_url, est_image)

    # Convert estimated image to blue and save it
    bin_img = (bin_data * 255).astype(numpy.float32)
    bin_image = numpy.empty(bin_data.shape + (3,)).astype(numpy.float32)
    bin_image[:, :, 0] = bin_img
    # bin_image = Image.fromarray(bin_image)
    # bin_image.save(bin_image_url)
    cv2.imwrite(bin_image_url, bin_image)

    # Save output to dictionary
    output['est_water'] = round(water * 100 / image_cal.size, 2)
    output['est_land'] = round((image_cal.size - water) * 100 / image_cal.size, 2)
    output['bin_water'] = round(count1 * 100 / bin_data.size, 2)
    output['bin_land'] = round(count0 * 100 / bin_data.size, 2)
    output['est'] = est_image_url[1:]
    output['bin'] = bin_image_url[1:]
    output['height'] = bin_data.shape[0]
    output['width'] = bin_data.shape[1]

    return output


def predict_com(image_path, image2_path):
    # Set file paths and output file names
    out_path = os.path.split(os.path.split(image_path)[0])[0] + "/output/"
    image_name = os.path.basename(image_path)
    est_image_url = out_path + image_name[:-4] + "_est" + ".jpg"
    bin_image_url = out_path + image_name[:-4] + "_bin" + ".jpg"
    image2_name = os.path.basename(image2_path)
    est_image_com_url = out_path + image2_name[:-4] + "_est" + ".jpg"
    bin_image_com_url = out_path + image2_name[:-4] + "_bin" + ".jpg"

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
    bin_data = predictions[1].numpy()
    est_data = predictions[2].numpy()

    # Generate prediction for comparison image
    predictions2 = learn.predict(image2_path)

    # Convert prediction to array for comparison image
    bin_data_com = predictions2[1].numpy()
    est_data_com = predictions2[2].numpy()

    # Calculate Binary data
    count0 = numpy.count_nonzero(bin_data == 0)
    count1 = numpy.count_nonzero(bin_data == 1)
    count0_com = numpy.count_nonzero(bin_data_com == 0)
    count1_com = numpy.count_nonzero(bin_data_com == 1)

    # Calculate Estimation data
    image_cal = (est_data[1] * 255).astype(numpy.uint8)
    image_cal_com = (est_data_com[1] * 255).astype(numpy.uint8)
    threshold = 128
    water = 0
    for n in range(0, 255):
        if n < threshold:
            water += numpy.count_nonzero(image_cal == n) * n / 255
        else:
            water += numpy.count_nonzero(image_cal == n)
    water_com = 0
    for n in range(0, 255):
        if n < threshold:
            water_com += numpy.count_nonzero(image_cal_com == n) * n / 255
        else:
            water_com += numpy.count_nonzero(image_cal_com == n)

    bin_img_com = (bin_data_com * 255).astype(numpy.float32)
    bin_image_com = numpy.empty(bin_data_com.shape + (3,)).astype(numpy.float32)
    bin_image_com[:, :, 0] = bin_img_com
    est_img_com = (est_data_com[1] * 255).astype(numpy.float32)
    est_image_com = numpy.empty(est_data_com[1].shape + (3,)).astype(numpy.float32)
    est_image_com[:, :, 0] = est_img_com

    for x in range(bin_data_com.shape[0]):
        for y in range(bin_data_com.shape[1]):
            if bin_data_com[x][y] == 0 and bin_data[x][y] == 1:
                bin_image_com[x][y] = [28, 237, 56]

            elif bin_data_com[x][y] == 1 and bin_data[x][y] == 0:
                bin_image_com[x][y] = [0, 51, 255]

            if image_cal[x][y] < image_cal_com[x][y] and image_cal_com[x][y] - image_cal[x][y] >= 20:
                est_image_com[x][y] = [0 * (image_cal_com[x][y] / 255), 51 * (image_cal_com[x][y] / 255), 255 * (image_cal_com[x][y] / 255)]

            elif image_cal[x][y] > image_cal_com[x][y] and image_cal[x][y] - image_cal_com[x][y] >= 20:
                est_image_com[x][y] = [28 * (image_cal[x][y] / 255), 237 * (image_cal[x][y] / 255),
                                       56 * (image_cal[x][y] / 255)]

    # Convert binary image to blue and save it
    est_img = (est_data[1] * 255).astype(numpy.float32)
    est_image = numpy.empty(est_data[1].shape + (3,)).astype(numpy.float32)
    est_image[:, :, 0] = est_img
    cv2.imwrite(est_image_url, est_image)

    # Convert estimated image to blue and save it
    bin_img = (bin_data * 255).astype(numpy.float32)
    bin_image = numpy.empty(bin_data.shape + (3,)).astype(numpy.float32)
    bin_image[:, :, 0] = bin_img
    cv2.imwrite(bin_image_url, bin_image)

    # Save binary comparison
    cv2.imwrite(bin_image_com_url, bin_image_com)

    # Save estimated comparison
    cv2.imwrite(est_image_com_url, est_image_com)

    # Save output to dictionary
    output['est_water'] = round(water * 100 / image_cal.size, 2)
    output['est_land'] = round((image_cal.size - water) * 100 / image_cal.size, 2)
    output['bin_water'] = round(count1 * 100 / bin_data.size, 2)
    output['bin_land'] = round(count0 * 100 / bin_data.size, 2)
    output['est_water_com'] = round(water_com * 100 / image_cal_com.size, 2)
    output['est_land_com'] = round((image_cal_com.size - water_com) * 100 / image_cal_com.size, 2)
    output['bin_water_com'] = round(count1_com * 100 / bin_data_com.size, 2)
    output['bin_land_com'] = round(count0_com * 100 / bin_data_com.size, 2)
    output['bin_water_diff'] = round(count1_com * 100 / bin_data_com.size, 2) - round(count1 * 100 / bin_data.size, 2)
    output['est_water_diff'] = round(water_com * 100 / image_cal_com.size, 2) - round(water * 100 / image_cal.size, 2)
    output['est'] = est_image_url[1:]
    output['bin'] = bin_image_url[1:]
    output['height'] = bin_data.shape[0]
    output['width'] = bin_data.shape[1]
    output['est_com'] = est_image_com_url[1:]
    output['bin_com'] = bin_image_com_url[1:]

    return output
