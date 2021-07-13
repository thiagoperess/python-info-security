import random, string

password_length = int(input('Digite o tamanho da senha desejada: '))

characters = string.ascii_letters + string.digits + '!@#$%&*()-+,.;?ç'

rnd = random.SystemRandom()

print(''.join(rnd.choice(characters) for i in range(password_length)))

