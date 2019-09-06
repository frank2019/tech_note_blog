cmake_minimum_required(VERSION 3.0)
include(CheckSymbolExists)

# Define executable
add_executable(myexe main.c)

# atan2 requires the math library to be linked
list(APPEND CMAKE_REQUIRED_LIBRARIES m)

check_symbol_exists(atan2 math.h HAVE_ATAN2)

if(NOT HAVE_ATAN2)
	message("do not HAVE_ATAN2")
endif()

# Add compile definitions if we have the library
if(HAVE_ATAN2)
	target_compile_definitions(myexe PRIVATE -DHAVE_ATAN2)
endif()