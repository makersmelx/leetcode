def mincostToHireWorkers(self, quality: list, wage: list, K: int) -> float:
    import heapq
    result = float('inf')
    total_quality = 0
    selected_quality = []

    info = [(_wage / _quality, _quality, _wage) for _quality, _wage in zip(quality, wage)]

    for _unit, _quality, _wage in sorted(info):
        total_quality += _quality
        heapq.heappush(selected_quality, -1 * _quality)

        if len(selected_quality) == K:
            result = min(result, _unit * total_quality)
            total_quality += heapq.heappop(selected_quality)

    return result
