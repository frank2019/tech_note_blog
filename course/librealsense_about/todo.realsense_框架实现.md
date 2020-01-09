





realsense 代码实现



## realsense c语言 API 

realsense 提供了c 语言接口位于：

```
librealsense\include\librealsense2\h
```

librealsense 的c语言API接口 是在



librealsense\include\librealsense2\h\rs_context.h

```c++
/**
* \brief Creates RealSense context that is required for the rest of the API.
* \param[in] api_version Users are expected to pass their version of \c RS2_API_VERSION to make sure they are running the correct librealsense version.
* \param[out] error  If non-null, receives any error that occurs during this call, otherwise, errors are ignored.
* \return            Context object
*/
rs2_context* rs2_create_context(int api_version, rs2_error** error);

/**
* \brief Frees the relevant context object.
* \param[in] context Object that is no longer needed
*/
void rs2_delete_context(rs2_context* context);
```

实现



```c++
rs2_context* rs2_create_context(int api_version, rs2_error** error) BEGIN_API_CALL
{
    verify_version_compatibility(api_version);

    return new rs2_context{ std::make_shared<librealsense::context>(librealsense::backend_type::standard) };
}
HANDLE_EXCEPTIONS_AND_RETURN(nullptr, api_version)

void rs2_delete_context(rs2_context* context) BEGIN_API_CALL
{
    VALIDATE_NOT_NULL(context);
    delete context;
}
NOEXCEPT_RETURN(, context)
```



## realsense c++ API



realsense的c++ 版本的API接口是在c语言API版本基础上封装的。

```c++
librealsense\include\librealsense2\hpp\rs_context.hpp

```

```c++
 /**
    * default librealsense context class
    * includes realsense API version as provided by RS2_API_VERSION macro
    */
    class context
    {
    public:
        context()
        {
            rs2_error* e = nullptr;
            _context = std::shared_ptr<rs2_context>(
                rs2_create_context(RS2_API_VERSION, &e),
                rs2_delete_context);
            error::handle(e);
        }

        /**
        * create a static snapshot of all connected devices at the time of the call
        * \return            the list of devices connected devices at the time of the call
        */
        device_list query_devices() const
        {
            rs2_error* e = nullptr;
            std::shared_ptr<rs2_device_list> list(
                rs2_query_devices(_context.get(), &e),
                rs2_delete_device_list);
            error::handle(e);

            return device_list(list);
        }

        /**
        * create a static snapshot of all connected devices at the time of the call
        * \return            the list of devices connected devices at the time of the call
        */
        device_list query_devices(int mask) const
        {
            rs2_error* e = nullptr;
            std::shared_ptr<rs2_device_list> list(
                rs2_query_devices_ex(_context.get(), mask, &e),
                rs2_delete_device_list);
            error::handle(e);

            return device_list(list);
        }

        /**
         * @brief Generate a flat list of all available sensors from all RealSense devices
         * @return List of sensors
         */
        std::vector<sensor> query_all_sensors() const
        {
            std::vector<sensor> results;
            for (auto&& dev : query_devices())
            {
                auto sensors = dev.query_sensors();
                std::copy(sensors.begin(), sensors.end(), std::back_inserter(results));
            }
            return results;
        }


        device get_sensor_parent(const sensor& s) const
        {
            rs2_error* e = nullptr;
            std::shared_ptr<rs2_device> dev(
                rs2_create_device_from_sensor(s._sensor.get(), &e),
                rs2_delete_device);
            error::handle(e);
            return device{ dev };
        }

        /**
        * register devices changed callback
        * \param[in] callback   devices changed callback
        */
        template<class T>
        void set_devices_changed_callback(T callback)
        {
            rs2_error* e = nullptr;
            rs2_set_devices_changed_callback_cpp(_context.get(),
                new devices_changed_callback<T>(std::move(callback)), &e);
            error::handle(e);
        }

        /**
         * Creates a device from a RealSense file
         *
         * On successful load, the device will be appended to the context and a devices_changed event triggered
         * @param file  Path to a RealSense File
         * @return A playback device matching the given file
         */
        playback load_device(const std::string& file)
        {
            rs2_error* e = nullptr;
            auto device = std::shared_ptr<rs2_device>(
                rs2_context_add_device(_context.get(), file.c_str(), &e),
                rs2_delete_device);
            rs2::error::handle(e);

            return playback { device };
        }

        void unload_device(const std::string& file)
        {
            rs2_error* e = nullptr;
            rs2_context_remove_device(_context.get(), file.c_str(), &e);
            rs2::error::handle(e);
        }

        void unload_tracking_module()
        {
            rs2_error* e = nullptr;
            rs2_context_unload_tracking_module(_context.get(), &e);
            rs2::error::handle(e);
        }

        context(std::shared_ptr<rs2_context> ctx)
            : _context(ctx)
        {}
        explicit operator std::shared_ptr<rs2_context>() { return _context; };
    protected:
        friend class rs2::pipeline;
        friend class rs2::device_hub;
        friend class rs2::software_device;

        std::shared_ptr<rs2_context> _context;
    };

```

