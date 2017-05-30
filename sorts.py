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
Key To Remember - Left of array is sorted and INSERTing to that array.
Psudo Code With Animation:
https://www.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/insertion-sort-pseudocode

Complexity :
http://www.geeksforgeeks.org/time-complexity-insertion-sort-inversions/

If we take a closer look at the insertion sort code, we can notice that every iteration of while loop
reduces one inversion.
The while loop executes only if i > j and arr[i] < arr[j]. Therefore total number of while loop iterations (For all values of i) is same as number of inversions.
Therefore overall time complexity of the insertion sort is O(n + f(n)) where f(n) is inversion count.
If the inversion count is O(n), then the time complexityof insertion sort is O(n).
In worst case, there can be n*(n-1)/2 inversions. The worst case occurs when the array is sorted in reverse order.
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
Key To Remember : Bubble up values as air bubbles in water.
Pseudocode:
procedure bubbleSort( list : array of items )

   loop = list.count;

   for i = 0 to loop-1 do:
      swapped = false

      for j = 0 to loop-1 do:

         /* compare the adjacent elements */
         if list[j] > list[j+1] then
            /* swap them */
            swap( list[j], list[j+1] )
            swapped = true
         end if

      end for

      /*if no number was swapped that means
      array is sorted now, break the loop.*/

      if(not swapped) then
         break
      end if

   end for

end procedure return list

More at - https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm
"""
#Python Code
k=[2,3,5,90,3,1,0,456,23,24,5,1,13]

for i in range(len(k)):
    print i
    for j in range(len(k)-1,i,-1):
        if k[j-1]>k[j]:
            k[j-1],k[j]=k[j],k[j-1]
        print "--",j
print k




"""
3.------------------------------Selectin Sort-------------------------
Key To Remember:SELECT and insert to right position

The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to do this,
a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location.
"""

#Python Code

k=[2,3,5,90,3,1,0,456,23,24,5,1,13]

for j in range(1,len(k)-1,1):
    max_index=0
    max=k[0]
    for i in range(len(k)-j):
       if k[i]>max:
           max_index =i
           max=k[i]
    k[len(k)-j],k[max_index]=k[max_index],k[len(k)-j]
print k



"""
4.------------------------------Merge Sort-------------------------
Key To Remember : Sorting happens while MERGING.

"""

def merge(left,right):
    print "merging ,left->{0} right->{1}".format(left,right)
    i=0
    j=0
    out =[]
    while i<len(left) or j < len(right):

       if left[i]<right[j]:
           out.append(left[i])
           i=i+1
       else :
           out.append(right[j])
           j=j+1

       if j>=len(right):
            out.extend(left[i:])
            break
       if i >= len(left):
           out.extend(right[j:])
           break
    return out


def merge_sort(list):
    print "\n\nlist->",list

    if len(list) > 1:
        mid = len(list)/2
        left = list[:mid]
        right=list[mid:]

        print "left->", left
        print "right->", right

        outl=merge_sort(left)
        outr=merge_sort(right)

        return merge(outl,outr)
    else:
        return list

d=[23,1,2,45,3,9,34,0,21]

f=merge_sort(d)
print  f


"""
5.------------------------------Quick Sort-------------------------
Key To Remember :

"""

def partition(ls,l,h):
    pivot=l
    for i in range (l+1,h+1):
        if ls[i] <= ls[l] :
           pivot=pivot+1
           ls[i],ls[pivot]=ls[pivot],ls[i]
    ls[pivot],ls[l]=ls[l],ls[pivot]
    return pivot


def qsort(lsit,l,h):
    print l,h
    if l<h:
        print "called",l,h
        p=partition(lsit,l,h)
        qsort(lsit,l,p-1)
        qsort(lsit,p+1,h)
    else :
        return


a=[4,1,2,5,0,43,21,12,42,3]

qsort(a,0,len(a)-1)
print a
