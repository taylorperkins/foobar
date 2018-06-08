def print_time(f):
    import time

    def inner(*args, **kwargs):
        start = time.time()
        val = f(*args, **kwargs)
        print("{}\n--- {} seconds ---\n".format(
            f.__name__,
            time.time() - start
        ))

        return val
    return inner
