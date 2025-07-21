# try for install dependences and turn on modules
while True:
    try: import subprocess, time, shutil
    except ImportError: subprocess.Popen('bash dependences/dependences.sh', shell=True)
    finally:
        import subprocess, time, shutil
        break

# variables

# functions
## clear
def clear ():
    subprocess.Popen('clear', shell=True)

def menu(menu_input, menu_output):
    menu = ['Brainfuck on Python',
            '\n',
            'Full command',
            f'==- {menu_output} -==',
            'Input command',
            f'==- {menu_input} -=='
            ]
    width = shutil.get_terminal_size().columns
    height_to_center = shutil.get_terminal_size().lines//2
    position = (width - max(map(len, menu)))
    print('\n'*height_to_center)
    # format
    for line in menu:
        print(line.center(width))
    print('\n'*height_to_center)

## main function
def core ():
    clear()
    time.sleep(0.5)
    menu(1,1)

# starter
time.sleep(1.5)
core()
