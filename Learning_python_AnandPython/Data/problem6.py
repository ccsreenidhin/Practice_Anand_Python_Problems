#Problem 6: Write a function reverse to reverse a list. Can you do this without using list slicing?

def reverse(arr):
   l=-1
   rl = []
   for i in arr :
          rl.append(arr[l])
          l-=1
   return rl



def rev(arr):
    rl = arr[::-1]
    return rl

print (rev([1,2,3,4]))

print (reverse([1,2,3,4]))
print (reverse(reverse([1,2,3,4])))
