# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CMake.app/Contents/bin/cmake

# The command to remove a file.
RM = /Applications/CMake.app/Contents/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/mike/dev/neetcode/_cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/mike/dev/neetcode/_cpp/build

# Include any dependencies generated for this target.
include Trees/CMakeFiles/Trees.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include Trees/CMakeFiles/Trees.dir/compiler_depend.make

# Include the progress variables for this target.
include Trees/CMakeFiles/Trees.dir/progress.make

# Include the compile flags for this target's objects.
include Trees/CMakeFiles/Trees.dir/flags.make

Trees/CMakeFiles/Trees.dir/Trees.cpp.o: Trees/CMakeFiles/Trees.dir/flags.make
Trees/CMakeFiles/Trees.dir/Trees.cpp.o: /Users/mike/dev/neetcode/_cpp/Trees/Trees.cpp
Trees/CMakeFiles/Trees.dir/Trees.cpp.o: Trees/CMakeFiles/Trees.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/mike/dev/neetcode/_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Trees/CMakeFiles/Trees.dir/Trees.cpp.o"
	cd /Users/mike/dev/neetcode/_cpp/build/Trees && /usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT Trees/CMakeFiles/Trees.dir/Trees.cpp.o -MF CMakeFiles/Trees.dir/Trees.cpp.o.d -o CMakeFiles/Trees.dir/Trees.cpp.o -c /Users/mike/dev/neetcode/_cpp/Trees/Trees.cpp

Trees/CMakeFiles/Trees.dir/Trees.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Trees.dir/Trees.cpp.i"
	cd /Users/mike/dev/neetcode/_cpp/build/Trees && /usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/mike/dev/neetcode/_cpp/Trees/Trees.cpp > CMakeFiles/Trees.dir/Trees.cpp.i

Trees/CMakeFiles/Trees.dir/Trees.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Trees.dir/Trees.cpp.s"
	cd /Users/mike/dev/neetcode/_cpp/build/Trees && /usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/mike/dev/neetcode/_cpp/Trees/Trees.cpp -o CMakeFiles/Trees.dir/Trees.cpp.s

# Object files for target Trees
Trees_OBJECTS = \
"CMakeFiles/Trees.dir/Trees.cpp.o"

# External object files for target Trees
Trees_EXTERNAL_OBJECTS =

Trees/Trees: Trees/CMakeFiles/Trees.dir/Trees.cpp.o
Trees/Trees: Trees/CMakeFiles/Trees.dir/build.make
Trees/Trees: Trees/CMakeFiles/Trees.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/mike/dev/neetcode/_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Trees"
	cd /Users/mike/dev/neetcode/_cpp/build/Trees && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Trees.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Trees/CMakeFiles/Trees.dir/build: Trees/Trees
.PHONY : Trees/CMakeFiles/Trees.dir/build

Trees/CMakeFiles/Trees.dir/clean:
	cd /Users/mike/dev/neetcode/_cpp/build/Trees && $(CMAKE_COMMAND) -P CMakeFiles/Trees.dir/cmake_clean.cmake
.PHONY : Trees/CMakeFiles/Trees.dir/clean

Trees/CMakeFiles/Trees.dir/depend:
	cd /Users/mike/dev/neetcode/_cpp/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/mike/dev/neetcode/_cpp /Users/mike/dev/neetcode/_cpp/Trees /Users/mike/dev/neetcode/_cpp/build /Users/mike/dev/neetcode/_cpp/build/Trees /Users/mike/dev/neetcode/_cpp/build/Trees/CMakeFiles/Trees.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Trees/CMakeFiles/Trees.dir/depend

