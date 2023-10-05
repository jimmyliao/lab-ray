import ray
ray.init(address='auto')
@ray.remote
def f():
    return 1
f.remote()

