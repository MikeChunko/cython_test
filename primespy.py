def primes(nb_primes):
    if nb_primes > 1000:
        nb_primes = 1000

    p = []
    len_p = 0
    n = 2
    while len_p < nb_primes:
        for i in p[:len_p]:
            if n % i == 0:
                break
        else:
            p.append(n)
            len_p += 1
        n += 1

    result_as_list = [prime for prime in p[:len_p]]
    return result_as_list
