# you are the manager at INFINITE hotel. the hotel has infinite rooms
# One day a finite number of tourists come to stay
# This includes
# A Captain
# an unknown number of families

# input: a list of room numbers for each tourist. Unordered
# input: size of each room (not the captains)
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
# 8
# 
# 2
# 1 2 1 2 3 4 4 3 5 = 25
# 1 2 3 4 5 = 15
# 1 1 2 2 3 3 4 4 5 5 = 30

def find_captain(room_list, room_size):
    room_set = set(room_list)
    captain_room = (sum(room_set) * room_size - sum(room_list))/(room_size - 1)
    return captain_room
        
    