def sumSubseqWidths(self, A: list) -> int:
    base = 10**9+7
    A.sort(reverse=True)
    incre, prev, ret = 2, A.pop(), 0
    while A:
        num = A.pop()
        ret = (ret + (incre - 1) * num - prev) % base
        incre = (incre * 2) % base
        prev = (prev * 2 + num) % base
    return ret


if __name__ == '__main__':
    case = [2, 1, 3]
    print(sumSubseqWidths(None, case))
