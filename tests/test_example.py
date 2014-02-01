__author__ = 'Vincent'

#Note: assuming correct inputs only, proper full names
#Do not account for: empty strings

def abbreviate_name(full_name):
    names = full_name.split()
    abbrev_name = ""
    for index, name in enumerate(names):
        if index == 0:
            abbrev_name += name
        else:
            abbrev_name += name[0] + ". "
    return abbrev_name
