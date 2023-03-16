print('__NEW__\n')


class Singleton(object):
    _instance = None  # Keep instance reference

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class LimitedInstances(object):
    _instances = []  # Keep track of instance reference
    limit = 5

    def __new__(cls, *args, **kwargs):
        if not len(cls._instances) <= cls.limit:
            raise RuntimeError("Count not create instance. Limit %s reached" % cls.limit)
        instance = object.__new__(cls, *args, **kwargs)
        cls._instances.append(instance)
        return instance

    def __del__(self):
        # Remove instance from _instances
        self._instance.remove(self)


print('\n__INIT__\n')


class A:
    def __init__(self, a, b, c=5, *args, **kwargs):
        self.a = a
        self.b = b
        self.d = self.a + self.b + c
        self.values = args
        self.dct = kwargs


a = A(1, 2, 454, 'ddd', logger='value', socket='value')
print(a.values)
print(a.dct)

print('\n__DEL__\n')


class FileReader:
    def __init__(self, filename):
        self.f = open(filename, 'rb')

    def get_stream(self):
        return self.f

    def close_stream(self):
        self.f.close()

    def __del__(self):
        self.close_stream()
