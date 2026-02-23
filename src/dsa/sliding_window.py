def length_of_longest_substring(s: str) -> int:
	"""
	Sliding window.

	Invariant:
		The substring s[left:right+1] contains no duplicate characters.

	Strategy:
		Track the most recent index of each character.
		When a repeated character is seen inside the current window,
		jump left to one past the previous occurrence.

	Time:	O(n)
	Space:  O(min(n,alphabet))
	"""

	last_seen: dict[str, int] = {}
	left = 0
	best = 0

	for right, ch in enumerate(s):
		if ch in last_seen and last_seen[ch] >= left:
			left = last_seen[ch] + 1

		last_seen[ch] = right
		window_len = right - left + 1
		if window_len > best:
			best = window_len

	return best

def character_replacement(s: str, k: int) -> int:
	"""
	Sliding window.

	Invariant:
		(window_length - max_frequency) <= k

	Time: O(n)
	Space: O(1) (bounded alphabet assumption)
	"""
	from collections import defaultdict

	count = defaultdict(int)
	left = 0
	max_freq = 0
	best = 0

	for right, ch in enumerate(s):
		count[ch] += 1
		max_freq = max(max_freq, count[ch])

		while (right - left + 1) - max_freq > k:
			count[s[left]] -= 1
			left += 1
		best = max(best,right - left + 1)
	return best

def min_subarray_len(target: int, nums: list[int]) -> int:
	"""
	Sliding window over positive integers.

	Invariant:
		window_sum == sum(num[left:right+1])

	Strategy:
		Expand right to increase sum.
		When sum >= target, shrink left as much as possible while maintaining sum >= target
		updating the best (minimum) length.

	Time: O(n)
	Space: O(1)
	"""
	
	left = 0
	window_sum = 0
	best = float("inf")

	for right, x in enumerate(nums):
		window_sum += x
		
		while window_sum >= target:
			best = min(best, right - left + 1)
			window_sum -= nums[left]
			left += 1

	return 0 if best == float("inf") else int(best)

def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
	"""
	Count subarrays with product < k.

	Requires nums to be positive integers.
	Invariant:
		product == product(nums[left:right + 1])
		and product < k aftre shrinking.
	Strategy:
		For each right, once the window is valid, the number of valid subarrays ending at right is (right - left + 1).
	Time: O(n)
	Space: O(1)
	"""

	if k <= 1:
		return 0
	left = 0
	product = 1
	total = 0

	for right, x in enumerate(nums):
		product *= x

		while product >= k and left <= right:
			product //= nums[left]	# safe: integers; but see note below
			left += 1
		
		total += right - left + 1
	return total