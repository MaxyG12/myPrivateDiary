from replit import db
import datetime

print("Private Diary")
print()

def add():
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def view():
  keys = db.keys()
  entryList = list(keys)
  entryList.sort(reverse=True)
  for key in entryList:
    print(f"{key}: {db[key]}")
    print()
    next = input("Next or exit? > ")
    if next.lower() == "exit":
      break

while True:
  def get_password():
    return input("Enter the password: ")

  def main():
    correct_password = "DogPound"
    attempts = 3

    while attempts > 0:
        user_password = get_password()
        if user_password == correct_password:
            print("Access granted!")
            break
        else:
            print(f"Access denied. {attempts} attempts remaining.")
            attempts -= 1

    if attempts == 0:
        print("Too many incorrect attempts. Exiting.")

  if __name__ == "__main__":
    main()
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  else: 
    print("Invalid input, try again")
  