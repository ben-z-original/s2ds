import cv2
import numpy as np
from torch import from_numpy, nn
from torchmetrics import JaccardIndex
from skimage.morphology import disk, thin

import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


class ltIoUMetric(nn.Module):
    """ Represents line-based, tolerant intersection-over-union (IoU). """

    def __init__(self, tolerance=5):
        super(ltIoUMetric, self).__init__()
        self.tolerance = tolerance

    def forward(self, output, target):
        return ltIoU(output, target, self.tolerance)


def ltIoU(output, target, tol=5):
    """ Computes line-based, tolerant intersection-over-union (IoU). """
    output_thin = np.copy(output)
    target_thin = np.copy(target)

    # thin predictions and labels
    for i in range(len(output)):
        [output_thin[i, ...], target_thin[i, ...]] = transform2lines(output[i, ...], target[i, ...], tol)

    # compute iou
    iou = JaccardIndex(num_classes=2, average=None)(from_numpy(output_thin), from_numpy(target_thin))
    return iou


def transform2lines(output, target, tol=5):
    """ Transform predictions and labels to thinned representation for line-base, tolerant IoU. """
    # thin predictions and labels
    output_thin = np.uint8(thin(output))
    target_thin = np.uint8(thin(target))

    # apply tolerance
    output_thin_dil = cv2.dilate(output_thin, disk(tol), iterations=1)
    target_thin_dil = cv2.dilate(target_thin, disk(tol), iterations=1)

    # derive true/false positives and negatives
    tp = target_thin * output_thin_dil
    fp = output_thin - output_thin * target_thin_dil
    fn = target_thin - tp

    output, target = tp + fp, tp + fn
    return output, target


def boundary_tolerance(lab, tolerance=2, ignore_index=7):
    """ Create ignore index at boundary of areal defects. """
    # exclude crack from tolerance
    lab_orig = np.copy(lab)
    lab = np.where(lab == 1, 0, lab)

    # determine boundary
    bound = cv2.Laplacian(lab, cv2.CV_64F)
    bound = cv2.dilate(np.where(bound != 0, 1, 0).astype(np.uint8), disk(tolerance), iterations=1)
    lab[bound == 1] = ignore_index

    # restore crack
    lab[lab_orig == 1] = 1
    return lab


def lab2class(lab):
    """ Convert color version of the ground truth into a class integers. """
    lab[lab < 200] = 0
    lab_mapped = np.zeros_like(lab[..., 0], np.uint8)
    lab_mapped[(lab == [255, 255, 255]).all(axis=2)] = 1
    lab_mapped[(lab == [255, 0, 0]).all(axis=2)] = 2
    lab_mapped[(lab == [255, 255, 0]).all(axis=2)] = 3
    lab_mapped[(lab == [0, 255, 255]).all(axis=2)] = 4
    lab_mapped[(lab == [0, 255, 0]).all(axis=2)] = 5
    lab_mapped[(lab == [0, 0, 255]).all(axis=2)] = 6
    return lab_mapped


def pred2class(pred):
    """ Convert color version of prediction to class integers. """
    pred_mapped = np.zeros_like(pred[..., 0], np.uint8)
    pred_mapped[(pred == [255, 255, 255]).all(axis=2)] = 0
    pred_mapped[(pred == [0, 0, 0]).all(axis=2)] = 1
    pred_mapped[(pred == [228, 26, 28]).all(axis=2)] = 2
    pred_mapped[(pred == [255, 127, 0]).all(axis=2)] = 3
    pred_mapped[(pred == [55, 126, 184]).all(axis=2)] = 4
    pred_mapped[(pred == [77, 175, 74]).all(axis=2)] = 5
    pred_mapped[(pred == [152, 78, 163]).all(axis=2)] = 6
    return pred_mapped


def imwrite_colormap(path, img):
    """ Convert class integers to color and write to disk. """
    colors = np.array([
        [255, 255, 255],
        [0, 0, 0],
        [228, 26, 28],
        [255, 127, 0],
        [55, 126, 184],
        [77, 175, 74],
        [152, 78, 163]]) / 255
    colors = colors[:np.max(img) + 1, :]
    colormap = matplotlib.colors.ListedColormap(colors, name='my_colormap_name')
    path = '.'.join(path.split(".")[:-1] + ["png"])
    plt.imsave(path, img, cmap=colormap)
