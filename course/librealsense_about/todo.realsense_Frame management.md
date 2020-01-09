

librealsense2为帧管理和同步提供了灵活的模型。文档将概述帧内存管理、线程之间的帧传递和同步。

## API Overview

核心的抽象类是`rs2::frame`类和 `rs2::device::start`方法，所有其他管理和同步原语都可以从这两个API中派生出来。

```
/**
 * Start passing frames into user provided callback
 * \param[in] callback   Stream callback, can be any callable object accepting rs2::frame
 */
template<class T>
void start(T callback) const;
```





## 参考链接

1. [Frame management](https://dev.intelrealsense.com/docs/frame-management)