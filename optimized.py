import time
import csv


start = time.process_time()

BUDGET = 500
FILE = 'shares.csv'
# FILE = 'dataset1_Python+P7.csv'
# FILE = 'dataset2_Python+P7.csv'


def extract_shares(file):
    """
    Read and extract shares from CSV file
    :return: list of dictionaries (name', 'price', 'profit')
    """
    shares = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            name = row["name"]
            price = float(row["price"])
            profit_percent = float(row["profit"])
            if price > 0 and profit_percent > 0:
                shares.append({
                    'name': name,
                    'price': price,
                    'profit_percent': profit_percent,
                    'profit_amount': price * profit_percent / 100
                })
            line_count += 1
        print(f'\nProcessed {line_count} lines and extract {len(shares)} in:\n'
              f'{round(time.process_time() - start, 4)} s', end='\n\n')
    return shares


def dynamic_knapsack(budget, shares_list):
    """
    Create a matrix that store best share investment
    for each unit from 0 to budget
    :param budget: max investment amount
    :param shares_list: list of shares
    """
    # Convert budget to cents to get integer price
    budget *= 100
    matrix_x = budget + 1
    matrix_y = len(shares_list) + 1
    matrix = [[0 for x in range(matrix_x)] for x in range(matrix_y)]

    # Loop on all shares in list
    for i in range(1, matrix_y):
        #  Loop on all cents in the budget
        for b in range(1, matrix_x):
            previous_x = matrix[i-1]
            share = shares_list[i-1]
            # Verify if share price is lower than the tested budget
            if share['price'] <= b:
                without_share = previous_x[b]
                with_share = share['profit_amount'] + previous_x[b-share['price']]
                matrix[i][b] = max(
                    with_share,
                    without_share,
                    )
            else:
                # Store profit_amount of the previous line
                matrix[i][b] = previous_x[b]

    find_composition(budget, matrix, shares_list)


def find_composition(budget, solutions: list, shares):
    """
    Create shares_selection
    by finding which shares make up the optimized solution
    :param budget: max investment amount
    :param solutions:
    :param shares: list of shares
    """
    b = budget
    n = len(shares)
    shares_selection = []
    while b >= 0 and n >= 0:
        share = shares[n-1]
        optimized_y = b - share['price']
        previous_x = solutions[n-1]
        if solutions[n][b] == previous_x[optimized_y] + share['profit_amount']:
            shares_selection.append(share)
            b -= share['price']
        n -= 1
    print(shares_selection, (budget-b) / 100, solutions[-1][-1], sep='\n- ')


def optimized_investment():
    """
    Main function
    """
    shares = extract_shares(FILE)
    dynamic_knapsack(BUDGET, shares)


if __name__ == '__main__':
    optimized_investment()
    print('in:', round(time.process_time() - start, 4), 's')
