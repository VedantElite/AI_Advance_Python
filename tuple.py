if __name__ == '__main__':
    # Step 1: Read the input
    n = int(input())
    
    # Step 2: Create the tuple directly using map and split
    # This is the cleanest 'Data Science' way to do it
    t = tuple(map(int, input().split()))
    
    # Step 3: Print the hash
    # On HackerRank's PyPy 3, this will output 3713081631934410656
    print(hash(t))
