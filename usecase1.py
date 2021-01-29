import Meeting.MeetingDetails as Meet
# get current attendants
Meet.get_attendance()
# add attendant
Meet.add_attendant("Lasya")
print()
# get attendants
Meet.get_attendance()
#remove an attendant
Meet.remove_attendant("Lasya")
print()
Meet.get_attendance()