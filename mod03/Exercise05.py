talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

talentsTOgrams = talents * 20 * 32 * 13.3
poundsTOgrams = pounds * 32 * 13.3
lotTOgrams = lots * 13.3

total_grams = talentsTOgrams + poundsTOgrams + lotTOgrams

kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000

print(f"The weight in modern units:\n{kilograms} kilograms and {remaining_grams:.2f} grams.")
