import commands as commands
import config as conf
import os

def command_processor(command, arguments):
    command                     = command.split("|")
    syntax                      = command[0]
    number_of_arguments         = command[1]
    event                       = "commands." + command[2]
    ###################################################
    if conf.clear_console_on_exec == True:
        os.system('cls' if os.name=='nt' else 'clear')

    try:
        exec(event)
    except:
        print(f"Err {event}")