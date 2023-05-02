
def find_basket_with_fake_coin(n: int, w: int, d: int, p: int) -> int:
    sum_weight_true_coins = (w * n * (n-1)) / 2

    difference_sum_weight_true_coins_and_sum_weight_wizard_coins = sum_weight_true_coins - p

    if difference_sum_weight_true_coins_and_sum_weight_wizard_coins > 0:
        num_fake_basket = int(difference_sum_weight_true_coins_and_sum_weight_wizard_coins / d)
        return num_fake_basket

    return n


def main():
    num_fake_basket = find_basket_with_fake_coin(4, 10, 2, 54)

    print(num_fake_basket)


if __name__ == '__main__':
    main()
