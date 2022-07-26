# Structural Defects Dataset (S2DS)

The S2DS dataset (<u>S</u>tructural <u>D</u>efects <u>D</u>ata<u>s</u>et) features 743 images of mostly concrete surfaces representing typical structural defects – such as crack or spalling – or control points. Each image is a 1024×1024 patch from a larger image. The classes covered are *background*, *crack*, *spalling*, *corrosion*, *efflorescence*, *vegetation*, *control point*.

## Citation
**The dataset must not be shared or distributed.**

Always link and cite the work properly:

```
@inproceedings{benz2022defects,
  title={Image-based Detection of Structural Defects using Hierarchical Multi-Scale Attention},
  author={Benz, Christian and Rodehorst, Volker},
  booktitle={DAGM German Conference on Pattern Recognition},
  year={2022},
  organization={Springer}
}
```


 

## Download
### ... from Google Drive
The S2DS dataset can be downloaded from Google drive:
```
https://drive.google.com/file/d/1PQ50QKfy2vnDOHSmw5bpBFi33hZsSXuM/view?usp=sharing
``` 

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
Example images

| Image                       | Label / Annotation              | 
|-----------------------------|---------------------------------|
| ![Image 812](test/812.png) 	| ![Image 812](test/812_lab.png) |
| ![Image 214](test/214.png) 	| ![Image 214](test/214_lab.png) |
| ![Image 685](test/685.png) 	| ![Image 685](test/685_lab.png) |
| ![Image 1028](test/1028.png) 	| ![Image 1028](test/1028_lab.png) |
| ![Image 312](test/312.png) 	| ![Image 312](test/312_lab.png) |
| ![Image 1602](test/1602.png) 	| ![Image 1602](test/1602_lab.png) |
| ![Image 347](test/347.png) 	| ![Image 347](test/347_lab.png) |
| ![Image 1612](test/1612.png) 	| ![Image 1612](test/1612_lab.png) |
| ![Image 1266](test/1266.png) 	| ![Image 1266](test/1266_lab.png) |
| ![Image 222](test/222.png) 	| ![Image 222](test/222_lab.png) |
| ![Image 1299](test/1299.png) 	| ![Image 1299](test/1299_lab.png) |
| ![Image 819](test/819.png) 	| ![Image 819](test/819_lab.png) |
| ![Image 1408](test/1408.png) 	| ![Image 1408](test/1408_lab.png) |
| ![Image 1006](test/1006.png) 	| ![Image 1006](test/1006_lab.png) |
| ![Image 73](test/73.png) 	| ![Image 73](test/73_lab.png) |
| ![Image 1504](test/1504.png) 	| ![Image 1504](test/1504_lab.png) |
| ![Image 1607](test/1607.png) 	| ![Image 1607](test/1607_lab.png) |
| ![Image 636](test/636.png) 	| ![Image 636](test/636_lab.png) |
| ![Image 40](test/40.png) 	| ![Image 40](test/40_lab.png) |
| ![Image 1898](test/1898.png) 	| ![Image 1898](test/1898_lab.png) |
| ![Image 1878](test/1878.png) 	| ![Image 1878](test/1878_lab.png) |
| ![Image 206](test/206.png) 	| ![Image 206](test/206_lab.png) |
| ![Image 230](test/230.png) 	| ![Image 230](test/230_lab.png) |
| ![Image 1897](test/1897.png) 	| ![Image 1897](test/1897_lab.png) |
| ![Image 1613](test/1613.png) 	| ![Image 1613](test/1613_lab.png) |
| ![Image 1494](test/1494.png) 	| ![Image 1494](test/1494_lab.png) |
| ![Image 1277](test/1277.png) 	| ![Image 1277](test/1277_lab.png) |
| ![Image 30](test/30.png) 	| ![Image 30](test/30_lab.png) |
| ![Image 821](test/821.png) 	| ![Image 821](test/821_lab.png) |
| ![Image 350](test/350.png) 	| ![Image 350](test/350_lab.png) |
| ![Image 300](test/300.png) 	| ![Image 300](test/300_lab.png) |
| ![Image 1606](test/1606.png) 	| ![Image 1606](test/1606_lab.png) |
| ![Image 1892](test/1892.png) 	| ![Image 1892](test/1892_lab.png) |
| ![Image 1891](test/1891.png) 	| ![Image 1891](test/1891_lab.png) |
| ![Image 1881](test/1881.png) 	| ![Image 1881](test/1881_lab.png) |
| ![Image 1604](test/1604.png) 	| ![Image 1604](test/1604_lab.png) |
| ![Image 1608](test/1608.png) 	| ![Image 1608](test/1608_lab.png) |
| ![Image 417](test/417.png) 	| ![Image 417](test/417_lab.png) |
| ![Image 1899](test/1899.png) 	| ![Image 1899](test/1899_lab.png) |
| ![Image 118](test/118.png) 	| ![Image 118](test/118_lab.png) |
| ![Image 219](test/219.png) 	| ![Image 219](test/219_lab.png) |
| ![Image 119](test/119.png) 	| ![Image 119](test/119_lab.png) |
| ![Image 1611](test/1611.png) 	| ![Image 1611](test/1611_lab.png) |
| ![Image 1369](test/1369.png) 	| ![Image 1369](test/1369_lab.png) |
| ![Image 413](test/413.png) 	| ![Image 413](test/413_lab.png) |
| ![Image 1893](test/1893.png) 	| ![Image 1893](test/1893_lab.png) |
| ![Image 1174](test/1174.png) 	| ![Image 1174](test/1174_lab.png) |
| ![Image 1016](test/1016.png) 	| ![Image 1016](test/1016_lab.png) |
| ![Image 1206](test/1206.png) 	| ![Image 1206](test/1206_lab.png) |
| ![Image 1042](test/1042.png) 	| ![Image 1042](test/1042_lab.png) |
| ![Image 1238](test/1238.png) 	| ![Image 1238](test/1238_lab.png) |
| ![Image 309](test/309.png) 	| ![Image 309](test/309_lab.png) |
| ![Image 232](test/232.png) 	| ![Image 232](test/232_lab.png) |
| ![Image 1407](test/1407.png) 	| ![Image 1407](test/1407_lab.png) |
| ![Image 1140](test/1140.png) 	| ![Image 1140](test/1140_lab.png) |
| ![Image 218](test/218.png) 	| ![Image 218](test/218_lab.png) |
| ![Image 696](test/696.png) 	| ![Image 696](test/696_lab.png) |
| ![Image 1430](test/1430.png) 	| ![Image 1430](test/1430_lab.png) |
| ![Image 1605](test/1605.png) 	| ![Image 1605](test/1605_lab.png) |
| ![Image 1614](test/1614.png) 	| ![Image 1614](test/1614_lab.png) |
| ![Image 647](test/647.png) 	| ![Image 647](test/647_lab.png) |
| ![Image 800](test/800.png) 	| ![Image 800](test/800_lab.png) |
| ![Image 1603](test/1603.png) 	| ![Image 1603](test/1603_lab.png) |
| ![Image 1256](test/1256.png) 	| ![Image 1256](test/1256_lab.png) |
| ![Image 91](test/91.png) 	| ![Image 91](test/91_lab.png) |
| ![Image 322](test/322.png) 	| ![Image 322](test/322_lab.png) |
| ![Image 633](test/633.png) 	| ![Image 633](test/633_lab.png) |
| ![Image 1419](test/1419.png) 	| ![Image 1419](test/1419_lab.png) |
| ![Image 1353](test/1353.png) 	| ![Image 1353](test/1353_lab.png) |
| ![Image 1873](test/1873.png) 	| ![Image 1873](test/1873_lab.png) |
| ![Image 52](test/52.png) 	| ![Image 52](test/52_lab.png) |
| ![Image 60](test/60.png) 	| ![Image 60](test/60_lab.png) |
| ![Image 1900](test/1900.png) 	| ![Image 1900](test/1900_lab.png) |
| ![Image 216](test/216.png) 	| ![Image 216](test/216_lab.png) |
| ![Image 1616](test/1616.png) 	| ![Image 1616](test/1616_lab.png) |
| ![Image 1610](test/1610.png) 	| ![Image 1610](test/1610_lab.png) |
| ![Image 677](test/677.png) 	| ![Image 677](test/677_lab.png) |
| ![Image 207](test/207.png) 	| ![Image 207](test/207_lab.png) |
| ![Image 209](test/209.png) 	| ![Image 209](test/209_lab.png) |
| ![Image 1027](test/1027.png) 	| ![Image 1027](test/1027_lab.png) |
| ![Image 656](test/656.png) 	| ![Image 656](test/656_lab.png) |
| ![Image 1617](test/1617.png) 	| ![Image 1617](test/1617_lab.png) |
| ![Image 1489](test/1489.png) 	| ![Image 1489](test/1489_lab.png) |
| ![Image 829](test/829.png) 	| ![Image 829](test/829_lab.png) |
| ![Image 1449](test/1449.png) 	| ![Image 1449](test/1449_lab.png) |
| ![Image 100](test/100.png) 	| ![Image 100](test/100_lab.png) |
| ![Image 1469](test/1469.png) 	| ![Image 1469](test/1469_lab.png) |
| ![Image 601](test/601.png) 	| ![Image 601](test/601_lab.png) |
| ![Image 814](test/814.png) 	| ![Image 814](test/814_lab.png) |
| ![Image 621](test/621.png) 	| ![Image 621](test/621_lab.png) |
| ![Image 1409](test/1409.png) 	| ![Image 1409](test/1409_lab.png) |
| ![Image 809](test/809.png) 	| ![Image 809](test/809_lab.png) |
| ![Image 201](test/201.png) 	| ![Image 201](test/201_lab.png) |
