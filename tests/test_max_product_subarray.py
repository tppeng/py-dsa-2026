import pytest

from dsa.dp_like import max_product_subarray


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, -2, 4], 6),          # [2,3]
        ([-2, 0, -1], 0),            # [0]
        ([-2], -2),
        ([0], 0),
        ([1, 2, 3, 4], 24),
        ([-1, -2, -9, -6], 108),     # whole array
        ([2, -5, -2, -4, 3], 24),    # [-2,-4,3]
        ([0, 2], 2),
        ([-2, 3, -4], 24),           # [3,-4,-2]? actually [ -2,3,-4 ] = 24
    ],
)
def test_max_product_subarray(nums, expected):
    assert max_product_subarray(nums) == expected