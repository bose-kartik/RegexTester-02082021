import re

def interface_section():
    global interface_tracker
    line_number = 0 ### Variable to track the on which line number, the function is working.
    
    for current_line in line: ### interface_start_pointer = [] saves all the start pointers for interface blocks
        if current_line[0:3] == 'int':
            interface_start_pointer.append(line_number)
            interface_tracker = interface_tracker + 1

        line_number = line_number + 1

    start_ptr_count = len(interface_start_pointer)
    for n in range(1,start_ptr_count): ### End Pointers for N-1th interface blocks.
        interface_end_pointer.append(int(interface_start_pointer[n])-1)

    
    line_count = len(line)
    for k in range(interface_start_pointer[-1],line_count): ### End Pointer for Nth interface block.
        current_line = line[k]
        if current_line == '\n' :
            interface_end_pointer.append(k)
            break

def interface_block(StartPtr,EndPtr):
    interface_list_tracker = 0
    interface_block_dict = {
        'name':'',
        'ip' :'',
        'mask':'',
        'description':''
    }
    interface_block_dict.clear
    
    for current_line in range(StartPtr,EndPtr):

        current_line_str = str(line[current_line])
        
        result = re.search(r'interface\s(\S+)', current_line_str , flags=0)
        if result:
            interface_block_dict.update(name= result.group(1))

        result = re.search(r'description\s(\S+)', current_line_str , flags=0)
        if result:
            interface_block_dict.update(description= result.group(1))

        result = re.search(r'ip\saddress\s(\S+)', current_line_str , flags=0)
        if result:
            spilt_result = result.group(1)
            ip_result = re.search(r'(\S+)\/', current_line_str , flags=0)
            if ip_result:
                interface_block_dict.update(ip= ip_result.group(1))
            mask_result = re.search(r'\/(\S+)', current_line_str , flags=0)
            if mask_result:
                interface_block_dict.update(mask= mask_result.group(1))
    
    interfaces.append(interface_block_dict)
            
interface_tracker = 0 ### Variable to track the number of interface present in File.
interface_start_pointer = [] ### List to track the Start Line Number of Interface Blocks
interface_end_pointer = [] ### List to track the End Line Number of Interface Blocks
interfaces = []

with open('sample.txt', 'r') as getter: ### Reading (and closing) the File : sample.txt
    line = getter.readlines() #### This makes the data as type : list
    
    interface_start_pointer.clear()
    interface_end_pointer.clear()
    interface_section() ### Saves Start & End Pointers to all the interface blocks

    ### Create Interface Blocks based on Start and End Ptr
    for k in range(len(interface_start_pointer)):
        interface_block(interface_start_pointer[k],interface_end_pointer[k])

#print(interfaces)
print(interface_start_pointer)
print(interface_end_pointer)
for k in interfaces:
    print(k)        

    

