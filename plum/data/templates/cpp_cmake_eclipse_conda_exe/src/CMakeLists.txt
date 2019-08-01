add_executable( [project_name] main.cpp)

target_include_directories( [project_name]
	PRIVATE
		${Boost_INCLUDE_DIRS}		
)