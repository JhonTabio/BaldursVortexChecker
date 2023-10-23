import os
from difflib import Differ

if __name__ == "__main__":
    mod_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Vortex\\baldursgate3\\mods"

    if not os.path.exists(mod_path):
        input(f"ERROR: Unable to locate Baldursgate3 Vortex mod folder. \nLocation={mod_path}\nPress enter to close.")
        exit()

    option = None

    while True:
        print("Please choose one of the following options\n")
        option = input("[G] Generate\n[C] Compare\n[O] Open Folder\n[I] Instructions\n[X] Exit\nInput: ").lower()[0]

        if option == 'x':
            break
        elif option == 'g':
            with open(mod_path + "\\version_checker.txt", 'w+') as f:
                mod_list = os.listdir(mod_path)

                for mod in mod_list:
                        f.write(mod + '\n')
                
                print("Successfully generated the file.")
        elif option == 'c':
            with open(mod_path + "\\version_checker.txt", 'r') as f1, open(os.path.expanduser("~") + "\\Downloads\\version_checker.txt", 'r') as f2, open(os.path.expanduser("~") + "\\Downloads\\output.txt", 'w+') as f3:
                differ = Differ()

                for line in differ.compare(f2.readlines(), f1.readlines()):
                    if line[0] == '+' or line[0] == '-' or line[0] == '?':
                        print(line)
                        f3.write(line + '\n')

        elif option == 'o':
            os.startfile(mod_path)
            print("Opened mods folder.\n\n")
        
        elif option == 'i':
            print("----------- HOW TO USE -----------")
            print("Terms: [LOCALFILE, HOSTFILE]")
            print("LOCALFILE - Your current list of mods, this file should be located within your mods folder")
            print("HOSTFILE - The list of mods you *want to replicate*, this is located in the downloads folder")
            print("\nIf you are going to host a lobby, you should generate and send your 'version_checker.txt' file to everyone else")
            print("The sent file will be the other's HOSTFILE")
            print("Do not move the files out their respective folders!")
            print("Ensure to have generated a file prior to doing anything else!")
            print("\nWhen comparing, this will generate an 'output.txt' file in the downloads folder")
            print("The content of the file is simple:")
            print("\t'+' - A mod that needs an update / to be downloaded")
            print("\t'-' - A mod that should be removed")
            print("----------- HOW TO USE -----------")
            input("Press enter when done reading")