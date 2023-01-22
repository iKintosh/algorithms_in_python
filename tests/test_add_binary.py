from src.leetcode.add_binary import Solution


def test_add_binary():
    assert Solution().addBinary(a = "1010", b = "1011") == "10101"
    assert Solution().addBinary(a = "101111", b = "10") == "110001"