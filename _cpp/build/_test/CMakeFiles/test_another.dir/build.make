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
include _test/CMakeFiles/test_another.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include _test/CMakeFiles/test_another.dir/compiler_depend.make

# Include the progress variables for this target.
include _test/CMakeFiles/test_another.dir/progress.make

# Include the compile flags for this target's objects.
include _test/CMakeFiles/test_another.dir/flags.make

_test/CMakeFiles/test_another.dir/another.cpp.o: _test/CMakeFiles/test_another.dir/flags.make
_test/CMakeFiles/test_another.dir/another.cpp.o: /Users/mike/dev/neetcode/_cpp/_test/another.cpp
_test/CMakeFiles/test_another.dir/another.cpp.o: _test/CMakeFiles/test_another.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/mike/dev/neetcode/_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object _test/CMakeFiles/test_another.dir/another.cpp.o"
	cd /Users/mike/dev/neetcode/_cpp/build/_test && /usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT _test/CMakeFiles/test_another.dir/another.cpp.o -MF CMakeFiles/test_another.dir/another.cpp.o.d -o CMakeFiles/test_another.dir/another.cpp.o -c /Users/mike/dev/neetcode/_cpp/_test/another.cpp

_test/CMakeFiles/test_another.dir/another.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_another.dir/another.cpp.i"
	cd /Users/mike/dev/neetcode/_cpp/build/_test && /usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/mike/dev/neetcode/_cpp/_test/another.cpp > CMakeFiles/test_another.dir/another.cpp.i

_test/CMakeFiles/test_another.dir/another.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_another.dir/another.cpp.s"
	cd /Users/mike/dev/neetcode/_cpp/build/_test && /usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/mike/dev/neetcode/_cpp/_test/another.cpp -o CMakeFiles/test_another.dir/another.cpp.s

# Object files for target test_another
test_another_OBJECTS = \
"CMakeFiles/test_another.dir/another.cpp.o"

# External object files for target test_another
test_another_EXTERNAL_OBJECTS =

_test/test_another: _test/CMakeFiles/test_another.dir/another.cpp.o
_test/test_another: _test/CMakeFiles/test_another.dir/build.make
_test/test_another: _test/CMakeFiles/test_another.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/mike/dev/neetcode/_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable test_another"
	cd /Users/mike/dev/neetcode/_cpp/build/_test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_another.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
_test/CMakeFiles/test_another.dir/build: _test/test_another
.PHONY : _test/CMakeFiles/test_another.dir/build

_test/CMakeFiles/test_another.dir/clean:
	cd /Users/mike/dev/neetcode/_cpp/build/_test && $(CMAKE_COMMAND) -P CMakeFiles/test_another.dir/cmake_clean.cmake
.PHONY : _test/CMakeFiles/test_another.dir/clean

_test/CMakeFiles/test_another.dir/depend:
	cd /Users/mike/dev/neetcode/_cpp/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/mike/dev/neetcode/_cpp /Users/mike/dev/neetcode/_cpp/_test /Users/mike/dev/neetcode/_cpp/build /Users/mike/dev/neetcode/_cpp/build/_test /Users/mike/dev/neetcode/_cpp/build/_test/CMakeFiles/test_another.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : _test/CMakeFiles/test_another.dir/depend

