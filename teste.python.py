nome = "Pablo"
def primeiraFuncao(txt):
    return txt.upper()

print(primeiraFuncao(nome))

alunos = ["André", "Douglas", "Aluan", "Gilmar"]
def segundaFuncao(txt,vlr):
    txt.append(vlr)
    return txt


print(segundaFuncao(alunos, nome))
