# Structural Defects Dataset (S2DS)

The S2DS dataset (<u>S</u>tructural <u>D</u>efects <u>D</u>ata<u>s</u>et) features 743 images of mostly concrete surfaces representing typical structural defects – such as crack or spalling – or control points. Each image is a 1024×1024 patch from a larger image. The classes covered are *background*, *crack*, *spalling*, *corrosion*, *efflorescence*, *vegetation*, *control point*.

## Terms and Conditions of Use
The S2DS dataset is publicly available for academic use only. While every effort has been made to ensure the accuracy of this database, we cannot accept responsibility for errors or omissions. The academic use of this database is free of charge. Any commercial distribution or act related to the commercial usage of this database is strictly prohibited. The distribution of this database to any parties that have not read and agreed to the terms and conditions of usage is strictly prohibited. Neither Bauhaus-Universität Weimar, nor any third parties who may provide information to us for the dissemination purpose, shall have any responsibility for or be liable in respect of the content or the accuracy of the provided information, or for any errors or omissions therein. The Bauhaus-Universität Weimar reserves the right to revise, amend, alter or delete the information provided herein at any time, but shall not be responsible for or liable in respect of any such revisions, amendments, alterations or deletions.<br>
*<sub>(Adapted from GAPs request form, https://www.tu-ilmenau.de/fileadmin/Bereiche/IA/neurob/Datasets/Request-Gaps3.pdf.)</sub>*

## Citation
**The dataset must not be shared or distributed.**

Always link and cite the work properly:

```
@inproceedings{benz2022image,
  title={Image-Based Detection of Structural Defects Using Hierarchical Multi-scale Attention},
  author={Benz, Christian and Rodehorst, Volker},
  booktitle={DAGM German Conference on Pattern Recognition},
  pages={337--353},
  year={2022},
  organization={Springer}
}
```


 

## Download
### ... from Google Drive
The S2DS dataset can be downloaded from Google drive:

https://drive.google.com/file/d/1PQ50QKfy2vnDOHSmw5bpBFi33hZsSXuM/view?usp=sharing


<!--- ### ... using Git *(only test set)*
The S2DS **test set** was pushed to github using Git LFS (*large file storage*, https://git-lfs.github.com/). 
It can be obtained running the usual:
```
git clone git@github.com:uncle-ben-z/s2ds.git
```
-->

## Classes
| Class         | Description                                  | Color                                            |
|---------------|----------------------------------------------|--------------------------------------------------|
| Crack         | Linear fractures in material                 | ![Color Crack](colors/crack.png)                 | 
| Spalling      | Material detachment from surface             | ![Color Spalling](colors/spalling.png)           |
| Corrosion     | Rust formation by oxidizing metal parts      | ![Color Corrosion](colors/corrosion.png)         |
| Efflorescence | Depositions of dissolved chemicals on surface | ![Color Efflorescence](colors/efflorescence.png) |
| Vegetation    | Surficial plant growth                       | ![Color Vegetation](colors/vegetation.png)       |
| Control Point | Geodetic fiducial markers for georeferencing | ![Color Control Point](colors/control_point.png) |
| Background    | All other classes                            | ![Color Background](colors/background.png)       |


## Split
The data were manually split into training, validation, and test set. Images of distinctly poor quality or almost invisible defects were incorporated into the training (and validation) set. The test contains only images with a fair chance of recognition.  

|               | Training |  | Validation |  | Test   |        |
|---------------|----------|---|------------|---|--------|--------|
| **Class**     | **Images**   | **Pixels** | **Images**     | **Pixels** | **Images** | **Pixels** |
 | Crack         | 180 | 0.6 M | 25 | 0.1 M | 27 | 0.1 M  |
 | Spalling      | 151 | 39.2 M | 23 | 3.3 M | 20 | 4.2 M |
 | Corrosion     | 209 | 8.8 M | 36 | 0.5 M | 38 | 0.9 M |
 | Efflorescence | 96 | 4.6 M | 13 | 0.6 M | 17 | 1.5 M |
 | Vegetation    | 97 | 15.7 M | 16 | 2.7 M | 18 | 2.9 M | 
 | Control Point | 70 | 1.5 M | 9 | 0.2 M | 10 | 0.2 M |
| Background    | 556 | 519.9 M | 87 | 83.8 M | 93 | 87.7 M |
 | **Total**         | **563** | **590.3 M** | **87** | **91.23 M** | **93** | **97.52 M**| 


## Examples
Downscales images from the test set. 

| Image                                | Label / Annotation              |    | Image                                | Label / Annotation                     |
|--------------------------------------|---------------------------------|----|--------------------------------------|----------------------------------------|
 | ![Image 201](thumbnails/201.jpg) 	   | ![Image 201](thumbnails/201_lab.jpg) |    | ![Image 1602](thumbnails/1602.jpg) 	 | ![Image 1602](thumbnails/1602_lab.jpg) | 
 | ![Image 1611](thumbnails/1611.jpg) 	 | ![Image 1611](thumbnails/1611_lab.jpg) |    | ![Image 821](thumbnails/821.jpg) 	   | ![Image 821](thumbnails/821_lab.jpg)   | 
 | ![Image 1408](thumbnails/1408.jpg) 	 | ![Image 1408](thumbnails/1408_lab.jpg) |    | ![Image 1891](thumbnails/1891.jpg) 	 | ![Image 1891](thumbnails/1891_lab.jpg) | 
 | ![Image 1881](thumbnails/1881.jpg) 	 | ![Image 1881](thumbnails/1881_lab.jpg) |    | ![Image 1256](thumbnails/1256.jpg) 	 | ![Image 1256](thumbnails/1256_lab.jpg) | 
 | ![Image 312](thumbnails/312.jpg) 	   | ![Image 312](thumbnails/312_lab.jpg) |    | ![Image 1299](thumbnails/1299.jpg) 	 | ![Image 1299](thumbnails/1299_lab.jpg) | 
 | ![Image 812](thumbnails/812.jpg) 	   | ![Image 812](thumbnails/812_lab.jpg) |    | ![Image 309](thumbnails/309.jpg) 	   | ![Image 309](thumbnails/309_lab.jpg)   | 
 | ![Image 206](thumbnails/206.jpg) 	   | ![Image 206](thumbnails/206_lab.jpg) |    | ![Image 1607](thumbnails/1607.jpg) 	 | ![Image 1607](thumbnails/1607_lab.jpg) | 
 | ![Image 118](thumbnails/118.jpg) 	   | ![Image 118](thumbnails/118_lab.jpg) |    | ![Image 1605](thumbnails/1605.jpg) 	 | ![Image 1605](thumbnails/1605_lab.jpg) | 
 | ![Image 216](thumbnails/216.jpg) 	   | ![Image 216](thumbnails/216_lab.jpg) |    | ![Image 1494](thumbnails/1494.jpg) 	 | ![Image 1494](thumbnails/1494_lab.jpg) | 
 | ![Image 232](thumbnails/232.jpg) 	   | ![Image 232](thumbnails/232_lab.jpg) |    | ![Image 207](thumbnails/207.jpg) 	   | ![Image 207](thumbnails/207_lab.jpg)   | 
 | ![Image 1419](thumbnails/1419.jpg) 	 | ![Image 1419](thumbnails/1419_lab.jpg) |    | ![Image 1489](thumbnails/1489.jpg) 	 | ![Image 1489](thumbnails/1489_lab.jpg) | 
 | ![Image 685](thumbnails/685.jpg) 	   | ![Image 685](thumbnails/685_lab.jpg) |    | ![Image 1266](thumbnails/1266.jpg) 	 | ![Image 1266](thumbnails/1266_lab.jpg) | 
 | ![Image 621](thumbnails/621.jpg) 	   | ![Image 621](thumbnails/621_lab.jpg) |    | ![Image 40](thumbnails/40.jpg) 	     | ![Image 40](thumbnails/40_lab.jpg)     | 
 | ![Image 633](thumbnails/633.jpg) 	   | ![Image 633](thumbnails/633_lab.jpg) |    | ![Image 1898](thumbnails/1898.jpg) 	 | ![Image 1898](thumbnails/1898_lab.jpg) | 
 | ![Image 1617](thumbnails/1617.jpg) 	 | ![Image 1617](thumbnails/1617_lab.jpg) |    | ![Image 300](thumbnails/300.jpg) 	   | ![Image 300](thumbnails/300_lab.jpg)   | 
 | ![Image 322](thumbnails/322.jpg) 	   | ![Image 322](thumbnails/322_lab.jpg) |    | ![Image 1873](thumbnails/1873.jpg) 	 | ![Image 1873](thumbnails/1873_lab.jpg) | 
 | ![Image 829](thumbnails/829.jpg) 	   | ![Image 829](thumbnails/829_lab.jpg) |    | ![Image 1603](thumbnails/1603.jpg) 	 | ![Image 1603](thumbnails/1603_lab.jpg) | 
 | ![Image 30](thumbnails/30.jpg) 	     | ![Image 30](thumbnails/30_lab.jpg) |    | ![Image 230](thumbnails/230.jpg) 	   | ![Image 230](thumbnails/230_lab.jpg)   | 
 | ![Image 1604](thumbnails/1604.jpg) 	 | ![Image 1604](thumbnails/1604_lab.jpg) |    | ![Image 52](thumbnails/52.jpg) 	     | ![Image 52](thumbnails/52_lab.jpg)     | 
 | ![Image 1369](thumbnails/1369.jpg) 	 | ![Image 1369](thumbnails/1369_lab.jpg) |    | ![Image 1449](thumbnails/1449.jpg) 	 | ![Image 1449](thumbnails/1449_lab.jpg) | 
 | ![Image 1893](thumbnails/1893.jpg) 	 | ![Image 1893](thumbnails/1893_lab.jpg) |    | ![Image 677](thumbnails/677.jpg) 	   | ![Image 677](thumbnails/677_lab.jpg)   | 
 | ![Image 809](thumbnails/809.jpg) 	   | ![Image 809](thumbnails/809_lab.jpg) |    | ![Image 1610](thumbnails/1610.jpg) 	 | ![Image 1610](thumbnails/1610_lab.jpg) | 
 | ![Image 413](thumbnails/413.jpg) 	   | ![Image 413](thumbnails/413_lab.jpg) |    | ![Image 1608](thumbnails/1608.jpg) 	 | ![Image 1608](thumbnails/1608_lab.jpg) | 
 | ![Image 218](thumbnails/218.jpg) 	   | ![Image 218](thumbnails/218_lab.jpg) |    | ![Image 1469](thumbnails/1469.jpg) 	 | ![Image 1469](thumbnails/1469_lab.jpg) | 
 | ![Image 1027](thumbnails/1027.jpg) 	 | ![Image 1027](thumbnails/1027_lab.jpg) |    | ![Image 1612](thumbnails/1612.jpg) 	 | ![Image 1612](thumbnails/1612_lab.jpg) | 
 | ![Image 814](thumbnails/814.jpg) 	   | ![Image 814](thumbnails/814_lab.jpg) |    | ![Image 91](thumbnails/91.jpg) 	     | ![Image 91](thumbnails/91_lab.jpg)     | 
 | ![Image 209](thumbnails/209.jpg) 	   | ![Image 209](thumbnails/209_lab.jpg) |    | ![Image 1277](thumbnails/1277.jpg) 	 | ![Image 1277](thumbnails/1277_lab.jpg) | 
 | ![Image 800](thumbnails/800.jpg) 	   | ![Image 800](thumbnails/800_lab.jpg) |    | ![Image 647](thumbnails/647.jpg) 	   | ![Image 647](thumbnails/647_lab.jpg)   | 
 | ![Image 1174](thumbnails/1174.jpg) 	 | ![Image 1174](thumbnails/1174_lab.jpg) |    | ![Image 1353](thumbnails/1353.jpg) 	 | ![Image 1353](thumbnails/1353_lab.jpg) | 
 | ![Image 119](thumbnails/119.jpg) 	   | ![Image 119](thumbnails/119_lab.jpg) |    | ![Image 1606](thumbnails/1606.jpg) 	 | ![Image 1606](thumbnails/1606_lab.jpg) | 
 | ![Image 1613](thumbnails/1613.jpg) 	 | ![Image 1613](thumbnails/1613_lab.jpg) |    | ![Image 1878](thumbnails/1878.jpg) 	 | ![Image 1878](thumbnails/1878_lab.jpg) | 
 | ![Image 417](thumbnails/417.jpg) 	   | ![Image 417](thumbnails/417_lab.jpg) |    | ![Image 1238](thumbnails/1238.jpg) 	 | ![Image 1238](thumbnails/1238_lab.jpg) | 
 | ![Image 1892](thumbnails/1892.jpg) 	 | ![Image 1892](thumbnails/1892_lab.jpg) |    | ![Image 1006](thumbnails/1006.jpg) 	 | ![Image 1006](thumbnails/1006_lab.jpg) | 
 | ![Image 1897](thumbnails/1897.jpg) 	 | ![Image 1897](thumbnails/1897_lab.jpg) |    | ![Image 347](thumbnails/347.jpg) 	   | ![Image 347](thumbnails/347_lab.jpg)   | 
 | ![Image 1616](thumbnails/1616.jpg) 	 | ![Image 1616](thumbnails/1616_lab.jpg) |    | ![Image 601](thumbnails/601.jpg) 	   | ![Image 601](thumbnails/601_lab.jpg)   | 
 | ![Image 1140](thumbnails/1140.jpg) 	 | ![Image 1140](thumbnails/1140_lab.jpg) |    | ![Image 636](thumbnails/636.jpg) 	   | ![Image 636](thumbnails/636_lab.jpg)   | 
 | ![Image 219](thumbnails/219.jpg) 	   | ![Image 219](thumbnails/219_lab.jpg) |    | ![Image 73](thumbnails/73.jpg) 	     | ![Image 73](thumbnails/73_lab.jpg)     | 
 | ![Image 350](thumbnails/350.jpg) 	   | ![Image 350](thumbnails/350_lab.jpg) |    | ![Image 222](thumbnails/222.jpg) 	   | ![Image 222](thumbnails/222_lab.jpg)   | 
 | ![Image 1504](thumbnails/1504.jpg) 	 | ![Image 1504](thumbnails/1504_lab.jpg) |    | ![Image 1407](thumbnails/1407.jpg) 	 | ![Image 1407](thumbnails/1407_lab.jpg) | 
 | ![Image 1900](thumbnails/1900.jpg) 	 | ![Image 1900](thumbnails/1900_lab.jpg) |    | ![Image 100](thumbnails/100.jpg) 	   | ![Image 100](thumbnails/100_lab.jpg)   | 
 | ![Image 60](thumbnails/60.jpg) 	     | ![Image 60](thumbnails/60_lab.jpg) |    | ![Image 1614](thumbnails/1614.jpg) 	 | ![Image 1614](thumbnails/1614_lab.jpg) | 
 | ![Image 1028](thumbnails/1028.jpg) 	 | ![Image 1028](thumbnails/1028_lab.jpg) |    | ![Image 1206](thumbnails/1206.jpg) 	 | ![Image 1206](thumbnails/1206_lab.jpg) | 
 | ![Image 1042](thumbnails/1042.jpg) 	 | ![Image 1042](thumbnails/1042_lab.jpg) |    | ![Image 1899](thumbnails/1899.jpg) 	 | ![Image 1899](thumbnails/1899_lab.jpg) | 
 | ![Image 1016](thumbnails/1016.jpg) 	 | ![Image 1016](thumbnails/1016_lab.jpg) |    | ![Image 696](thumbnails/696.jpg) 	   | ![Image 696](thumbnails/696_lab.jpg)   | 
 | ![Image 656](thumbnails/656.jpg) 	   | ![Image 656](thumbnails/656_lab.jpg) |    | ![Image 819](thumbnails/819.jpg) 	   | ![Image 819](thumbnails/819_lab.jpg)   |
