cmake_minimum_required(VERSION 3.6)
project([project_name] CXX)

set(CMAKE_VERBOSE_MAKEFILE ON)

option(TEST_BUILD "Enable tests" OFF)

find_package(Boost 1.67 REQUIRED COMPONENTS thread date_time program_options filesystem regex)
find_package(PkgConfig REQUIRED)

include_directories( ${CMAKE_CURRENT_SOURCE_DIR}/src )

set(SHARED_LIBS
		Boost::thread
		Boost::date_time
		Boost::program_options	
		Boost::filesystem
		Boost::regex
	    Boost::disable_autolinking
	    # Put additional libraries here
	    rt
)

add_subdirectory(src)
