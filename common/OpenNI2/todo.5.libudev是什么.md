

## libudev

linux 下的设备管理库，提供本地设备枚举管理的API





## 使用流程

1. 初始化
首先调用udev_new，创建一个udev library context。udev library context采用引用记数机制，创建的context默认引用记数为1，使用udev_ref和udev_unref增加或减少引用记数，如果引用记数为0，则释放内部资源。
2. 枚举设备
使用udev_enumrate_new创建一个枚举器，用于扫描系统已接设备。使用udev_enumrate_ref和udev_enumrate_unref增加或减少引用记数。
使用udev_enumrate_add_match/nomatch_xxx系列函数增加枚举的过滤器，过滤关键字以字符表示，如"block"设备。
使用udev_enumrate_scan_xxx系列函数扫描/sys目录下，所有与过滤器匹配的设备。扫描完成后的数据结构是一个链表，使用udev_enumerate_get_list_entry获取链表的首个结点，使用udev_list_entry_foreach遍历整个链表。
3. 监控设备插拔 udev的设备插拔基于netlink实现。
使用udev_monitor_new_from_netlink创建一个新的monitor，函数的第二个参数是事件源的名称，可选"kernel"或"udev"。基于"kernel"的事件通知要早于"udev"，但相关的设备结点未必创建完成，所以一般应用的设计要基于"udev"进行监控。
使用udev_monitor_filter_add_match_subsystem_devtype增加一个基于设备类型的udev事件过滤器，例如: "block"设备。
使用udev_monitor_enable_receiving启动监控过程。监控可以使用udev_monitor_get_fd获取一个文件描述符，基于返回的fd可以执行poll操作，简化程序设计。
插拔事件到达后，可以使用udev_monitor_receive_device获取产生事件的设备映射。调用udev_device_get_action可以获得一个字符串："add"或者"remove"，以及"change", "online", "offline"等，但后三个未知什么情况下会产生。

4、获取设备信息
使用udev_list_entry_get_name可以得到一个设备结点的sys路径，基于这个路径使用udev_device_new_from_syspath可以创建一个udev设备的映射，用于获取设备属性。获取设备属性使用udev_device_get_properties_list_entry，返回一个存储了设备所有属性信息的链表，使用udev_list_entry_foreach遍历链表，使用udev_list_entry_get_name和udev_list_entry_get_value获取属性的名称和值。





## 参考链接

1. [libudev使用说明书](https://blog.csdn.net/coroutines/article/details/38067805)
2. [libudev — API for enumerating and introspecting local devices](https://www.freedesktop.org/software/systemd/man/libudev.html)
3. [udev实现原理](https://blog.csdn.net/chituhuan/article/details/52383610)
4. [Linux udev识别移动设备](https://blog.csdn.net/chrisnotfound/article/details/79097044)
5. https://blog.csdn.net/zhaoyi2/article/details/90263523

