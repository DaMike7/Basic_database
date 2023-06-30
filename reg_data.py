import random
def Data(Administration):
    #Head
    #a loop to authenticate user
    head = True
    while head:
        username = input('\nenter username '.upper())
        if username == '':
            print('\ninvalid')

        elif username == Administration.USERNAME():
            print('\nAlmost there!')
            
            for b in range(1):
                try:
                    otp = random.randint(3421,9765)
                    verify = int(input(f'\nyour otp is \'{otp}\'\n\tenter otp to proceed '.upper()))
                    if verify == otp:
                        print('Welcome Admin !')
                        change = input('\nenter \'c\' to change default username or enter any key to continue '.title()).upper()

                        if change == '':
                            pass

                        elif change == 'C':
                            print('\nokay')
                            Administration.change_username()
                            Data(Administration)
                            
                    else:
                        Data.head()

                except:
                    print('\ninvalid')
                    head = True
                else:
                    head = False

        else:
            print('\nincorrect')
    
    #body
    body1 = True
    while body1:
        sfn = input('\nenter student\'s full name\n'.upper()).title() #sfn = student's full name
        if sfn == '':
            print('\n*empty')

        elif ' ' in sfn:
            body1 = False

        else:
            print('*enter full name')

    body2 = True
    while body2:
        try:
            sa = int(input('\nenter student\'s age '.upper())) #sa = students age
            if sa == '':
                print('*\nempty')
            else:
                body2 = False

        except:
            print('*digits only')
            body2 = True
        else:
            body3 = True
            while body3:
                ci = input('\nstudent email address or phone number\n'.upper()) #contact info
                if ci == '':
                    print('\n*empty')
                elif ci .endswith('@gmail.com') or len(ci) == 11:
                    body3 = False
                    print('\nsaving info....')
                    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    lenght = 2
                    num = random.randint(202312,202398)
                    letters = ''.join(random.sample(upper_case,lenght))
                    reg_no = f'{num}{letters}'
                    print(f'{sfn}\'s registration number is {reg_no}')

                else:
                    print('invalid input')

    data_dic = {
            'REGISTRATION NUMBER':reg_no,
            'STUDENT\'S FULL NAME':sfn,
            'STUDENT\'S AGE':sa,
            'STUDENT CONTACT INFO':ci
            }

    Access['Names'] = sfn
    student_file = f'{sfn}.txt'
    with open(student_file,'w') as f:
        for k,v in data_dic.items():
            f.write(f'{k} : {v}\n')

    
    Again = input('\n\nenter \'a\' to enter another data ')
    if Again == 'a':
        Data.body1()

    else:
        print('\n\nsaved data\n'.upper())
        with open(saved_data,'a') as sd:
            for s in Access.values():
                sd.write(f'{s}\n')

        with open(saved_data) as s:
            read = s.read()
        print('Names\n')
        print(read)

        open_file = True
        while open_file:
            choice = input('\nenter a file name to be opened ')
            try:
                print('\nprocessing...\n')
                with open(f'{choice}.txt') as c:
                    OPEN = c.read()
                print(OPEN)
                if choice == 'q':
                    exit()

            except FileNotFoundError:
                print(f'\n*{choice}.txt not found! or invalid input\nenter \'q\' to quit'.title())


class Setting:
    def __init__(self,admin_username):
        self.admin_username = admin_username

    def USERNAME(self):
        name =f'{self.admin_username}'
        return name

    def change_username(self):
    #a method to change username'
        change = True
        while change:
            new_username = input('\nenter new username\n'.title())
            if len(new_username) >= 8:
                self.admin_username = new_username
                change = False
                print('*Username changed !')

            else:
                print('\n*lenght of new username must be greater than 7')

saved_data = 'saved_data.txt'
Access = {}
Administration = Setting('Admin')
Data(Administration)
