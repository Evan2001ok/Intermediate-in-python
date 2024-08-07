# Prompt the user to enter names, assignment counts, and grades separated by commas
names = input("Enter names separated by commas: ").split(',')
assignments = input("Enter assignment counts separated by commas: ").split(',')
grades = input("Enter grades separated by commas: ").split(',')

# Convert assignment counts and grades to integers
assignments = [int(a.strip()) for a in assignments]
grades = [int(g.strip()) for g in grades]

# Remove leading and trailing spaces from names
names = [n.strip() for n in names]

# Use zip() to combine the lists
zipped_lists = zip(names, assignments, grades)

# Loop through the combined lists and print the required message for each student
for n, a, g in zipped_lists:
    # Calculate potential grade after submitting all assignments
    p_g = 2 * a + g
    # Print reminder message for each student
    print(f'Hi {n}')
    print(f'This is a reminder that you have {a} assignments left to submit before you can graduate. Your current grade is {g} and can increase to {p_g} if you submit all assignments before the due date.')
    print()
