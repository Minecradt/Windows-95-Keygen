from random import randint
print("##     ##    ###    ########  ########    ########  ##    ##    ##     ## #### ##    ## ########  ######  ########     ###    ########  ######## \n###   ###   ## ##   ##     ## ##          ##     ##  ##  ##     ###   ###  ##  ###   ## ##       ##    ## ##     ##   ## ##   ##     ##    ##    \n#### ####  ##   ##  ##     ## ##          ##     ##   ####      #### ####  ##  ####  ## ##       ##       ##     ##  ##   ##  ##     ##    ##    \n## ### ## ##     ## ##     ## ######      ########     ##       ## ### ##  ##  ## ## ## ######   ##       ########  ##     ## ##     ##    ##    \n##     ## ######### ##     ## ##          ##     ##    ##       ##     ##  ##  ##  #### ##       ##       ##   ##   ######### ##     ##    ##    \n##     ## ##     ## ##     ## ##          ##     ##    ##       ##     ##  ##  ##   ### ##       ##    ## ##    ##  ##     ## ##     ##    ##    \n##     ## ##     ## ########  ########    ########     ##       ##     ## #### ##    ## ########  ######  ##     ## ##     ## ########     ##    \n\n")
def SendErrorMessage(Error):
    print(Error)
while(True):
    print("How Many Keys Do You Want To Generate?")
    keys = input("")
    
    try: 
        keys = int(keys)
    except ValueError:
        SendErrorMessage("Type a Number In!")
    else:
        if not (keys)<1:
            break
        else:
            SendErrorMessage("Value must be Greater Than 0!")
keys = (keys) + 1
for i in range(1,keys):
    part1 = str(randint(1,365))
    while(len(part1)<3):
        part1 = "0" + (part1)
    
    while(True):
        part2 = randint(11111,99999)
        sums = 0
        for a in (str(part2)):
            sums = (sums + int(a))
        # print(sums,part2)
        if ((sums) % 7==0):
            break
    randomnum = str(randint(0,9))
    for f in range(1,5):
        randomnum = randomnum + str(randint(0,9))
    part2 = str(part2)
    tempvar = randint(1,2)
    if (tempvar == 1):
        part3 = str(randint(95,99))
    else:
        part3 = "0" + str(randint(1,3))
    print(part1 + part3 + "-OEM-00" + part2 + "-" + randomnum)
