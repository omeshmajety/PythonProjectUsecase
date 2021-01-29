import usecase2 as state_name
import json

# write the indian state names to a text file
with open('Indian_states.txt', 'w') as Indian_states_list:
    Indian_states_list.write(json.dumps(state_name.States))