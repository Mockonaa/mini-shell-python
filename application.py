def load_config():
    cfg = open("installed_app.cfg", "r")
    temp = cfg.read()
    temp2 = ""
    temp3 = []
    for i in range(len(temp)):
        if temp[i] == "\n":
            temp3.append(temp2)
            temp2 = ""
        elif temp[i] == " " or temp[i] == "":
            pass
        else:
            temp2 += temp[i]
    if temp2 != "":
        temp3.append(temp2)

    # Phase 2, we seek for empty entries and delete them if found
    for i in range(len(temp3) - 1):
        if temp3[i] == "":
            temp3.remove(temp3[i])
    return temp3
