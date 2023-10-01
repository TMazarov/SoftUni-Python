architect_name = input()
number_of_projects = int(input())
# One project takes 3hrs. to complete
total_hours_for_all_projects = number_of_projects * 3

print(f'The architect {architect_name} will need {total_hours_for_all_projects}'
      f' hours to complete {number_of_projects} project/s.')
