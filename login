def Login(self):
    while True:
        username = raw_input('\nPlease log in by providing your user credentials \nUser Name :')

        if (username == users[0]['username'] or username == users[1]['username']):
            password = raw_input('Password : ')
            if (password == users[0]['password'] or password == users[1]['password']):
                print('Successfully logged in!')
                print (
                'Welcome,' + username + '! Please choose of the following options by entering the corresponding menu number.')
                global LoggedUserName
                LoggedUserName = username;
                return True;
                break;
            else:
                print('Your password is not correct. Please try again!')
        else:
            print ('Your username is not correct. Please try again!')
