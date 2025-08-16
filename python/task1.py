'''
You have two friends’ favorite fruit lists:

alice = ["apple", "banana", "cherry", "apple", "mango"]
bob   = ["banana", "kiwi", "mango", "banana", "apple"]


Tasks:

Find the unique fruits Alice likes (no duplicates, keep order).

Find the fruits both Alice and Bob like.

Find the fruits that are in Alice’s list but not in Bob’s.
'''
alice = ["apple", "banana", "cherry", "apple", "mango"]
bob   = ["banana", "kiwi", "mango", "banana", "apple"]
print(f"the unique fruits Alice likes {dict.fromkeys(alice)}")
print(f"the fruits both Alice and Bob like {set(alice) & set(bob)}")
print(f"the fruits that are in Alice’s list but not in Bob’s {set(alice)-set(bob)}")
