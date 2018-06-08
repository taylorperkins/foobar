from heapq import heappush, heappop


def answer(l):
    """What a job for heapq :)"""
    h = list()

    for version in l:
        split_version = [int(val) for val in version.split(".")]
        split_version_len = len(split_version)

        if split_version_len != 3:
            while split_version_len != 3:
                split_version.append(None)
                split_version_len += 1

        heappush(h, split_version)

    sorted_l = []
    for i in range(len(l)):
        heap = [str(val) for val in heappop(h) if val is not None]
        sorted_l.append('.'.join(heap))

    return sorted_l
