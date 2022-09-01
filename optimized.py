import time
import csv


start = time.process_time()


def extract_shares():
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
              f'{time.process_time() - start} s')
    return shares


def optimized_investment():
    shares = extract_shares()
    shares.sort(key=lambda x: x['price'], reverse=True)


if __name__ == '__main__':
    optimized_investment()
    print(time.process_time() - start, 's')
