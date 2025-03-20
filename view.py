import flet as ft
from flet.core.types import MainAxisAlignment, TextAlign


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""

        def buttonClicked1(e):
            t.value = f"Dropdown changed to {self._selezionaLingua.value}"
            t.text_align=TextAlign.CENTER
            self.page.update()
        def buttonClicked2(e):
            t.value = f"Dropdown changed to {self._selezionaModalità.value}"
            t.text_align = TextAlign.LEFT
            self.page.update()

        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        t= ft.Text()

        # riga 1
        self._selezionaLingua= ft.DropdownM2(label="Select language", hint_text="Choose your language", options=[ft.dropdownm2.Option("english"),ft.dropdownm2.Option("italian"),ft.dropdownm2.Option("spanish"),],autofocus=True,width=610,
                                             on_change=buttonClicked1)
        row1= ft.Row([self._selezionaLingua])

        #riga 2
        self._selezionaModalità=ft.DropdownM2(label="Search Modality", hint_text="Choose your modality", options=[ft.dropdownm2.Option("Default"),ft.dropdownm2.Option("Linear"),ft.dropdownm2.Option("Dichotomic"),],autofocus=True,
                                              on_change=buttonClicked2)
        self._frase= ft.TextField(label="Add your sentence here")
        self._bottoneCheck= ft.ElevatedButton(text="Spell check", on_click= self.__controller.handleSpellCheck)
        row2= ft.Row([self._selezionaModalità,self._frase,self._bottoneCheck])

        #riga 3
        self._output= ft.ListView(expand=1, spacing=10, padding=10,auto_scroll=True)

        self.page.add(row1,row2,t,self._output)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()



