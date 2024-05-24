import timeit

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    result = {}
    while amount > 0:
        for coin in coins:
            if dp[amount] == dp[amount - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                amount -= coin
                break
    return result

# Оцінка часу виконання для обох функцій за допомогою timeit
def evaluate_performance(amount, num_runs=1000):
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=num_runs)
    dp_time = timeit.timeit(lambda: find_min_coins(amount), number=num_runs)
    return greedy_time / num_runs, dp_time / num_runs

# Приклад використання
amount = 113
print("Жадібний алгоритм результат:", find_coins_greedy(amount))
print("Динамічний алгоритм результат:", find_min_coins(amount))

# Оцінка продуктивності
greedy_time, dp_time = evaluate_performance(10000)
print(f"Жадібний алгоритм час: {greedy_time:.10f} секунд")
print(f"Динамічний алгоритм час: {dp_time:.10f} секунд")