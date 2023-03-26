from loyality import main as loyalitymain

choice = True
while choice:
    loyalitymain()
    flag = input('Do you want to repeat process? Type "r"/"restart" for repeat or any other symbol to exit: ').strip()
    if flag.lower() != 'r' and flag.lower() != 'restart':
        choice = False