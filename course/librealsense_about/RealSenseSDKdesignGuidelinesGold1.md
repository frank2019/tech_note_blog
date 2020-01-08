# SDK Design Guidelines

version 2 



> Intel® RealSense™ technology will changehow you interact- not simply with your
> devices, but with the world around you. You'll work and play like never before,
> because your devices can see, hear, and feel you. 



## Introduction 

Welcome! 

想象一下新的导航方式拥有更多感官和传感器的世界集成到计算中未来的平台。给你的用户一种新的、自然的、引人入胜的方式体验你的应用程序。在英特尔我们很高兴能提供这些工具这次旅行的基础是Intel Real SenseTM SDK-并查看期待着看到你所做的用。

​    在新的几个月里，你将能够融入新的能力到你的应用中包括近距离手部追踪，语音识别、人脸跟踪、背景分割和对象跟踪从根本上改变人们与他们的设备和他们周围的世界。

### Intel RealSense SDK Architecture 

![](res/arch.png)

- SDK core： SDK 由简单几部分组成，最基础组件是SDK core，它的主要功能之一是：管理两类型的模块

  - 输入输出模块
  - 能力模块

  两类模块提供SDK的功能实现。

- I/O modules ： i/o  模块从设备抓取数据，发送数据到输出设备或者能力模块。能力模块包含各种模式检测和识别算法 比如：脸部跟踪和识别，手部跟踪，姿势识别 和语音识别和合成。

- SDK core 的另一个核心职能是 管理execution pipeline 。有可能有多个模块 同时包含在管道中，因此管道必须有一个管理器。如果你想用在您的应用程序中多个摄像头或其他输入设备，您可能需要多个管道，每个管道都有自己的管道经理。

### Hardware and Software Requirements and Supported Tools 

| Required Hardware                    | A system with a minimum of a 4th generation Intel® Core™ processor,either IA-32 or Intel® 64, with integrated or peripheral depth camera |
| ------------------------------------ | ------------------------------------------------------------ |
| Required OS                          | Microsoft Windows* 8.1 OS (64-bit) Desktop Mode<br/>Microsoft Windows 8.1 New UI (Metro) Mode (coming soon)** |
| Supported Programming Languages      | C++, C#, Java*, JavaScript                                   |
| Supported IDE                        | Microsoft Visual Studio* C++ 2010-2013 with service pack 1 or newer |
| Supported Development Optional Tools | Microsoft .NET* 4.0 Framework for C# development<br/>Unity* PRO 4.1.0 or later for Unity game development<br/>Processing* 2.1.2 or later for Processing framework development<br/>Java JDK 1.7.0_11 or higher for Java development |



### Additional SDK Features 

| Input Device Management   | Easily share camera between applications                     |
| ------------------------- | ------------------------------------------------------------ |
| Multi-mode Support        | Support multiple usage modes within single app (e.g., finger<br/>tracking + speech + face tracking) or between apps |
| Power Management State    | Manage battery life                                          |
| Extensible Framework      | Plug in your own algorithms, add in new usage modes, and<br/>support new devices |
| Privacy Notification Tool | Notify user when camera is turned on by an app               |



### Integrated Depth Camera 

Each of the effective ranges cater to specific interactions: 

| Short Range: 20-55cm (HVGA, 120FPS)                          | Long Range: 20-60cm (VGA, 60FPS)                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| For slow and fast hand movements<br/>Hand skeleton motion up to 2m/s | For slower hand movements<br/>Hand skeleton motions up to .75m/s |
| Single hand                                                  | 2 hands                                                      |

等高线模式BLOB跟踪工作高达1m/s，最多2个BLOB在VGA模式下从20-85cm，最多2m/s在HVGA

模式从20-75厘米。在35-70厘米的范围内，3D人脸跟踪效果最好，而2D人脸跟踪效果在35-120厘米，



blob tracking ：  是指目标跟踪。

## Overview 

### Input Modalities 

新的Intel Real SenseTM技术为彻底重新定义我们与之交互的方式提供了惊人的机会我们的计算设备。要为这个平台设计一个成功的应用程序，你必须了解它的优势。一定要确保利用组合不同的输入模式。这将使它成为一种更令人兴奋和自然的体验对于使用者来说，可以尽量减少手、手指或声音的疲劳

好的设计应该是可以很容易地扩展到不同的模式和模式组合。也要记住你的一些用户可能更喜欢某些模式而不是其他模式，或者有不同的能力。不管投入多少使用的方法，总是至关重要的是研究和评估用户如何实际参与他们的设备，然后建立支持这些自然运动的界面。这里有一些传统和真实感的快速描述方式，以及每种方式最适合用于：

#### Hands

半空手势识别 允许非常富有和2D或3D对象的互动。他们也允许更容易，更文字化直接操纵。不过，此方式长时间会比较累，而且精度有限

#### Face 

感知自然表达，和情感参与的最佳模式，但精确度有限，且各个年龄段的表达，基于文化和个性的原因有很大的差异性。

#### Speech 

人类的语言是强大而令人信服的表达方式。声音是用户不在其他传感器范围内是的首选。同时也考虑环境噪音及社会适当性。

#### Touch 

Very concrete and easy to understand, with the additional benefit of having tactile feedback to touch
events and fairly good precision. However, touch is limited to 2D interaction. It is not as flexible as mid-air
gesture. 

#### Mouse. 

The best modality for the accurate indication of a 2D point. Large-scale screen movements can be made with small mouse movements 

#### Keyboard. 

Allows for quick and accurate text entry for adults, when voice cannot be used. Keyboard shortcuts can be quick escapes, but are not intuitive 



### High-Level Design Principles (高层设计原则)



现实启发，但不是现实的克隆。你应该从现实世界中汲取灵感。英特尔Real Sense建立于

我们在日常生活中使用的自然技能。每天我们都用手去捕捉和操纵物体和声音

去交流。利用这些自然的人类能力。然而，不要盲目地模仿现实。在虚拟环境中

环境，我们可以放松物理世界的规则，使互动更容易。例如，这是非常困难的

用户精确地将他们的虚拟手指包裹在一个虚拟对象上，以便将其捡起来。使用英特尔Real SenseSDK，它

用户可能更容易在虚拟对象的短距离内执行抓取操作，以便拾取它。





## Hands 

#### Contour Mode 

#### Skeleton Tracking 

#### Gesture Recognition 



## Face 

Face Recognition 

### Facial Expressions 

Emotion Recognition 



## Speech 

## Background Removal 



## Object Tracking 