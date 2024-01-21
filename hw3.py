import timeit
from  typing import Callable

from bm import boyer_moore_search
from kmp import kmp_search
from rk import rabin_karp_search


def read_file(filename):
    with open(filename, 'r', encoding='cp1251') as f:
        return f.read()


def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)

def print_results(results):
    title = f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Час виконання, сек'}"

    print(title)
    print("-" * len(title))
    for result in results:
        print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")   


if __name__ == '__main__':
    text_1 = read_file('article_1.txt')
    text_2 = read_file('article_2.txt')
    # рядки унікальні для статті 
    pattern_article_1 = "його позиція у структурі даних"
    pattern_article_2 = "програмна імітаційна модель"

    results_article_1 = []
    results_article_2 = []
    for pattern in (pattern_article_1, pattern_article_2):
        time = benchmark(boyer_moore_search, text_1, pattern)
        results_article_1.append((boyer_moore_search.__name__, pattern, time))
        time = benchmark(kmp_search, text_1, pattern)
        results_article_1.append((kmp_search.__name__, pattern, time))
        time = benchmark(rabin_karp_search, text_1, pattern)
        results_article_1.append((rabin_karp_search.__name__, pattern, time))

    for pattern in (pattern_article_2, pattern_article_1):
        time = benchmark(boyer_moore_search, text_2, pattern)
        results_article_1.append((boyer_moore_search.__name__, pattern, time))
        time = benchmark(kmp_search, text_2, pattern)
        results_article_1.append((kmp_search.__name__, pattern, time))
        time = benchmark(rabin_karp_search, text_2, pattern)
        results_article_1.append((rabin_karp_search.__name__, pattern, time))

    print('Стаття 1')
    print_results(results_article_1)
    print('Стаття 2')
    print_results(results_article_2)
