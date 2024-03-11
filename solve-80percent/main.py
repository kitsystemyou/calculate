import random


def is_full(array: list[bool], k: int) -> bool:
    for i in range(k, len(array) - 1):
        if not array[i]:
            return False
    return True


def calulate_dice_result(array: list[bool], k: int) -> list[bool]:
    dice: int = random.randint(1, 100)
    # print("dice: ", dice)
    dice -= 1
    if dice > k - 1:
        # print("dice is bigger than k")
        array[dice] = True
        return array
    else:
        # print("dice is smoller than k")
        # Change a random false value to true (bigger than k)
        false_indices = [i for i, val in enumerate(array[k:]) if not val]
        if false_indices:
            random_index = random.choice(false_indices)
            array[random_index + k - 1] = True
        return array


# 1game means 200times dice roll
def try_1_game(k: int) -> bool:
    array: list[bool] = [False for _ in range(100)]
    for i in range(200):
        new_array = calulate_dice_result(array, k)
        array = new_array
        del new_array
    return is_full(array, k)


def try_100_games(k: int) -> list[bool]:
    result: list[bool] = []
    for i in range(1000):
        result.append(try_1_game(k))
    return result


if __name__ == "__main__":
    for k in range(1, 101):
        print("k = ", k)
        result_array = try_100_games(k)
        print("success rate = ", result_array.count(True) / len(result_array))
    print("-- END --")
    # for i, val in enumerate(array):
    #     print(i, val)

# TODO: 200times, calculate whether 80% or not
