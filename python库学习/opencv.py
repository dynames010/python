import cv2
img = cv2.imread(r'D:\xzc\video\boli\indoorbacklight_BL_1\green_frame_129.png')
img_cv2_method = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
R,G,B = cv2.split(img_cv2_method)
green_mean = img[:, :, 1].mean()
red_mean = img[:,:,0].mean()
blue_mean = img[:,:,2].mean()
print('红色分量均值：{0}'.format(red_mean))
print('绿色分量均值：{0}'.format(green_mean))
print('蓝色分量均值：{0}'.format(blue_mean))

#cv2.imshow('figure_R',R)
#cv2.imshow('figure_G',G)
#cv2.imshow('figure_B',B)
cv2.waitKey(0)
#import numpy as np
# import matplotlib.pyplot as plt
#
# # 读取图片
# pic_file=r'D:\xzc\video\indoor.png'
# img_bgr = cv2.imread(pic_file,cv2.IMREAD_COLOR)
# cv2.imshow("input",img_bgr)
# # 分别获取三个通道的ndarray数据
# img_b=img_bgr[:,:,0]
# img_g=img_bgr[:,:,1]
# img_r=img_bgr[:,:,2]
#
# '''按R、G、B三个通道分别计算颜色直方图'''
# b_hist = cv2.calcHist([img_bgr],[0],None,[256],[0,255])
# g_hist = cv2.calcHist([img_bgr],[1],None,[256],[0,255])
# r_hist = cv2.calcHist([img_bgr],[2],None,[256],[0,255])
# m,dev = cv2.meanStdDev(img_bgr)  #计算G、B、R三通道的均值和方差
# # img_r_mean=np.mean(r_hist)  #计算R通道的均值
# # print(m)
# # print(dev)
#
# '''显示三个通道的颜色直方图'''
# plt.plot(b_hist,label='B',color='blue')
# plt.plot(g_hist,label='G',color='green')
# plt.plot(r_hist,label='R',color='red')
# plt.legend(loc='best')
# plt.xlim([0,256])
# plt.show()
# cv2.waitKey(0)