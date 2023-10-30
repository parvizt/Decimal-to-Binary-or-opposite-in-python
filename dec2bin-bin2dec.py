from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BinaryDecimalConverterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.binary_input = TextInput(hint_text='Enter binary number')
        self.decimal_output = TextInput(hint_text='Decimal result')
        self.convert_button = Button(text='Convert to Decimal', on_press=self.convert_to_decimal)
        self.convert_to_binary_button = Button(text='Convert to Binary', on_press=self.convert)

        layout.add_widget(self.binary_input)
        layout.add_widget(self.decimal_output)
        layout.add_widget(self.convert_button)
        layout.add_widget(self.convert_to_binary_button)
        return layout

    def convert_to_decimal(self, instance):
        binary_input = self.binary_input.text.strip()
        if binary_input:
            try:
                decimal_output = str(int(binary_input, 2))
                self.decimal_output.text = 'Decimal result: ' + decimal_output
            except ValueError:
                self.decimal_output.text = 'Invalid binary input'
        else:
            self.decimal_output.text = 'Enter a binary number first'

    def convert(self, instance):
        decimal_input = self.decimal_output.text.strip()
        if decimal_input:
            try:
                decimal_input = int(decimal_input)
                binary_output = bin(decimal_input)[2:]
                self.binary_input.text = binary_output
            except ValueError:
                self.binary_input.text = 'Invalid decimal input'
        else:
            self.binary_input.text = 'Enter a decimal number first'

if __name__ == '__main__':
    BinaryDecimalConverterApp().run()
