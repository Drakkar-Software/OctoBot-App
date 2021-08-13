import _ctypes
import time


def fix_lipthread():
    print("fix_lipthread")
    origin_dlopen = _ctypes.dlopen

    def new_dlopen(name, flag, *args, **kwargs):
        print("new_dlopen")
        if name == "libpthread.so.0":
            print("libpthread.so.0")
            return
        return origin_dlopen(name, flag, *args, **kwargs)

    _ctypes.dlopen = new_dlopen


def main():
    import octobot.cli as cli
    from octobot_app.app import main

    # start OctoBot
    bot_process = cli.start_background_octobot_with_args(in_subprocess=True)

    # TODO : improve
    # wait until web server is up
    time.sleep(5)

    # start App
    main().main_loop()


if __name__ == '__main__':
    fix_lipthread()
    main()
