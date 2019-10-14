

## 目标

本文描述 OpenNI 2 驱动开发



## 简介



這篇，大概來講一下 OpenNI 2 的驅動程式模組的東西；對於硬體的存取，OpenNI 2 基本上還是採用 plug-in 的模式，在程式執行時，他會去試著使用 \OpenNI2\Drivers 這個目錄下的 dll 檔，如果確認是符合 OpenNI 2 Driver 的架構的話，就會試著拿來用。

目前官方有提供三個模組：PS1080.dll、Kinect.dll、OniFile.dll，分別代表三種不同的資料來源。

- PS1080.dll 對應的就是使用 PrimeSense 官方驅動程式的裝置，包括了 ASUS Xtion 系列感應器，或是 PrimeSense 自家的感應器，都會使用到這個模駔。 
- Kinect.dll 則是透過 Microsoft Kinect for Windows SDK，來對 Microsoft Kinect 系列的感應器做支援，如果進去看的話，就會發現他是使用 Microsoft Kinect for Windows SDK 來做開發的。 
- OniFile.dll 是一個虛擬的裝置，是用來讀取錄製下來的 ONI 檔的。





## openNI驱动的实现



而對於驅動程式模組這部分，雖然 OpenNI 沒有提供相關文件，不過由於整個 SDK 是開放原始碼的，所以這部分也是有提供原始碼的。這些模組的原始碼，都在 https://github.com/OpenNI/OpenNI2/tree/master/Source/Drivers。可以看到，除了提供的三個 binary 外，這邊還有 DummyDevice 和 TestDevice 另外兩個模組，算是不實用、單純用來做測試參考之用的。

基本上，要開發一個 OpenNI 2 的 driver 來存取自己的裝置，需要依循著 OpenNI 2 定義的介面，而這些定義，則是由 \Include\Driver\OniDriverAPI.h 這個檔案（[GitHub](https://github.com/OpenNI/OpenNI2/blob/master/Include/Driver/OniDriverAPI.h)）所提供的。在 oni::driver 這個 namespace 下，包含了 DriverService、DriverBase、DeviceBase、StreamBase 這四個類別。

1. 其中，DriverService 比較像是在作紀錄之用的，在實作自己的驅動程式模組的時候，是可以無視的。 
2. 而 DriverBase 就相當於是要開發的驅動程式模組的主程式，他必須要去管理所有可控制的裝置；而他最後會透過 ONI_EXPORT_DRIVER() 這個巨集匯出，讓外部可以使用；實際上 OpenNI SDK 主要就是透過這個類別，來存取一個驅動程式模組的內容。 
3. DeviceBase 則是對應到 openni::Device，基本上就是對應到單一硬體裝置，要提供建立感應器的 stream、各項 device 屬性的設定介面。
4. 最後，StreamBase 就是對應到 openni::VideoStream，提供單一感應器的資料讀取與控制。

如果想要自己針對特定的裝置，自己寫一個驅動程式模組的話，可以參考官方的 TestDevice、並在參考 Kinect 這個模組（個人不怎麼建議參考 PS1080 這個模組，因為它太複雜了…），稍微摸一下，應該是可以寫得出來的～但是如果要寫的完整，就得下很多工了。

Heresy 自己是有成功地以 TestDevice 為基礎，寫出一個可以使用 OpenCV 來開啟 webcam 的驅動程式模組，不過目前還在調整中；而由於 OpenNI 主要的應用是積雲深度攝影機，所以其實只能讀取彩色的影像的 OpenCV，好像也沒什麼用實際用處就是了。 ^^"

下面，算是一些 Heresy 自己的筆記：

- ##### DriverBase

  - 一定要實做出來的函式，包括了 deviceOpen()、deviceClose()、shutdown()。               
    另外由於 OpenNI 2 一開始就會呼叫 initialize() 做初始化，所以應該也是需要實作的。
  - OpenNI 2 主要應該是透過呼叫 initialize() 時傳進來的三個 callback function，來對驅動程式提供的裝置做管理，當建立新的 device 的資訊（OniDeviceInfo）後想讓 OpenNI 2 能辨識的到，就需要呼叫 deviceConnect() 這個 callback function。
  - 所以，如果不希望 OpenNI 2 的 enumerateDevices() 會直接列出這個裝置、或是不希望在使用 ANY_DEVICE 來開啟裝置的時候可以直接看到自己寫的 device 的話，就不要在 initialize() 裡面，去呼叫 deviceConnect()；相對的，則是需要去實作 tryDevice() 這個函式，讓他去測試外部傳進來的指定 URI，在符合條件的時候、再去呼叫 deviceConnect()，讓 OpenNI 2 可以使用這個 device。

- ##### DeviceBase

  - 需要實作的的函式主要是 getSeneorInfoList()、createStream()、destoryStream()；如果需要其他設定功能，則需要實作 setProperty() 等函式。

- ##### StreamBase

  - 真正用來讀取資料的地方，實作也最複雜。需要實作的函式包括了：start()、stop()、addRefToFrame()、releaseFrame()。一樣，如果需要參數設定等功能，就需要實作 setProperty() 等函式。
  - 在 TestDevice 裡，他的 start() 會去建立一個新的 thread，來做資料的讀取；而當有新的資料的時候，會去呼叫 raiseNewFrame() 這個 callback function，來告訴 OpenNI 有新的畫面了。
  - 讀取出來的影像，要以 OniDriverFrame 的形式來做輸出，必須在這裡透過 addRefToFrame()、releaseFrame() 來做 reference count，做記憶體資源的管理，確定何時要把她的資料釋放掉。
  - 在 OpenNI 2 SDK 裡面，是透過 VideoStream 的 setVideoMode() 來修改感應器的解析度；不過在驅動程式層面，會收到的命令是 setProperty()，所以如果要讓 VideoStream 可以修改解析度的話，是需要實作 setProperty() 的內容的（propertyId 會是 ONI_STREAM_PROPERTY_VIDEO_MODE）。
  - 將深度圖轉換到世界座標系統的計算，基本上應該是基於感應器的 FOV 來做計算的。所以如果是在寫深度感應器的 driver 的話，就必須要透過 getProperty() 提供鏡頭的 FOV 參數（應該是 ONI_STREAM_PROPERTY_HORIZONTAL_FOV 和 ONI_STREAM_PROPERTY_VERTICAL_FOV）。              
    （Heresy 自己沒試過）

這篇大概就先這樣了。基本上，只是一些下去看、試著修改的經驗分享了。實際上，除非是要自己做硬體，或是想要讓其他的深度感應器也能在 OpenNI 的架構下使用，不然應該是沒必要研究這部分的。







https://kheresy.wordpress.com/2013/04/18/concept-of-openni2-driver/