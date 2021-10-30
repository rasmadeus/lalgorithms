cmake_minimum_required(VERSION 3.10)
project(lalgorithms VERSION 1.0.0)

enable_testing()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_subdirectory(graphs)
