#O que é numpy?: é uma biblioteca que oferece estruturas de dados não nativas do python com suporte matemáticas
# Por que numpy?: oferece desempenho e ferramentas superiores à biblioteca padrão.
# O numpy trabalha com a ideia de vetores (arrays), conhecidos como ndarrays
# Com a diferença de que ndarrays só trabalham com dados do mesmo tipo que lembram muito as listas do python.
# Outra vantagem: por trabalhar com um só tipo de dado, o ndarray tem um desempenho muito melhor se comparado com listas.
import numpy
import plotly.express
# 1 - Exemplo de criação:
#ndarray1 = numpy.zeros(10000)
#print(f' 1 - Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')
#ndarray1 = numpy.ones(10000)
#print(f' 2 - Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')
#ndarray1 = numpy.linspace(10, 2, 1000)
#print(f' 3 - Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')

#vetor_a = numpy.linspace(10, 1000, 100)
#vetor_b = numpy.linspace(10,3000,100)
#vetor_c = numpy.linspace(10,8000,100)

#print(vetor_a)
#print(vetor_b)
#(vetor_c)

# Numpy já tem métodos bem diretos de como salvar um arquivo no formato .txt
#numpy.savetxt('vetor_a.txt', vetor_a, fmt='%f', delimiter=';')
#numpy.savetxt('vetor_b.txt', vetor_b, fmt='%f', delimiter=';')
#numpy.savetxt('vetor_c.txt', vetor_c, fmt='%f', delimiter=';')

array_a = numpy.loadtxt('vetor_a.txt', dtype=numpy.float64, delimiter=';')
array_b = numpy.loadtxt('vetor_b.txt', dtype=numpy.float64, delimiter=';')
array_c = numpy.loadtxt('vetor_c.txt', dtype=numpy.float64, delimiter=';')
print(array_a)

array_abc = numpy.vstack([array_a, array_b, array_c])
print(array_abc)
array_abc = array_abc.transpose()
print(array_abc)
fig = plotly.express.line(array_abc)
fig.show()