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


def optimized_investment():
    """
    Main function
    """
    shares = extract_shares(FILE)

    print('\nSorted by: Profit Percent')
    greedy_knapsack(
        sorted(
            shares,
            key=lambda x: x['profit_percent'],
            reverse=True
        ),
        BUDGET,
    )
    print('\nSorted by: Profit Percent * Profit Amount')
    greedy_knapsack(
        sorted(
            shares,
            key=lambda x: x['profit_percent']*x['profit_amount'],
            reverse=True
        ),
        BUDGET,
    )


def greedy_knapsack(shares_list, budget):
    selection = []
    total_profit = 0
    for share in shares_list:
        if share['price'] <= budget:
            selection.append(share)
            budget -= share['price']
            total_profit += share['profit_amount']

    print(selection, BUDGET - budget, total_profit, sep='\n- ')


if __name__ == '__main__':
    optimized_investment()
    print('in:', round(time.process_time() - start, 4), 's')
