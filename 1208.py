def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    _ret = 0
    _len = -float('inf')
    start = 0
    end = 0

    for i in range(len(s)):
        if abs(ord(s[i]) - ord(t[i])) <= maxCost:
            start = end = i
            break

    while end < len(s):
        _ret += abs(ord(s[end]) - ord(t[end]))
        while _ret > maxCost:
            _ret -= abs(ord(s[start]) - ord(t[start]))
            start += 1

        _len = max(_len, end-start+1)

        end += 1

    return _len


if __name__ == "__main__":
    s = "abcd"
    t = "bcde"
    maxCost = 3
    print(equalSubstring(None, s, t, maxCost))
