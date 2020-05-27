



# librealsense API层 功能



# 概述及目标

本文主要描述 librealsense 对外提供的功能有哪些。

本文以librealsense c语言接口API  为依据，进行描述，抽象该SDK定义的主要概念，及提供的主要功能。



librealsense c语言接口API。

- librealsense 的C++ 接口是在C语言接口的基础上封装的。
- 使用的是面对对象的方式。
- 头文件位于: include\librealsense2\中 后缀为.h的文件。



# 主要的对象

## 基础对象

多数api 都离不开的。

### rs2_context

rs2_context  跟大多数SDK的context一样用来存储rs2的上下文信息，多数的API 都会用到此对象。



**功能**

1. 创建/删除rs2_context

2. 注册设备状态变化回调事件(当有新设备连接进来或者有设备断开连接)

3. 移除跟踪模块(TM2 position-tracking sensor)

4. 创建设备rs2_device并添加到context中

5. 将已有软件设备 添加到context

6. context 删除一个回访文件设备 (playback device)

7. 查询当前设备列表

    

   

### rs2_device/rs2_device_list

rs2 上下文，设备信息，设备接口

**功能**

5. 设备列表中设备的创建/删除/查询数量/是否包含等
6. 通过设备查询rs2_camera_info，以及查询设备是否支持此rs2_camera_info（camera name，设备序列号，主设备固件版本等等）
7. 设备复位
8. 发送RAW数据到设备并接收回应
9. 检测设备是否支持某项扩展或者功能（rs2_extension）
10. 从设备获取 rs2_sensor_list
11. 使能设备进入loopback模式（指定 bag 文件）
12. 关闭/查询  设备 loopback 模式。
13. 连接/断开 tm2_controller
14. 复位设备到工厂校准模式
15. 写校准到EEPROM?（rs2_write_calibration）
16. 更新固件，带进度回调。
17. 从设备备份固件（此固件包含所有的校准信息和设备信息，但是不等同于原固件镜像，也不能被回写到设备）
18. 使用raw buffer  更新 固件直接写入到固件的flash上,带进度回调。
19. 使能设备进入更新模式。
20. 设备自校准，根据输入的校准参数进行校准(会加大深度噪声),返回健康系数作为参考。
21. 使用给定的平面距离进行校准。
22. 从FLASH读取/设置 校准表..



### rs2_device_hub

封装了处理设备连接/断开的句柄



1. 创建/删除rs2_device_hub；
2. 查询当前连接的设备；
3. 查询设备是否处于连接中。





### rs2_sensor/rs2_sensor_list



sensor  指设备内的传感对象  比如 depth sensor，ir sensor 等等。



1. 删除rs2_sensor_list

2. 从rs2_sensor_list 中创建/查询/删除rs2_sensor 

3. 通过rs2_sensor  创建rs2_device

4. 通过rs2_sensor  查询rs2_camera_info

5. rs2_is_sensor_extendable_to

6. 获取深度传感器深度单位

7. 从rs2_frame/rs2_sensor中获取baseline

8. 设置/获取自动曝光算法要使用的活动区域

9. rs2_open 通过提交配置，打开用于独占访问的子设备

10. rs2_open_multiple  （通过提交复合配置文件，指定一个或多个流配置文件，打开用于独占访问的子设备

    这种方法应用于相互依赖的流，如深度和红外，必须一起配置）

11. rs2_close

12. rs2_start  开始获取数据帧， 回调方式

13. rs2_start_queue  开始获取数据帧， 数据帧放在给定的rs2_frame_queue 中。

14. rs2_stop

15. rs2_set_notifications_callback   注册通告的回调。在enum rs2_notification_category 中定义了一些支持的通过说明。

16. 获取通告  描述/时间戳/严重程度/分类/序列化数据。

17. 获取sensor 所支持的流特性列表（rs2_stream_profile_list  ） 

18. 从rs2_sensor 获取 特定sensor所推荐的处理块列表（ rs2_processing_block_list）



### rs2_stream_profile/rs2_stream_profile_list

每一个rs2_stream_profile 是sensor所支持的流类型。



1. 从list中获取profile/删除列表
2. 解析或者设置rs2_stream_profile
3. 利用现有的profile构造新的profile
4. 删除profile
5. 判断profile是否支持某个特性
6. 从profile 中获取分辨率，内参，外参
7. 在rs2_stream_profile之间拷贝参数
8. 设置给定sensor 的给定 rs2_stream_profile 的  rs2_intrinsics，rs2_motion_device_intrinsic



？？

### rs2_processing_block/rs2_processing_block_list

处理块，对数据帧特定功能的处理模块



1. rs2_processing_block_list 的查找/删除/

2. 创建深度可视化着色处理块；

3. 创建基于时间戳的同步处理块

4. 创建点云处理块

5. 创建yuv解码处理块（已经基于CUDA SSE2等优化，会增加更多的支持如GLSL openCL）

6. 创建深度阈值处理块

7. 创建深度单位转换处理块

8. 创建自定义功能处理块，方便中间件开发者自定义处理块功能

9. 为给定的处理块 添加定制的option

10. 启动处理块 支持回调方式，队列方式；

11. 传递一个rs2_frame 到给定处理块

12. 删除处理块

13. 创建对齐处理块

14. 创建深度滤波后处理降采样模块  rs2_create_decimation_filter_block

15. 创建深度滤波 时域处理块  rs2_create_temporal_filter_block

16. 创建深度滤波 空间处理块rs2_create_spatial_filter_block

17. 创建视察转深度 处理块

18. 创建 HoleFilling 滤波器 处理块

19. 创建打印帧率处理块

20. rs2_create_zero_order_invalidation_block

21. 获取处理块信息

22. 检查处理块是否支持rs2_camera_info/rs2_extension

    



### rs2_frame_queue

realsense 自定义的带同步功能的队列。



1. 创建/删除队列
2. 延时等待/非阻塞获取rs2_frame
3. 入列rs2_frame

   





### rs2_pipeline

pipeline简化了用户与设备 计算机视觉处理模块的交互.

抽象了相机的配置和流 视觉模块.

它使应用程序集中于模块的计算机视觉输出或设备输出数据。

管道可以管理计算机视觉模块，这些模块是作为处理块实现的。

管道是处理块接口的使用者，而应用程序则使用计算机视觉界面.



1. 创建/删除rs2_pipeline
2. 使用默认配置/指定配置启动pipline，可带回调。
3. 阻塞/非阻塞方式获取一帧数据。
4. 获取当前的rs2_pipeline_profile/当前的rs2_device；
5. 停止rs2_pipeline



### rs2_pipeline_profile

当前rs2_pipeline的信息和特性



1. 删除rs2_pipeline_profile

2. 从rs2_pipeline_profile 获取 rs2_stream_profile_list；

   



### rs2_config

配置可以让用户为pipeline  选择  设备/流/处理块/滤波器等；



1. 创建/删除rs2_config；
2. 配置config  开启指定流/(序列号)设备，使用指定的指定帧格式；
3. 配置config  关闭流；
4. 配置config 录制到文件。
5. 根据rs2_config 解析得到rs2_pipeline_profile；
6. 判断rs2_config  是否与rs2_pipeline  匹配。





### rs2_frame



每帧数据中包含一些只读元数据，用于表示帧的一些信息，主要有：帧序号，帧时间戳，增益水平，自动曝光，曝光值，白平衡，到达时间，。。。。





**功能项**

1. 获取帧的指定元数据值。

2. 检测帧是否支持指定元数据。

3. 获取帧时间戳类型。硬件时钟/系统时钟/硬件时钟转换为系统时钟。

4. 获取时间戳

5. 获取sensor

6. 获取

7. 获取数据/数据大小。

8. 获取分辨率

9. 获取每帧的字节数   仅数据区？

10. 获取帧中每像素的比特数。

11. rs2_frame_add_ref

12. rs2_keep_frame

13. 获取rs2_vertex数据

14. rs2_export_to_ply

15. rs2_get_frame_texture_coordinates

16. rs2_get_frame_points_count

17. 获取rs2_stream_profile

18. 判断帧是否支持 rs2_extension

19. 使用处理块提供的帧源分配新的视频帧/运动帧/points帧

20. rs2_allocate_composite_frame  复合帧 是什么？

21. 从复合帧中释放帧

22. 获取复合帧的个数

23. 分发指定的帧

24. 从rs2_frame帧中获取姿态数据 rs2_pose

    

### rs2_options/rs2_options_list

特性集合



**功能**

1. 判断指定option 是否只读

2. 判断是否支持指定option

3. 获取/设置 option

4. 获取支持的option 列表，列表长度

5. 删除 rs2_options_list

6. 从rs2_options_list 中回去option

7. 从list获取 option

8. 获取指定option的范围/name/描述

   

### record_device/playback_device(rs2_device)

rs2_device的一种，用于存储 设备数据到文件。



**功能**

1. 创建record_device，可标识是否压缩。
2. 暂停记录设备
3. 恢复记录设备
4. 从record_device 中获取记录文件名
5. 创建回放设备
6. 从回放设备获取文件名
7. 从回放设备获取录制时间
8. 设置要播放的位置
9. 获取当前播放到的位置
10. 回放设备回放暂停/恢复
11. 回放设备设置是否real-time  mode
12. 检测回放设备是否处于real-time mode.
13. 回放设备 设置状态变化回调
14. 获取状态
15. 回放设备设置速率
16. 回放设备停止。



### rs_advanced_mode.h

rs2_device advanced-mode 控制，可对固件进行一些参数的配置。



1. 开关 advanced-mode
2. 检测设备是否开启advanced-mode
3. 设置/获取 深度控制参数(STDepthControlGroup)
4. 设置获取 
   1. STRsm
   2. STRauSupportVectorControl
   3. STColorControl
   4. STRauColorThresholdsControl
   5. STSloColorThresholdsControl
   6. STSloPenaltyControl
   7. STHdad
   8. STColorCorrection
   9. STDepthTableControl
   10. STAEControl
   11. STCensusRadius
   12. STAFactor

5. 可以使用JSON 模式加载如上配置参数；
6. 读取json格式的配置参数。



### rs.h

一些 关于常用数据结构 日志等的定义

#### rs2_raw_data_buffer

裸数据buffer

**功能**

1. 获取buffer size/buffer数据
2. 删除buffer



功能

1. 从rs2_frame 获取指定像素的距离
2. 获取指定时间点，正常或record mode时 返回系统时间，回放模式时返回当前的录制中的时间。
3. 写一条日志到librealsense log
4. 获取SDK版本
5. 设置记录日志到文件/到标准输出。

----



### TM2 position-tracking sensor

#### rs2_import_localization_map



## 特性属性集合

### rs2_extension

@rs_types.h

1. enum rs2_extension
2. 指定了一些高级的功能(能力) 可能会实现



主要包含的能力，比如 调试，深度帧，视频帧，动作帧，姿态帧，TM2 跟踪传感器，等等。



### rs2_camera_info

@rs_sensor.h

1. enum rs2_camera_info

2. 设备中定义的只读字符串；

3. 并不是每种设备支持所有属性；

   

主要包含的内容有：  名字，设备序列号，固件版本，推荐固件版本，设备所连接的端口的唯一标识符，开启固件日志操作码，是否处于adviced-mode，usb 产品ID，EEPROM是否被锁，USB类型(USB2.0/USB3.0),intel 产品线，ASIC 序列号，Firmware update ID 



## 接口的封装

以rs2_device为例子，

rs2_device 的定义如下：

```c++
struct rs2_device
{
    std::shared_ptr<librealsense::context> ctx;
    std::shared_ptr<librealsense::device_info> info;
    std::shared_ptr<librealsense::device_interface> device;
};
```

使用智能指针对其中的成员进行了封装，具体的实现都在 namespace librealsense  对应的类中。

 namespace librealsense 中实现的类的基础上组合，封装。





## 疑问

1. tracking_module  是什么

2. rs2_device_hub  是什么

3. software_device  是什么

4. loopback模式

   

   rs2_connect_tm2_controller



