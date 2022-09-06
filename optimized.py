import time
import csv


start = time.process_time()

BUDGET = 500


def extract_shares():
    """
    Read and extract shares from CSV file
    :return: list of dictionaries (name', 'price', 'profit')
    """
    shares = []
    with open('shares.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            name, price, profit_percent = row["name"], float(row["price"]), row["profit"]
            if price > 0:
                shares.append({
                    'name': name,
                    'price': int(price * 100),
                    'profit_amount': price * float(profit_percent) / 100
                })
            line_count += 1
        print(f'\nProcessed {line_count} lines in:\n'
              f'{round(time.process_time() - start, 4)} s', end='\n\n')
    return shares


def dynamic_algo(budget, shares_list):
    """
    Create a matrix that store best share investment
    for each unit from 0 to budget
    :param budget: max investment amount
    :param shares_list: list of shares
    """
    # Convert budget to cents to get integer price
    budget *= 100
    matrice = [[0 for x in range(budget + 1)] for x in range(len(shares_list) + 1)]

    for i in range(1, len(shares_list) + 1):
        for b in range(1, budget + 1):
            if shares_list[i-1]['price'] <= b:
                matrice[i][b] = max(
                    shares_list[i-1]['profit_amount']
                    + matrice[i-1][b-shares_list[i-1]['price']],
                    matrice[i-1][b],
                )
            else:
                matrice[i][b] = matrice[i - 1][b]

    b = budget
    n = len(shares_list)
    shares_selection = []

    while b >= 0 and n >= 0:
        share = shares_list[n - 1]
        if matrice[n][b] == matrice[n - 1][b - share['price']] + share['profit_amount']:
            shares_selection.append(share)
            b -= share['price']

        n -= 1

    print(shares_selection, (budget - b) / 100, matrice[-1][-1], sep='\n- ')


def optimized_investment():
    """
    Main function
    """
    shares = extract_shares()
    dynamic_algo(BUDGET, shares)


if __name__ == '__main__':
    optimized_investment()
    print('in:', round(time.process_time() - start, 4), 's')
