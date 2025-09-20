"""
CRUD

Create a program that displays the following menu:

1.Display database
2.Add an item
3.Delete an item
4.Change an item 
5.Quit

The program contains a list o fitems;for example,fruits.

If you select 1,the program displays the items in the list,numbering each item
For example:

0:orange
1.banana
2.blackberry

If you select 2 the program asks you to enter a new item.It adds what you've typed to the list.

If you select 3,the program asks you enter the list number of an item to delete.It deletes the 
specified item from the list.

If you select 4, the program asks you to enter the list number of an item to change,then asks you 
to enter text.It changes the specified item to the 
specified item to the specified text.

Id you select 5 , the program quits.

Until you quit with option 5,the program displays the menu again after every action.
"""

def print_menu():
    print("\n=== MENU ===")
    print("1. Display database")
    print("2. Add an item")
    print("3. Delete an item")
    print("4. Change an item")
    print("5. Quit")

def display(database):
    if not database:
        print("Database boş.")
        return
    for i, item in enumerate(database):
        print(f"{i}:{item}")

def add_item(database):
    new_item = input("Enter a new item: ").strip()
    if not new_item:
        print("Boş öğe eklenmedi.")
        return
    database.append(new_item)
    print(f"Added -> {len(database)-1}:{new_item}")

def _prompt_int(msg):
    """Sayı girilene kadar sorar."""
    while True:
        raw = input(msg).strip()
        try:
            return int(raw)
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")

def delete_item(database):
    if not database:
        print("Silecek öğe yok (liste boş).")
        return
    display(database)
    idx = _prompt_int("Enter the list number of an item to delete (0..N-1): ")
    if 0 <= idx < len(database):
        removed = database.pop(idx)
        print(f"Deleted -> {idx}:{removed}")
    else:
        print("Geçersiz indeks.")

def change_item(database):
    if not database:
        print("Değiştirilecek öğe yok (liste boş).")
        return
    display(database)
    idx = _prompt_int("Enter the list number of an item to change (0..N-1): ")
    if not (0 <= idx < len(database)):
        print("Geçersiz indeks.")
        return
    new_text = input("Enter new text: ").strip()
    if not new_text:
        print("Boş metin kabul edilmez.")
        return
    old = database[idx]
    database[idx] = new_text
    print(f"Changed -> {idx}:{old}  =>  {idx}:{new_text}")

def main():
    
    database = ["orange", "banana", "blackberry"]

    while True:
        print_menu()
        choice = input("Enter your selection (1-5): ").strip()
        if choice == "1":
            display(database)
        elif choice == "2":
            add_item(database)
        elif choice == "3":
            delete_item(database)
        elif choice == "4":
            change_item(database)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Geçersiz seçim. 1-5 arası bir değer gir.")

    main()