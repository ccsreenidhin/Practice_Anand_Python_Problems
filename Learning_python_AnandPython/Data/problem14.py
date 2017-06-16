#Problem 14: Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.


def uniq(arr, key):
    ul = [key(arr[0])]
    for i in arr:
       if key(i) not in ul:
            ul.append(i)
        
    return ul



print uniq(['python','java','Python','Java'], key=lambda s: s.lower())
