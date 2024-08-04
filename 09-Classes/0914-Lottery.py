from random import choices


list = ["1", "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "a", "b", "c", "d", "e"]

lottery = choices(list, k=4)
print(f"If you get {lottery[0]}, {lottery[1]}, {
      lottery[2]}, and {lottery[3]}, you win!")
