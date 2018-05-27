"""Arquivo popup."""
import tkinter as tk
from tkinter import (Label, Button, TOP)


def msg_erro(mensagem):
    """Popup de mensagens de erro."""
    popup = tk.Tk()
    popup.wm_title('Erro')
    lb_erro = Label(popup, text=mensagem, width=40, height=10)
    lb_erro.pack(side=TOP)
    bt_ok = Button(popup, text='OK', command=popup.destroy, width=10)
    bt_ok.pack(side=TOP)
    popup.mainloop
