import pytest

from dsa.sliding_window import character_replacement

@pytest.mark.parametrize(
	"s, k, expected",
	[
		("", 0, 0),
		("A", 0, 1),
		("AA", 0, 2),
		("AB", 0, 1),
		("AB", 1, 2),
		("AABABBA", 1, 4),
		("AAAA", 2, 4),
		("ABCDE", 1, 2),
		("BAAAB", 2, 5),
	],
)

def test_character_replacement(s, k, expected):
	assert character_replacement(s, k) == expected	
