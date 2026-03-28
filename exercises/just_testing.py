def odd_and_even(list1: list[int]) -> list[int]:
    result: list[int] = []
    for x in range(0, len(list1), 2):
        if list1[x] % 2 != 0:
            result.append(list1[x])
    return result


def short_words(list1: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    list2: list[str] = []
    for x in list1:
        if len(x) < 5:
            list2.append(x)
        else:
            print(f"{x} is too long!")
    return list2


def multiples(vals: list[int]) -> list[bool]:
    mults: list[bool] = []
    mults.append(vals[0] % vals[len(vals) - 1] == 0)
    idx: int = 1
    while idx < len(vals):
        mults.append(vals[idx] % vals[idx - 1] == 0)
        idx += 1
    return mults


def value_exists(d: dict[str, int], num: int) -> bool:
    for key in d:
        if d[key] == num:
            return True
    return False


def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
    for key in inp:
        if inp[key] % 2 == 0:
            inp[key] = inp[key] + n
        else:
            inp[key] = inp[key] - n


def free_biscuits(input: dict[str, list[int]]) -> dict[str, bool]:
    """Check each game to see if we get free biscuits."""
    result: dict[str, bool] = {}
    for key in input:
        list_to_sum: list[int] = input[key]
        sum: int = 0
        for element in list_to_sum:
            sum += element
            if sum >= 100:
                result[key] = True
            else:
                result[key] = False
    return result

free_biscuits({“UNCvsDuke”:[38, 20, 42],“UNCvsState”:[9, 51, 16, 23]})

my_list: list[int] = list()
my_list.append(8)
my_list.append(0)
my_list.append(3)
my_list.append(-1)
my_list[0] = 0
print(my_list)

summed_list: list[int] = [sum(my_list)]
print(summed_list)