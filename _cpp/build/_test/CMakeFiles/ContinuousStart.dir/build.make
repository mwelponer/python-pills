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

# Utility rule file for ContinuousStart.

# Include any custom commands dependencies for this target.
include _test/CMakeFiles/ContinuousStart.dir/compiler_depend.make

# Include the progress variables for this target.
include _test/CMakeFiles/ContinuousStart.dir/progress.make

_test/CMakeFiles/ContinuousStart:
	cd /Users/mike/dev/neetcode/_cpp/build/_test && /Applications/CMake.app/Contents/bin/ctest -D ContinuousStart

ContinuousStart: _test/CMakeFiles/ContinuousStart
ContinuousStart: _test/CMakeFiles/ContinuousStart.dir/build.make
.PHONY : ContinuousStart

# Rule to build all files generated by this target.
_test/CMakeFiles/ContinuousStart.dir/build: ContinuousStart
.PHONY : _test/CMakeFiles/ContinuousStart.dir/build

_test/CMakeFiles/ContinuousStart.dir/clean:
	cd /Users/mike/dev/neetcode/_cpp/build/_test && $(CMAKE_COMMAND) -P CMakeFiles/ContinuousStart.dir/cmake_clean.cmake
.PHONY : _test/CMakeFiles/ContinuousStart.dir/clean

_test/CMakeFiles/ContinuousStart.dir/depend:
	cd /Users/mike/dev/neetcode/_cpp/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/mike/dev/neetcode/_cpp /Users/mike/dev/neetcode/_cpp/_test /Users/mike/dev/neetcode/_cpp/build /Users/mike/dev/neetcode/_cpp/build/_test /Users/mike/dev/neetcode/_cpp/build/_test/CMakeFiles/ContinuousStart.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : _test/CMakeFiles/ContinuousStart.dir/depend

