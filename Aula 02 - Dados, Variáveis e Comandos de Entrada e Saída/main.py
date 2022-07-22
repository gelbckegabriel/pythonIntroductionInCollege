# Composição de dados.
nota = 8.5
txt = 'Você tirou %f na matéria da faculdade!' % nota
print(txt)

txt = 'Você tirou %.2f na matéria da faculdade!' % nota # .2f é utilizado para limitar o número de casas decimais.
print(txt)

disciplina = 'Algoritmos'
txt = 'Você tirou %.2f na matéria de %s da faculdade!' % (nota, disciplina)
print(txt)

# Composição de dados mais moderna.
txt = 'Você tirou {} em {} na faculdade' .format(nota, disciplina)
print(txt)

# Fatiar string.
materia = 'Lógica de Programação e Algoritmos'
print(materia[0:6])

# length é igual a len.
tamanhoMateria = len(materia)
print(tamanhoMateria)