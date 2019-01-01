

import sys
# import neural_style
sys.path.insert(0, './fast_neural_style')
sys.path.insert(0, './fast_neural_style/neural_style')
import neural_style

# 
# C:/Users/brantb/AppData/Local/conda/conda/envs/PyTorchE1/python.exe  neural_style/neural_style.py train --dataset D:\local\coco --style-image D:\locadataset_parent_dirt\00000000000#1.jpg --save-model-dir style_imgs --epocs 2 --cudapData/Local/conda/conda/envs/PyT'. style_imgs --epocs 2 --cudapData/Local/conda/conda/envs/PyTorchE1/python.ex1

# sys.argv  = [R'c:\local\PyTorchTesting\examples\fast_neural_style\test_neural_style.py', 'train','--dataset', R'D:\local\coco', '--style-image', R'D:\local\coco\CocoSubset\000000000001.jpg',  R'--save-model-dir',  R'C:\local\PyTorchTesting\examples\saved_models2', R'--epochs', '2', '--cuda', '1']

main_file = R'C:\local\PyTorchTesting\examples\fast_neural_style\neural_style\neural_style.py'

do_training = False

if do_training:
    dataset_parent_dir = R'D:\local\coco'
    style_img = R'D:\local\coco\CocoSubset\000000000001.jpg'
    # save_model_dir = 'saved_models2'
    #save_model_dir = R'C:\local\PyTorchTesting\examples\saved_models2'
    save_model_dir = '.'

    sys.argv  = [main_file, 'train','--dataset', dataset_parent_dir, '--style-image', style_img,  R'--save-model-dir', save_model_dir, R'--epochs', '2', '--cuda', '1']

else:
# eval --content-image </path/to/content/image> --model </path/to/saved/model> --output-image </path/to/output/image> --cuda 0
    content_img = R'D:\local\coco\CocoSubset\000000000345.jpg'
    model_file = R'C:\local\PyTorchTesting\examples\epoch_2_Tue_Jan__1_13_46_12_2019_100000.0_10000000000.0.model'
    output_img = R'C:\local\PyTorchTesting\examples\epoch_2_Tue_Jan__1_13_46_12_2019_100000.0_10000000000.0.model.jpg'
 
    sys.argv  = [main_file, 'eval','--content-image', content_img, '--model', model_file,  '--output-image', output_img, '--cuda', '1']



print(sys.argv)
neural_style.main()


