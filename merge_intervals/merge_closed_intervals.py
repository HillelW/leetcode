def sort_intervals_by_left_endpoint(intervals: list[list[int]]) -> None:
    intervals.sort(key=lambda interval: interval[0])


def merge_closed_intervals(intervals: list[list[int]]) -> list[int]:
    result = []
    sort_intervals_by_left_endpoint(intervals)

    for interval in intervals:
        if not result:
            result.append(interval)
        else:
            left_endpoint = interval[0]
            while result and result[-1][1] >= left_endpoint:
                left_endpoint = min(left_endpoint, result.pop()[0])
            result.append([left_endpoint, interval[1]])
    return result

assert merge_closed_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]