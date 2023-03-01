import splitfolders

input_folder = 'C:/Users/abdul/OneDrive/Desktop/lumpy_disease/training/LumpyVillage'

splitfolders.ratio(input_folder, output= "training/dataset",
                   ratio=(.7, .2, .1),
                   group_prefix=None)
