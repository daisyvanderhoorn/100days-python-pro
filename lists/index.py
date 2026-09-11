import random

friends = ["David", "Victor", "Casper"]
print(friends)                       # standard way to display a full list

new_friend = "Omair"

# --- INDEXING ---
print(f"First entry [0]: {friends[0]}")
print(f"Last entry [-1]: {friends[-1]}")

friends.append(new_friend)
random_friend = random.choice(friends)
print(f"Random friend selected: {random_friend}")

random_friend_index = friends.index(random_friend)   # find an item's index
print(f"Random friend's index: {random_friend_index}")

# --- SLICING: LIST[START:END:STEP] ---
another_friend = "Marieke"
friends.insert(random_friend_index, another_friend)  # shifts items right
print(friends)

random_index = friends.index(random.choice(friends))
print(f"Deleting friend at index: {random_index}")
friends.pop(random_index)                             # remove by index
print(friends)

LIST_LENGTH = len(friends)
print(f"Length of list: {LIST_LENGTH}")
print(f"Full list: {friends[:LIST_LENGTH]}")          # same as friends[:] or print(friends)
print(f"Reverse list: {friends[::-1]}")

random_friend = random.choice(friends)
friends.remove(random_friend)                          # remove by value
print(friends)

new_friendslist = ["Mark", "Lisa", "Pieter", "Chanel"] # extend the list
friends.extend(new_friendslist)
print(f"New friendslist: {friends[:]}")
