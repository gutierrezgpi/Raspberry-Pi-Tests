'''
Arquivo que ativa a porta de dados separada do REPL
'''

import usb_cdc

usb_cdc.enable(console=True, data=True)
