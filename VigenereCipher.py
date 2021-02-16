import tkinter as tk
from tkinter import scrolledtext, END

root = tk.Tk()
root['bg'] = '#111111'
root.title('Caesar 2.0')
root.geometry('750x750')
root.resizable(width=False, height=False)

alph = [
    'з', 'я', 'H', '2', 'X', 'т', '%', 'u', '?', 'v',
    'м', 'е', 'U', '1', 's', '3', 'ъ', 'Q', '/', 'и',
    '@', 'д', 'ы', 'Ж', 'f', 'g', ';', 'б', 'Z', '8',
    'Э', '~', 'N', '{', 'R', 'G', '}', 'K', 'Ф', 'n',
    'd', 'a', 'М', 'Л', 'j', '"', 'В', 'А', 'Ю', 'с',
    'B', 'w', 'ч', '$', 'ю', 'z', 'Ы', '|', 'Я', ')',
    'D', 'r', 'M', 'ш', '*', 'h', 'l', 'Ч', 'O', 'y',
    'Р', '^', 'L', 'С', 'k', '0', 'c', 'Ц', 't', 'Б',
    '[', '.', '<', 'Г', 'A', 'b', 'Ъ', 'ф', 'Т', 'W',
    '5', 'к', 'а', 'q', 'в', '>', 'Ь', 'Ё', '4', '=',
    "'", 'J', 'о', 'Н', ' ', 'З', 'п', 'н', '!', 'л',
    'Е', 'Y', '6', 'E', 'I', 'ж', 'F', 'm', 'у', '_',
    'ё', 'Ш', 'г', 'э', '+', 'К', '(', 'И', 'О', 'У',
    ':', 'х', '7', '`', 'П', '-', 'Х', 'S', 'щ', 'e',
    '&', 'p', 'V', 'o', 'Щ', 'P', 'ь', ']', '9', 'Д',
    'р', 'x', 'T', ',', '#', 'C', 'i', 'ц', '\\', 'й', 'Й'
    ]

def encrypt():
    msg = msg_text.get('1.0','end-1c')
    pas = keyword.get()
    if pas == '':
        out_text.configure(state='normal')
        out_text.delete('1.0', END)
        out_text.insert('1.0', 'Input Keyword!')
        out_text.yview(END)
    elif msg == '':
        out_text.configure(state='normal')
        out_text.delete('1.0', END)
        out_text.insert('1.0', 'Input message to encrypt!')
        out_text.yview(END)
    else:
        # msg_index = [alph.index(letter) for letter in msg if not '\n']
        msg_index = []
        for letter in msg:
            if letter != '\n':
                msg_index.append(alph.index(letter))
            else:
                msg_index.append('\n')
        pas_index = [alph.index(letter) for letter in pas]
        pas_index = pas_index * (len(msg_index)//len(pas_index) + 1)
        for i in range(0, len(msg_index)):
            if msg_index[i] != '\n':
                rot_alph = alph[pas_index[i]:] + alph[:pas_index[i]]
                msg_index[i] = rot_alph[msg_index[i]]
        result = ''.join(msg_index)
        out_text.configure(state='normal')
        out_text.delete('1.0', END)
        out_text.insert('1.0', result)
        out_text.yview(END)

def decrypt():
    msg = msg_text.get('1.0','end-1c')
    pas = keyword.get()
    if pas == '':
        out_text.configure(state='normal')
        out_text.delete('1.0', END)
        out_text.insert('1.0', 'Input Keyword!')
        out_text.yview(END)
    elif msg == '':
        out_text.configure(state='normal')
        out_text.delete('1.0', END)
        out_text.insert('1.0', 'Input message to decrypt!')
        out_text.yview(END)
    else:
        msg_list = list(msg)
        pas_index = [alph.index(letter) for letter in pas]
        pas_index = pas_index * (len(msg_list)//len(pas_index) + 1)
        decrypted = []
        for i in range(0, len(msg_list)):
            rot_alph = alph[pas_index[i]:] + alph[:pas_index[i]]
            if msg_list[i] != '\n':
                decrypted.append(rot_alph.index(msg_list[i]))
            else:
                decrypted.append('\n')
        # output = [alph[letter] for letter in decrypted if not '\n']
        output = []
        for letter in decrypted:
            if letter != '\n':
                output.append(alph[letter])
            else:
                output.append('\n')
        result = ''.join(output)
        out_text.configure(state='normal')
        out_text.delete('1.0', END)
        out_text.insert('1.0', result)
        out_text.yview(END)


frame_title = tk.Frame(root, bg='#111111')
frame_title.place(relwidth=1, relheight=0.15)
title = tk.Label(frame_title, text='Vigenere 2.0', font=('Courier', 50, 'bold'), pady=30, bg='#111111', fg='green')
title.pack()

frame_desc = tk.Frame(root, bg='#111111')
frame_desc.place(rely=0.15, relwidth=1, relheight=0.25)
desc = '  This is Vigenere 2.0 - useful tool to encrypt and decrypt messages using keyword (see the Vigenere cipher for more information).\n  To encrypt or decrypt the message input keyword and the message in according windows and press encrypt/decrypt button.'
description = tk.Label(frame_desc, text=desc, font=('Courier', 20), pady=20, bg='#111111', fg='green', wraplength=700, justify='left')
description.pack()

frame_key = tk.Frame(root, bg='#111111')
frame_key.place(rely=0.4, relwidth=0.5, relheight=0.1)
key_label = tk.Label(frame_key, text='Keyword:', font=('Courier', 20), bg='#111111', fg='green', justify='left')
key_label.pack()
keyword = tk.Entry(frame_key, font=('Courier', 20), bg='#333333', fg='green', width=27, justify='left', bd=0)
keyword.pack()

frame_enc = tk.Frame(root, bg='#111111')
frame_enc.place(rely=0.4, relx=0.5, relwidth=0.25, relheight=0.1)
enc_btn = tk.Button(frame_enc, text='Encrypt', font=('Courier', 20), fg='green', highlightbackground='#333333', width=13, height=3, command=encrypt)
enc_btn.pack()

frame_dec = tk.Frame(root, bg='#111111')
frame_dec.place(rely=0.4, relx=0.75, relwidth=0.25, relheight=0.1)
dec_btn = tk.Button(frame_dec, text='Decrypt', font=('Courier', 20), fg='green', highlightbackground='#333333', width=13, height=3, command=decrypt)
dec_btn.pack()

frame_msg = tk.Frame(root, bg='#111111')
frame_msg.place(rely=0.5, relwidth=0.5, relheight=0.5)
msg_text = scrolledtext.ScrolledText(frame_msg, font=('Courier', 14), fg='green', height=26, width=44, bg='#333333')
msg_text.pack()

frame_out = tk.Frame(root, bg='#111111')
frame_out.place(rely=0.5, relx=0.5, relwidth=0.5, relheight=0.5)
out_text = scrolledtext.ScrolledText(frame_out, font=('Courier', 14), fg='green', height=26, width=44, bg='#333333', state='disable')
out_text.pack()

root.mainloop()
