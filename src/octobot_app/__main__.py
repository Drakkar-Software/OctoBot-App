import time

import octobot.cli as cli
from octobot_app.app import main

if __name__ == '__main__':
    # start OctoBot
    bot_process = cli.start_background_octobot_with_args(in_subprocess=True)

    # TODO : improve
    # wait until web server is up
    time.sleep(5)

    # start App
    main().main_loop()
