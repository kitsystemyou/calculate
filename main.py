import random


def roll_dice_100() -> int:
    return random.randint(1, 100)


def challange_k(k: int) -> int:
    return k


def is_full(array: list[bool], k: int) -> bool:
    for i in range(k, len(array) - 1):
        if not array[i]:
            return False
    return True


def calulate_dice_result(array: list[bool], k: int) -> list[bool]:
    dice: int = roll_dice_100()
    print("dice: ", dice)
    dice -= 1
    if dice > k - 1:
        print("dice is bigger than k")
        array[dice] = True
        return array
    else:
        print("dice is smoller than k")
        # Change a random false value to true (bigger than k)
        false_indices = [i for i, val in enumerate(array[k:]) if not val]
        if false_indices:
            random_index = random.choice(false_indices)
            array[random_index + k - 1] = True
        return array


if __name__ == "__main__":
    k = 50
    array: list[bool] = [False for _ in range(100)]
    calulate_dice_result(array, 50)
    for i in range(100):
        new_array = calulate_dice_result(array, k)
        array = new_array
        del new_array
    print("-- END --")
    # for i, val in enumerate(array):
    #     print(i, val)
    print(is_full(array, k))

# TODO: 200times, calculate whether 80% or not
