
import random
user_choice: int = random.choice([1, 2, 3, 4, 5, 6])
if user_choice < 2:
    print("User made a choice lower than 2")
elif user_choice == 2:
    print("User's choice was exactly 2")
else:
    print("User's choice was larger than 2")