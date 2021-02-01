# lambda func allows us to choose what kind of sorting of the array that we want 
#   prevents us form being confined to just ascending or descending 
#   here it defaults to ascending order 
def merge_sort(my_list, sort_func= lambda x, y: x < y):

    # 1. Exit Statement
    #   only gets called n number of times
    if len(my_list) <= 1:
        return my_list

    middle_idx = len(my_list) // 2

    # 2. Recurse
    # left = merge_sort(my_list[0:middle_idx])
    # will return a sorted list from "left side"
    left = merge_sort(my_list[:middle_idx], sort_func)

    # right = merge_sort(my_list[middle_idx:len(my_list)-1])
    # will return a sorted list from "right side"
    right = merge_sort(my_list[middle_idx:], sort_func)

    # 3. Resolve Recursion
    sorted_list = merge(left, right, sort_func)
    return sorted_list


def merge(left, right, sort_func) -> []:

    combined = []

    left_idx = 0
    right_idx = 0

    # Run while there's uncompared values in both lists
    while left_idx < len(left) and right_idx < len(right):

        # sort based on the type the user wants
        if sort_func(left[left_idx],right[right_idx]):
            # add the left value in
            combined.append(left[left_idx])

            # increment to compare to next left element
            left_idx += 1

        else:
            combined.append(right[right_idx])
            right_idx += 1

    # If there's uncompared values in right list, add the uncompaed values into combined
    while right_idx < len(right):
        combined.append(right[right_idx])
        right_idx += 1

    # if there's uncompared values values in left list, add the uncompared values into combined
    while left_idx < len(left):
        combined.append(left[left_idx])
        left_idx += 1
    return combined
'''
arr = [6, 5, 7, 5, 8, 43, 9, 4, 8, 9, 12]
result = merge_sort(arr, lambda left, right: left > right)  # left > right descending
print(result)
result = merge_sort(arr, lambda left, right: left < right)  # left < right ascending
print(result)
#'''

# Distance it takes to get to each hotel 
def hotelTravel(hotel_distance, distance_day): 
    # Start at 0 
    hotel_distance.append(0)
    # merge the hotel_distances just in case we're given an unordered array 
    hotel_distance = merge_sort(hotel_distance)
    # where we currently are
    current_hotel_idx = 0
    # where we have visited
    visited_hotels = []
    # number of hotels on our trip
    num_hotels = len(hotel_distance)

    for check_hotel_idx, _ in enumerate(hotel_distance): 

        if check_hotel_idx + 1 == num_hotels: 
            # At last hotel/end, we've made it
            visited_hotels.append(check_hotel_idx)
            break 

        # how far are we from the next hotel 
        next_hotel_distance = hotel_distance[check_hotel_idx + 1]

        if distance_day < next_hotel_distance - hotel_distance[current_hotel_idx]:
            # distance we can travel in a day < the distance b/w our current hotel and the next possible hotel 
            current_hotel_idx = check_hotel_idx
            
            visited_hotels.append(current_hotel_idx)

    return visited_hotels


hotelDistances = [12, 3, 4, 2, 12, 2, 3, 5, 7, 8, 4, 3, 6, 8, 9, 5, 9, 6, 4, 6, 8, 13, 15, 17, 19, 20]
distPerDay = 3
print(hotelTravel(hotelDistances, distPerDay))

# [5, 13, 19, 21, 23, 24, 26]