talent= float(input("Enter the talents: "))
pound= float(input("Enter the pounds: "))
lot= float(input("Enter the lots: "))
total_lots = talent * 20 * 32 + pound * 32 + lot * 1
total_grams = total_lots * 13.3
kilograms = total_grams // 1000
gram_left = total_grams % 1000
print(f"The weight in modern units {int(kilograms)} kilograms and {gram_left:.2f} grams.")