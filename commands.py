import config as conf

def name(name):
    return print(f"Name: {name}")

def sum(number_one, number_two):
    return print(f"Sum {number_one} + {number_two} = {int(number_one) + int(number_two)}")

# SYSTEM DEF #
def exit_system():
    print("The system is shutting down now..")
    conf.actived = False

def command_list():
    if len(commands) != 0:
        print(f"Command / Shortcut")
        for key in commands.keys():
            for _key, _item in commands_shortcut.items():
                if _item == key:
                    print(f"{key} / {_key}")
                    break
            if _item != key:
                print(f"{key} / No shortcut")
    else:
        print(f"There are no commands yet.")

commands = {
    "!exit": "!exit|0|exit_system()",
    "!commands": "!commands|0|command_list()",
    "@name": "@name <name>|1|name(arguments[0])",
    "@sum": "@sum <number_one> <number_two>|2|sum(arguments[0], arguments[1])"
}

commands_shortcut = {
    "!cmds": "!commands",
    "@n": "@name"
}