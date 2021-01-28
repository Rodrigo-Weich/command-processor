from processor import command_processor
from commands import commands, commands_shortcut
import config as conf

def command_init(str):
    for i in range(len(conf.symbols)):
        if str[:1] == list(conf.symbols.items())[i][1]:

            str = str.split()
            if len(str) > 0:
                command_arguments = str
                command = str.pop(0)

            if commands.__contains__(command) or commands_shortcut.__contains__(command):
                if command in commands:
                    if len(str) < int(commands.get(command).split("|")[1]):
                        print(f"The syntax of the command {command} is wrong, please try using {commands.get(command).split('|')[0]}")
                    else:
                        command_processor(commands.get(command), command_arguments)
                elif command in commands_shortcut:
                    if len(str) < int(commands.get(commands_shortcut.get(command)).split("|")[1]):
                        print(f"The syntax of the command {command} is wrong, please try using {commands.get(commands_shortcut.get(command)).split('|')[0]}")
                    else:
                        command_processor(commands.get(commands_shortcut.get(command)), command_arguments)
            else:
                print(f"The command {command} doesn't exists.")

while conf.actived == True:
    command_init(input("Command: ").lower())