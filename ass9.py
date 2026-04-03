# Assignment 9 - Full Program

# -------------------------------
# 1. Count non-blank lines
# -------------------------------
def count_lines(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() != "":
                count += 1
    return count


# -------------------------------
# 2. Find keyword line numbers
# -------------------------------
def find_keyword_lines(filename, keyword):
    result = []
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if keyword in line:
                result.append(i)
    return result


# -------------------------------
# 3. Calculate average score
# -------------------------------
def average_score(filename):
    total = 0
    count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                name, score = line.strip().split(',')
                total += float(score)
                count += 1
    
    return total / count if count > 0 else 0


# -------------------------------
# 4. Caesar Cipher
# -------------------------------
def caesar_cipher_file(input_file, shift, direction, output_file):
    if direction.lower() == "left":
        shift = -shift

    result = ""

    with open(input_file, 'r') as file:
        text = file.read()

    for char in text:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result += new_char
        else:
            result += char

    with open(output_file, 'w') as file:
        file.write(result)


# -------------------------------
# MAIN PROGRAM (test everything)
# -------------------------------
if __name__ == "__main__":
    print("=== Assignment 9 Program ===")

    # --- Question 1 ---
    file1 = input("Enter file name for line count: ")
    print("Non-blank lines:", count_lines(file1))

    # --- Question 2 ---
    file2 = input("\nEnter file name for keyword search: ")
    keyword = input("Enter keyword: ")
    print("Keyword found on lines:", find_keyword_lines(file2, keyword))

    # --- Question 3 ---
    file3 = input("\nEnter file name for average score: ")
    print("Average score:", average_score(file3))

    # --- Question 4 ---
    input_file = input("\nEnter input file for Caesar cipher: ")
    shift = int(input("Enter shift amount: "))
    direction = input("Enter direction (left/right): ")
    output_file = input("Enter output file name: ")

    caesar_cipher_file(input_file, shift, direction, output_file)
    print("Cipher complete! Output saved to", output_file)