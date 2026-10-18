# Python learning project by Edius Ahlqvistus started 2026-10-18


def main() -> None:
    backpack: list[str] = ["Goblin Spectacles"]

    while True:
        main_menu()

        choice = input("Choose an option from the menu: ").strip().lower()

        match choice:
            case "1":
                backpack_view(backpack)
            case "2":
                backpack_add(backpack)
            case "3":
                backpack_remove(backpack)
            case ("q" | "quit"):
                print("Goodbye!")
                return
            case _:
                print("Invalid option!")


def backpack_view(backpack: list[str]) -> None:
    if not backpack:
        print("A textile void waiting to be filled with shiny goblin "
              "garbage or rocks you mistook for artifacts.")
        return

    backpack_inventory = "\n".join(f"{number}. {item}" for number, item in enumerate(backpack, start=1))

    print(f"Your backpack contains:\n{backpack_inventory}")


def backpack_add(backpack: list[str]) -> None:
    while True:
        choice = input("\nWhat do you want to add to your backpack? 'b'(back): ").strip()
        if not choice:
            print("\nReally funny... Nothing has been added, just as you wanted!")
            continue
        if choice in ("b", "B"):
            break

        backpack.append(choice)
        print(f"{choice} added to your backpack!")


def backpack_remove(backpack: list[str]) -> None:
    while True:
        if not backpack:
            print("Your backpack contains dust and dirt! Returning to main menu. ")
            return

        backpack_view(backpack)
        choice = input("\nEnter the number of the item you want to remove. 'b'(back): ").strip()

        if choice in ("b", "B"):
            break

        try:
            selected_number = int(choice)
        except ValueError:
            print("Use a number from the list.")
            continue

        if 0 < selected_number <= len(backpack):
            item = backpack.pop(selected_number - 1)
            print(f"{item} removed from your backpack!")
        else:
            print("Use a number from the list.")
            continue

        if not backpack:
            print("Your backpack is now empty! Returning to main menu. ")
            break


def main_menu() -> None:
    print("\n=== The Bottomless Backpack ===")
    print()
    print("1: View backpack.")
    print("2: Add item to backpack.")
    print("3: Remove item from backpack.")
    print("q: Quit.")


if __name__ == "__main__":
    main()
