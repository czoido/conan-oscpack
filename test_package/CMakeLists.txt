cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example example.cpp)

IF(WIN32)
    target_link_libraries(example ${CONAN_LIBS} Ws2_32 winmm)
ELSE(WIN32)
    target_link_libraries(example ${CONAN_LIBS})
ENDIF(WIN32)
