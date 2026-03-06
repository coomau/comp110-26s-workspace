"A program that asks for the number of tea‑party guests and calculates the required tea bags, treats, and total cost."

__author__: str = "730736150"


def main_planner(guests: int) -> None:
    "given the number of tea‑party guests, calculates the required tea bags, treats, and total cost."
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost:",
        "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        ),
    )


def tea_bags(people: int) -> int:
    "Get the correct amount of tea bags for the amount of attendees, 2 per person"
    return 2 * people


def treats(people: int) -> int:
    "Get the correct amount of treats for the amount of tea, 1.5 per tea bag"
    return 1.5 * tea_bags(people=people)


def cost(tea_count: int, treat_count: int) -> float:
    "assume each tea bag costs $0.50 and each treat costs $0.75. collect the total cost of the tea party"
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
