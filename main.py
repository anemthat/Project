from get_calendar import *
from create_events import *
from Login.login import *
import sys
print('\nWelcome To WTC Code Clinics Booking System\n')
print('\nPlease Login\n')




valid_commands = ['Book', 'Volunteer', 'Cancel_book', 'Cancel_volunteer', 'View','Help','logout']


def help_command():
    ''' this function has the info to be printed when 
    you input a commands
    '''

    # print('I can understand these commands:')
    return '''I can understand these commands:

HELP - provide information about commands
VIEW - View calendar
BOOK - Book avaiable slots
VOLUNTEER - Volunteer to help students
CANCEL BOOKING - Student to cancel booking
CANCEL VOLUNTEERING - Volunteer to cancel volunteering slot'''


while True:
    identity = input('Are you a student or Volunteer?: ').lower()
    if identity == 'student':
        print(help_command())
        break
    elif identity == 'volunteer':
        print(help_command())
        break
    else:
        continue



def check_valid_commands():

    while True:
        print(valid_commands)
        user_input = input("Enter command to continue from the valid commands?:  ")
        if user_input == valid_commands[4]:
            (generate_token())
        elif user_input == valid_commands[1]:
            print(create_volunteer())

        elif user_input == valid_commands[0]:
            email = input("Enter your email")
            print(booking(id, email))
        elif user_input == valid_commands[2]:
            print (cancel_booking(id))
        elif user_input == valid_commands[3]:
            pass
        elif user_input == valid_commands[6]:
            sys.exit("logging out")
           
        else:
            print("Please enter a valid command: ")



if __name__ == '__main__':
    
    check_valid_commands()
    delete_token()
    
