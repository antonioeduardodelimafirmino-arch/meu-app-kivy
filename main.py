from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

# Muda a cor de fundo para um azul escuro
Window.clearcolor = (0.1, 0.1, 0.2, 1)

class app7(App):
    def build(self):
        # Muda a cor do texto para branco
        return Button(text='Meu Primeiro App!', font_size='30sp', color=(1, 1, 1, 1))

if __name__ == '__main__':
    app7().run()
