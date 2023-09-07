def bubble_sort(arr)
  # defining the algorithm function & get the len coz counting usually starts from 1.
  n= arr.length

  #create a var to store the state if swapped no.s

  swapped = true;

  while swapped do 
    swapped = false
    (n-1).times do |i|
      if arr[i] > arr[i+1]
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        swapped = true
      end
    end

    #display once one sort of the array is complete
    puts arr.inspect
  end
  arr
end 

numbers = [9,8,7,6,5,4,3,2,1]
sorted_numbers = bubble_sort(numbers)
puts "Final Sorted Array: #{sorted_numbers}"