import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from torch.autograd import Variable
import numpy as np
from PIL import Image
import time
import os.path as osp
from KMeans import kmeans


class config():
    def __init__(self, input='./data/', output='./output/'):
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.input = input
        self.output = output


class Data():
    def __init__(self):
        self.transform = transforms.Compose(
            [
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor()
            ]
        )
    def trans(self, input):
        return self.transform(input)


class net(nn.Module):
    def __init__(self):
        super(net, self).__init__()
        self.net = models.resnet50(pretrained=True)

    def forward(self, input):
        output = self.net.conv1(input)
        output = self.net.bn1(output)
        output = self.net.relu(output)
        output = self.net.maxpool(output)
        output = self.net.layer1(output)
        output = self.net.layer2(output)
        output = self.net.layer3(output)
        output = self.net.layer4(output)
        output = self.net.avgpool(output)
        return output


def main(e1='./data/', e2='./output/', k=3):
    cfg = config(e1, e2)
    device = cfg.device

    trans = Data()
    file_path = cfg.input
    if not osp.exists(cfg.output): os.makedirs(cfg.output, exist_ok=True)
    model = net()
    model.to(device)

    y_all = []
    animal_list = []
    for animal in os.listdir(file_path):
        imgPatn = file_path + '/' + animal
        animal_list.append(imgPatn)
        img = Image.open(imgPatn)
        img = trans.trans(img)
        # print(img.shape)  # torch.Size([3, 224, 224])
        with torch.no_grad():
            x = Variable(torch.unsqueeze(img, dim=0).float(), requires_grad=False)
            # print(x.shape)  # torch.Size([1, 3, 224, 224])
            x = x.to(device)
            y = model(x)  # # (1, 2048, 1, 1)
            y = y.squeeze(dim=0).view(1, -1).cpu()
            y = y.data.numpy().tolist()[0]
            # print(y.shape)  # (2048, )
            y_all.append(y)
    np.savetxt('./output/animal.txt', y_all, delimiter=',')
    labels = kmeans(k)
    ani = [[] for _ in range(k)]
    for i in range(len(animal_list)):
        ani[labels[i]].append(animal_list[i])
    return ani


if __name__ == '__main__':
    main()
