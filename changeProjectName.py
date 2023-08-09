
def main(newProjectName):
    import os
    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent

    MANAGE_PY_PATH = BASE_DIR / "manage.py"
    PROJECT_DIR_PATH = BASE_DIR / "projectName"
    ASGI_PY_PATH = BASE_DIR / PROJECT_DIR_PATH / "asgi.py"
    SETTINGS_PY_PATH = BASE_DIR / PROJECT_DIR_PATH / "settings.py"
    WSGI_PY_PATH = BASE_DIR / PROJECT_DIR_PATH / "wsgi.py"

    PATHS_HAVE_PROJECT_NAME = [
        MANAGE_PY_PATH,
        ASGI_PY_PATH,
        SETTINGS_PY_PATH,
        WSGI_PY_PATH
    ]

    FILE_CONTENTS = [

    ]

    for path in PATHS_HAVE_PROJECT_NAME:
        with open(path, "r+") as file:
            FILE_CONTENTS.append(file.readlines())

    for index, path in enumerate(PATHS_HAVE_PROJECT_NAME):
        with open(path, "w+") as file:
            for line in FILE_CONTENTS[index]:
                if "projectName" in line:
                    line = line.replace("projectName", newProjectName)
                file.write(line)

    os.rename(PROJECT_DIR_PATH, BASE_DIR / newProjectName)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        newProjectName = sys.argv[1]
        main(newProjectName)
    else:
        print("Please Enter the New Project Name")
