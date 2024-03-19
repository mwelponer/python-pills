cmake_minimum_required(VERSION 3.0.0)
project(thecherno VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17")

add_subdirectory(_test)
add_subdirectory(ArraysAndHashing)
add_subdirectory(TwoPointers)
add_subdirectory(SlidingWindow)
add_subdirectory(Stack)
add_subdirectory(BinarySearch)
add_subdirectory(LinkedList)
add_subdirectory(Trees)
add_subdirectory(HeapPriorityQueue)
#add_subdirectory(BackTracking)
add_subdirectory(Graphs)

#target_sources(thecherno PRIVATE Utils.cpp)
#target_include_directories(thecherno PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
