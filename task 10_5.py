from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        all_data = file.readlines()


filenames = [f'file {number}.txt' for number in range(1, 5)]

start_1 = datetime.now()
for file in filenames:
    read_info(file)
end_1 = datetime.now()

print(end_1 - start_1)


if __name__ == '__main__':
    start_2 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_2 = datetime.now()
    print(end_2 - start_2)
