def descriptografar (pontos: str) -> str:
    for msg_criptografada in linhas[1:]:
        if pontos == ".":
           letra = 'a'
        if pontos == "..":
            letra = "b"
        if pontos == "...":
            letra = "c"
        if pontos == ". .":
            letra = "d"
        if pontos == ".. ..":
            letra = "e"
        if pontos == "... ...":
            letra = "f"
        if pontos == ". . .":
            letra = "g"
        if pontos == ".. .. ..":
            letra = "h"
        if pontos == "... ... ...":
            letra = "i"
        if pontos == ". . . .":
            letra = "j"
        if pontos == ".. .. .. ..":
            letra = "k"
        if pontos == "... ... ... ...":
            letra = "l"
        if pontos == ". . . . .":
            letra = "m"
        if pontos == ".. .. .. .. ..":
            letra = "n"
        if pontos == "... ... ... ... ...":
            letra = "o"
        if pontos == ". . . . . .":
            letra = "p"
        if pontos == ".. .. .. .. .. ..":
            letra = "q"
        if pontos == "... ... ... ... ... ...":
            letra = "r"
        if pontos == ". . . . . . .":
            letra = "s"
        if pontos == ".. .. .. .. .. .. ..":
            letra = "t"
        if pontos == "... ... ... ... ... ... ...":
            letra = "u"
        if pontos == ". . . . . . . .":
            letra = "v"
        if pontos == ".. .. .. .. .. .. .. ..":
            letra = "w"
        if pontos == "... ... ... ... ... ... ... ...":
            letra = "x"
        if pontos == ". . . . . . . . .":
            letra = "y"
        if pontos == ".. .. .. .. .. .. .. .. ..":
            letra = "z"

        for pontos in linhas:
            return letra
            pass

with open('desafio.txt') as txt:
    linhas = txt.read().splitlines()
    for msg_criptografada in linhas[1:]:
        print(descriptografar(msg_criptografada), " <- ", msg_criptografada)