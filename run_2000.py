import time


def timer(function, *args):
    """
    :param function: A function to measure it run time on the given arguments.
    :param args: An arguments for the given function.
    :return: The run time of the given function on the given arguments.
    """
    start_time = time.time()
    function(args)
    return time.time() - start_time


if __name__ == '__main__':
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
