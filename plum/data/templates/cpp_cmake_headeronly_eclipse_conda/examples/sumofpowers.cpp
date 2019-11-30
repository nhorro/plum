#include <vector>
#include <iostream>
#include <[project_name]/[project_name].hpp>

int main(int argc, const char* argv[])
{
	std::vector<int> v = { 1,2,3,4,5,6,7,8 };
	int r = [project_name]::vector_sum_pow<int>(v);
	std::cout << r << std::endl;
	return 0;
}
