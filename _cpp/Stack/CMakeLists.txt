cmake_minimum_required(VERSION 3.0.0)

project(Stack VERSION 0.1.0)

add_executable(Stack Stack.cpp)
#target_sources(ArraysAndHashing PRIVATE log.cpp)
target_include_directories(Stack PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_include_directories(Stack PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../include)

