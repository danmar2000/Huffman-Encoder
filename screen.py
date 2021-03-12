from tkinter import Tk, Entry, Button, Label
from huffman import *

window = Tk()
window.geometry("1000x700")
window['bg'] = 'ghost white'
window.title('Huffman Encoder')

lbl_result = Label(window, font=('Tahoma', '12'), bg='ghost white')
lbl_encoder = Label(window, font=('Tahoma', '14'), bg='ghost white')


def start_huffman(my_data):
    lbl_result['text'] = 'Binary Code: '+huffman(my_data) + '\n'
    lbl_encoder['text'] = 'Encoding Table: ''\n'+encoder2txt(create_encode_table(my_data, create_priority_list(my_data, create_freq_table(my_data))))


lbl_title = Label(window, text='Huffman Encoder', font=('Tahoma', '36'), bg='ghost white')
entry_text = Entry(window, font=('Tahoma', '24'), bg='sky blue')
entry_text.insert(0, 'Enter the data')
btn_cmd = Button(window, text='Encode', font=('Tahoma', '24'), command=lambda: start_huffman(entry_text.get()))

lbl_title.pack()
entry_text.pack()
btn_cmd.pack()
lbl_result.pack()
lbl_encoder.pack()

window.mainloop()
