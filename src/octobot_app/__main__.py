import time


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
    main()
