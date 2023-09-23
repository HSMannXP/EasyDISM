import os

while True:
    print('Welcome to EasyDISM') # Welcome
    print('Please choose an option')
    print('1.Get-Imageinfo')
    print('2.Apply-Image')
    print('3.Mount-Image')
    print('4.Unmount-Image')
    ch = input('-> ')

    if ch == '1':
        x = input('Imagefile?(ex:E:\install.wim): ') # Get where
        os.system(f'Dism /Get-ImageInfo /imagefile:{x}') # Run commend
    elif ch == '2':
        x = input('Imagefile?(ex:E:\install.wim): ')  # Get where
        y = input('ApplyDir?(ex:E:\): ')  # Get applydir
        z = input('Index?: ') # Get index
        os.system(f'DISM.exe /Apply-Image /ImageFile:{x} /ApplyDir:{y} /Index:{z}') # Run commend
    elif ch == '3':
        x = input('Imagefile?(ex:E:\install.wim): ')  # Get where
        y = input('Index?: ')  # Get index
        z = input('MountDir?: ') # Get mountdir
        ch2 = input('If you want to mount readonly?(y,n): ')
        if ch2.lower() == 'y': # ch2 is yes
            os.system(f'DISM /Mount-image /imagefile:{x} /Index:{y} /MountDir:{z} /readonly') # Run commend
        elif ch2.lower() == 'n': # ch2 is no
            os.system(f'DISM /Mount-image /imagefile:{x} /Index:{y} /MountDir:{z}') # Run commend
        else:
            print("You didn't choose in y or n")
    elif ch == '4':
        x = input('MountDir?: ')  # Get mountdir
        ch3 = input('If you want to commit?(y,n): ')
        if ch3.lower() == 'y': # ch3 is yes
            os.system(f'Dism /Unmount-image /MountDir:{x} /Commit') # Run commend
        elif ch3.lower() == 'n': # ch3 is no
            os.system(f'Dism /Unmount-image /MountDir:{x} /discard')  # Run commend
        else:
            print("You didn't choose in y or n")