
## About NOAA Applied Seal Classification

![Screen Shot 2022-08-30 at 11 07 17 AM](https://user-images.githubusercontent.com/30137615/187511219-dc4096e4-ff76-4938-99e2-37f0133c3e9a.png)

This is the codebase of a research project that integrates mathematics with the science that informs fishery managers authored by Xinyi Xiang, Helena Williams and Erin Moreland.

## Major Steps Taken
### Step1:
- Data cleansing and organization. See more on the folder structures in Wiki.

### Step2:
- Our main goal in this step was detecting changes in seal population age trends depends on the accuracy of estimation and thus the quality of input data.
- Once we loaded the aerial images captured by flight cameras into the machine, the collections of images can be further bucketed into three major sets in a proportion of 6:2:2 - with the train sets being the most predominant part, this is in order to avoid classification corner cases as much as we can.
- The classification classes are thus divided into two, embedded in the configuration file’s categories part, mapping to an integer category id that is unique and backtraceable. We have soon narrowed down the most crucial elements for each annotation, after this we attempt first to organize the base directory in a tree structure similar to the right.

### Step3:
- A standard training framework for any detection and instance segmentation tasks, based on facebook’s open source framework detectron2.
- Due to its wide support of transformer based detection framework out-of-box and the only framework that enables YOLOv4 + InstanceSegmentation in single stage style, YOLOv7 has a set of requirements. The packages are summarized in the txt file under the root directory of this project. We also prepared a GitHub wiki page with clear documentation on the specific solutions to some more commonly seen error during installation, creating an easy plugin into transformers based detector.
  - In regards to the hardware tools, we have used nvcc and nvidia-smi to obtain the details and look for the most compatible versions of pytorch and CUDA. Kudos to Ben who really helped us a lot in terms of switching to a Debian-based OS and handling version incompatibilities.
- Another thing we discovered with anaconda virtual environment, besides its flexibility to work with different versions of the main programming, is also the pre programmed simplicity of its workflow, we were able to create a virtual environment for the model in a much efficient way with much fewer lines of commands.

### Step4:
- An outline of our tasks in the pre-training stage is listed here
    - We have matched each and every image with their respective JSON keys and convert the retrieved data from both comma separated values and annotated images.
    - We have also changed the source code accordingly so each layer of data loaders is looking at the right directory to locate source data files.
    - Finally, each set is registered as a COCO instance from our .yaml file, and we now hold every inputs a custom training scripts requests.


## ©️ License

Code released under GPL license. Please pull request to this source repo before you make your changes public or commercial usage. All rights reserved by Xinyi Xiang.
