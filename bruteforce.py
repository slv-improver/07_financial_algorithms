import time


start = time.process_time()

SHARES = [
    {'name': 'Action-1', 'price': 20, 'profits': 5},
    {'name': 'Action-2', 'price': 30, 'profits': 10},
    {'name': 'Action-3', 'price': 50, 'profits': 15},
    {'name': 'Action-4', 'price': 70, 'profits': 20},
    {'name': 'Action-5', 'price': 60, 'profits': 17},
    {'name': 'Action-6', 'price': 80, 'profits': 25},
    {'name': 'Action-7', 'price': 22, 'profits': 7},
    {'name': 'Action-8', 'price': 26, 'profits': 11},
    {'name': 'Action-9', 'price': 48, 'profits': 13},
    {'name': 'Action-10', 'price': 34, 'profits': 27},
    {'name': 'Action-11', 'price': 42, 'profits': 17},
    {'name': 'Action-12', 'price': 110, 'profits': 9},
    {'name': 'Action-13', 'price': 38, 'profits': 23},
    {'name': 'Action-14', 'price': 14, 'profits': 1},
    {'name': 'Action-15', 'price': 18, 'profits': 3},
    {'name': 'Action-16', 'price': 8, 'profits': 8},
    {'name': 'Action-17', 'price': 4, 'profits': 12},
    {'name': 'Action-18', 'price': 10, 'profits': 14},
    {'name': 'Action-19', 'price': 24, 'profits': 21},
    {'name': 'Action-20', 'price': 114, 'profits': 18},
]
CUSTOMER_BUDGET = 500

combinations_list = []


def profits_calc(price, percent):
    return price*percent/100


def binary_tree_investment(index: int, remaining_budget: int, combination: list):
    """ Recursive function.
    Create all combinations and insert them in combinations_list
        Parameters:
            :param index: iterator
            :param remaining_budget: budget to invest in the next share
            :param combination: the list created by the binary tree
    """
    if index < len(SHARES):
        share = SHARES[index]
        combination_a = combination_b = combination[:]
        binary_tree_investment(index + 1, remaining_budget, combination_a)
        if remaining_budget >= share['price']:
            combination_b.append(share)
            remaining_budget -= share['price']
            binary_tree_investment(index+1, remaining_budget, combination_b)
    else:
        combinations_list.append(combination)


def bruteforce():
    """ Try all investment combinations.
    And find the one with most profits.
    """
    binary_tree_investment(0, CUSTOMER_BUDGET, [])
    print(len(combinations_list), 'combinations in:')
    print(time.process_time() - start, 's')
    best_combination = {'index': 0, 'winnings': 0}
    for i, combination in enumerate(combinations_list):
        invest_combination = {'index': i, 'cost': 0, 'winnings': 0}
        for share in combination:
            invest_combination['winnings'] += profits_calc(
                share['price'],
                share['profits'],
            )
            invest_combination['cost'] += share['price']
        if invest_combination['winnings'] > best_combination['winnings']:
            best_combination = invest_combination
    for share in combinations_list[best_combination['index']]:
        print(
            f"{share['name']:<10}",
            f"{share['price']:<5}",
            f"{share['profits']:<5}",
        )
    print(
        'Result:',
        best_combination['cost'],
        round(best_combination['winnings'], 2),
        sep='\n- '
    )
    print(time.process_time() - start, 's')


if __name__ == '__main__':
    bruteforce()
