def interface_section():
    global interface_tracker
    line_number = 0 ### Variable to track the on which line number function is working.
    
    for current_line in line:
        if current_line[0:3] == 'int':
            interface_start_pointer.append(line_number)
            interface_tracker = interface_tracker + 1

        line_number = line_number + 1


interface_tracker = 0 ### Variable to track the number of interface present in File.
interface_start_pointer = [] ### List to track the Start Line Number of Interface Blocks

with open('sample.txt', 'r') as getter: ### Reading (and closing) the File : sample.txt
    line = getter.readlines() #### This makes the data as type : list
    interface_start_pointer.clear()
    interface_section() # Saves Start Pointers to all the interface blocks
        
print('Total Interfaces in File : ' + str(interface_tracker))

        

    

