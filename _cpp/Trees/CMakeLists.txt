cmake_minimum_required(VERSION 3.0.0)

project(Trees VERSION 0.1.0)

add_executable(Trees Trees.cpp)
#target_sources(ArraysAndHashing PRIVATE log.cpp)
target_include_directories(Trees PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_include_directories(Trees PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../include)

