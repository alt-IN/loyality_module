from os import makedirs
from os.path import split as pathsplit, exists as pathexists, dirname as pathdirname, join as pathjoin
from pandas import read_csv
from sys import executable


DEFAULT_SOURCE_DIR=('db','loyality_table.csv')
DEFAULT_SOURCE_HEADERS=['ID', 'FREE_ITEMS']

# Create csv file and dirs if not exists.
def create_file(source_file):
    try:
        makedirs(pathsplit(source_file)[0], exist_ok=True)
        with open(source_file,'w') as workfile:
            workfile.write(','.join(DEFAULT_SOURCE_HEADERS))
        workfile.close()
    except:
        raise OSError("Cannot create file in default directory: {}".format(source_file))

# Get stock value of free items for user
def scan_file(id, sfile):
    # data_csv = DataFrame()
    data_csv = read_csv(sfile, index_col='ID')
    try:
        val = int(data_csv.loc[id,'FREE_ITEMS'])
    except:
        val = 0
    return data_csv,val

# Update new value of free items for user
def write_file(id, sfile, data, value):
    data.loc[id,'FREE_ITEMS'] = int(value)
    data.to_csv(sfile)
    

# Define the rule of loyalite
def loyalty_program(purchases):
    return purchases // 5

def main():
    # Set source file and create if not exist
    source_file = pathjoin(pathdirname(executable),*DEFAULT_SOURCE_DIR)
    if not pathexists(source_file):
        create_file(source_file)

    #Ask for user ID
    user_id = None
    while not user_id:
        user_id = input("User id (only numbers): ").strip()
        if not user_id.isdigit():
            user_id = None
    user_id = int(user_id)

    # Ask the user for the number of purchases
    num_purchases = None
    while not num_purchases:
        num_purchases = input("How many purchases have you made (only numbers)? ").strip()
        if not num_purchases.isdigit():
            num_purchases = None
    num_purchases = int(num_purchases)

    # Calculate the number of free items earned
    new_free_items = loyalty_program(num_purchases)

    data_csv, prev_free_items = scan_file(user_id, source_file)
    # print(data_csv.dtypes)

    # Ask the user if they want to use their free item now or save it for later
    if new_free_items >= 1:
        use_now = input(
            "You have earned a {} free item(s)! Do you want to use it now? (y/n): ".format(new_free_items))
        flag = 0

        while flag != 1:
            if use_now.lower().strip() == "y" or use_now.lower().strip() == "yes":
                if new_free_items != 1:
                    write_file(user_id, source_file, data_csv, int(prev_free_items + new_free_items - 1))
                print("Enjoy your free item(s)! Your left free items: {}".format(int(prev_free_items + new_free_items - 1)))
                flag = 1
            elif use_now.lower().strip() == "n" or use_now.lower().strip() == "no":
                write_file(user_id, source_file, data_csv, int(prev_free_items + new_free_items))
                print("Your free item(s) has been saved for later use. Now you have {} free items left".format(int(prev_free_items + new_free_items)))
                flag = 1
            else:
                use_now = input(
                    "You have earned a {} free item(s)! Do you want to use it now? Please enter (yes or no): ".format(new_free_items))
    else:
        print("Sorry, you have not earned a free item this time. Your actual stock of free items: {}".format(prev_free_items))




if __name__ == "__main__":
    main()
