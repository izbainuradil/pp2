def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


def fibonacci(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current


squares = (x * x for x in range(10))


if __name__ == "__main__":
    print(list(even_numbers(10)))
    print(list(fibonacci(10)))
    for number in Countdown(5):
        print(number)
    print(list(squares))