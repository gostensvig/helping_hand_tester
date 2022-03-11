import os


def run_command(my_command):
    split_cmd = my_command.split(" ")
    print(my_command)
    print(split_cmd)
    os.system(f'gnome-terminal -- bash -c "{my_command}; exec bash"')
