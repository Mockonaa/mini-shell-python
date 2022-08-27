# Mini Shell in Python


import command_parser as com_par
import application as app
import installer as app_inst
from random import *
from time import *
import importlib


release_info = "Simple Python Shell"
release_ver = "v0.1b"
command = None
builtin_command = ["echo", "version", "exit", "app_list", "help", "app-manager"]
extern_command = []


def app_reload():
    global extern_command
    print("Reloading Apps...")
    extern_command = app.load_config()
    print("Successfully Loaded " + str(len(extern_command)) + " Apps!")


def shell_startup():
    global extern_command
    print(release_info, release_ver, "Shell Initialization started!")
    print("Searching for installed Applications...")
    sleep(1)
    found = app.load_config()
    print(len(found), "Apps found!")
    extern_command = app.load_config()
    print("Loading Apps...")
    sleep(2)
    print("Apps Successfully loaded!")
    print("Shell Initialization finished!")
    sleep(1)
    shell()


def shell():
    global command
    global extern_command
    while True:
        command = str(input(">> "))
        base_command = com_par.get_command(command)
        if base_command in builtin_command:
            if base_command == "echo":
                command_arg = com_par.get_argument(command)
                print(command_arg)
            elif base_command == "version":
                print(release_info, release_ver)
            elif base_command == "app_list":
                print("List of Installed Apps:")
                print(*extern_command, sep="\n")
            elif base_command == "help":
                print("List of Built-in Apps:")
                print(*builtin_command, sep="\n")
            elif base_command == "exit":
                print("Goodbye o/")
                break
            elif base_command == "app-manager":
                command_arg = com_par.get_multiple_arg(command)
                if command_arg == 15:
                    print("app-manager Help file")
                    print("Available Arguments:")
                    print("install *name*   - install an app named *name*")
                    print("uninstall *name* - uninstall an app named *name*")
                    print("reload           - reload apps from config")
                    print("help             - Show this message")
                elif command_arg[0] == "install":
                    res = app_inst.install_app(command_arg[1])
                    if res == 42:
                        app_reload()
                elif command_arg[0] == "uninstall":
                    print("Not Implemented Yet.")
                    print("Please Remove manually the App from")
                    print("installed_app.cfg and reload")
                    print("with 'app-manager reload'")
                elif command_arg[0] == "reload":
                    app_reload()
                else:
                    print("app-manager Help file")
                    print("Available Arguments:")
                    print("install *name*   - install an app named *name*")
                    print("uninstall *name* - uninstall an app named *name*")
                    print("reload           - reload apps from config")
                    print("help             - Show this message")

        if base_command in extern_command:

            execution_temp = randint(111111, 999999)
            execution_temp2 = "exec_" + str(execution_temp)
            execution_data = ["from apps." + base_command + " import main", "import os", "main()",
                              "os.remove('" + execution_temp2 + ".py')"]
            execution_file = open(execution_temp2 + ".py", "w")
            for k in execution_data:
                execution_file.writelines(k)
                execution_file.writelines("\n")
            execution_file.close()
            importlib.import_module(execution_temp2)


shell_startup()
