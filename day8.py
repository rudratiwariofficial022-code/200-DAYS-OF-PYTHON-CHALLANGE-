def solve():
    height = int(input())
    age = int(input())

    # Check disqualification conditions
    if height < 120 or age < 5:
        print("Not Allowed")
        return

    # Check if either condition requires an adult
    if (120 <= height <= 140) or (5 <= age <= 12):
        print("Must ride with Adult")
        print(200)
    else:
        print("Can ride alone")
        print(300)

if __name__ == "__main__":
    solve()