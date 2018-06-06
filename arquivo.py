"""cria arquivo de log .txt."""
import os.path


def grava_arquivo(caminho, texto):
    """Função grava arquivo."""
    if caminho:
        caminhoarq = caminho + '/log.txt'
    else:
        caminhoarq = 'log.txt'
    if os.path.isfile(caminhoarq):
        parametro = 'a'
    else:
        parametro = 'w'
    arq = open(caminhoarq, parametro)
    linha = ''
    for linha in texto:
        arq.write(linha + '\n')
    arq.write('\n')
    arq.close
