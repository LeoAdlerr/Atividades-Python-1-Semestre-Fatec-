
print("\033[0;35mCadastre-se(usuário deve ser diferente da senha!)\033[m")
usuario=str(input("usuário: "))
senha=str(input("senha:"))
while usuario == senha:
	print("\033[0;31mERRO: o usuário não pode ser igual a senha, tente novamente!\033[m")
	senha = str(input("digite a nova senha: "))
else:
	print("\033[0;33mcadastrado efetuado com sucesso\033[m")
	print(f"Nome do usuário= {usuario}")
	print(f"Senha= {senha}")