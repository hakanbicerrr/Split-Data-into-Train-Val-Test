import splitfolders
from pathlib import Path

input_data_folder = Path('C:/Users/hakan/OneDrive/Masaüstü/ESOGÜ/20-21-Güz/Bilgisayarla Görü/Ödev/BilgisayarlaGoru/whole_dataset') #Input folder that you want to split into train,validation and test folders.
output_data_folder = Path('C:/Users/hakan/OneDrive/Masaüstü/ESOGÜ/20-21-Güz/Bilgisayarla Görü/Ödev/BilgisayarlaGoru/Training1') #Output folder which will contain training,val and test.

#This easily splits your data according to ratio. I personally prefer %70 - %30.
splitfolders.ratio(input_data_folder,
                   output_data_folder,
                   seed=1337,ratio=(.7, .3))