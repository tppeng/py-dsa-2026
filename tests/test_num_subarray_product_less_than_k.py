import pytest

from dsa.sliding_window import num_subarray_product_less_than_k

@pytest.mark.parametrize(
	"nums, k, expected",
	[
		([10, 5, 2, 6], 100, 8),
		([1, 2, 3], 0, 0),
		([1, 2, 3], 1, 0),
		([1, 1, 1], 2, 6),	# all subarrays valid: 3+2+1 = 6
		([2, 5, 3, 10], 30, 6),
		([100], 50, 0),
		([3], 10, 1),
	],
)

def test_num_subarray_product_less_than_k(nums, k, expected):
	assert num_subarray_product_less_than_k(nums, k) == expected
