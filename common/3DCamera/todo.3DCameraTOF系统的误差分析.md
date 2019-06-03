





连续调制TOF图像误差来源及降噪处理

http://www.wanfangdata.com.cn/details/detail.do?_type=perio&id=hfgydxxb201204012





在现有技术中，TOF深度相机的主要误差来源有以下三种：

1、由奇次谐波带来的周期性误差，亦简称为“wiggling”。

2、由入射光强度变化而引起的误差。

3、由于积分时间不同而带来的误差。



要获取精确地获得深度信息必须对这些误差进行校正(Lindner
M,Kolb A.Calibration of the intensity-related distance error of the PMD
ToF-camera[C]//Optics East 2007.International Society for Optics and 
Photonics,2007:67640W-67640W-8.)。同时又由于制造上的原因每个像素点不可				
能完全相同，在TOF深度相机矫正时往往会对每个像素的偏移进行校正，再对其他误差进行全局的标定。