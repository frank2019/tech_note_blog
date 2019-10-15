



## OpenNI::initialize()

- 用于初始化openni库
- 用于加载所有存在得驱动，同时查看哪一个设备存在。
- 禁止在调用此函数之前调用库得其他函数。



流程

1.  OpenNI::initialize()
2. oniInitialize(ONI_API_VERSION)
3. g_Context.initialize();



该函数主要的一个主要功能是枚举 usb 设备，在 windows 下是通过注册表中读取每个
usb 设备的信息和 我们保存 PID， VID 的设备 List 进行比较，对设备进行枚举，枚举到的
设备保存在 Hash 链表 ms_devices。 