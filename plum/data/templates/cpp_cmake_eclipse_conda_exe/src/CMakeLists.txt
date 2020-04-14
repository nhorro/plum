<<<<<<< HEAD
cmake_minimum_required(VERSION 3.6)

# Boost
find_package(Boost 1.67)

# Target
add_executable( [project_name]
	main.cpp
=======
add_executable( ${PROJECT_NAME}
    main.cpp    
>>>>>>> cpp cmake template
)

target_include_directories( ${PROJECT_NAME}
	PRIVATE
<<<<<<< HEAD
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
=======
		${Boost_INCLUDE_DIRS}		
)

target_link_libraries( ${PROJECT_NAME}
	PRIVATE 
		${SHARED_LIBS}
)

install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION bin
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
)
>>>>>>> cpp cmake template
