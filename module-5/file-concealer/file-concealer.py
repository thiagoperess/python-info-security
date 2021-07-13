import ctypes

attribute_hide = 0x02

turn_back = ctypes.windll.kernel.SetFileAtrributesW('ocultar.txt', attribute_hide)

if turn_back:
    print('Arquivo foi ocultado!')
else:
    print('Arquivo não foi ocultado!')