LOG_TXT = 'log.txt'


def save_to_log(operation: str) -> None:
    with open(LOG_TXT, "a") as f:
        f.write(operation + '\n')


def read_lines(num_of_lines: int):
    count = 0
    with open(LOG_TXT, 'r') as f:
        for line in reversed(list(f)):
            if count == num_of_lines:
                break
            count += 1
            print('Line {}: {}'.format(count, line.strip()))
