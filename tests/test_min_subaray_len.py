import pytest

from dsa.sliding_window import min_subarray_len

@pytest.mark.parametrize(
	"target, nums, expected",
	[
		(7, [2, 3, 1, 2, 4, 3], 2), 	# [4, 3]
		(4, [1, 4, 4], 1),		# [4]
		(11, [1, 1, 1, 1, 1], 0),	# none
		(3, [1, 1, 1], 3),		# whole array
		(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 2), #[7, 8] or [10, 7]
		(1, [1], 1),
		(100, [1, 2, 3], 0),
	],
)

def test_min_subarray_len(target, nums, expected):
	assert min_subarray_len(target, nums) == expected
