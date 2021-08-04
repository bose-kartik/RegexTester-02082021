def interface_section():
    global interface_tracker
    line_number = 0 ### Variable to track the on which line number, the function is working.
    
    for current_line in line: ### interface_start_pointer = [] saves all the start pointers for interface blocks
        if current_line[0:3] == 'int':
            interface_start_pointer.append(line_number)
            interface_tracker = interface_tracker + 1

        line_number = line_number + 1

    start_ptr_count = len(interface_start_pointer)
    for n in range(1,start_ptr_count): ### End Pointer for N-1th interface blocks,
        interface_end_pointer.append(int(interface_start_pointer[n])-2)

    
    line_count = len(line)
    for k in range(12,line_count): ### End Pointer for Nth interface block.
        current_line = line[k]
        if current_line == '\n' :
            interface_end_pointer.append(k)
            break
    
    

interface_tracker = 0 ### Variable to track the number of interface present in File.
interface_start_pointer = [] ### List to track the Start Line Number of Interface Blocks
interface_end_pointer = [] ### List to track the End Line Number of Interface Blocks

with open('sample.txt', 'r') as getter: ### Reading (and closing) the File : sample.txt
    line = getter.readlines() #### This makes the data as type : list
    
    interface_start_pointer.clear()
    interface_end_pointer.clear()
    interface_section() ### Saves Start & End Pointers to all the interface blocks


        
#print('Total Interfaces in File : ' + str(interface_tracker))
print(interface_start_pointer)
print(interface_end_pointer)

        

    

