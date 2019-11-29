# Reference: http://qt-project.org/doc/qt-5.0/qtdoc/cmake-manual.html

# Add folder where are supportive functions
set(CMAKE_INCLUDE_CURRENT_DIR ON)

project(unit-tests)

set(CMAKE_INCLUDE_CURRENT_DIR ON)



ob_include_directories(${LIBINI_INCLUDE_DIRS} ${OBCDEVICE_PUBLIC_HEADERS} ${OBLOGGER_PUBLIC_INC} ${UNIT_TESTS_INCLUDE_DIR} ${LIBSOFTFILTER_INCLUDE_DIRS} ${OBDEPTH_TOF_INC_PUBLIC} ${LIBOPENCV_INCLUDE_DIRS})


#link_directories(${LIBDOTHIN_PATH} ${LIBMX6500_PATH} ${LIBPNG_PATH} ${OBLOGGER_LIBRARIES} ${UNIT_TESTS_COMMON_DIR} ${LIBSOFTFILTER_PATH} 
#				${LIBOPENCV_PATH}
#				${LIBTOF_DEPTH_EXT_PATH}
#				${LIBOPENCV2413_PATH}				)

link_directories(${LIBDOTHIN_PATH} ${LIBMX6500_PATH} ${LIBPNG_PATH} ${OBLOGGER_LIBRARIES} ${UNIT_TESTS_COMMON_DIR} ${LIBSOFTFILTER_PATH} 
				${LIBOPENCV_PATH} )

#add_library(postfilter STATIC IMPORTED)
#set_property(TARGET postfilter PROPERTY IMPORTED_LOCATION ${LIBSOFTFILTER_PATH})



############################################################################
##TOF device unit tests  mlx
############################################################################
link_directories( ${LIBTOF_DEPTH_EXT_PATH}
				${LIBOPENCV2413_PATH} )
add_executable(tof-unit-device-test 
	test_main.cpp 
	tof_device_test.cpp
	tof_property_test.cpp
	tof_phase_stream_test.cpp
	tof_ext_streams_test.cpp
	tof_multi-thread_test.cpp
	multi-thread_lock_test.cpp
	common.cpp)

add_dependencies(tof-unit-device-test ${OBCDEVICE_LIBRARY} ${OBLOGGER_LIBRARY})

target_link_libraries(tof-unit-device-test
	obcdevice
	${OBLOGGER_LIBRARY}
	${LIBSOFTFILTER_NAME}
	${OBDEPTH_TOF_LIBRARY}
)

############################################################################
##TOF device unit tests  SensorTest
############################################################################
link_directories( ${LIBTOF_DEPTH_EXT_PATH}
				${LIBOPENCV2413_PATH} )
add_executable(tof-sensor-test 
	test_main.cpp 
	TestSensor.cpp
	common.cpp)

add_dependencies(tof-sensor-test ${OBCDEVICE_LIBRARY} ${OBLOGGER_LIBRARY})

target_link_libraries(tof-sensor-test
	obcdevice
	${OBLOGGER_LIBRARY}
	${LIBSOFTFILTER_NAME}
	${OBDEPTH_TOF_LIBRARY}
)



#install(FILES common.cpp DESTINATION unit-tests)
#install(FILES common.h DESTINATION unit-tests)
install(FILES tof_device_test.cpp DESTINATION unit-tests)
install(FILES tof_ext_stream_s5k33dxx_test.cpp DESTINATION unit-tests)
install(FILES tof_ext_streams_test.cpp DESTINATION unit-tests)
install(FILES tof_multi-thread_s5k33dxx_test.cpp DESTINATION unit-tests)
install(FILES tof_multi-thread_test.cpp DESTINATION unit-tests)
install(FILES tof_phase_stream_s5k33dxx_test.cpp DESTINATION unit-tests)
install(FILES tof_phase_stream_test.cpp DESTINATION unit-tests)
install(FILES tof_property_test.cpp DESTINATION unit-tests)
install(FILES tof_unit_tests_cmd_howto.md DESTINATION unit-tests)



