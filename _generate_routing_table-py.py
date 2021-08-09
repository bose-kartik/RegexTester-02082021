import re

routes = []

count = 0

with open('sample_rt.txt', 'r') as getter:
    line = getter.read()
    blocks = re.findall(r"(\d+\.\d+\.\d+\.\d+\/\d+.*?)(?=^\S+)", line, flags=re.I|re.M|re.S)
    
    for current_line in blocks:
        alg = ''
        destination = ''
        mask = ''
        interface = ''
        next_hop_ip = ''

        alg_search = re.search(r'\[(.*)\/', current_line)

        destination_search = re.search(r'\d+\.\d+\.\d+\.\d+\/\d+', current_line)
        
        interface_hop_search = re.search(r'\n(\s.*)', current_line)

        if alg_search:
            alg = alg_search.group(1)

        if destination_search:
            destination_split = destination_search.group(0).split('/')
            destination = destination_split[0]
            mask = destination_split[1]

        if interface_hop_search:
            if alg != 'Direct' or 'Local':
                interface_search = re.search(r'(\d+.\d+.\d+.\d+)', interface_hop_search.group(1))
                if interface_search:
                    interface = interface_search.group(1)
                
            if alg != 'Local':
                next_hop_ip_search = re.search(r'via.(\S+)\.', interface_hop_search.group(1))
                if next_hop_ip_search:
                    next_hop_ip = next_hop_ip_search.group(1)

        route_block = {
            'alg': alg,
            'destination': destination,
            'mask': mask,
            'interface': interface,
            'next_hop_ip': next_hop_ip
        }
        routes.append(route_block)

print(routes)
        
