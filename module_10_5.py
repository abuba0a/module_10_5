import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline().strip()
            all_data.append(file)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start1 = datetime.now()
for i in filenames:
    read_info(i)
end1 = datetime.now()
print(f'{end1 - start1} (линейный)')


if __name__ == '__main__':
    start2 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end2 = datetime.now()
    print(f'{end2 - start2} (многопроцессный)')
