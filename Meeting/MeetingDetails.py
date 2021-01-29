# initial attendants
meeting_attendees = [
    "Omesh", "Gayathri", "Badri", "Sabari",
    "Kiran", "Rakesh", "Aashrith", "Vamsi"
]

# get the current attendants
def get_attendance():
    for employee_name in meeting_attendees:
        print(employee_name)
# add a new attendant
def add_attendant(new_joinee):
    meeting_attendees.append(new_joinee)
# remove an attendant
def remove_attendant(new_joinee):
    meeting_attendees.remove(new_joinee)





