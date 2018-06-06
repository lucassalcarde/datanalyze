"""Arquivo com função que faz analise e alteração das variaveis."""
from math import floor, ceil


class AlterarVariavel:
    """Classe altera variaveis."""

    def __init__(self):
        """Função inicializa."""
        super(AlterarVariavel, self).__init__()

    def mudar_alternativa(self, banco, pesq_campo, pergunta,
                          alter_corrente, alter_mudar, diferenca,
                          valor_alterado):
        """Função para analise e alteração de variaveis."""
        lista_indices = list(banco[(banco[pergunta] == alter_mudar) &
                                   (banco.index >= pesq_campo)].index)
        pulo = floor(len(lista_indices) / diferenca)
        resto = 0
        mensagem = ''
        if pulo == 0:
            mensagem = 'Número insuficiente de ' + alter_mudar +\
                       ' na projeção'
            pulo = 1
        elif pulo == 1 and len(lista_indices) % diferenca != 0:
            resto = ceil(diferenca / (len(lista_indices) - diferenca))
        contador = 0
        cont_pulo = 0
        cont_resto = 1
        valor_corrente = banco.groupby(pergunta).size()

        while cont_pulo < len(lista_indices) and contador < diferenca \
                and valor_corrente[alter_mudar] > valor_alterado:
            banco.loc[lista_indices[cont_pulo], pergunta] = alter_corrente
            if resto != 0 and cont_resto == resto:
                cont_pulo += pulo
                cont_resto = 0
            cont_pulo += pulo
            cont_resto += 1
            contador += 1
            valor_corrente = banco.groupby(pergunta).size()
        if contador < diferenca:
            lista_indices = list(banco[(banco[pergunta] == alter_mudar) &
                                       (banco.index < pesq_campo)].index)
            cont_pulo = len(lista_indices) - 1
            pulo = floor(cont_pulo / (diferenca - contador))
            resto = 0
            if pulo == 0:
                mensagem = 'Número insuficiente de ' + alter_mudar + \
                    ' no banco de dados. Erro'
                pulo = 1
            elif pulo == 1 and cont_pulo % (diferenca - contador) != 0:
                resto = ceil((diferenca - contador) /
                             len(lista_indices) - (diferenca - contador))
            cont_resto = 1
            while cont_pulo > 0 and contador < diferenca\
                    and valor_corrente[alter_mudar] > valor_alterado:
                banco.loc[lista_indices[cont_pulo], pergunta] = alter_corrente
                if resto != 0 and cont_resto == resto:
                    cont_pulo -= pulo
                    cont_resto = 0
                cont_pulo -= pulo
                cont_resto += 1
                contador += 1
                valor_corrente = banco.groupby(pergunta).size()
        if alter_corrente == '31 a 50' or alter_corrente == 'ENSINO MÉDIO':
            return mensagem, (diferenca - contador)
        return mensagem
