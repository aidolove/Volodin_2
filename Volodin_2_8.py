a = int(input())
b = int(input())
c = int(input())

if (a % 2) == 0 and (b % 2) != 0:
    print('yes')
else:
    if (a % 2) == 0 and (c % 2) != 0:
        print('yes')
    else:
        if (b % 2) == 0 and (a % 2) != 0:
            print('yes')
        else:
            if (b % 2) == 0 and (c % 2) != 0:
                print('yes')
            else:
                if (c % 2) == 0 and (a % 2) != 0:
                    print('yes')
                else:
                    if (c % 2) == 0 and (b % 2) != 0:
                        print('yes')
                    else:
                        print('no')
                                        
