a = {
    "fdsajkl;": "in-out",
    "jkl;fdsa": "in-out",
    "asdf;lkj": "out-in",
    ";lkjasdf": "out-in",
    "asdfjkl;": "stairs",
    ";lkjfdsa": "reverse"
}

b = input()
if b not in a.keys():
    print("molu")
else:
    print(a[b])
