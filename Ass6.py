# ================================
# 1. Five Greatest Numbers
# ================================
def top_five_numbers():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to quit): ")
        if user_input == "":
            break
        numbers.append(float(user_input))

    numbers.sort(reverse=True)

    print("Top 5 numbers:")
    print(numbers[:5])


# ================================
# 2. Month → Season
# ================================
def month_to_season():
    seasons = ("winter", "spring", "summer", "autumn")

    month = int(input("Enter month (1-12): "))

    if month in (12, 1, 2):
        print("Season:", seasons[0])
    elif month in (3, 4, 5):
        print("Season:", seasons[1])
    elif month in (6, 7, 8):
        print("Season:", seasons[2])
    else:
        print("Season:", seasons[3])


# ================================
# 3. Name Checker (Set)
# ================================
def name_checker():
    names = set()

    while True:
        name = input("Enter a name (or press Enter to quit): ")
        if name == "":
            break

        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)

    print("\nAll names:")
    for n in names:
        print(n)


# ================================
# 4. Word Frequency + Top 5
# ================================
def word_stats(text):
    words = text.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    top5 = dict(sorted_words[:5])
    total_words = len(words)
    top5_count = sum(top5.values())

    proportion = (top5_count / total_words) * 100

    print("Top 5:", top5)
    print("Total words:", total_words)
    print(f"Proportion: {top5_count} / {total_words} = {proportion:.2f}%")


# ================================
# 5. Remove Odd Numbers
# ================================
def remove_odds(numbers):
    return [n for n in numbers if n % 2 == 0]


# ================================
# MAIN PROGRAM
# ================================
def main():
    print("1. Top 5 Numbers")
    print("2. Month to Season")
    print("3. Name Checker")
    print("4. Word Statistics")
    print("5. Remove Odd Numbers")

    choice = input("Choose a task (1-5): ")

    if choice == "1":
        top_five_numbers()

    elif choice == "2":
        month_to_season()

    elif choice == "3":
        name_checker()

    elif choice == "4":
        text = input("Enter text: ")
        word_stats(text)

    elif choice == "5":
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        filtered = remove_odds(nums)
        print("Original list:", nums)
        print("Even numbers only:", filtered)

    else:
        print("Invalid choice")


# Run program
main()
