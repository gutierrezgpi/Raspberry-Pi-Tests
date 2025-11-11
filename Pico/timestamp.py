import time

segundos = time.time()
'''Retorna o tempo atual em segundos desde 1º de janeiro de 1970.'''

timestamp = time.monotonic()
'''
Retorna um valor de tempo sempre crescente com um ponto de referência desconhecido. Use-o apenas para comparar com outros valores obtidos time.monotonic() durante a mesma execução do código.
'''

print(f"Tempo atual: {segundos} segundos")
print(f"Faz {timestamp} segundos desde que a placa foi ligada")
