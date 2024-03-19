cmake_minimum_required(VERSION 3.0.0)

project(Graphs VERSION 0.1.0)

add_executable(Graphs Graphs.cpp)
#target_sources(Graphs PRIVATE log.cpp)
target_include_directories(Graphs PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_include_directories(Graphs PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../include)

