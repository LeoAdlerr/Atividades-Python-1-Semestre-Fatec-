
def integradorstr(n, base):
    str = ""
    while (n > 0):
        digit = n % base
        n = int(n / base)
        str = chr(digit + ord('0')) + str
    return str


# function to check for palindrome
def éPalindromo(i, k):
    temp = i

    m = 0
    while (temp > 0):
        m = (temp % 10) + (m * 10)
        temp = int(temp / 10)

    if (m == i):

        str = integradorstr(m, k)
        str1 = str

        if (str[::-1] == str1):
            return i
    return 0

def somadePalindromos(n, k):
    soma = 0
    for i in range(n):
        soma += éPalindromo(i, k)
    print(f"A soma é: {soma}")

n = 500000
k = 2

somadePalindromos(n, k)

