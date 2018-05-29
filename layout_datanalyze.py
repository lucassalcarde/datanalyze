"""Layout do programa."""
import bd
from msgerro import msg_erro
import datanalyze
import os.path
import tkinter as tk
from tkinter import (TOP, RIGHT, LEFT, RAISED, FLAT, SUNKEN, X, W, Y)
from tkinter import (PhotoImage, Button, Label, Entry, IntVar, Radiobutton,
                     Scrollbar, Text, INSERT, DISABLED)
from tkinter import *  #NOQA
from tkinter.filedialog import askopenfilename

cdados = bd.Entrada()
trabdados = datanalyze.Trabalhando_dados()


class Aplicacao(tk.Frame):
    """Classe do layout."""

    def __init__(self, master=None):
        """Função inicializadora."""
        tk.Frame.__init__(self, master, bd=2)
        self.Corpo_Menu()
        self.Tela_inicial()
        self.toolbar_abrirtotal = ''
        self.caminho = ''
        self.banco = ''
        self.projetado = ''

    def Corpo_Menu(self):
        """Função do Menu."""
        toolbar = tk.Frame(self.master, bd=1, relief=RAISED)

        img_abrir = PhotoImage(file=r'imagens\abrir.png')
        bt_abrir = Button(toolbar, image=img_abrir, relief=FLAT,
                          command=self.bt_abrir_click)
        bt_abrir.image = img_abrir
        bt_abrir.pack(side=LEFT, padx=2, pady=2)

        img_projecao = PhotoImage(file=r'imagens\projecao.png')
        self.bt_projecao = Button(toolbar, relief=FLAT, image=img_projecao,
                                  command=self.bt_projecao_click,
                                  state=DISABLED)
        self.bt_projecao.image = img_projecao
        self.bt_projecao.pack(side=LEFT, padx=2, pady=2)

        self.bt_variaveis = Button(toolbar, relief=FLAT, image=img_projecao,
                                   state=DISABLED)
        self.bt_variaveis.image = img_projecao
        self.bt_variaveis.pack(side=LEFT, padx=2, pady=2)

        img_sair = PhotoImage(file=r'imagens\sair.png')
        btsair = Button(toolbar, image=img_sair, relief=FLAT,
                        command=self.quit)
        btsair.image = img_sair
        btsair.pack(side=RIGHT, padx=2, pady=2)
        toolbar.pack(side=TOP, fill=X)
        self.pack()

    def Tela_inicial(self):
        """Corpo da tela inicial."""
        self.lb_status = Label(root, bg='black', fg='white', pady=1, padx=1,
                               text='Nenhum Banco de Dados Aberto',
                               width=w, height=1, font=('Verdana', 10, 'bold'),
                               borderwidth=10, relief=SUNKEN)
        self.lb_status.pack()
        self.lb_statusqt = Label(root, bg='black', fg='white', pady=1, padx=1,
                                 width=w, height=1,
                                 font=('Verdana', 10, 'bold'),
                                 borderwidth=10, relief=SUNKEN)
        self.lb_statusqt.pack()

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

    def abrir_pasta(self):
        """função escolher caminho."""
        servidor = r'//SERVIDOR/salvar aqui/PESQUISAS'
        filetypes = (("xls files", "*.xls"), ("xlsx files", "*.xlsx"))
        root.filedialog = askopenfilename(initialdir=servidor,
                                          title="Selecione o Arquivo",
                                          filetypes=filetypes)
        if self.ed_nome.winfo_exists():
            self.ed_nome.insert(0, str(root.filedialog))
        elif self.ed_dist.winfo_exists():
            self.ed_dist.insert(0, str(root.filedialog))

    def bt_abrir_click(self):
        """Função botão abrir."""
        if self.toolbar_abrirtotal:
            self.finaliza_frame()

        def abrir_banco_click():
            """Abertura de campo e limpeza(exclui treinamento e vazias)."""
            nomedigitado = self.ed_nome.get().strip()
            estado = self.rb_projecao.get()
            qt_projecao = ed_val_projecao.get().strip()
            if nomedigitado:
                if qt_projecao and str.isnumeric(qt_projecao):
                    self.mensagem, *listabd = cdados.abrir_banco(
                                                  banco_excel=nomedigitado,
                                                  op=estado,
                                                  projecao=qt_projecao)
                    if listabd:
                        self.banco = listabd[0]
                        self.nome_pla = listabd[1]
                        listcaminho = self.nome_pla.split('/')
                        del listcaminho[-1]
                        self.caminho = '/'.join(listcaminho)
                        self.projetado = str(listabd[2])
                        self.pesq_campo = str(listabd[3])
                        self.lb_status['text'] = self.nome_pla

                        self.lb_statusqt['text'] = 'Qt Campo: ' + \
                            self.pesq_campo + '     Qt Projetado: ' + \
                            self.projetado
                        self.bt_projecao['state'] = 'normal'
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
        self.toolbar_abrirtotal = tk.Frame(self.master, bd=1, relief=FLAT)
        toolbaralinha = tk.Frame(self.toolbar_abrirtotal, bd=1, relief=FLAT)
        toolbar_abrir = tk.Frame(toolbaralinha, bd=1, relief=FLAT)
        modelo = r'Digite nome do arquivo igual o modelo ' \
                 r'/2018/MAIO/SÃO PAULO/SÃO PAULO.xls'
        lb_nome = Label(toolbar_abrir, text=modelo, anchor=W)
        lb_nome.pack(side=TOP, padx=2, pady=12)
        self.ed_nome = Entry(toolbar_abrir, width=60)
        self.ed_nome.pack(side=LEFT, padx=2, pady=12)
        img_abrir = PhotoImage(file=r'imagens\abrir-menor.png')
        bt_abrir = Button(toolbar_abrir, image=img_abrir, relief=FLAT,
                          command=self.abrir_pasta)
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

    def bt_projecao_click(self):
        """Click botao projecao."""
        '''def abrir_pasta():
            servidor = r'//SERVIDOR/salvar aqui/PESQUISAS'
            filetypes = (("xls files", "*.xls"), ("xlsx files", "*.xlsx"))
            root.filedialog = askopenfilename(initialdir=servidor,
                                              title="Selecione o Arquivo",
                                              filetypes=filetypes)
            ed_dist.insert(0, str(root.filedialog))'''

        def bt_projetar_click():
            dist = self.ed_dist.get().strip()
            if self.caminho:
                nome_planilha = self.caminho + '/' + ed_nomepla.get().strip()
            else:
                nome_planilha = ed_nomepla.get().strip()
            if dist:
                if os.path.isfile(dist):  # verifica se existe arquivo
                    if ed_nomepla.get():
                        self.mensagem, *listapj = trabdados.projecao_pesquisa(
                                                      self.banco,
                                                      self.projetado,
                                                      dist, nome_planilha)
                        if listapj:
                            for l in listapj[0]:
                                tx_log.insert(INSERT, l + '\n\n')
                            self.banco = listapj[1]
                            self.lb_status['text'] = nome_planilha
                            self.bt_variaveis['state'] = 'normal'
                            bt_projetar['state'] = DISABLED
                        else:
                            msg_erro(self.mensagem)
                    else:
                        msg_erro('Digite um nome para arquivo projetado')
                else:
                    msg_erro('Nome de arquivo inexistente,\ntente outra vez'
                             ' Entre com uma Distribuição existente')
            else:
                msg_erro('Selecione ou digite arquivo distribuição')

        if self.toolbar_abrirtotal:
            self.finaliza_frame()
        self.toolbar_abrirtotal = tk.Frame(self.master, bd=1, relief=FLAT)
        modelo = r'Digite nome do arquivo de distribuição igual o modelo ' \
                 r'/2018/MAIO/SÃO PAULO/DISTRIBUIÇÃO SÃO PAULO.xls'
        lb_dist = Label(self.toolbar_abrirtotal, text=modelo)
        lb_dist.pack(side=TOP, padx=2, pady=1)
        toolbarlinha = tk.Frame(self.toolbar_abrirtotal, bd=1, relief=FLAT)
        self.ed_dist = Entry(toolbarlinha, width=60)
        self.ed_dist.pack(side=LEFT, padx=2, pady=1)
        img_abrir = PhotoImage(file=r'imagens\abrir-menor.png')
        bt_abrir = Button(toolbarlinha, image=img_abrir, relief=FLAT,
                          command=self.abrir_pasta)
        bt_abrir.image = img_abrir
        bt_abrir.pack(side=LEFT, pady=1)
        toolbarlinha.pack(side=TOP)
        lb_nomepla = Label(self.toolbar_abrirtotal,
                           text='Nome Arquivo Projetado')
        lb_nomepla.pack()
        ed_nomepla = Entry(self.toolbar_abrirtotal, width=60)
        ed_nomepla.pack()
        bt_projetar = Button(self.toolbar_abrirtotal, text='PROJETAR',
                             command=bt_projetar_click)
        bt_projetar.pack()
        if int(self.banco.shape[0]) == int(self.projetado):
            bt_projetar['state'] = DISABLED
        lbespaco = Label(self.toolbar_abrirtotal)
        lbespaco.pack(side=TOP, pady=20)
        toolbarlog = tk.Frame(self.toolbar_abrirtotal, bd=1, relief=FLAT)
        barra = Scrollbar(self.toolbar_abrirtotal)
        tx_log = Text(self.toolbar_abrirtotal, width=75, height=20)
        barra.pack(side=RIGHT, fill=Y)
        tx_log.pack(side=TOP)
        barra.config(command=tx_log.yview)
        tx_log.config(yscrollcommand=barra.set)
        toolbarlog.pack(side=TOP)
        self.toolbar_abrirtotal.pack(side=TOP)


root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f'{w}x{h}+0+0')
root.title('Datanalyze')
app = Aplicacao(root)
app.mainloop()
