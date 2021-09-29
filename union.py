import itertools


def main():
    filenames = input()
    files = filenames.split(" ")
    dfa1 =

def union(dfa1, dfa2):
    product = itertools.product(dfa1.states, dfa2.states)
    for v in product:
        print(v[0] + v[1])

if __name__ == "__main__":
    main()