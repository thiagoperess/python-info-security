import hashlib

archive1 = 'a.txt'
archive2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(archive1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(archive2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo {archive1} é diferente do arquivo {archive2}')
    print(f'O hash do arquivo {archive1} é: ', hash1.hexdigest())
    print(f'O hash do arquivo {archive2} é: ', hash2.hexdigest())
else:
    print(f'O arquivo {archive1} é igual ao arquivo {archive2}')
    print(f'O hash do arquivo {archive1} é: ', hash1.hexdigest())
    print(f'O hash do arquivo {archive2} é: ', hash2.hexdigest())
