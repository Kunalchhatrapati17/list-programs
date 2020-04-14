if __name__=="__main__":
 arr = []
 n = int(input("enter the number of elements"))
 for i in range(0,n):
    s=int(input())
    arr.append(s)
 print (arr)
 while True:
  print("Press 1 for reverse \n Press 2 for odd position \n Press 3 for even position \n Press 4 for copy elements into another list \n Press 5 find duplicate elements \n Press 6 finding sum of all the elements in the list\n Press 7 for finding largest value in list \n Press 8 for finding smallest value in list \n Press 9 for sorting elements in ascending order \n Press 10 for sorting elements in descending order \n ")

  option=int(input("your choice"))
  def print_reverse(arr):
    print ("reverse of an list")
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i],end=" ")

  def odd_position(arr):
    print ("odd position")
    for i in range(0, len(arr), 2):
        print (arr[i],end=" ")

  def even_position(arr):
    print ("even position")
    for i in range(1, len(arr), 2):
        print (arr[i],end=" ")

  def copy_into_another_list(arr):
     arr2 = [None] * len(arr)
     for i in range(0, len(arr)):
         arr2[i] = arr[i]
     print("Elements of original list: ")
     for i in range(0, len(arr)):
         print(arr[i],end=" ")

     print()

     # Displaying elements of list arr2
     print("Elements of new list: ")
     for i in range(0, len(arr2)):
         print(arr2[i],end=" ")

  def duplicate_elements(arr):
      print ("duplicate elements")
      for i in range(0, len(arr)):
          for j in range(i + 1, len(arr)):
              if (arr[i] == arr[j]):
                  print(arr[j],end=" ")

  def sum_of_list_elements(arr):
      sum = 0;

      # Loop through the list to calculate sum of elements
      for i in range(0, len(arr)):
          sum = sum + arr[i];

      print("Sum of all the elements of an list: " + str(sum))

  def largest_element(arr):
      max = arr[0]

      # Loop through the list
      for i in range(0, len(arr)):
          # Compare elements of list with max
          if (arr[i] > max):
              max = arr[i]

      print("Largest element present in given list: " + str(max))

  def smallest_element(arr):
      min = arr[0];

      # Loop through the list
      for i in range(0, len(arr)):
          # Compare elements of list with min
          if (arr[i] < min):
              min = arr[i]

      print("Smallest element present in given list: " + str(min))

  def ascending_order(arr):
        temp = 0

        # Displaying elements of original list
        print("Elements of original list: ")
        for i in range(0, len(arr)):
            print(arr[i], end=" ")

            # Sort the list in ascending order
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] > arr[j]):
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp

        print()

        # Displaying elements of the list after sorting

        print("Elements of list sorted in ascending order: ")
        for i in range(0, len(arr)):
            print(arr[i], end=" ")

  def descending_order(arr):
        temp = 0

        # Displaying elements of original list
        print("Elements of original array: ")
        for i in range(0, len(arr)):
            print(arr[i]),

            # Sort the list in descending order
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] < arr[j]):
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp

        print()

        # Displaying elements of list after sorting
        print("Elements of list sorted in descending order: ")
        for i in range(0, len(arr)):
            print(arr[i],end=" ")
  dictionary={
    1: print_reverse,
    2: odd_position,
    3: even_position,
    4: copy_into_another_list,
    5: duplicate_elements,
    6: sum_of_list_elements,
    7: largest_element,
    8: smallest_element,
    9: ascending_order,
    10: descending_order}
  dictionary.get(option)(arr)
  print ("\n")
  a=input("do you want to continue" "(y/n) ")
  if a == "y":
    continue
  else:
    break

