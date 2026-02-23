def max_product_subarray(nums: list[int]) -> int:
	"""
	Maximum product subarray.

	Strategy:
		Track both the max and min product ending at current index,
		because multiplying by a negative swaps roles

	Time: O(n)
	Space: O(1)
	"""
	if not nums:
		raise ValueError("nums must be non-empty")

	max_end = nums[0]
	min_end = nums[0]
	best = nums[0]

	for x in nums[1:]:
		# If x is negative, max and min swap after multiplication.
		if x < 0:
			max_end, min_end = min_end, max_end

		max_end = max(x, max_end * x)
		min_end = min(x, min_end * x)

		if max_end > best:
			best = max_end
	return best