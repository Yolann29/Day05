reu = [["Monday", "3:30 PM", "Joe", "Samantha"], ["Tuesday", "6:30 PM", "Joe", "Dave", "Kate", "George"], ["Wednesday", "4:00 PM", "Clara", "George", "Joe", "Nathan"]]
name = input("Give a name    ")
meeting = []
for meet in reu:
    if name in meet:
        meeting.append(meet[0])
if meeting != []:
    print(meeting)
else:
    print("none")