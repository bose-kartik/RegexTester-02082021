import re

interfaces = []

output = open('sample.txt').read()
blocks = re.findall(r"(interface.*?)(?=^\S+)", output, re.S | re.I | re.M)
for bl in blocks:
    _name = ""
    _ip_address = ""
    _description = ""
    _ip_mask = ""
    _name_search = re.search(r'interface\s+(\S+)', bl)
    _ip_search = re.search(r'ip\s+address\s+(\d+\.\d+\.\d+\.\d+\/\d+)', bl)
    _description_search = re.search(r'description\s+(\S+)', bl)
    if _name_search:
        _name = _name_search.group(1)
        if _ip_search:
            _ip_setup = _ip_search.group(1).split("/")
            _ip_address = _ip_setup[0]
            if len(_ip_setup) > 1:
                _ip_mask = _ip_setup[1]
        if _description_search:
            _description = _description_search.group(1)
        _interface = {
            "name": _name,
            "ip" : _ip_address,
            "mask": _ip_mask,
            "description":_description
        }
        interfaces.append(_interface)

print(interfaces)

        

    

