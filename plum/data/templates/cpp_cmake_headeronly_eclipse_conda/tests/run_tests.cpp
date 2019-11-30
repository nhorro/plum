#include <[project_name]/[project_name].hpp> // TODO: replace

#include <vector>
#include <iostream>
#include <gtest/gtest.h>

struct [project_name]_test : public testing::Test
{
	void SetUp()
	{

	}

	void TearDown()
	{

	}
};

TEST_F([project_name]_test, sumofpowerstest)
{
	std::vector<int> v = { 1,2,3,4,5,6,7,8 };
	ASSERT_EQ ( 204, [project_name]::vector_sum_pow<int>(v) );
}

int main(int argc, char **argv)
{
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
