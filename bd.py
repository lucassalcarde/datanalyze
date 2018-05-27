"""Carrega arquivo e transforma em df."""
import pandas as pd
import os.path


class Entrada:
    """classe abrindo banco e recebendo valores de dados presente e futuro."""

    def abrir_banco(self, banco_excel, op, projecao):
        """Função para abrir xls."""
        if os.path.isfile(banco_excel):  # verifica se existe arquivo
            banco = pd.read_excel(banco_excel, 'Plan1')
            '''
            Apaga linhas com Treinamento e vazias na coluna entrevistadora
            '''
            limpando_banco = banco.query('Entrevistadora == "Treinamento" | '
                                         'Entrevistadora != Entrevistadora')
            banco.drop(limpando_banco.index, inplace=True)
        else:
            print('retorna msg de erro')
            return ['Arquivo inexistente,\ndigite ou selecione'
                    'arquivo existente']
        if op == 1:
            projecao = int(banco.shape[0])
            campo = int(banco.qt_campo.max())
        elif op == 0:
            if banco.shape[0] < int(projecao):
                campo = banco.shape[0]
            else:
                return ['Arquivo com valor igual ou '
                        'acima\nespecificado para projeção']
        return ['ok', banco, banco_excel, projecao, campo]
