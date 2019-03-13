import primespy
import primes
import time

start_time = time.time()
print(primes.primes(1000))
print("cython: %s seconds" % (time.time() - start_time))

start_time = time.time()
print(primespy.primes(1000))
print("python: %s seconds" % (time.time() - start_time))
