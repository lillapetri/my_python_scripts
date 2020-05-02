'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated
by commas except for the last two names, which should be
separated by an ampersand.
'''

def namelist(names):
    x=''
    if len(names) == 0:
        return x
    elif len(names) == 1:
        return names[0]['name']
    elif len(names)>=2:
        for i in range(len(names) - 1):
            x += f"{names[i]['name']}, "
        return f"{x.strip(', ')} & {names[-1]['name']}"

def namelist2(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]


# Tests
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([]))