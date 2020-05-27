



## Intel RealSense SDK Architecture 



![](res/arch.png)



- SDK core： SDK 由简单几部分组成，最基础组件是SDK core，它的主要功能之一是：管理两类型的模块

  - 输入输出模块
  - 能力模块

  两类模块提供SDK的功能实现。

- I/O modules ： i/o  模块从设备抓取数据，发送数据到输出设备或者能力模块。能力模块包含各种模式检测和识别算法 比如：脸部跟踪和识别，手部跟踪，姿势识别 和语音识别和合成。


- SDK core 的另一个核心职能是 管理execution pipeline 。有可能有多个模块 同时包含在管道中，因此管道必须有一个管理器。如果你想用在您的应用程序中多个摄像头或其他输入设备，您可能需要多个管道，每个管道都有自己的管理器。



## 未来要添加的功能

| Input Device Management   | Easily share camera between applications                     |
| ------------------------- | ------------------------------------------------------------ |
| Multi-mode Support        | Support multiple usage modes within single app (e.g., finger<br/>tracking + speech + face tracking) or between apps |
| Power Management State    | Manage battery life                                          |
| Extensible Framework      | Plug in your own algorithms, add in new usage modes, and<br/>support new devices |
| Privacy Notification Tool | Notify user when camera is turned on by an app               |





## 参考链接

1. [RealSenseSDKdesignGuidelinesGold.pdf](https://software.intel.com/sites/default/files/managed/0b/0a/RealSenseSDKdesignGuidelinesGold.pdf)