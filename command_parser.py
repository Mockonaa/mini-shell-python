def get_command(com):
    dat = []
    if type("aaa") == type(com):
        for i in range(len(com)):
            dat.append(com[i])
        if " " in dat:
            j = 0
            while dat[j] != " ":
                j += 1
            com_final = ""
            for i in range(j):
                com_final += dat[i]
            return com_final
        return com
    else:
        return 14


def get_argument(com):
    # Deprecated
    dat = []
    if type("aaa") == type(com):
        for i in range(len(com)):
            dat.append(com[i])
        if " " in dat:
            j = 0
            while dat[j] != " ":
                j += 1
            for i in range(j+1):
                dat.remove(dat[0])
            arg = ""
            for i in range(len(dat)):
                arg += dat[i]
            return arg
        else:
            return 14


def get_multiple_arg(com):
    """
    Error code 14: Invalid Input
    Error code 15: No Arguments
    """
    if type("aaa") == type(com):
        temp = ""
        arg_list = []
        for i in range(len(com)):
            if com[i] != " ":
                temp += com[i]
            elif com[i] == " ":
                arg_list.append(temp)
                temp = ""
        if temp != "":
            arg_list.append(temp)
        if len(arg_list) == 1:
            return 15
        else:
            arg_list.remove(arg_list[0])
        return arg_list
    else:
        return 14
