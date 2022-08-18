import cv2
import glob
import time
import numpy as np
import fiftyone as fo
import fiftyone.zoo as foz
import fiftyone.brain as fob
import fiftyone.core.config as fcf

import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

try:
    dataset = fo.load_dataset("s2ds")
    dataset.delete()
except:
    pass

mode = "train"
display = True

# display stored dataset
if display:
    dataset = fo.Dataset.from_dir(
        dataset_dir=f"./export/{mode}",
        dataset_type=fo.types.COCODetectionDataset,
        name="s2ds",
        label_types=["detections", "segmentations"],
    )
    session = fo.launch_app(dataset)
    session.wait()

# create dataset
else:
    classes = {0: "background",
               1: "crack",
               2: "spalling",
               3: "corrosion",
               4: "efflorescence",
               5: "vegetation",
               6: "control_point"}

    files = glob.glob(f"../{mode}/[0-9][0-9][0-9].png")
    files.sort()

    samples = []
    for f in files:
        sample = fo.Sample(filepath=f)

        lab = cv2.imread(f.replace(".png", "_mapped.png"), cv2.IMREAD_GRAYSCALE)
        # dilate the cracks
        lab_dil = cv2.dilate(np.uint8(lab == 1), kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
        lab[lab_dil == 1] = 1

        sample["segmentation"] = fo.Segmentation(mask=lab)
        sample["detections"] = sample["segmentation"].to_detections(mask_targets=classes, mask_types='thing')
        sample["polylines"] = sample["segmentation"].to_polylines(mask_targets=classes, mask_types='thing')

        # fix: remove too short polylines
        pop_idxs = []
        for i, polyline in enumerate(sample["polylines"].polylines):
            # print(len(polyline.points), len(polyline.points[0]))
            if len(polyline.points[0]) < 3:  # needed, otherwise dataset loading crashes
                pop_idxs.append(i)
        for i in pop_idxs[::-1]:
            sample["polylines"].polylines.pop(i)

        samples.append(sample)

    # create dataset
    dataset = fo.Dataset("s2ds")
    dataset.info["year"] = "2022"
    dataset.info["version"] = "1.0"
    dataset.info["contributor"] = "Christian Benz"
    dataset.info["description"] = "The Structural Defects Dataset (S2DS) represents structural damages " + \
                                  "that are visible on the surface of (concrete) structures. It covers the " + \
                                  "classes 'background', 'crack', 'spalling', 'corrosion', 'efflorescence', " + \
                                  "'vegetation', 'control_point'."

    dataset.default_classes = [str(elem) for elem in classes.keys()]
    dataset.default_mask_targets = classes
    dataset.mask_targets = {
        "segmentation": classes,
    }

    dataset.save()
    dataset.add_samples(samples)

    app_config = fcf.AppConfig()
    # app_config.color_pool = ['#000000', '#0000ff', '#ff0000', '#00ffff', '#ffff00', '#00ff00', '#ff00ff', '#ffffff']

    session = fo.launch_app(dataset, auto=False, config=app_config)

    dataset.export(
        export_dir=f"./export/{mode}",
        dataset_type=fo.types.COCODetectionDataset,
        label_field="polylines",
        overwrite=True,
    )

    time.sleep(1)  # needed for colors
    session.refresh()

    session.wait()
