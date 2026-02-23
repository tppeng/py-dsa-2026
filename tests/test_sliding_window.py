import pytest

from dsa.sliding_window import length_of_longest_substring

@pytest.mark.parametrize(
	"s, expected",
	[
		("", 0),
		("a", 1),
		("aaaa", 1),	 	# counting repeating "a"
		("ab", 2),
		("abcabcbb", 3),	# counting repeating "abc"
		("bbbbb", 1),		# counting repeating "b"
		("aggaeg", 3), 		# counting "gae"
		("acaf", 3), 		# counting "caf"
		("rogers", 5), 		# counting "roger"
		("account", 5), 	# counting "count"
	],
)

def test_length_of_longest_substring(s, expected):
	assert length_of_longest_substring(s) == expected  
