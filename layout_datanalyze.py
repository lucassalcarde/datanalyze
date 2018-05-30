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
        self.frametl_abrirtotal = ''  # frame externo usado construir cada tela
        self.caminho = ''  # caminho banco de dados
        self.banco = ''  # dataframe
        self.pesq_campo = ''  # armazena qt entrevistas feitas em campo
        self.projetado = ''  # qt entrevistas final

    def Corpo_Menu(self):
        """Função do Menu."""
        frametl = tk.Frame(self.master, bd=1, relief=RAISED)

        img_abrir = PhotoImage(file=r'imagens\abrir.png')
        bt_abrir = Button(frametl, image=img_abrir, relief=FLAT,
                          command=self.bt_abrir_click)
        bt_abrir.image = img_abrir
        bt_abrir.pack(side=LEFT, padx=2, pady=2)

        img_projecao = PhotoImage(file=r'imagens\projecao.png')
        self.bt_projecao = Button(frametl, relief=FLAT, image=img_projecao,
                                  command=self.bt_projecao_click,
                                  state=DISABLED)
        self.bt_projecao.image = img_projecao
        self.bt_projecao.pack(side=LEFT, padx=2, pady=2)

        self.bt_variaveis = Button(frametl, relief=FLAT, image=img_projecao,
                                   command=self.bt_variaveis_click)  # state=DISABLED,
        self.bt_variaveis.image = img_projecao
        self.bt_variaveis.pack(side=LEFT, padx=2, pady=2)

        img_sair = PhotoImage(file=r'imagens\sair.png')
        btsair = Button(frametl, image=img_sair, relief=FLAT,
                        command=self.quit)
        btsair.image = img_sair
        btsair.pack(side=RIGHT, padx=2, pady=2)
        frametl.pack(side=TOP, fill=X)
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
        self.frametl_abrirtotal.destroy()

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
        if self.frametl_abrirtotal:
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
                        if self.banco.shape[0] == self.projetado:
                            self.bt_variaveis['state'] = 'normal'
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
        self.frametl_abrirtotal = tk.Frame(self.master, bd=1, relief=FLAT)
        frametlalinha = tk.Frame(self.frametl_abrirtotal, bd=1, relief=FLAT)
        frametl_abrir = tk.Frame(frametlalinha, bd=1, relief=FLAT)
        modelo = r'Digite nome do arquivo igual o modelo ' \
                 r'/2018/MAIO/SÃO PAULO/SÃO PAULO.xls'
        lb_nome = Label(frametl_abrir, text=modelo, anchor=W)
        lb_nome.pack(side=TOP, padx=2, pady=12)
        self.ed_nome = Entry(frametl_abrir, width=60)
        self.ed_nome.pack(side=LEFT, padx=2, pady=12)
        img_abrir = PhotoImage(file=r'imagens\abrir-menor.png')
        bt_abrir = Button(frametl_abrir, image=img_abrir, relief=FLAT,
                          command=self.abrir_pasta)
        bt_abrir.image = img_abrir
        bt_abrir.pack(side=LEFT, pady=12)
        frametl_abrir.pack(side=LEFT)

        frametl_projecao = tk.Frame(frametlalinha, bd=1, relief=FLAT)
        lb_projecao = Label(frametl_projecao,
                            text='Arquivo Já está projetado?')
        lb_projecao.pack(side=TOP, padx=2, pady=2)
        self.rb_projecao = IntVar()
        self.rb_projecao.set(0)
        Radiobutton(frametl_projecao, text='Não Projetado', value=0,
                    variable=self.rb_projecao).pack(anchor=W)
        Radiobutton(frametl_projecao, text='Projetado', value=1,
                    variable=self.rb_projecao).pack(anchor=W)
        frametl_projecao.pack(side=LEFT, padx=50)

        frametl_val_projecao = tk.Frame(frametlalinha, bd=1,
                                        relief=FLAT)
        lb_val_projecao = Label(frametl_val_projecao, text='Valor Projeção')
        lb_val_projecao.pack(side=TOP, ipadx=2, pady=13)
        ed_val_projecao = Entry(frametl_val_projecao, width=20)
        ed_val_projecao.pack(side=TOP, padx=2, pady=13)
        frametl_val_projecao.pack(side=LEFT)
        frametlalinha.pack(side=TOP)
        bt_abrirbanco = Button(self.frametl_abrirtotal, text='ABRIR',
                               command=abrir_banco_click)
        bt_abrirbanco.pack(side=TOP)
        self.frametl_abrirtotal.pack(side=TOP)

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
                            self.log_geral = listapj[0]
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

        if self.frametl_abrirtotal:
            self.finaliza_frame()
        self.frametl_abrirtotal = tk.Frame(self.master, bd=1, relief=FLAT)
        modelo = r'Digite nome do arquivo de distribuição igual o modelo ' \
                 r'/2018/MAIO/SÃO PAULO/DISTRIBUIÇÃO SÃO PAULO.xls'
        lb_dist = Label(self.frametl_abrirtotal, text=modelo)
        lb_dist.pack(side=TOP, padx=2, pady=1)
        frametllinha = tk.Frame(self.frametl_abrirtotal, bd=1, relief=FLAT)
        self.ed_dist = Entry(frametllinha, width=60)
        self.ed_dist.pack(side=LEFT, padx=2, pady=1)
        img_abrir = PhotoImage(file=r'imagens\abrir-menor.png')
        bt_abrir = Button(frametllinha, image=img_abrir, relief=FLAT,
                          command=self.abrir_pasta)
        bt_abrir.image = img_abrir
        bt_abrir.pack(side=LEFT, pady=1)
        frametllinha.pack(side=TOP)
        lb_nomepla = Label(self.frametl_abrirtotal,
                           text='Nome Arquivo Projetado')
        lb_nomepla.pack()
        ed_nomepla = Entry(self.frametl_abrirtotal, width=60)
        ed_nomepla.pack()
        bt_projetar = Button(self.frametl_abrirtotal, text='PROJETAR',
                             command=bt_projetar_click)
        bt_projetar.pack()
        if int(self.banco.shape[0]) == int(self.projetado):
            bt_projetar['state'] = DISABLED
        lbespaco = Label(self.frametl_abrirtotal)
        lbespaco.pack(side=TOP, pady=20)
        frametllog = tk.Frame(self.frametl_abrirtotal, bd=1, relief=FLAT)
        barra = Scrollbar(self.frametl_abrirtotal)
        tx_log = Text(self.frametl_abrirtotal, width=75, height=20)
        barra.pack(side=RIGHT, fill=Y)
        tx_log.pack(side=TOP)
        barra.config(command=tx_log.yview)
        tx_log.config(yscrollcommand=barra.set)
        frametllog.pack(side=TOP)
        self.frametl_abrirtotal.pack(side=TOP)

    def bt_variaveis_click(self):
        """Criar tela para analise e acerto de variaveis."""
        if self.frametl_abrirtotal:
            self.finaliza_frame()

        def bt_sexo_click():
            trabdados.arruma_variaveis_sexo(self.banco, self.pesq_campo)

        def bt_idade_click():
            pass

        def bt_escolaridade_click():
            pass

        def bt_religiao_click():
            pass

        self.frametl_abrirtotal = tk.Frame(self.master, bd=1, relief=FLAT)
        frametl_left = tk.Frame(self.frametl_abrirtotal, bd=1, relief=FLAT)
        bt_todos = Button(frametl_left, text='ARRUMAR TODOS',
                          command='', width=20)
        bt_todos.pack(side=TOP, pady=20)
        bt_sexo = Button(frametl_left, text='SEXO', command=bt_sexo_click,
                         width=20)
        bt_sexo.pack(side=TOP, pady=20)
        bt_idade = Button(frametl_left, text='IDADE', command=bt_idade_click,
                          width=20)
        bt_idade.pack(side=TOP, pady=20)
        bt_escolaridade = Button(frametl_left, text='ESCOLARIDADE',
                                 command=bt_escolaridade_click, width=20)
        bt_escolaridade.pack(side=TOP, pady=20)
        bt_religiao = Button(frametl_left, text='RELIGIÃO',
                             command=bt_religiao_click, width=20)
        bt_religiao.pack(side=TOP, pady=20)
        frametl_left.pack(side=LEFT, pady=80, padx=20)
        frametl_right = tk.Frame(self.frametl_abrirtotal, bd=1, relief=FLAT)
        barra = Scrollbar(frametl_right)
        tx_log = Text(frametl_right, width=75, height=20)
        barra.pack(side=RIGHT, fill=Y)
        tx_log.pack(side=TOP)
        barra.config(command=tx_log.yview)
        tx_log.config(yscrollcommand=barra.set)
        frametl_right.pack(side=LEFT, pady=80, padx=20)
        self.frametl_abrirtotal.pack(side=TOP)


root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f'{w}x{h}+0+0')
root.title('Datanalyze')
app = Aplicacao(root)
app.mainloop()
