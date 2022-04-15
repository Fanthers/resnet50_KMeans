# resnet50_KMeans
+ 目的是为了对图片进行去重

## 0.安装
+ conda create -n RNKM python==3.8
+ conda activate RNKM
+ conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.1 -c pytorch

注意torch版本要根据自己电脑配置选择合适的，还要对上python版本

## 1.准备数据
+ 把要去重的图片放在data目录下
+ 创建output目录用来保存输出

## 2.运行命令：
+ python main.py

## 3.设置
+ 输入路径：要选择data目录下
+ 输出路径：要选择在output目录下
+ 选定KMeans初始簇类：默认3
+ 点击Run按钮

## 4.结果
+ 会在output目录下生成animal.txt提取结果向量，还有分完簇之后，每个簇放在了同一个文件夹
