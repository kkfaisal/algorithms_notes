""" _______  _______  _______ _________
(  ____ \(  ___  )(  ____ )\__   __/
| (    \/| (   ) || (    )|   ) (
| (_____ | |   | || (____)|   | |
(_____  )| |   | ||     __)   | |
      ) || |   | || (\ (      | |
/\____) || (___) || ) \ \__   | |
\_______)(_______)|/   \__/   )_(

"""

"""
1.--------------------Insertion Sort----------------------------
Psudo Code With Animation:
https://www.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/insertion-sort-pseudocode

Complexity :
http://www.geeksforgeeks.org/time-complexity-insertion-sort-inversions/

If we take a closer look at the insertion sort code, we can notice that every iteration of while loop
reduces one inversion.
The while loop executes only if i > j and arr[i] < arr[j]. Therefore total number of while loop iterations
(For all values of i) is same as number of inversions.
Therefore overall time complexity of the insertion sort is O(n + f(n)) where f(n) is inversion count. If the inversion count is O(n), then the time complexity
of insertion sort is O(n). In worst case, there can be n*(n-1)/2 inversions. The worst case occurs
when the array is sorted in reverse order.
So the worst case time complexity of insertion sort is O(n2).
"""
#Code in Python :
k=[2,3,5,90,3,1,0,456,23,24,5,1,13]
for i in range (1,len(k)):
    j=i
    while j>0 and k[j-1]>k[j]:
        k[j-1],k[j]=k[j],k[j-1]
        j=j-1
    #print k
print k

"""
2.--------------------Bubble Sort------------------------------



"""
