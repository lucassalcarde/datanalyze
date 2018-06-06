"""Classe e Funções que analizam e corrigem diferenças no banco de dados."""
import acerto_variavel
import pandas as pd
from math import floor
from random import randint, choice


mudanca = acerto_variavel.AlterarVariavel()


class TrabalhandoVar:
    """Classe com funções que analisam banco de dados."""

    def __init__(self):
        """inicializadora."""
        super(TrabalhandoVar, self).__init__()

    def arruma_variaveis_sexo(self, banco, pesq_campo):
        """
        Função Acerta variavel sexo.

        Acerta valor variavel sexo de acordo como numero randomico gerado
        vai de opção em opção da variavel verificando
        onde tem que aumentar e onde tem que diminuir
        """
        log = []
        sexo = banco.groupby('SEXO').size()
        menor_sexo = int(floor(0.5050 * banco.shape[0]))
        maior_sexo = int(0.54 * banco.shape[0])
        # define valor do FEMININO
        sexo_alterado = randint(menor_sexo, maior_sexo)
        pergunta = 'SEXO'
        log.append('FEMININO ' + str(sexo[0]) + ' - MASCULINO ' + str(sexo[1]))

        if sexo.FEMININO > sexo_alterado:  # Entra se tiver muito Feminino
            alter_mudar = 'FEMININO'
            alter_corrente = 'MASCULINO'
            # diferença a ser alterada
            diferenca = sexo.FEMININO - sexo_alterado
            log.append('FEMININO ' + str(sexo.FEMININO) + ' - VALOR FINAL ' +
                       str(sexo_alterado) + ' - DIFERENÇA ' + str(diferenca))
            msg = mudanca.mudar_alternativa(
                      banco=banco,
                      pesq_campo=pesq_campo,
                      pergunta=pergunta,
                      alter_corrente=alter_corrente,
                      alter_mudar=alter_mudar,
                      diferenca=diferenca,
                      valor_alterado=sexo_alterado)
            if msg:
                log.append(msg)
        elif sexo.MASCULINO > sexo_alterado:  # Entre se tiver muito Masculino
            alter_mudar = 'MASCULINO'
            alter_corrente = 'FEMININO'
            # define valor masculino
            sexo_alterado = banco.shape[0] - sexo_alterado
            # diferença a ser alterada
            diferenca = sexo.MASCULINO - sexo_alterado
            log.append('MASCULINO ' + str(sexo.MASCULINO) + ' - VALOR FINAL' +
                       str(sexo_alterado) + ' - DIFERENÇA' + str(diferenca))
            msg = mudanca.mudar_alternativa(
                      banco=banco,
                      pesq_campo=pesq_campo,
                      pergunta=pergunta,
                      alter_corrente=alter_corrente,
                      alter_mudar=alter_mudar,
                      diferenca=diferenca,
                      valor_alterado=sexo_alterado)
            if msg:
                log.append(msg)
        else:
            log.append('Variavel sexo com valor aceitavel!')
        sexo = banco.groupby('SEXO').size()
        log.append('FEMININO ' + str(sexo[0]) + ' - MASCULINO ' + str(sexo[1]))
        return [log]

    def arrumar_variaveis_idade(self, banco, pesq_campo):
        """
        Função Arruma variavel Idade.

        Acerta valor variavel idade de acordo como numero randomico gerado
        vai de opção em opção da variavel verificando onde tem que aumentar
        e onde tem que diminuir
        """
        log = []
        idade = banco.groupby('IDADE').size()
        pergunta = 'IDADE'
        log.append('IDADE ' + str(idade['16 a 30']) + ' ' +
                   str(idade['31 a 50']) + ' ' + str(idade['MAIS DE 50']))
        menor_16 = int(floor(0.2075 * banco.shape[0]))
        maior_16 = int(0.2450 * banco.shape[0])
        menor_50 = int(floor(0.33 * banco.shape[0]))
        maior_50 = int(0.36 * banco.shape[0])

        idade_16_alterado = randint(menor_16, maior_16)  # gera valor final 16
        idade_50_alterado = randint(menor_50, maior_50)  # gera valor final 50
        # calcula 31 que falta
        idade_31_alterado = 400 - (idade_16_alterado + idade_50_alterado)
        log.append('SERÁ ALTERADO ' + str(idade_16_alterado) + ' ' +
                   str(idade_31_alterado) + ' ' + str(idade_50_alterado))

        if idade['16 a 30'] < idade_16_alterado:
            '''se 16 a 30 faltando transfere de 31 a 50 aleatoriamente'''
            alter_mudar = '31 a 50'
            alter_corrente = '16 a 30'
            diferenca = idade_16_alterado - idade[0]  # falta para valor final
            log.append('16 a 30 ' + str(idade['16 a 30']) + ' - VALOR FINAL' +
                       str(idade_16_alterado) + ' - DIFERENÇA' +
                       str(diferenca))
            msg = mudanca.mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                            pergunta=pergunta,
                                            alter_corrente=alter_corrente,
                                            alter_mudar=alter_mudar,
                                            diferenca=diferenca,
                                            valor_alterado=0)
            if msg:
                log.append(msg)
        if idade['MAIS DE 50'] < idade_50_alterado:
            '''se mais de 50 faltando transfere de 31 a 50 aleatoriamente'''
            alter_mudar = '31 a 50'
            alter_corrente = 'MAIS DE 50'
            diferenca = idade_50_alterado - idade[2]
            log.append('MAIS DE 50 ' + str(idade['MAIS DE 50']) + ' - VALOR FINAL' +
                       str(idade_50_alterado) + ' - DIFERENÇA' +
                       str(diferenca))
            msg = mudanca.mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                            pergunta=pergunta,
                                            alter_corrente=alter_corrente,
                                            alter_mudar=alter_mudar,
                                            diferenca=diferenca,
                                            valor_alterado=0)
            if msg:
                log.append(msg)
        idade = banco.groupby('IDADE').size()
        if idade['31 a 50'] < idade_31_alterado:
            '''se 31 a 50 faltando, verifica qual opção
            tem acima e transfere aleatoriamente'''
            alter_corrente = '31 a 50'
            diferenca = idade_31_alterado - idade[1]
            log.append('31 a 50 ' + str(idade['31 a 50']) + ' - VALOR FINAL ' +
                       str(idade_31_alterado) + ' - DIFERENÇA ' +
                       str(diferenca))
            if idade['16 a 30'] > idade_16_alterado:
                alter_mudar = '16 a 30'
                log.append('    16 a 30 ' + str(idade['16 a 30']) +
                           ' - VALOR FINAL ' +
                           str(idade_16_alterado) + ' - DIFERENÇA ' +
                           str(diferenca))
                msg, diferenca = mudanca.\
                    mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                      pergunta=pergunta,
                                      alter_corrente=alter_corrente,
                                      alter_mudar=alter_mudar,
                                      diferenca=diferenca,
                                      valor_alterado=idade_16_alterado)
                '''if msg:
                    log.append(msg)'''
            idade = banco.groupby('IDADE').size()
            if idade['MAIS DE 50'] > idade_50_alterado:
                alter_mudar = 'MAIS DE 50'
                log.append('    MAIS DE 50 ' + str(idade['MAIS DE 50']) +
                           ' - VALOR FINAL ' +
                           str(idade_50_alterado) + ' - DIFERENÇA ' +
                           str(diferenca))
                msg, diferença = mudanca.mudar_alternativa(
                                     banco=banco,
                                     pesq_campo=pesq_campo,
                                     pergunta=pergunta,
                                     alter_corrente=alter_corrente,
                                     alter_mudar=alter_mudar,
                                     diferenca=diferenca,
                                     valor_alterado=idade_50_alterado)
                if msg:
                    log.append(msg)
        idade = banco.groupby('IDADE').size()
        log.append('IDADE ACERTADO ' + str(idade['16 a 30']) + ' ' +
                   str(idade['31 a 50']) + ' ' + str(idade['MAIS DE 50']))
        return [log]

    def arrumar_variaveis_escolaridade(banco, pesq_campo):
        """Função Analisa e acerta variavel escolaridade."""
        pergunta = 'ESCOLARIDADE'
        menor_fund = int(floor(0.39 * banco.shape[0]))
        maior_fund = int(0.42 * banco.shape[0])
        menor_sup = int(floor(0.14 * banco.shape[0]))
        maior_sup = int(0.17 * banco.shape[0])

        esco_fund_alterada = randint(menor_fund, maior_fund)
        esco_sup_alterada = randint(menor_sup, maior_sup)
        esco_med_altereada = 400 - (esco_fund_alterada + esco_sup_alterada)
        print('ESCOLARIDADE', esco_fund_alterada, esco_med_altereada,
              esco_sup_alterada)
        alter_mudar = 'ENSINO MÉDIO'

        escolaridade = banco.groupby('ESCOLARIDADE').size()
        if escolaridade['ENSINO FUNDAMENTAL'] < esco_fund_alterada:
            '''se fund. faltando transfere de medio aleatoriamente'''

            alter_corrente = 'ENSINO FUNDAMENTAL'
            diferenca = esco_fund_alterada - escolaridade['ENSINO FUNDAMENTAL']
            mudanca.mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                      pergunta=pergunta,
                                      alter_corrente=alter_corrente,
                                      alter_mudar=alter_mudar,
                                      diferenca=diferenca,
                                      valor_alterado=0)
        escolaridade = banco.groupby('ESCOLARIDADE').size()
        if escolaridade.SUPERIOR < esco_sup_alterada:
            '''se superior faltando transfere de medio aleatoriamente'''
            alter_corrente = 'SUPERIOR'
            diferenca = esco_sup_alterada - escolaridade.SUPERIOR
            mudanca.mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                      pergunta=pergunta,
                                      alter_corrente=alter_corrente,
                                      alter_mudar=alter_mudar,
                                      diferenca=diferenca,
                                      valor_alterado=0)
        escolaridade = banco.groupby('ESCOLARIDADE').size()
        if escolaridade['ENSINO MÉDIO'] < esco_med_altereada:
            '''se medio faltando, verifica qual opção tem acima e
            transfere aleatoriamente'''
            alter_corrente = 'ENSINO MÉDIO'
            diferenca = esco_med_altereada - escolaridade[1]
            # contador = 0
            if escolaridade['ENSINO FUNDAMENTAL'] > esco_fund_alterada:
                alter_mudar = 'ENSINO FUNDAMENTAL'
                diferenca = mudanca. \
                    mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                      pergunta=pergunta,
                                      alter_corrente=alter_corrente,
                                      alter_mudar=alter_mudar,
                                      diferenca=diferenca,
                                      valor_alterado=esco_fund_alterada)
            if escolaridade.SUPERIOR > esco_sup_alterada:
                alter_mudar = 'SUPERIOR'
                mudanca.mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                          pergunta=pergunta,
                                          alter_corrente=alter_corrente,
                                          alter_mudar=alter_mudar,
                                          diferenca=diferenca,
                                          valor_alterado=esco_sup_alterada)

    def arrumar_variaveis_religiao(banco, pesq_campo, nome_pla):
        """Função analisa e corrige variavel religião."""
        pergunta = 'RELIGIÃO'
        religiao = banco.groupby('RELIGIÃO').size()
        menos_outras = int(floor(0.0275 * banco.shape[0]))
        maior_outras = int(0.05 * banco.shape[0])
        if religiao.OUTRAS not in range(menos_outras, maior_outras):
            '''se outras acima ou abaixo acerta diferença'''
            outras_alterado = randint(menos_outras, maior_outras)
            if religiao.OUTRAS > outras_alterado:
                diferenca = religiao.OUTRAS - outras_alterado
                alter_mudar = 'OUTRAS'
                alter_corrente = 'CATÓLICA'
                mudanca.mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                          pergunta=pergunta,
                                          alter_corrente=alter_corrente,
                                          alter_mudar=alter_mudar,
                                          diferenca=diferenca,
                                          valor_alterado=outras_alterado)
            if religiao.OUTRAS < outras_alterado:
                diferenca = outras_alterado - religiao.OUTRAS
                alter_mudar = 'CATÓLICA'
                alter_corrente = 'OUTRAS'
                mudanca.mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                          pergunta=pergunta,
                                          alter_corrente=alter_corrente,
                                          alter_mudar=alter_mudar,
                                          diferenca=diferenca,
                                          valor_alterado=0)
        else:
            print('outras correto')
            outras_alterado = religiao.OUTRAS

        menos_nt = int(floor(0.06 * banco.shape[0]))
        maior_nt = int(0.0925 * banco.shape[0])
        if religiao['NÃO TEM'] not in range(menos_nt, maior_nt):
            nt_alterado = randint(menos_nt, maior_nt)
            if religiao['NÃO TEM'] > nt_alterado:
                diferenca = religiao['NÃO TEM'] - nt_alterado
                alter_mudar = 'NÃO TEM'
                alter_corrente = 'CATÓLICA'
                mudanca.mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                          pergunta=pergunta,
                                          alter_corrente=alter_corrente,
                                          alter_mudar=alter_mudar,
                                          diferenca=diferenca,
                                          valor_alterado=nt_alterado)
            if religiao['NÃO TEM'] < nt_alterado:
                diferenca = nt_alterado - religiao['NÃO TEM']
                alter_mudar = 'CATÓLICA'
                alter_corrente = 'NÃO TEM'
                mudanca.mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                          pergunta=pergunta,
                                          alter_corrente=alter_corrente,
                                          alter_mudar=alter_mudar,
                                          diferenca=diferenca,
                                          valor_alterado=0)
        else:
            print('não tem correto')
            nt_alterado = religiao['NÃO TEM']

        religiao = banco.groupby('RELIGIÃO').size()
        menos_eva = int(floor(0.35 * banco.shape[0]))
        maior_eva = int(0.39 * banco.shape[0])
        if religiao['EVANGÉLICA'] not in range(menos_eva, maior_eva):
            eva_alterado = randint(menos_eva, maior_eva)
            if religiao['EVANGÉLICA'] < eva_alterado:
                diferenca = eva_alterado - religiao['EVANGÉLICA']
                alter_mudar = 'CATÓLICA'
                alter_corrente = 'EVANGÉLICA'
                mudanca.mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                          pergunta=pergunta,
                                          alter_corrente=alter_corrente,
                                          alter_mudar=alter_mudar,
                                          diferenca=diferenca,
                                          valor_alterado=0)
            if religiao['EVANGÉLICA'] > eva_alterado:
                diferenca = religiao['EVANGÉLICA'] - eva_alterado
                alter_mudar = 'EVANGÉLICA'
                alter_corrente = 'CATÓLICA'
                mudanca.mudar_alternativa(banco=banco, pesq_campo=pesq_campo,
                                          pergunta=pergunta,
                                          alter_corrente=alter_corrente,
                                          alter_mudar=alter_mudar,
                                          diferenca=diferenca,
                                          valor_alterado=eva_alterado)
        else:
            print('evangelico correto')
            eva_alterado = religiao['EVANGÉLICA']
        print('religião', eva_alterado, nt_alterado, outras_alterado)

        '''writer = pd.ExcelWriter(nome_pla)
        banco.to_excel(writer, 'Plan1')
        writer.save()'''

def perguntas_pesquisa(banco, pesq_campo, nome_pla):
    lista_perguntas = list(banco.columns)  # lista de perguntas da pesquisa

    for pergunta in lista_perguntas:
        if pergunta == 'SETOR':
            break
        lista_alterperg = list(banco.groupby(pergunta).groups.keys())

        for alterperg in lista_alterperg:
            lista_variaveis = ['SEXO', 'IDADE', 'ESCOLARIDADE', 'RELIGIÃO']
            dic_var_falta = {}
            for variaveis in lista_variaveis:
                lista_altervar = list(banco.groupby(variaveis).groups.keys())
                lista_alt_falta = []
                for altervar in lista_altervar:
                    if altervar == 'OUTRAS' or altervar == 'NÃO TEM':
                        continue
                    # print(pergunta, alterperg, variaveis, altervar)
                    cruz_falta = list(banco[(banco[pergunta] == alterperg) &
                                            (banco[variaveis] == altervar)].index)  # armazena indice de alternativa sem certo cruzamento
                    # print(cruz_falta)
                    if not cruz_falta:  # verifica se teve alguma alternativa sem cruzamento
                        lista_alt_falta.append(altervar)  # lista de alternativa de variavel que falta
                if lista_alt_falta:
                    dic_var_falta.update(
                        {variaveis: lista_alt_falta})  # dicionario com variaveis e suas alternativas que faltam
            if dic_var_falta:
                if pergunta == 'PROBLEMAS':
                    continue
                item_falta = lista_alterperg.index(alterperg)
                linha0 = ''
                linha1 = ''
                linha2 = ''
                for chave in dic_var_falta:  # cria codigo para incluir variaveis que faltam
                    cont = 0
                    for alternativa in dic_var_falta[chave]:
                        if cont == 0:
                            linha0 += ' & (banco[\'' + \
                                      chave + '\'] == \'' + \
                                      alternativa + '\')'
                        elif cont == 1:
                            linha1 += ' & (banco[\'' + \
                                      chave + '\'] == \'' + \
                                      alternativa + '\')'
                        elif cont == 2:
                            linha2 += ' & (banco[\'' + \
                                      chave + '\'] == \'' + \
                                      alternativa + '\')'
                        cont += 1
                codigos = [linha0, linha1, linha2]
                while '' in codigos:  # apaga itens em branco na lista
                    codigos.remove('')
                resultado_corrente = banco.groupby(pergunta).size()
                alternativa = resultado_corrente.idxmax()  # maior alternativa
                comandos = []
                cont = 0
                for cod in codigos:  # concatenando pergunta e alternativa a variaveis que faltam
                    comandos.append('list(banco[(banco[\'' + \
                                    pergunta + '\'] == \'' + \
                                    alternativa + '\')' + \
                                    cod + '].index)')
                    ind_troca = eval(comandos[cont])  # transforma string em um comando literal
                    if ind_troca:
                        banco.loc[ind_troca[-1], pergunta] = alterperg
                    else:
                        print('Não foi encontrado combinação de variavel para ',
                              pergunta, alterperg)
                    cont += 1

        if 'BOA' in lista_alterperg:
            '''Trantando ÓTIMA zerado'''
            if 'ÓTIMA' not in lista_alterperg:
                resultado_corrente = banco.groupby(pergunta).size()
                if resultado_corrente.BOA < 44:
                    alternativa = 'REGULAR'
                if resultado_corrente.BOA >= 44:
                    alternativa = 'BOA'
                ind_troca = list(banco[(banco[pergunta] == alternativa) &
                                       (banco.index >= pesq_campo)].index)
                if 19 < resultado_corrente.BOA < 32:
                    banco.loc[ind_troca[randint(0, len(ind_troca) - 1)],
                              pergunta] = 'ÓTIMA'
                elif resultado_corrente.BOA >= 32:
                    cont = randint(3, 5)
                    while True:  # randomiza qts ótima adiciona e quais suas variaveis
                        sexo = choice(['MASCULINO', 'FEMININO'])
                        idade = choice(['16 a 30', '31 a 50', 'MAIS DE 50'])
                        escolaridade = choice(['ENSINO FUNDAMENTAL',
                                               'ENSINO MÉDIO', 'SUPERIOR'])
                        religiao = choice(['CATÓLICA', 'EVANGÉLICA'])
                        ind_troca = list(banco[(banco[pergunta] == alternativa) &
                                               (banco['SEXO'] == sexo) &
                                               (banco['IDADE'] == idade) &
                                               (banco['ESCOLARIDADE'] == escolaridade) &
                                               (banco['RELIGIÃO'] == religiao)].index)
                        if ind_troca:  # verifica se achou algum indice com as variaveis random
                            banco.loc[ind_troca[-1], pergunta] = 'ÓTIMA'
                            cont -= 1
                        if cont == 0:
                            break
                elif resultado_corrente.BOA <= 19:
                    print(pergunta, ' Alternativa boa abaixo de 4%, '
                                    'ÓTIMA continua zerado')

            '''Trantando RUIM zerado'''
            if 'RUIM' not in lista_alterperg:
                resultado_corrente = banco.groupby(pergunta).size()
                if resultado_corrente.REGULAR < 40:
                    alternativa = 'BOA'
                if resultado_corrente.REGULAR >= 40:
                    alternativa = 'REGULAR'
                cont = randint(3, 5)
                while True:
                    sexo = choice(['MASCULINO', 'FEMININO'])
                    idade = choice(['16 a 30', '31 a 50', 'MAIS DE 50'])
                    escolaridade = choice(['ENSINO FUNDAMENTAL',
                                           'ENSINO MÉDIO', 'SUPERIOR'])
                    religiao = choice(['CATÓLICA', 'EVANGÉLICA'])
                    ind_troca = list(banco[(banco[pergunta] == alternativa) &
                                           (banco['SEXO'] == sexo) &
                                           (banco['IDADE'] == idade) &
                                           (banco['ESCOLARIDADE'] == escolaridade) &
                                           (banco['RELIGIÃO'] == religiao)].index)
                    if ind_troca:  # verifica se achou algum indice com as variaveis random
                        banco.loc[ind_troca[-1], pergunta] = 'RUIM'
                        cont -= 1
                    if cont == 0:
                        break

            '''Trantando PÉSSIMA zerado'''
            if 'PÉSSIMA' not in lista_alterperg:
                resultado_corrente = banco.groupby(pergunta).size()
                ind_troca = list(banco[(banco[pergunta] == 'REGULAR') &
                                       (banco.index >= pesq_campo)].index)
                if not ind_troca:
                    print('regular sem nenhuma projeção')
                    exit()
                if 11 < resultado_corrente.RUIM < 16:
                    banco.loc[ind_troca[randint(0, len(ind_troca) - 1)],
                              pergunta] = 'PÉSSIMA'
                elif resultado_corrente.RUIM >= 16:
                    if resultado_corrente.REGULAR < 36:
                        alternativa = 'BOA'
                    if resultado_corrente.REGULAR >= 36:
                        alternativa = 'REGULAR'
                    cont = randint(3, 5)
                    while True:
                        sexo = choice(['MASCULINO', 'FEMININO'])
                        idade = choice(['16 a 30', '31 a 50', 'MAIS DE 50'])
                        escolaridade = choice(['ENSINO FUNDAMENTAL',
                                               'ENSINO MÉDIO', 'SUPERIOR'])
                        religiao = choice(['CATÓLICA', 'EVANGÉLICA'])
                        ind_troca = list(banco[(banco[pergunta] == alternativa) &
                                               (banco['SEXO'] == sexo) &
                                               (banco['IDADE'] == idade) &
                                               (banco['ESCOLARIDADE'] == escolaridade) &
                                               (banco['RELIGIÃO'] == religiao)].index)
                        if ind_troca:  # verifica se achou algum indice com as variaveis random
                            banco.loc[ind_troca[-1], pergunta] = 'PÉSSIMA'
                            cont -= 1
                        if cont == 0:
                            break
                elif resultado_corrente.RUIM <= 11:
                    print(pergunta, ' Alternativa ruim abaixo de 3%, '
                                    'péssima continua zerado')

            '''Trantando NÃO SOUBE RESPONDER zerado'''
            if 'NÃO SOUBE RESPONDER' not in lista_alterperg:
                resultado_corrente = banco.groupby(pergunta).size()
                if resultado_corrente.REGULAR < 36:
                    alternativa = 'BOA'
                if resultado_corrente.REGULAR >= 36:
                    alternativa = 'REGULAR'
                cont = randint(2, 5)
                while True:
                    sexo = choice(['MASCULINO', 'FEMININO'])
                    idade = choice(['16 a 30', '31 a 50', 'MAIS DE 50'])
                    escolaridade = choice(['ENSINO FUNDAMENTAL',
                                           'ENSINO MÉDIO', 'SUPERIOR'])
                    religiao = choice(['CATÓLICA', 'EVANGÉLICA'])
                    ind_troca = list(banco[(banco[pergunta] == alternativa) &
                                           (banco['SEXO'] == sexo) &
                                           (banco['IDADE'] == idade) &
                                           (banco['ESCOLARIDADE'] == escolaridade) &
                                           (banco['RELIGIÃO'] == religiao)].index)
                    if ind_troca:  # verifica se achou algum indice com as variaveis random
                        banco.loc[ind_troca[-1], pergunta] = 'NÃO SOUBE RESPONDER'
                        cont -= 1
                    if cont == 0:
                        break

    writer = pd.ExcelWriter(nome_pla)
    banco.to_excel(writer, 'Plan1')
    writer.save()


'''def menu():
    while True:
        print('*' * 40)
        if 'banco' in dir():
            print(f'Banco de dados com: {banco.shape[0]} entrevistas ')
        else:
            print('\33[31mNenhum banco aberto!\33[0m')
        print('*' * 40)
        print('1) Abrir Banco')
        print('2) Especificar projeção')
        print('3) projeção')
        print('4) variaveis principais')
        print('5) Perguntas da Pesquisa')
        print('*' * 40)
        print('0) Sair')

        opcao = int(input('Opção: '))

        if opcao == 1:
            banco, nome_pla, projetado, pesq_campo = bd.abrir_banco()

        elif opcao == 2:
            print('Opção inativa')

        elif opcao == 3:
            if banco.shape[0] == projetado:
                print('Pesquisa já projetada!')
            else:
                banco, nome_pla = projecao_pesquisa(banco, projetado)  # faz projeção e retorna data frama do banco projetado

        elif opcao == 4:
            if 'banco' in dir():
                if banco.shape[0] == projetado:
                    arruma_variaveis_sexo(banco, pesq_campo)
                    arrumar_variaveis_idade(banco, pesq_campo)
                    arrumar_variaveis_escolaridade(banco, pesq_campo)
                    arrumar_variaveis_religiao(banco, pesq_campo, nome_pla)
                else:
                    print('Banco não está projetado.')
            else:
                print('Nenhum banco aberto.')
        elif opcao == 5:
            if 'banco' in dir():
                if banco.shape[0] == projetado:
                    perguntas_pesquisa(banco, pesq_campo, nome_pla)
                else:
                    print('banco não está projetado.')
            else:
                print('nenhum banco aberto.')
        elif opcao == 0:
            break


menu()'''
