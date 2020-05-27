





### Q   usb获取数据帧

librealsense\src\mf\mf-uvc.cpp

OnReadSample

```
 STDMETHODIMP source_reader_callback::OnReadSample(HRESULT hrStatus,
            DWORD dwStreamIndex,
            DWORD /*dwStreamFlags*/,
            LONGLONG llTimestamp,
            IMFSample *sample)
```

本函数负责从usb获取数据帧。

```
stream.callback(profile, f, continuation);
```



IMFSourceReaderCallback



```
void aggregator::handle_frame(frame_holder frame, synthetic_source_interface* source)
```



### todo.realsense_SDK是否可以拿到原始IR数据