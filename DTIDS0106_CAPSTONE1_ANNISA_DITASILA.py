# RENT DATABASE

database = {'id': [1,2,3,4],
 'type of accomodation': ['house', 'apartment','condos','studio'],
 'location':['Bali','Jakarta','Jakarta','West java'],
 'price':[4500000,3000000,6000000,2500000],
 'bedroom':[4,2,4,1],
 'bathroom':[2,1,2,1],
 'm2':[300,100,250,60],
 'availability':['yes','no','yes','yes'],
 'contact':[21345,216789,219078,218900],
 'booked':['no','no','no','no']
 }

# USER DATABASE
user_database = {'username':['admin','a'],'password':['admin','a'],'type_of_account':['admin','user']}

# IMPORT LIBRARIES
from tabulate import tabulate


# SHOW DATA USING TABULATE
def database_wo_contact_booked():
    keys = list(database.keys())
    database_wo_contact_booked = {key: [value[i] for i, availability in enumerate(database['availability']) if availability == 'yes'] for key, value in database.items() if key not in ['contact', 'booked']}
    print(tabulate(database_wo_contact_booked, headers=keys, tablefmt="presto"))

def show_user_database():
    keys = list(user_database.keys())
    print(tabulate(user_database, headers=keys))


# admin interface - 1. add user
def adding_user():
    show_user_database()
    while True:
        new_username = input('create username: ').casefold()
        if new_username not in user_database['username']:
            new_password = input('create password: ')
            while True:
                user_type = input('Enter type of account: ')
                if user_type == 'admin' or user_type == 'user':
                    user_database['type_of_account'].append(user_type)
                    user_database['username'].append(new_username)
                    user_database['password'].append(new_password)
                    print("User added successfully.")
                    show_user_database()
                    break
                else:
                    print('Invalid input. Choose admin or user')
                    continue
            break
        else:
            print('Username already exists. Choose another!')


# admin interface - 2. remove user
def remove_user():
    show_user_database()
    while True:
        username_to_remove = input('Enter username to remove: ')
        if username_to_remove in user_database['username']:
            index = user_database['username'].index(username_to_remove)
            del user_database['username'][index]
            del user_database['password'][index]
            del user_database['type_of_account'][index]
            print('User removed successfully!')
            show_user_database()
            break
        else:
            print('Username not found. Input the correct username')
            continue



# admin interface - 3. edit user
def edit_user():
    while True:
        show_user_database()
        username_to_edit = input('Enter username to edit: ')
        if username_to_edit in user_database['username']:
            print('''
                Enter the number you want to edit:
                    1. change username
                    2. change password
                    3. change type of account
                    4. back to admin interface
                ''')
            while True:
                input_what_to_edit = input('Input number you want to edit: ')
                if input_what_to_edit.isdigit():
                    input_what_to_edit = int(input_what_to_edit)
                if input_what_to_edit == 1:
                    while True:
                        new_username = input('Enter new username: ')
                        if new_username == username_to_edit:
                            print('you put the same username. Choose another!')
                            continue
                        if username_to_edit in user_database['username']:
                            index = user_database['username'].index(username_to_edit)
                            user_database['username'][index] = new_username
                            print('User edited successfully!')
                            show_user_database()
                            return
                        else:
                            print('Username already exists. Choose another!')
                            continue
                elif input_what_to_edit == 2:
                    while True:
                        new_password = input('Enter new password: ')
                        if username_to_edit in user_database['username']:
                            index = user_database['username'].index(username_to_edit)
                            if new_password in user_database['password'][index]:
                                print('You entered the same password')
                                continue
                            else:
                                user_database['password'][index] = new_password
                                print('User edited successfully!')
                                show_user_database()
                                break
                        else:
                            print('Password already exists. Choose another!')
                            continue
                elif input_what_to_edit == 3:
                    while True:
                        user_type = input('Enter type of account: ')
                        if username_to_edit in user_database['username'] and (user_type == 'admin' or user_type == 'user'):
                            index = user_database['username'].index(username_to_edit)
                            if user_type in user_database['type_of_account'][index]:
                                print('You entered the same type of account')
                                continue
                            else:
                                user_database['type_of_account'][index] = user_type
                                show_user_database()
                                print('User edited successfully!')
                                break
                        else:
                            print('Invalid input. Choose admin or user')
                            continue
                elif input_what_to_edit == 4:
                    return
                else:
                    print('Incorrect input. Enter 1, 2 or 3!')
                    continue
        else:
            print('Username not found. Input the correct username')
            continue

def add_to_rent_database():
    while True:
        while True:
            new_id = input('Enter new id of accomodation: ')
            if new_id.isdigit():
                new_id = int(new_id)
                if new_id not in database['id']:
                    database['id'].append(new_id)
                    break
                else:
                    print('Id already exists. Choose another!')
                    continue
        while True:
            new_type = input('Enter type of accommodation: ').lower()
            if new_type == 'house' or new_type == 'apartment' or new_type == 'condos' or new_type =='studio':
                database['type of accomodation'].append(new_type)
                break
            else:
                ('type of accomodation: house, apartment, condos, studio')
                continue
        while True:
            new_location = input('Enter location: ').capitalize()
            database['location'].append(new_location)
            break
        while True:
            new_price = input('Enter price: ')
            if new_price.isdigit():
                database['price'].append(new_price)
                break
            else:
                print('Please enter price correctly!')
                continue
        while True:
            new_bedroom = input('Enter number of bedrooms: ')
            if new_bedroom.isdigit():
                database['bedroom'].append(new_bedroom)
                break
            else:
                print('Please enter number of bedrooms correctly!')
                continue
        while True:
            new_bathroom = input('Enter number of bathrooms: ')
            if new_bathroom.isdigit():
                database['bathroom'].append(new_bathroom)
                break
            else:
                print('Please enter number of bathrooms correctly!')
                continue
        while True:
            new_m2 = input('Enter area (m2): ')
            if new_m2.isdigit():
                database['m2'].append(new_m2)
                break
            else:
                print('Please enter area (m2) correctly!')
                continue
        while True:
            new_availability = input('Enter availability (yes/no): ')
            if new_availability == 'yes' or new_availability == 'no':
                database['availability'].append(new_availability)
                break
            else:
                print('Invalid input. Choose yes or no')
                continue
        while True:
            new_contact = input('Enter contact number: ')
            if new_contact.isdigit():
                database['contact'].append(new_contact)
                break
            else:
                print('Please enter contact number correctly!')
                continue
        new_booked = 'no'
        database['booked'].append(new_booked)
        print("New data added to the database successfully.")
        keys = list(database.keys())
        print(tabulate(database, headers=keys))
        break

# admin interface - edit something to rental apartment database
def edit_rent_database():
    keys = list(database)
    print(tabulate(database, headers=keys))
    while True:
        input_id = input('input id of the accomodation to edit: ') 
        if input_id.isdigit():
            input_id = int(input_id)
            if input_id in database['id']:
                while True:
                    print('''
                    Enter the number you want to edit:
                        1. change id
                        2. change type of accomodation
                        3. change location
                        4. change price
                        5. change number of bedrooms
                        6. change number of bathrooms
                        7. change area (m2)
                        8. change availability
                        9. change contact number
                        10. change booked accomodation
                        11. back to admin interface
                        ''')
                    input_what_to_edit = input('what to edit: ')
                    if input_what_to_edit.isdigit():
                        input_what_to_edit = int(input_what_to_edit)
                    if input_what_to_edit == 1:
                        index = database['id'].index(input_id)
                        while True:
                            new_id = input('Enter new id of accomodation: ')
                            if new_id.isdigit():
                                new_id = int(new_id)
                                if new_id not in database['id']:
                                    database['id'][index] = new_id
                                    print('User edited successfully!')
                                    print(tabulate(database, headers=keys))
                                    break
                                else:
                                    print('Id already exists. Choose another!')
                                    continue
                            else:
                                print('Id must be a number')
                                continue
                    elif input_what_to_edit == 2:
                        while True:
                                new_type = input('Enter type of accommodation: ').lower()
                                if new_type == 'house' or new_type == 'apartment' or new_type == 'condos' or new_type =='studio':
                                    database['type of accomodation'][index] = new_type
                                    print('User edited successfully!')
                                    print(tabulate(database, headers=keys))
                                    break
                                else:
                                    ('type of accomodation: house, apartment, condos, studio')
                                    continue
                    elif input_what_to_edit == 3:
                        while True:
                            new_location = input('Enter location: ').capitalize()
                            database['location'][index] = new_location
                            print('User edited successfully!')
                            print(tabulate(database, headers=keys))
                            break
                    elif input_what_to_edit == 4:
                        while True:
                            new_price = input('Enter price: ')
                            if new_price.isdigit():
                                new_price = int(new_price)
                                database['price'][index] = new_price
                                print('User edited successfully!')
                                print(tabulate(database, headers=keys))
                                break
                            else:
                                print('Price must be a number')
                                continue
                    elif input_what_to_edit == 5:
                        while True:
                            new_bedroom = input('Enter number of bedrooms: ')
                            if new_bedroom.isdigit():
                                new_bedroom = int(new_bedroom)
                                database['bedroom'][index] = new_bedroom
                                print('User edited successfully!')
                                print(tabulate(database, headers=keys))
                                break
                            else:
                                print('Number of bedrooms must be a number')
                                continue
                    elif input_what_to_edit == 6:
                        while True:
                            new_bathroom = input('Enter number of bathrooms: ')
                            if new_bathroom.isdigit():
                                new_bathroom = int(new_bathroom)
                                database['bathroom'][index] = new_bathroom
                                print('User edited successfully!')
                                print(tabulate(database, headers=keys))
                                break
                            else:
                                print('Number of bathrooms must be a number')
                                continue
                    elif input_what_to_edit == 7:
                        while True:
                            new_m2 = input('Enter area (m2): ')
                            if new_m2.isdigit():
                                new_m2 = int(new_m2)
                                database['m2'][index] = new_m2
                                print('User edited successfully!')
                                print(tabulate(database, headers=keys))
                                break
                            else:
                                print('Area (m2) must be a number')
                                continue
                    elif input_what_to_edit == 8:
                        while True:
                            new_availability = input('Enter availability (yes/no): ')
                            if new_availability == 'yes' or new_availability == 'no':
                                database['availability'][index] = new_availability
                                print('User edited successfully!')
                                print(tabulate(database, headers=keys))
                                break
                            else:
                                print('Invalid input. Choose yes or no')
                                continue
                    elif input_what_to_edit == 9:
                        while True:
                            new_contact = input('Enter contact number: ')
                            if new_contact.isdigit():
                                new_contact = int(new_contact)
                                database['contact'][index] = new_contact
                                print('User edited successfully!')
                                print(tabulate(database, headers=keys))
                                break
                            else:
                                print('Contact number must be a number')
                                continue
                    elif input_what_to_edit == 10:
                        while True:
                            new_booked = input('Enter booked: yes or no: ')
                            if new_booked == 'yes' or new_booked == 'no':
                                database['booked'][index] = new_booked
                                print('User edited successfully!')
                                print(tabulate(database, headers=keys))
                                break
                            else:
                                print('Invalid input. Choose yes or no')
                                continue
                    elif input_what_to_edit == 11:
                        return True
                    else:
                        print('input the correct choice!')
                        continue
        else:
            print('Id not found. Input the correct id')
            
        
def remove_rent_database():
    keys = list(database.keys())
    print(tabulate(database, headers=keys))
    while True:
        id_database = input('insert id of accomodation to remove from the database: ')
        if id_database.isdigit():
            id_database = int(id_database)
            if id_database in database['id']:
                index = database['id'].index(id_database)
                del database['id'][index]
                del database['type of accomodation'][index]
                del database['location'][index]
                del database['price'][index]
                del database['bedroom'][index]
                del database['bathroom'][index]
                del database['m2'][index]
                del database['availability'][index]
                del database['contact'][index]
                del database['booked'][index]
                print('Accomodation removed successfully')
                print(tabulate(database,headers=keys))
                break
            else:
                print('Id not found. Input the correct id')
                continue
        else:
            print('Input an Id of accomodation to remove from database table')
        
def admin_interface():
    while True:
        print('''  
            Welcome to CheapApartment.com - Management System

            What would you like to do?
            1. Manage User Database
            2. Manage Accommodation Database
            3. Exit
            ''')
        admin_manage_user_database = input('chose 1, 2, or 3: ')
        if admin_manage_user_database.isdigit():
            admin_manage_user_database = int(admin_manage_user_database)
            while True:
                if admin_manage_user_database == 1:
                    print('''
                            Manage user database
                            1. Add new user
                            2. Remove user
                            3. Edit User
                            4. Exit
                            ''')
                    input_admin_choice = input('chose 1 until 4: ')
                    if input_admin_choice.isdigit():
                        input_admin_choice = int(input_admin_choice)
                        if input_admin_choice == 1:
                            adding_user()
                            continue
                        elif input_admin_choice == 2:
                            remove_user()
                            continue
                        elif input_admin_choice == 3:
                            edit_user()
                            continue
                        elif input_admin_choice == 4:
                            print('Thank you for visiting this website! Have a great day!')
                            break
                    else:
                        print('incorrect input, try again: ')
                elif admin_manage_user_database == 2:
                    print('''
                            Manage user database
                            1. Add accomodation
                            2. Edit accomodation 
                            3. Remove accomodation
                            4. Exit
                            ''')
                    admin_manage_accomodation_database = input('What would you like to do? ')
                    if admin_manage_accomodation_database.isdigit():
                        admin_manage_accomodation_database = int(admin_manage_accomodation_database)
                        if admin_manage_accomodation_database == 1:
                            add_to_rent_database()
                            continue
                        elif admin_manage_accomodation_database== 2:
                            edit_rent_database()
                            continue
                        elif admin_manage_accomodation_database == 3:
                            remove_rent_database()
                            continue
                        elif admin_manage_accomodation_database == 4:
                            print('Thank you for visiting this website! Have a great day!')
                            break
                        else:
                            print('incorrect input, try again 1: ')
                            continue
                elif admin_manage_user_database == 3:
                    print('Thank you for visiting this website! Have a great day!')
                    return 'exit'
                else:
                    print('incorrect input, try again 2: ')
                    break
        else:
            print('incorrect input, try again 3: ')
            continue
    

def sorting(database, option_sort, reverse=False):
    database_aa = {key: [value[i] for i, availability in enumerate(database['availability']) if availability == 'yes'] for key, value in database.items() if key not in ['contact', 'booked']}
    sequence = sorted(range(len(database_aa['type of accomodation'])), key=lambda item: database[option_sort][item], reverse=reverse)
    sort_id = [database_aa['id'][i] for i in sequence]
    sort_accomodation = [database_aa["type of accomodation"][i] for i in sequence]
    sort_location = [database_aa["location"][i] for i in sequence]
    sort_price= [database_aa["price"][i] for i in sequence]
    sort_bedroom = [database_aa["bedroom"][i] for i in sequence]
    sort_bathroom = [database_aa["bathroom"][i] for i in sequence]
    sort_m2 = [database_aa["m2"][i] for i in sequence]
    sort_availability = [database_aa["availability"][i] for i in sequence]
    database_sorted = {"sort_id": sort_id,"type_of_accomodation": sort_accomodation, "location":sort_location,  "price": sort_price, 'bedroom':sort_bedroom, 'bathroom':sort_bathroom, 'm2': sort_m2, "availability": sort_availability}
    return database_sorted


def sort_choices():
    print('''  
        How would you like to sort?
        1. Sort ascending
        2. Sort descending    ''')

# USER INTERFACE - 1. DISPLAYING RENTALS ACCOMODATION
def show_accommodations():
    database_wo_contact_booked()
    while True:
        print('''
            1. Sort by type of accomodation
            2. Sort by location
            3. Sort by price
            4. Sort by availability
            5. back to menu
                ''')
        option_sort = input("Enter your choice: ")
        if option_sort.isdigit():
            option_sort = int(option_sort)
            while True:
                if option_sort == 1:
                    sort_choices()
                    sort_asc_desc = input('choose 1 or 2: ')
                    if sort_asc_desc.isdigit():
                        sort_asc_desc = int(sort_asc_desc)
                        if sort_asc_desc == 1:
                            sorted_database = sorting(database, "type of accomodation")
                            print(tabulate(sorted_database, headers=sorted_database.keys(), tablefmt="presto"))
                            break
                        elif sort_asc_desc == 2:
                            sorted_database = sorting(database, "type of accomodation", reverse=True)
                            print(tabulate(sorted_database, headers=sorted_database.keys(), tablefmt="presto"))
                            break
                    else:
                        print('Invalid option, choose a number displayed')
                elif option_sort == 2:
                    sort_choices()
                    sort_asc_desc = input('choose 1 or 2: ')
                    if sort_asc_desc.isdigit():
                        sort_asc_desc = int(sort_asc_desc)
                        if sort_asc_desc == 1:
                            sorted_database = sorting(database, "location")
                            print(tabulate(sorted_database, headers=sorted_database.keys(), tablefmt="presto"))
                            return
                        elif sort_asc_desc == 2:
                            sorted_database = sorting(database, "location", reverse=True)
                            print(tabulate(sorted_database, headers=sorted_database.keys(), tablefmt="presto"))
                            return
                elif option_sort == 3:
                    sort_choices()
                    sort_asc_desc = input('choose 1 or 2: ')
                    if sort_asc_desc.isdigit():
                        sort_asc_desc = int(sort_asc_desc)
                        if sort_asc_desc == 1:
                            sorted_database = sorting(database, "price")
                            print(tabulate(sorted_database, headers=sorted_database.keys(), tablefmt="presto"))
                            return
                        elif sort_asc_desc == 2:
                            sorted_database = sorting(database, "price", reverse=True)
                            print(tabulate(sorted_database, headers=sorted_database.keys(), tablefmt="presto"))
                            return
                elif option_sort == 4:
                    sort_choices()
                    sort_asc_desc = input('choose 1 or 2: ')
                    if sort_asc_desc.isdigit():
                        sort_asc_desc = int(sort_asc_desc)
                        if sort_asc_desc == 1:
                            sorted_database = sorting(database, "availability")
                            print(tabulate(sorted_database, headers=sorted_database.keys(), tablefmt="presto"))
                            return
                        elif sort_asc_desc == 2:
                            sorted_database = sorting(database, "availability", reverse=True)
                            print(tabulate(sorted_database, headers=sorted_database.keys(), tablefmt="presto"))
                            return
                elif option_sort == 5:
                    return
        else:
            print('Invalid option, choose a number displayed')
            break

def print_row_by_index(database, index=None):
    if index != None:
        booked_entries = {key: [value[index]] for key, value in database.items()}
    else:
        booked_entries = {key: [value[i] for i, booked in enumerate(database['booked']) if booked == 'yes'] for key, value in database.items()}
    print(tabulate(booked_entries, headers=booked_entries.keys(), tablefmt="presto"))


def rent_accomodation():
    database_wo_contact_booked()
    while True:
        choise_rental_accomodation = input('Please select id of the accommodations you wish to rent: ')
        if choise_rental_accomodation.isdigit():
            choise_rental_accomodation = int(choise_rental_accomodation)
            try:
                index = database['id'].index(choise_rental_accomodation)
            except ValueError:
                print('Incorrect input, try again')
                continue
            while True:
                if choise_rental_accomodation in database['id'] and database['availability'][index]=='yes':
                    renting_process = {key: value[index] for key, value in database.items()}
                    contact_number = renting_process['contact']
                    print('You will rent {} in {} with {} bedroom, {} bathroom with {} m2 and Rp.{}/month'.format(
                        renting_process["type of accomodation"],
                        renting_process["location"],
                        renting_process["bedroom"],
                        renting_process["bathroom"], 
                        renting_process["m2"],
                        renting_process["price"]
                    ))    
                    print('You need to make a deposit of Rp. 100,000 to get in touch with the agent of property in case you want to cancel. the deposit will be automatically cancelled when the owner or agency is notified of the deposit change')
                    while True:
                        opt_transaction = input('do you want to make deposit? (yes/no)')
                        if opt_transaction.lower() == 'yes' or opt_transaction.lower() == 'y':
                            while True:
                                deposit_amount = input('Enter the amount of money: ')
                                if deposit_amount.isdigit():
                                    deposit_amount = int(deposit_amount)
                                if deposit_amount >= 100000:
                                    index = database['id'].index(choise_rental_accomodation)
                                    database['booked'][index] = 'yes'
                                    database['availability'][index] = 'no'
                                    print('Deposit made successfully!')
                                    print("Change:", deposit_amount - 100000, "\nThanks, the owner will contact you sooner!")
                                    print("Current booked:")
                                    print_row_by_index(database, index)
                                    return
                                elif deposit_amount < 100000:
                                    print("\nTransaction canceled. You have insufficient funds. Please try again.")
                                    continue
                                else:
                                    print('Transaction canceled. You have insufficient funds. Please try again.')
                                    continue
                        elif opt_transaction.lower() == 'no' or opt_transaction.lower() == 'n':
                            return
                        else:
                            print('Please select yes or no')
                            continue
                elif choise_rental_accomodation in database['id'] and database['availability'][index]=='no':
                    print('Sorry, this accomodation is not available at the moment. Please try again later!')
                    break
                else:
                    print('Id of the accomodation not found. Pleasae input again!')
                    break

def manage_booked():
    print_row_by_index(database, index=None)


# Main user interface function
def user_interface():
    while True:
        print('''
            1. Show accomodation
            2. Rent accomodation
            3. Booked accomodation
            4. Exit
            ''')
        choice = input("Enter your choice: ")
        if choice == '1':
            show_accommodations()
        elif choice == '2':
            rent_accomodation()
        elif choice == '3':
            manage_booked()
        elif choice == '4':
            print('Thank you for visiting this website! Have a great day!')
            return
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

def welcoming(): 
    print('''
    
    Welcome to CheapApartment.com
    find your best accomodation!

    LOGIN TO ENTER THE PROGRAM!
    --------------------------->
    
    ''')


# MAIN PAGE
verified_welcoming = True
attempts = 0

while verified_welcoming:
    welcoming()
    input_user_login = input('Please enter your username: ')
    input_password = input('Please enter your password: ')
    
    while True:
        if input_user_login in user_database['username']:
            index = user_database['username'].index(input_user_login)
            if input_password == user_database['password'][index] and user_database['type_of_account'][index] == 'admin':
                result = admin_interface()
                if result == "exit":
                    verified_welcoming = True 
                break 
            elif input_password == user_database['password'][index] and user_database['type_of_account'][index] == 'user':
                user_interface()
                break  
            else:
                print('Invalid password. Please try again!')
                attempts += 1
                if attempts == 5:
                    verified_welcoming = False  
                    break  
            break
        else:
            print('Invalid username. Please try again!')
            attempts += 1
            if attempts == 5:
                verified_welcoming = False  
                break  
            break



