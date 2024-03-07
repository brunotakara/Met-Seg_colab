# Cell 1
!pip install monai

# Cell 2
!git clone https://github.com/brunotakara/Met-Seg_colab

# Cell 3
from google.colab import drive
drive.mount('gdrive', force_remount = True)

# Cell 4
import os

folder = 'gdrive/MyDrive/path\ to \ your\ folder\ with\ the\ Scans'

inputs = []
for item in os.listdir(folder):
    # Verify if it is a directory, note that it only works if the directory itself contains other folders for each Scan_001, Scan_002, etc..
    if os.path.isdir(os.path.join(folder, item)):
        # Add this folder into the list
        inputs.append(os.path.join(folder, item))

inputs.sort()

# Cell 5

# Loop to iterate the inputs, they should not have spaces in their path, because Python's interpreter and bash interpreter are not the same so it will raise errors due to backslashes poping in your string 

for scan, input_file in enumerate(inputs):

    # this is your bash command over all scans
    os.system(f'python Met-Seg/met-seg --i {input_file} --o gdrive/MyDrive/Path\ where\ you\ want\ to\ store\ your\ preds/Scan_{scan+1:03} --c gdrive/MyDrive/\path\ where\ you\ saved\ your\ weights/3d_model.pth -device 0')
