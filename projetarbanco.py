"""Classe e Funções que analizam e corrigem diferenças no banco de dados."""
from salva_arquivo import salvando_arquivo
import pandas as pd
from math import floor, ceil


class TrabalhandoDados:
    """Classe com funções que analisa e projeta banco de dados."""

    def __init__(self):
        """Função inicializa."""
        super(TrabalhandoDados, self).__init__()

    def projecao_pesquisa(self, banco, projetado, setor_final, nome_pla):
        """
        Projeção banco de dadosself.

        Agrupa variavel setor e carrega distribuição final, verifica quando
        falta cada setor. Armazena em resultado as linhas copiadas depois
        concatena o banco principal com resultado
        """
        projetado = int(projetado)
        setor = banco.groupby('SETOR').size()
        distribuicao = pd.read_excel(setor_final, 'Plan2')

        cont = 0
        pulo = 0  # numero de linhas pula em cada setor na projeção
        # cria um dataframe apenas com nomes das colunas
        resultado = pd.DataFrame(columns=banco.columns)
        log = []

        for nome_setor, valor in setor.iteritems():
            '''Verifica quantas entrevistas faltam cada setor'''

            if nome_setor == distribuicao.SETOR[cont]:
                falta = int(int(distribuicao.TOTAL[cont] * projetado) -
                            int(valor))
                if falta == 0:
                    log.append(f'Setor {nome_setor} com quantidade correta')
                    cont += 1
                    continue
                elif falta > 0:
                    pulo = floor(valor / falta)
                    resto = 0
                    if pulo == 1 and valor % falta != 0:
                        resto = ceil(falta / (valor - falta))
                    elif pulo == 0:
                        return ['Numero de entrevistas insuficiente '
                                '\npara projetar setor ' + nome_setor]
                elif falta < 0:
                    return [f'Setor {nome_setor} está \nacima do numero '
                            f'de entrevista final.']
                setor_projetando = banco.query('SETOR == @nome_setor')
                linha = 0  # linha a ser copiada
                cont_falta = 0  # contador para não ultrapassar quantas faltam
                cont_resto = 1
                log.append(nome_setor + ' - Resto: ' + str(resto))
                log.append('Total: ' +
                           str((distribuicao.TOTAL[cont] * projetado)) +
                           ' - Atual: ' + str(valor) +
                           ' - Falta: ' + str(falta))
                while linha < valor and cont_falta < falta:
                    resultado = resultado.append(setor_projetando.iloc[linha])
                    if resto != 0 and cont_resto == resto:
                        linha += pulo
                        cont_resto = 0
                    cont_resto += 1
                    linha += pulo
                    cont_falta += 1
            else:
                return['Problema na ordem do setor.']
            cont += 1

        frames = [banco, resultado]
        resultado = pd.concat(frames, ignore_index=True)
        resultado['qt_campo'] = banco.shape[0]
        salvando_arquivo(resultado, nome_pla)
        banco = pd.read_excel(nome_pla, 'Plan1')
        return ['ok', log, banco]  # verificar o que precisa retornar
