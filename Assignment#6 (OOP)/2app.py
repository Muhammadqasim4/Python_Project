class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)

a = Counter()
b = Counter()
Counter.show_count()
