

`3D` Camera  `TOF` 与 结构光

```

```



TOF和结构光都是当前主流的3D camera方案之一。



#### TOF

TOF这个3D模块中最核心的器件在于TOF芯片，它集众多功能于一身，**包括驱动投射器，接收反射光线，进而生成raw图，再送给软件处理成深度信息**

1. TOF芯片从CCD转向CMOS，在功耗方面实现了很大的突破，使在手机上应用得以可能。







#### 3D Camera 方案对比



|          | 3D结构光              | TOF                    | 双目方案             |
| -------- | --------------------- | ---------------------- | -------------------- |
| 基础原理 | 散斑结构光            | 飞行时间               | 视觉方案             |
| 激光电源 | 15000散斑             | 均匀面光源             | 无                   |
| 工作距离 | 0.2m=1.2m             | 0.4-5m                 | <2m                  |
| 深度精度 | <=1mm                 | 绝对1%，相对0.5%       | 5%-10%               |
| 适用范围 | 全天候                | 全天候                 | 暗光无特征点无法使用 |
| 功耗     | 中                    | 中                     | 高                   |
| 应用范围 | 人脸识别 支付，3D美颜 | 3D建模 AR应用 体感游戏 | 背景虚化             |





http://tools.android-studio.org/index.php/notes



