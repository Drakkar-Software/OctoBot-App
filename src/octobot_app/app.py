import threading

import toga
import os
import octobot.cli as cli
import octobot_services.constants as services_constants
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


class OctoBot(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)

        os.putenv(services_constants.ENV_AUTO_OPEN_IN_WEB_BROWSER, "false")

        x = threading.Thread(target=cli.start_background_octobot_with_args, args=())
        x.start()

        self.webview = toga.WebView(style=Pack(flex=1))
        self.url_input = toga.TextInput(
            initial='https://beeware.org/',
            style=Pack(flex=1)
        )

        box = toga.Box(
            children=[
                toga.Box(
                    children=[
                        self.url_input,
                        toga.Button('Go', on_press=self.load_page, style=Pack(width=50, padding_left=5)),
                    ],
                    style=Pack(
                        direction=ROW,
                        alignment=CENTER,
                        padding=5,
                    )
                ),
                self.webview,
            ],
            style=Pack(
                direction=COLUMN
            )
        )

        self.main_window.content = box
        self.webview.url = self.url_input.value

        # Show the main window
        self.main_window.show()

    def load_page(self, widget):
        self.webview.url = self.url_input.value


def main():
    return OctoBot()
