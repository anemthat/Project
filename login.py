from tkinter import *
from functools import partial

print('\nWelcome To WTC Code Clinics Booking System\n')
print('\nPlease Login\n')

SpecialSym =['$', '@', '#', '%', '.', '!', '?', '_' , '+', '-']
val = True 
def validateLogin(username, password):
	global val, SpecialSym
		
		
	print('Welcome: ', username.get())

	if'@student.wethinkcode.co.za' not in username.get():
		print ('enter the username again')

	if len(password.get()) < 8:
		print('Length should be at least 8 characters')
		val = False
		
	elif len(password.get()) > 20:
		print('length should be not be greater than 20 characters')
		val = False
		
	elif not any(char.isdigit() for char in password.get()):
		print('Password should have at least one digit')
		val = False
		
	elif not any(char.isupper() for char in password.get()):
		print('Password should have at least one uppercase letter')
		val = False
		
	elif not any(char.islower() for char in password.get()):
		print('Password should have at least one lowercase letter')
		val = False
		
	elif not any(char in SpecialSym for char in password.get()):
		print('Password should have at least one of the symbols $@#.!?')
		val = False
	else:
		print('User logged in successfully')
	return



#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  


validateLogin = partial(validateLogin, username, password)


#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0) 



tkWindow.mainloop()


