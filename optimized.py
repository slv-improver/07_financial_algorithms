import time
import csv


start = time.process_time()


def optimized_investment():
    with open('shares.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            print(f'\t{row["name"]}, {row["price"]}, {row["profit"]}')
            line_count += 1
        print(f'\nProcessed {line_count} lines in:')


if __name__ == '__main__':
    optimized_investment()
    print(time.process_time() - start, 's')
