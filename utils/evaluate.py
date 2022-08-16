import os
import cv2
import subprocess
import numpy as np
import pandas as pd
from torch import from_numpy
from torchmetrics import JaccardIndex
from utils import ltIoUMetric, pred2class, lab2class, boundary_tolerance

import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

if __name__ == "__main__":
    files = np.arange(650, 743)
    # files.sort()

    pred_paths = ["results/ensemble/STRUDEF_{}.png",
                  "../hma/7_argmax/{}.png"]
    true_path = "../test/{}_lab.png"

    pred_acc = [np.empty((0, 1024, 1024), np.uint8)] * len(pred_paths)
    true_acc = np.empty((0, 1024, 1024), np.uint8)

    for f in files:
        print(f)

        # get predictions
        for i, p in enumerate(pred_paths):
            pred = cv2.imread(p.format(f), cv2.IMREAD_COLOR)
            pred = cv2.cvtColor(pred, cv2.COLOR_BGR2RGB)
            pred = pred2class(pred)
            pred_acc[i] = np.append(pred_acc[i], pred.reshape(1, 1024, 1024), axis=0)

        # get label
        true = cv2.imread(true_path.format(f), cv2.IMREAD_COLOR)
        true = cv2.cvtColor(true, cv2.COLOR_BGR2RGB)
        true = lab2class(true)
        true = boundary_tolerance(true)
        true_acc = np.append(true_acc, true.reshape(1, 1024, 1024), axis=0)

    tolerances = [0, 2, 4, 8, 16, 32]

    iou = np.empty((len(pred_acc), 7))
    ltiou = np.empty((len(pred_acc), len(tolerances), 2))

    for i in range(len(pred_acc)):
        # non-crack
        iou[i, ...] = JaccardIndex(num_classes=8, average=None, ignore_index=7)(from_numpy(pred_acc[i]),
                                                                                from_numpy(true_acc))
        # crack
        pred_acc[i] = np.where((pred_acc[i] != 1), 0, 1).astype(np.uint8)
        true_acc_tmp = np.where((true_acc != 1), 0, 1).astype(np.uint8)

        for j, tol in enumerate(tolerances):
            ltiou[i, j, ...] = ltIoUMetric(tolerance=tol).forward(pred_acc[i], true_acc_tmp)

    print(iou)
    print(ltiou)

    # latex output
    latex_iou = "\\documentclass[preview]{standalone}\n"
    latex_iou += "\\usepackage{booktabs}\n"
    latex_iou += "\\begin{document}\n"

    latex_iou += pd.DataFrame(
        dict(Classes=['Background', 'Crack', 'Spalling', 'Corrosion', 'Efflorescence', 'Vegetation', 'Control Point'],
             nnUNet=iou[0], HMA=iou[1])).to_latex(float_format="{:0.3f}".format)

    latex_iou += "\\end{document}"

    latex_path = "../tex/table_iou.tex"
    with open(latex_path, 'w') as f:
        f.write(latex_iou)

    subprocess.run(["pdflatex", latex_path])

    # cleanup
    os.remove(latex_path.replace(".tex", ".log"))
    os.remove(latex_path.replace(".tex", ".aux"))




