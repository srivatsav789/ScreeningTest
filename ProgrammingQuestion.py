# 7.11,8,9:00,9:15,14:30,15:00

'''
floor - 7
room_no - 11
max_people - 8
free slots - (9:00,9:15) , (14:30,15:00)
'''
#strptime('15:30','%H:%M')

'''
input ->  Given n team members with the floor on which they work and the time they want to meet
data ->  list of conference rooms identified by their floor and room number as a decimal number, maximum number of people it fits and pairs of times they are open

'''
from datetime import datetime
import collections

def parse_txt_make_ds(file_path : str):
    with open(file_path) as f :
        dictionary = {}
        all_rooms = f.read().split("\n")
        for room in all_rooms :
            floor_room = room.split(",")[0]
            room = room.replace(f"{floor_room}," , "")
            rest_stats = room.split(",")
            max_capacity = int(rest_stats[0])
            timings = rest_stats[1:]
            new_timings = []
            if len(timings) > 2 :
                for i in range(0,len(timings),2):
                    new_timings.append((datetime.strptime(timings[i],'%H:%M') , datetime.strptime(timings[i+1],'%H:%M')))
            else :
                new_timings.append(((datetime.strptime(timings[0],'%H:%M') , (datetime.strptime(timings[1],'%H:%M')))))
            dictionary[floor_room] = {"max_capacity" : max_capacity , "Timings" : new_timings}
    #dictionary = sort_dict(dictionary)
    return dictionary

def sort_dict(dictionary : dict):
    new_dict = {}
    for item , stats in dictionary.items():
        new_dict[float(item)] = stats
    od = collections.OrderedDict(sorted(new_dict.items()))
    dict_ = {}
    for item , stats in od.items():
        dict_[str(item)] = stats
    return dict_

# Test case 
# 5,8,10:30,11:30
# 5 members , 8th floor , Timing 

#test_case = input()
#test_case = "5,8,10:30,11:30"

def parse_input(test_case : str):
    all_stats = test_case.split(",")
    size = int(all_stats[0])
    floor = int(all_stats[1])
    timings = (datetime.strptime(all_stats[2],'%H:%M') , datetime.strptime(all_stats[3],'%H:%M'))
    return {"size" : size , "floor" : floor , "timings" : timings}

#input_stats = parse_input("5,8,10:30,11:30")

def produce_output(test_case : str , room_file_path : str):
    rooms_dictionary = parse_txt_make_ds(room_file_path)
    input_stats = parse_input(test_case)
    possibilities = []
    for item , stats in rooms_dictionary.items():
        if stats['max_capacity'] >= input_stats['size']:
            for time1 , time2 in stats['Timings']:
                if time1.time() <= input_stats['timings'][0].time() and time2.time() >= input_stats['timings'][1].time():
                    possibilities.append(item)
        else :
            continue
    current_best = None
    output = None
    for pos in possibilities :
        floor , room = pos.split(".")
        floor , room = int(floor) , int(room)
        if current_best is None :
            current_best = abs(floor - input_stats["floor"])
            output = str(floor) + "." + str(room)
        else :
            current = abs(floor - input_stats["floor"])
            if current < current_best :
                current_best = current
                output = str(floor) + "." + str(room)
    return output


'''
Extra Point work ! 

def extra_point(test_case : str , room_file_path : str):
    rooms_dictionary = parse_txt_make_ds(room_file_path)
    input_stats = parse_input(test_case)
    possibilities = []
    possible_rooms = []
    for item , stats in rooms_dictionary.items():
        if stats['max_capacity'] > input_stats['size']:
            possible_rooms.append(item)
    make_poss_room_dict = {}
    for pos_room in possible_rooms :
        make_poss_room_dict[pos_room] = rooms_dictionary[pos_room]["Timings"]
    start_time = input_stats["timings"][0]
    end_time = input_stats["timings"][1]
    for floor_room , timings in make_poss_room_dict.keys():
        for time in range(0 , len(timings) , 2):
'''