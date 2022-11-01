def arq_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve algum erro na criação do arquivo.')
    else:
        print(f'{nome} criado com sucesso!')

def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve algum erro com a leitura do arquivo.')
    else:
        print(a.read())
    finally:
        a.close()

def adicionar_pessoa(arq, nome = 'desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve algum erro em abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro em gravar os dados da pessoa.')
        else:
            print(f'Novo registro de {nome} gravado.')
            a.close()