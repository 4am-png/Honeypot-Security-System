cmake_minimum_required(VERSION 3.10)
project(CppAnalyzer)

set(CMAKE_CXX_STANDARD 17)

include_directories(${PROJECT_SOURCE_DIR}/src)


file(GLOB SOURCES src/*.cpp)

add_executable(cpp_analyzer ${SOURCES})

