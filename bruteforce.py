SHARES = [
    {'name': 'Action-1', 'price': 20, 'benefits': 5},
    {'name': 'Action-2', 'price': 30, 'benefits': 10},
    {'name': 'Action-3', 'price': 50, 'benefits': 15},
    {'name': 'Action-4', 'price': 70, 'benefits': 20},
    {'name': 'Action-5', 'price': 60, 'benefits': 17},
    {'name': 'Action-6', 'price': 80, 'benefits': 25},
    {'name': 'Action-7', 'price': 22, 'benefits': 7},
    {'name': 'Action-8', 'price': 26, 'benefits': 11},
    {'name': 'Action-9', 'price': 48, 'benefits': 13},
    {'name': 'Action-10', 'price': 34, 'benefits': 27},
    {'name': 'Action-11', 'price': 42, 'benefits': 17},
    {'name': 'Action-12', 'price': 110, 'benefits': 9},
    {'name': 'Action-13', 'price': 38, 'benefits': 23},
    {'name': 'Action-14', 'price': 14, 'benefits': 1},
    {'name': 'Action-15', 'price': 18, 'benefits': 3},
    {'name': 'Action-16', 'price': 8, 'benefits': 8},
    {'name': 'Action-17', 'price': 4, 'benefits': 12},
    {'name': 'Action-18', 'price': 10, 'benefits': 14},
    {'name': 'Action-19', 'price': 24, 'benefits': 21},
    {'name': 'Action-20', 'price': 114, 'benefits': 18},
]
CUSTOMER_BUDGET = 500

combinations_list = []


def benefits_calc(price, percent):
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
    And find the one with most benefits.
    """
    binary_tree_investment(0, CUSTOMER_BUDGET, [])


if __name__ == '__main__':
    bruteforce()
