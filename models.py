## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        #self.conv1 = nn.Conv2d(1, 32, 5)
        self.conv1 = nn.Conv2d(1, 10, 5)
        self.conv2 = nn.Conv2d(10, 20, 5)
        
        self.fc1 = nn.Linear(56180, 1000)
        self.out = nn.Linear(1000, 136)
        #self.fc2 = nn.Linear(128, 64)
        #self.out = nn.Linear(64, 
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        

        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        ## x = self.pool(F.relu(self.conv1(x)))
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        print('conv1: ' + str(x.shape))
        x = F.relu(F.max_pool2d(self.conv2(x), 2))
        print('conv2: ' + str(x.shape))
        
        x = x.view(-1, 56180)
        x = F.relu(self.fc1(x))
        x = self.out(x)
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
