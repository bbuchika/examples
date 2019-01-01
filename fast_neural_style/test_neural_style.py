

import sys

# 
# C:/Users/brantb/AppData/Local/conda/conda/envs/PyTorchE1/python.exe  neural_style/neural_style.py train --dataset D:\local\coco --style-image D:\locadataset_parent_dirt\00000000000#1.jpg --save-model-dir style_imgs --epocs 2 --cudapData/Local/conda/conda/envs/PyT'. style_imgs --epocs 2 --cudapData/Local/conda/conda/envs/PyTorchE1/python.ex1


# sys.argv  = [R'c:\local\PyTorchTesting\examples\fast_neural_style\test_neural_style.py', 'train','--dataset', R'D:\local\coco', '--style-image', R'D:\local\coco\CocoSubset\000000000001.jpg',  R'--save-model-dir',  R'C:\local\PyTorchTesting\examples\saved_models2', R'--epochs', '2', '--cuda', '1']


main_file = R'C:\local\PyTorchTesting\examples\fast_neural_style\neural_style\neural_style.py'
dataset_parent_dir = R'D:\local\coco'
style_img = R'D:\local\coco\CocoSubset\000000000001.jpg'
# save_model_dir = 'saved_models2'
#save_model_dir = R'C:\local\PyTorchTesting\examples\saved_models2'
save_model_dir = '.'

sys.argv  = [main_file, 'train','--dataset', dataset_parent_dir, '--style-image', style_img,  R'--save-model-dir', save_model_dir, R'--epochs', '2', '--cuda', '1']

print(sys.argv)
# import neural_style/neural_style


# import neural_style
sys.path.insert(0, './fast_neural_style')
sys.path.insert(0, './fast_neural_style/neural_style')
import neural_style

neural_style.main()

# import neural_style.neural_style





