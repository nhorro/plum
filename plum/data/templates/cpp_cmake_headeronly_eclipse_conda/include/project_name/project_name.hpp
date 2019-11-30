#ifndef [project_name]_HPP
#define [project_name]_HPP

#include <vector>
#include <algorithm>
#include "detail/[project_name]_impl.hpp"

namespace [project_name] {

template <typename T>
inline T vector_sum_pow(const std::vector<T>& v)
{
	T result = 0;
	std::for_each(v.begin(), v.end(), [&result](const T& e) { result+=detail::pow_impl(e); } );
	return result;
}

}

#endif // [project_name]_HPP
