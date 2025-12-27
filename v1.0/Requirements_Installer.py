import json
import sys
import subprocess


lang_path = "./data/lang.json"
requirements_path = "./requirements.txt"


def Install_Requirements(lang):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
        if lang == "RU":
            print("Зависимости успешно установлены.")
        elif lang == "EN":
            print("Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        if lang == "RU":
            print(f"Ошибка при установке: {e}")
        elif lang == "EN":
            print(f"Installation error: {e}")


def Change_Language():
    print("1 -- RU\n2 -- EN")

    Language = int(input("Select language\n"))
    if Language == 1:
        print("Вы выбрали русский язык")
        with open(lang_path, "w", encoding='utf-8') as file:
            python_data = {
                "lang": "RU"
            }
            json.dump(python_data, file, ensure_ascii=False, indent=4)
            Install_Requirements("RU")

    elif Language == 2:
        print("You have chosen English")
        with open(lang_path, "w", encoding='utf-8') as file:
            python_data = {
                "lang": "EN"
            }
            json.dump(python_data, file, ensure_ascii=False, indent=4)
            Install_Requirements("EN")
    else:
        print("Error")


with open(lang_path, "r", encoding="utf-8") as file:
    data = json.load(file)
    if data["lang"] == "RU":
        Install_Requirements("RU")
    elif data["lang"] == "EN":
        Install_Requirements("EN")
    else:
        Change_Language()