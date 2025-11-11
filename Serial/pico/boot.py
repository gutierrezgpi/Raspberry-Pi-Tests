'''
Arquivo que ativa a porta de dados separada do REPL

Colocar dentro do CIRCUITPY junto com o arquivo code.py
'''

import usb_cdc

usb_cdc.enable(console=True, data=True)
