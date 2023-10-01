number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
total_hours = number_of_pages / pages_per_hour
hours_needed = int(total_hours / number_of_days)

print(hours_needed)
