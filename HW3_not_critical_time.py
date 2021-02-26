from time import time, sleep


def benchmark(func):
    def helper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        rez_time = time() - start
        if rez_time > 0.45:
            print(f'WARNING! Method_1 is slow. Time = {rez_time} sec')
        return res
    return helper

def DecorTimeCrit(cls):
    def helper(*args, **kwargs):
        for attr_str in dir(cls):
            if attr_str.startswith('__'):
                continue

            attr = getattr(cls, attr_str)
            if callable(attr):
                decor_attr = benchmark(attr)
                setattr(cls, attr_str, decor_attr)
        return cls(*args, **kwargs)
    return helper

@DecorTimeCrit#(critical_time=0.45)
class Test:
    def method_1(self):
        print('slow method start')
        sleep(1)
        print('slow method finish')

    def method_2(self):
        print('fast method start')
        sleep(0.1)
        print('fast method finish')


t = Test()

t.method_1()
t.method_2()


# slow method start
# slow method finish
# WARNING! method_1 slow. Time = ??? sec.
# fast method start
# fast method finish