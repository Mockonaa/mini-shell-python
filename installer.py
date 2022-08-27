import importlib


def install_app(app_name):
    try:
        importlib.import_module("apps." + app_name)
    except ImportError:
        print("Application Package not Found.")
        return 14
    else:
        cfg = open("installed_app.cfg", "a")
        cfg.write(app_name + "\n")
        cfg.close()
        return 42
