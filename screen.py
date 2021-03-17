from tkinter import Tk, Entry, Button, Label
from huffman import EncodeTable

window = Tk()
window.geometry("1000x700")
window['bg'] = 'ghost white'
window.title('Huffman Encoder')

lbl_result = Label(window, font=('Tahoma', '12'), bg='ghost white')
lbl_encoder = Label(window, font=('Tahoma', '14'), bg='ghost white')


def start(my_data):
    encoder = EncodeTable(my_data)
    lbl_result['text'] = 'Binary Code: ' + encoder.encode() + '\n'
    lbl_encoder['text'] = 'Encoding Table: ''\n' + str(encoder)


lbl_title = Label(window, text='Huffman Encoder', font=('Tahoma', '36'), bg='ghost white')
entry_text = Entry(window, font=('Tahoma', '20'), bg='sky blue')
entry_text.insert(0, 'Enter the data')
btn_cmd = Button(window, text='Encode', font=('Tahoma', '24'), command=lambda: start(entry_text.get()))

lbl_title.pack()
entry_text.pack()
btn_cmd.pack()
lbl_result.pack()
lbl_encoder.pack()

window.mainloop()
