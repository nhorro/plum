cmake_minimum_required(VERSION 3.6)

# Boost
find_package(Boost 1.67)

# Target
add_executable( [project_name]
	main.cpp
)

target_include_directories( [project_name]
	PRIVATE
		${Boost_INCLUDE_DIRS}
)

target_link_libraries( [project_name]
	PRIVATE    	
		dl
		#Boost::program_options
		#Boost::system
		#Boost::regex
		#Boost::thread
		#Boost::system			
		rt
)

install( TARGETS [project_name]
  	 RUNTIME DESTINATION bin )
