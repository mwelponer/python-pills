cmake_minimum_required(VERSION 3.0.0)

project(LinkedList VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -std=c++17")

add_executable(LinkedList LinkedList.cpp)
#target_sources(ArraysAndHashing PRIVATE log.cpp)
target_include_directories(LinkedList PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_include_directories(LinkedList PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../include)

