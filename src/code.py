__author__ = 'Vincent'

def abbreviate_name(full_name):
    names = full_name.split()
    abbrev = ""

    i = 0
    while i<len(names)-1:
        abbrev += names[i][0] +". "
        i += 1
    abbrev += names[i]
    return abbrev