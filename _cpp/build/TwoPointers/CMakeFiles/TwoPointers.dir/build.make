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
include TwoPointers/CMakeFiles/TwoPointers.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include TwoPointers/CMakeFiles/TwoPointers.dir/compiler_depend.make

# Include the progress variables for this target.
include TwoPointers/CMakeFiles/TwoPointers.dir/progress.make

# Include the compile flags for this target's objects.
include TwoPointers/CMakeFiles/TwoPointers.dir/flags.make

TwoPointers/CMakeFiles/TwoPointers.dir/TwoPointers.cpp.o: TwoPointers/CMakeFiles/TwoPointers.dir/flags.make
TwoPointers/CMakeFiles/TwoPointers.dir/TwoPointers.cpp.o: /Users/mike/dev/neetcode/_cpp/TwoPointers/TwoPointers.cpp
TwoPointers/CMakeFiles/TwoPointers.dir/TwoPointers.cpp.o: TwoPointers/CMakeFiles/TwoPointers.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/mike/dev/neetcode/_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object TwoPointers/CMakeFiles/TwoPointers.dir/TwoPointers.cpp.o"
	cd /Users/mike/dev/neetcode/_cpp/build/TwoPointers && /usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT TwoPointers/CMakeFiles/TwoPointers.dir/TwoPointers.cpp.o -MF CMakeFiles/TwoPointers.dir/TwoPointers.cpp.o.d -o CMakeFiles/TwoPointers.dir/TwoPointers.cpp.o -c /Users/mike/dev/neetcode/_cpp/TwoPointers/TwoPointers.cpp

TwoPointers/CMakeFiles/TwoPointers.dir/TwoPointers.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/TwoPointers.dir/TwoPointers.cpp.i"
	cd /Users/mike/dev/neetcode/_cpp/build/TwoPointers && /usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/mike/dev/neetcode/_cpp/TwoPointers/TwoPointers.cpp > CMakeFiles/TwoPointers.dir/TwoPointers.cpp.i

TwoPointers/CMakeFiles/TwoPointers.dir/TwoPointers.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/TwoPointers.dir/TwoPointers.cpp.s"
	cd /Users/mike/dev/neetcode/_cpp/build/TwoPointers && /usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/mike/dev/neetcode/_cpp/TwoPointers/TwoPointers.cpp -o CMakeFiles/TwoPointers.dir/TwoPointers.cpp.s

# Object files for target TwoPointers
TwoPointers_OBJECTS = \
"CMakeFiles/TwoPointers.dir/TwoPointers.cpp.o"

# External object files for target TwoPointers
TwoPointers_EXTERNAL_OBJECTS =

TwoPointers/TwoPointers: TwoPointers/CMakeFiles/TwoPointers.dir/TwoPointers.cpp.o
TwoPointers/TwoPointers: TwoPointers/CMakeFiles/TwoPointers.dir/build.make
TwoPointers/TwoPointers: TwoPointers/CMakeFiles/TwoPointers.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/mike/dev/neetcode/_cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable TwoPointers"
	cd /Users/mike/dev/neetcode/_cpp/build/TwoPointers && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/TwoPointers.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
TwoPointers/CMakeFiles/TwoPointers.dir/build: TwoPointers/TwoPointers
.PHONY : TwoPointers/CMakeFiles/TwoPointers.dir/build

TwoPointers/CMakeFiles/TwoPointers.dir/clean:
	cd /Users/mike/dev/neetcode/_cpp/build/TwoPointers && $(CMAKE_COMMAND) -P CMakeFiles/TwoPointers.dir/cmake_clean.cmake
.PHONY : TwoPointers/CMakeFiles/TwoPointers.dir/clean

TwoPointers/CMakeFiles/TwoPointers.dir/depend:
	cd /Users/mike/dev/neetcode/_cpp/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/mike/dev/neetcode/_cpp /Users/mike/dev/neetcode/_cpp/TwoPointers /Users/mike/dev/neetcode/_cpp/build /Users/mike/dev/neetcode/_cpp/build/TwoPointers /Users/mike/dev/neetcode/_cpp/build/TwoPointers/CMakeFiles/TwoPointers.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : TwoPointers/CMakeFiles/TwoPointers.dir/depend

