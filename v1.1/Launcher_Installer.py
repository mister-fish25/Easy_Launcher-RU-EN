import minecraft_launcher_lib as mll
import subprocess
import json
import os
import time

lang_path = "./data/lang.json"
minecraft_path = "./data/minecraft_path.json"
java_path = ""

def Change_JAVA(version):
    first_version = str(version).replace(".", "")
    print(first_version)
    need_version = float(first_version[1:])
    print(need_version)
    global java_path
    if need_version <= 16.5:
        with open(minecraft_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            java_path = data["path2"] + str("\\jre-legacy\\windows-x64\\jre-legacy\\bin\\java.exe")
    elif need_version > 16.5 and need_version < 20.5:
        with open(minecraft_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            java_path = data["path2"] + str("\\java-runtime-delta\\windows-x64\\java-runtime-delta\\bin\\java.exe")
    elif need_version >= 20.5:
        with open(minecraft_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            java_path = data["path2"] + str("\\java-runtime-alpha\\windows-x64\\java-runtime-alpha\\bin\\java.exe")

# C:\\Users\\<username>\\Documents\\mine
def Install_Minecraft(version, path):
    mll.install.install_minecraft_version(version=version, minecraft_directory=path, callback={"setProgress":lambda e: print(e)})

def Run_Minecraft(version, path, nickname):
    Change_JAVA(version)
    time.sleep(1)
    options = {
        "username": nickname,
        "jvmArguments": [
            "-javaagent:./data/authlib-injector.jar=ely.by"
        ],
        "executablePath": f"{java_path}"
    }
    command = mll.command.get_minecraft_command(version=version, minecraft_directory=path, options=options)
    subprocess.run(command)


with open(lang_path, "r", encoding="utf-8") as file:
    data = json.load(file)
    if data["lang"] == "RU":
        print("1 -- Установить версию\n2 -- Запустить Майнкрафт\n3 -- Просмотреть доступные версии")
        V1 = int(input("Ваш выбор:\n"))
        if V1 == 1:
            with open(minecraft_path, "r", encoding="utf-8") as file2:
                data2 = json.load(file2)
                print(f"Путь до папки Майнкрафта -- {data2["path"]}")
                print("Введите версию для установки")
                version_minecraft = str(input())
                Install_Minecraft(version_minecraft, data2["path"])
        elif V1 == 2:
            with open(minecraft_path, "r", encoding="utf-8") as file2:
                data2 = json.load(file2)
                print(f"Путь до папки Майнкрафта -- {data2["path"]}")
                print("Введите версию для запуска")
                version_minecraft = str(input())
                print("Введите свой никнейм")
                nickname = str(input())
                Run_Minecraft(version_minecraft, data2["path"], nickname)
        elif V1 == 3:
            with open(minecraft_path, "r", encoding="utf-8") as file2:
                data2 = json.load(file2)
                path_to_folder = (data2["path"] + "\\versions")
                all_items = os.listdir(path_to_folder)
                folders = [item for item in all_items if os.path.isdir(os.path.join(path_to_folder, item))]
                print(folders)
    elif data["lang"] == "EN":
        print("1 -- Install version\n2 -- Run Minecraft\n3 -- View available versions")
        V1 = int(input("Your choice:\n"))
        if V1 == 1:
            with open(minecraft_path, "r", encoding="utf-8") as file2:
                data2 = json.load(file2)
                print(f"Path to the Minecraft folder -- {data2["path"]}")
                print("Enter the version to install")
                version_minecraft = str(input())
                Install_Minecraft(version_minecraft, data2["path"])
        elif V1 == 2:
            with open(minecraft_path, "r", encoding="utf-8") as file2:
                data2 = json.load(file2)
                print(f"Path to the Minecraft folder -- {data2["path"]}")
                print("Enter the version to run")
                version_minecraft = str(input())
                print("Enter your nickname")
                nickname = str(input())
                Run_Minecraft(version_minecraft, data2["path"], nickname)
        elif V1 == 3:
            with open(minecraft_path, "r", encoding="utf-8") as file2:
                data2 = json.load(file2)
                path_to_folder = (data2["path"] + "\\versions")
                all_items = os.listdir(path_to_folder)
                folders = [item for item in all_items if os.path.isdir(os.path.join(path_to_folder, item))]
                print(folders)