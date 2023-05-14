import matplotlib.pyplot as plt
import numpy as np

#绘制折线图
# t = np.arange(0,2,0.1)
# #plt.plot(range(3),[1,2,3])
# plt.plot(t,t,t*3,t*3,'g:')
# plt.scatter(t,t*5)
#plt.bar(range(4),[1,2,3,4])
# plt.show()

#绘制散点图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('PSNR均值')
plt.xlabel('1541测试结果')
plt.ylabel('不同配置PSNR均值')

#绘制直方图
a = np.array([22,10,5,3,65,79,5])
#用Numpy生成直方图数据，再用plt作图，a表示传入的数组数，bins中连续的元素表示直方图的边界
np.histogram(a,bins = [0,10,20,30,40,50,80])
plt.hist(a, bins = [0,10,20,30,40,50,80])
plt.title('histogram')
plt.show()

#plt.subplot(211)
# plt.plot([25.36,14.47,14.23,17.21,15.85,19.55,21.38], color='green',linewidth=3, label='ASR 1497')
# plt.plot([26.05,14.84,14.56,14.45,13.85,18.76,10.94], color='red',linewidth=3, label='HK')
plt.plot([31.5,32.26,31.6], color='yellow',linewidth=3,lable='ASR 1541')
index_name = ['H264_VBR', 'H265_CBR', 'H265_VBR']
plt.legend(loc = 'best')
#index_name = ['暗室0lux','暗室30lux','暗室60lux','工位静态','工位动态','办公室走廊','夜景']
plt.xticks(range(3),index_name)
#plt.yticks(range(25))
plt.show()

