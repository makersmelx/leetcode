def largestMultipleOfThree(self, digits: list) -> str:
    digits.sort()
    remain = sum(digits) % 3

    if digits[len(digits) - 1] == 0:
        return "0"

    if remain == 0:
        return ''.join([str(i) for i in digits[::-1]])

    for _index, _digit in enumerate(digits):
        if _digit % 3 == remain:
            new_digits = digits
            new_digits.pop(_index)
            return ''.join([str(i) for i in new_digits[::-1]])

    if len(digits) < 3:
        return ""

    first = []
    for _index, _digit in enumerate(digits):
        if len(first) >= 3:
            break
        if _digit % 3 != 0:
            first.append(_index)

    _sum = 0
    for _index in first:
        _sum += digits[_index]

    if len(first) == 2 and _sum % 3 == remain:
        ret = ""
        for _i, _d in enumerate(digits):
            if _i != first[0] and _i != first[1]:
                ret += str(_d)
        return ret[::-1]

    for _i, _index in first[::-1]:
        if (digits[first[(_i + 1) % 3]] + digits[first[(_i - 1) % 3]] % 3) == remain:
            ret = ""
            for __i, _d in enumerate(digits):
                if __i != first[(_i + 1) % 3] and __i != first[(_i - 1) % 3]:
                    ret += str(_d)
            return ret[::-1]
    return ""


if __name__ == '__main__':
    largestMultipleOfThree(None, [9, 8, 6, 8, 6])
