def bubble_sort(arr)
  # defining the algorithm function & get the len coz counting usually starts from 1.
  n= arr.length

  #create a var to store the state if swapped no.s

  swapped = true;

  while swapped do 
    swapped = false
    (n-1).times do |i|
      if arr[i] > arr[i+1]
        #compare the numbers  if the one in front is greater 
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

        # if the its greater their positions are swapped
        swapped = true
      end

      # since we are using times the above loop is run and since the unsorted number is always bubbled to its right position, comparing it again is a waste of time hence n-1 used
    end

    #display once one sort of the array is complete
    puts arr.inspect
  end

  #return the array.
  arr
end 

numbers = [9,8,7,6,5,4,3,2,1]
sorted_numbers = bubble_sort(numbers)
puts "Final Sorted Array: #{sorted_numbers}"