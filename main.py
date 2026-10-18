# Python learning project by Edius Ahlqvistus started 2026-10-18


def main() -> None:
    backpack: list[str] = ["Pigeon Feather", "Goblin Spectacles", "Wooden Truncheon"]

    while True:
        main_menu()

        choice = input("Choose an option from the menu: ").strip().lower()

        match choice:
            case "1":
                backpack_view(backpack)
            case "2":
                backpack_add()
            case "3":
                backpack_remove()
            case "q":
                print("Goodbye!")
                return
            case _:
                print("Invalid option!")


def backpack_view(backpack: list[str]) -> None:
    if not backpack:
        print("A textile void waiting to be filled with shiny goblin "
              "garbage or rocks you mistook for artifacts.")
        return

    backpack_inventory = "\n".join(f" * {item}" for item in backpack)

    print(f"Your backpack contains:\n{backpack_inventory}")


def backpack_add() -> None:
    print("Nothing to add at the moment. Work in progress.")


def backpack_remove() -> None:
    print("Nothing to remove at the moment. Work in progress.")


def main_menu() -> None:
    print("\n=== The Bottomless Backpack ===")
    print()
    print("1: View backpack.")
    print("2: Add item to backpack.")
    print("3: Remove item from backpack.")
    print("q: Quit.")


if __name__ == "__main__":
    main()
