#  Drakkar-Software OctoBot-App
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
from kivy.app import App
from kivy.lang import Builder

kv = '''
Button:
    text: 'Start OctoBot!'
    on_press: app.start()
'''


class ServiceApp(App):
    def build(self):
        return Builder.load_string(kv)

    def start(self):
        from octobot.cli import main
        main()


if __name__ == '__main__':
    ServiceApp().run()
