import time

while True:
    Username = input ("Enter Username: ")
    Password = input ("Enter Password: ")

    if Username == 'ilovepython' and Password == 'python[@#467]':
        time.sleep(1)
        print ("Login successful!")
        time.sleep(1)
        print ("-----Welcome-----")
        exit()
    else:
        print ("Worng UserName or Password")
