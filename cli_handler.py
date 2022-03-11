import os


def run_command(my_command, output_lbl):
    split_cmd = my_command.split(" ")
    print(my_command)
    print(split_cmd)
    os.system(f'gnome-terminal -- bash -c "{my_command}; exec bash"')
    output_lbl.configure(text="Command was run")
