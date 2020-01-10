





## src\environment.h



### class environment

- environment  是一个单例模式的类
- 重要成员变量并提供get/set函数 time_service(),用以提供时间函数get_time()
- 成员函数generate_stream_id()   用于生成stream id  基于原子操作累加。
-  成员函数extrinsics_graph& get_extrinsics_graph() 用于获取成员变量。



```c++
 class environment
    {
    public:
        static environment& get_instance();

        extrinsics_graph& get_extrinsics_graph();

        int generate_stream_id() { return _stream_id.fetch_add(1); }

        void set_time_service(std::shared_ptr<platform::time_service> ts);
        std::shared_ptr<platform::time_service> get_time_service();

     	//禁止构造函数和赋值函数
        environment(const environment&) = delete;
        environment(const environment&&) = delete;
        environment operator=(const environment&) = delete;
        environment operator=(const environment&&) = delete;
    private:

        extrinsics_graph _extrinsics;
        std::atomic<int> _stream_id;
        std::shared_ptr<platform::time_service> _ts;
        environment(){_stream_id = 0;}

    };
```



### class extrinsics_graph