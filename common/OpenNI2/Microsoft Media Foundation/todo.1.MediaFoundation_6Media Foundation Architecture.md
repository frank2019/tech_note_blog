# Media Foundation Architecture

- 05/31/2018 							
- 2 minutes to read
-  [	![img](https://github.com/drewbatgit.png?size=32) 												![img](https://github.com/msatranjr.png?size=32) 									 								](https://github.com/MicrosoftDocs/win32/blob/docs/desktop-src/medfound/media-foundation-architecture.md) 							

This section describes the general design of Microsoft Media  Foundation. For information about using Media Foundation for specific  programming tasks, see [Media Foundation Programming Guide](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-programming-guide).

## In this section

| Topic                                                        | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Overview of the Media Foundation Architecture](https://docs.microsoft.com/en-us/windows/win32/medfound/overview-of-the-media-foundation-architecture) | Gives a high-level overview of the Media Foundation architecture. |
| [Media Foundation Primitives](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-primitives) | Describes some basic interfaces that are used throughout Media Foundation.  Almost all Media Foundation applications will use these interfaces. |
| [Media Foundation Platform APIs](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-platform-apis) | Describes core Media Foundation functions, such as asynchronous callbacks and work queues.   Some applications might use platform-level interfaces. Also, custom  plug-ins, such as media sources and MFTs, use these interfaces. |
| [Media Foundation Pipeline](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-pipeline) | The Media Foundation pipeline layer consists of media sources, MFTs,  and media sinks. Most applications do not call methods directly on the  pipeline layer. Instead, applications use one of the higher layers, such  as the Media Session or the Source Reader and Sink Writer. |
| [Media Session](https://docs.microsoft.com/en-us/windows/win32/medfound/media-session) | The Media Session manages data flow in the Media Foundation pipeline. |
| [Source Reader](https://docs.microsoft.com/en-us/windows/win32/medfound/source-reader) | The Source Reader enables an application to get data from a media  source, without the applicating needing to call the media source APIs  directly. The Source Reader can also perform decoding of compressed  streams. |
| [Protected Media Path](https://docs.microsoft.com/en-us/windows/win32/medfound/protected-media-path) | The protected media path (PMP) provides a protected environment for  playing premium video content. It is not necessary to use the PMP when  writing a Media Foundation application. |

 

## Related topics

-  [About Media Foundation](https://docs.microsoft.com/en-us/windows/win32/medfound/about-the-media-foundation-sdk) 
-  [Media Foundation: Essential Concepts](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-programming--essential-concepts) 
-  [Media Foundation and COM](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-and-com) 
-  [Media Foundation Programming Guide](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-programming-guide) 