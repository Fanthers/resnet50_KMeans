import tkinter as tk
import tkinter.filedialog

import resnet50_kMeans
import cv2 as cv
import os
import os.path as osp


cat, dog, panda = [], [], []

color = ['red', 'green', 'blue', 'pink']
# 获取输入图片路径和输出路径
def path():
    global cat, dog, panda, color
    inp = vai_ei.get()
    out = vai_eo.get()
    k = int(vai_k.get())
    res = resnet50_kMeans.main(inp, out, k)
    for i in range(len(res)):
        if not osp.exists(out + '/' + str(i)): os.makedirs(out + '/' + str(i), exist_ok=True)
        for img_path in res[i]:
            img = cv.imread(img_path)
            cv.imwrite(out + '/' + str(i) + '/' + img_path.split('/')[-1], img)

        # 第7步，在图形界面上设定标签
        l1 = tk.Label(window, text=str(res[i]), bg=color[i%len(color)], font=('Arial', 12), wraplength=600)
        # 第8步，放置标签
        l1.place(x=0, y=160+80*i)


def selectPath(source):
    if source:
        path_ = tkinter.filedialog.askdirectory()
        vai_ei.set(path_)
    else:
        path_ = tkinter.filedialog.askdirectory()
        vai_eo.set(path_)


if __name__ == '__main__':
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()
    # 第2步，给窗口的可视化起名字
    window.title('Image deduplication')
    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('500x600')
    # 第4步，用户信息
    tk.Label(window, text='Input path:', font=('Arial', 12)).place(x=10, y=10)
    tk.Label(window, text='Output path:', font=('Arial', 12)).place(x=10, y=40)
    tk.Label(window, text='Num of label:', font=('Arial', 12)).place(x=10, y=70)
    # 第5步，用户自己输入
    vai_ei = tk.StringVar()  # 用于获取输入变量
    ei_path = tk.Entry(window, textvariable=vai_ei, show=None, font=('Arial', 14))
    ei_path.place(x=120, y=10)
    b1 = tk.Button(window, text='select', font=('Arial', 12), width=10, height=1, command=lambda: selectPath(source=True))  # 传参数时候必须要用lambda
    b1.place(x=380, y=10)

    vai_eo = tk.StringVar()
    eo_path = tk.Entry(window, textvariable=vai_eo, show=None, font=('Arial', 14))
    eo_path.place(x=120, y=40)
    b2 = tk.Button(window, text='select', font=('Arial', 12), width=10, height=1, command=lambda: selectPath(source=False))
    b2.place(x=380, y=40)

    vai_k= tk.StringVar()
    k_path = tk.Entry(window, textvariable=vai_k, show=None, font=('Arial', 14))
    k_path.place(x=120, y=70)

    # 第6步，在窗口界面设置放置Button按键
    b = tk.Button(window, text='Run', font=('Arial', 12), width=10, height=1, command=path)
    b.place(x=120, y=110)

    window.mainloop()
