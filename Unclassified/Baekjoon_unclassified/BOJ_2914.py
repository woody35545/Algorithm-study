import sys

total_number_of_record, average_number_of_copyright = map(int, sys.stdin.readline().rstrip().split(" "))

number_of_copyright = 0


def get_least_number_of_copyright():
    global total_number_of_record, average_number_of_copyright, number_of_copyright

    number_of_copyright = (average_number_of_copyright - 1) * total_number_of_record + 1

    return number_of_copyright


print(get_least_number_of_copyright())
