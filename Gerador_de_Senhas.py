import random
import string

#objeto com o tamanho da senha
tamanho=int(input('Digite a quantidade de dígitos da senha que será gerada: '))

# objeto estrutura da senha que será gerada (letras maiúsculas e minúsculas +  números +caracteres descritos)
chars=string.ascii_letters + string.digits + string.punctuation +'!@#$%¨&*()_+;:.,/*-'

#objeto que utiliza a classe os.urandom
rnd=random.SystemRandom() #os.urandom

#mostra a senha gerada
print(''.join(rnd.choice(chars)for i in range(tamanho)))