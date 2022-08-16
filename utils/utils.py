import numpy as np

def lab2class(lab):
    """ Convert color version of the ground truth into a class integers. """
    lab_mapped = lab * 0
    lab[lab < 200] = 0
    lab_mapped[np.where((lab == [255, 255, 255]).all(axis=2))] = [1, 1, 1]
    lab_mapped[np.where((lab == [255, 0, 0]).all(axis=2))] = [2, 2, 2]
    lab_mapped[np.where((lab == [255, 255, 0]).all(axis=2))] = [3, 3, 3]
    lab_mapped[np.where((lab == [0, 255, 255]).all(axis=2))] = [4, 4, 4]
    lab_mapped[np.where((lab == [0, 255, 0]).all(axis=2))] = [5, 5, 5]
    lab_mapped[np.where((lab == [0, 0, 255]).all(axis=2))] = [6, 6, 6]
    return np.uint8(lab_mapped[..., 0])

def pred2class(pred):
    """ Convert color version of prediction to class integers. """
    lab_mapped = pred * 0
    lab_mapped[np.where((pred == [255, 255, 255]).all(axis=2))] = [0, 0, 0]
    lab_mapped[np.where((pred == [0, 0, 0]).all(axis=2))] = [1, 1, 1]
    lab_mapped[np.where((pred == [228, 26, 28]).all(axis=2))] = [2, 2, 2]
    lab_mapped[np.where((pred == [255, 127, 0]).all(axis=2))] = [3, 3, 3]
    lab_mapped[np.where((pred == [55, 126, 184]).all(axis=2))] = [4, 4, 4]
    lab_mapped[np.where((pred == [77, 175, 74]).all(axis=2))] = [5, 5, 5]
    lab_mapped[np.where((pred == [152, 78, 163]).all(axis=2))] = [6, 6, 6]
    return np.uint8(lab_mapped[..., 0])

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
    colors = colors[:np.max(img)+1, :]
    colormap = matplotlib.colors.ListedColormap(colors, name='my_colormap_name')
    path = '.'.join(path.split(".")[:-1] + ["png"])
    plt.imsave(path, img, cmap=colormap)