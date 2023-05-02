
def get_new_older_byte(value: int) -> int:
    return (value & 0xff) << 8


def get_new_junior_byte(value: int) -> int:
    return (value >> 8) & 0xff


def reverse_change_and_older_byte_in_number(value: int):
    older_byte = get_new_older_byte(value)
    junior_byte = get_new_junior_byte(value)

    return older_byte | junior_byte


def main():
    new_num = reverse_change_and_older_byte_in_number(4660)
    print(new_num)


if __name__ == '__main__':
    main()
