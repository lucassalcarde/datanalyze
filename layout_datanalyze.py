"""Layout do programa."""
import bd
from msgerro import msg_erro
import tkinter as tk
from tkinter import (TOP, RIGHT, LEFT, RAISED, FLAT, SUNKEN, X, W)
from tkinter import (PhotoImage, Button, Label, Entry, IntVar, Radiobutton)
from tkinter import *  #NOQA
from tkinter.filedialog import askopenfilename

cdados = bd.Entrada()


class Aplicacao(tk.Frame):
    """Classe do layout."""

    def __init__(self, master=None):
        """Função inicializadora."""
        tk.Frame.__init__(self, master, bd=2)
        self.Corpo_Menu()
        self.Tela_inicial()
        self.toolbar_abrirtotal = ''

    def Corpo_Menu(self):
        """Função do Menu."""
        '''self.menubar = tk.Menu(self)
        filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Dados', menu=filemenu)
        filemenu.add_command(label='Projetar')

        filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Variaveis', menu=filemenu)
        filemenu.add_command(label='Arrumar Variaveis')

        filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add()
        filemenu.add_command(label='Sair')

        self.master.config(menu=self.menubar)'''

        toolbar = tk.Frame(self.master, bd=1, relief=RAISED)

        img_abrir = PhotoImage(file=r'imagens\abrir.png')
        bt_abrir = Button(toolbar, image=img_abrir, relief=FLAT,
                          command=self.bt_abrir_click)
        bt_abrir.image = img_abrir
        bt_abrir.pack(side=LEFT, padx=2, pady=2)

        img_projecao = PhotoImage(file=r'imagens\projecao.png')
        bt_projecao = Button(toolbar, relief=FLAT, image=img_projecao,
                             command=self.finaliza_frame)
        bt_projecao.image = img_projecao
        bt_projecao.pack(side=LEFT, padx=2, pady=2)

        bt_variaveis = Button(toolbar, relief=FLAT, image=img_projecao)
        bt_variaveis.image = img_projecao
        bt_variaveis.pack(side=LEFT, padx=2, pady=2)

        img_sair = PhotoImage(file=r'imagens\sair.png')
        btsair = Button(toolbar, image=img_sair, relief=FLAT,
                        command=self.quit)
        btsair.image = img_sair
        btsair.pack(side=RIGHT, padx=2, pady=2)
        toolbar.pack(side=TOP, fill=X)
        self.pack()

    def Tela_inicial(self):
        """Corpo da tela inicial."""
        self.lb_status = Label(root, bg='black', fg='white', pady=1,
                               text='Nenhum Banco de Dados Aberto',
                               width=w, height=3, font=('Verdana', 10, 'bold'),
                               borderwidth=10, relief=SUNKEN)
        self.lb_status.pack()

    def finaliza_frame(self):
        """Destroi frame ativo quando abre um novo."""
        self.toolbar_abrirtotal.destroy()

    '''def msg_erro(self):
        """Popup de mensagens de erro."""
        popup = tk.Tk()
        popup.wm_title('Erro')
        lb_erro = Label(popup, text=self.mensagem, width=40, height=10)
        lb_erro.pack(side=TOP)
        bt_ok = Button(popup, text='OK', command=popup.destroy, width=10)
        bt_ok.pack(side=TOP)
        popup.mainloop'''

    def bt_abrir_click(self):
        """Função botão abrir."""
        if self.toolbar_abrirtotal:
            self.finaliza_frame()

        def abrir_pasta():
            servidor = r'\\SERVIDOR\salvar aqui\PESQUISAS'
            filetypes = (("xls files", "*.xls"), ("xlsx files", "*.xlsx"))
            root.filedialog = askopenfilename(initialdir=servidor,
                                              title="Selecione o Arquivo",
                                              filetypes=filetypes)
            ed_nome.insert(0, str(root.filedialog))

        def abrir_banco_click():
            """Abertura de campo e limpeza(exclui treinamento e vazias)."""
            nomedigitado = ed_nome.get().strip()
            print(nomedigitado)
            estado = self.rb_projecao.get()
            qt_projecao = ed_val_projecao.get().strip()
            if nomedigitado:
                if qt_projecao and str.isnumeric(qt_projecao):
                    self.mensagem, *listabd = cdados.abrir_banco(
                                                  banco_excel=nomedigitado,
                                                  op=estado,
                                                  projecao=qt_projecao)
                    if listabd:
                        msg_erro(listabd)
                        self.banco = listabd[0]
                        self.nome_pla = listabd[1]
                        self.projetado = listabd[2]  # arrumar dados já constam aqui
                        self.pesq_campo = listabd[3]
                    else:
                        msg_erro(self.mensagem)
                else:
                    self.mensagem = 'Valor projeção invalido'
                    msg_erro(self.mensagem)
            else:
                self.mensagem = 'Nome de arquivo vazio'
                msg_erro(self.mensagem)

        # banco, nome_pla, projetado, pesq_campo = bd.abrir_banco()
        # self.lb_status['text'] = f'{nome_pla}\n{projetado} {pesq_campo}'
        self.toolbar_abrirtotal = tk.Frame(self.master, bd=1, relief=RAISED)
        toolbaralinha = tk.Frame(self.toolbar_abrirtotal, bd=1, relief=FLAT)
        toolbar_abrir = tk.Frame(toolbaralinha, bd=1, relief=FLAT)
        modelo = r'Digite nome do arquivo igual o modelo ' \
                 r'\2018\MAIO\SÃO PAULO\SÃO PAULO.xls'
        lb_nome = Label(toolbar_abrir, text=modelo, anchor=W)
        lb_nome.pack(side=TOP, padx=2, pady=12)
        ed_nome = Entry(toolbar_abrir, width=60)
        ed_nome.pack(side=LEFT, padx=2, pady=12)
        img_abrir = PhotoImage(file=r'imagens\abrir-menor.png')
        bt_abrir = Button(toolbar_abrir, image=img_abrir, relief=FLAT,
                          command=abrir_pasta)
        bt_abrir.image = img_abrir
        bt_abrir.pack(side=LEFT, pady=12)
        toolbar_abrir.pack(side=LEFT)

        toolbar_projecao = tk.Frame(toolbaralinha, bd=1, relief=FLAT)
        lb_projecao = Label(toolbar_projecao,
                            text='Arquivo Já está projetado?')
        lb_projecao.pack(side=TOP, padx=2, pady=2)
        self.rb_projecao = IntVar()
        self.rb_projecao.set(0)
        Radiobutton(toolbar_projecao, text='Não Projetado', value=0,
                    variable=self.rb_projecao).pack(anchor=W)
        Radiobutton(toolbar_projecao, text='Projetado', value=1,
                    variable=self.rb_projecao).pack(anchor=W)
        toolbar_projecao.pack(side=LEFT, padx=50)

        toolbar_val_projecao = tk.Frame(toolbaralinha, bd=1,
                                        relief=FLAT)
        lb_val_projecao = Label(toolbar_val_projecao, text='Valor Projeção')
        lb_val_projecao.pack(side=TOP, ipadx=2, pady=13)
        ed_val_projecao = Entry(toolbar_val_projecao, width=20)
        ed_val_projecao.pack(side=TOP, padx=2, pady=13)
        toolbar_val_projecao.pack(side=LEFT)
        toolbaralinha.pack(side=TOP)
        bt_abrirbanco = Button(self.toolbar_abrirtotal, text='ABRIR',
                               command=abrir_banco_click)
        bt_abrirbanco.pack(side=TOP)
        self.toolbar_abrirtotal.pack(side=TOP)

        self.pack()


root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f'{w}x{h}+0+0')
root.title('Datanalyze')
app = Aplicacao(root)
app.mainloop()
