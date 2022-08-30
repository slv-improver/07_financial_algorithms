import time
import csv


start = time.process_time()


def extract_shares():
    shares = []
    with open('shares.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            print(f'\t{row["name"]}, {row["price"]}, {row["profit"]}')
            shares.append({
                'name': row['name'],
                'price': int(row['price']),
                'profit': int(row['profit'])
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
