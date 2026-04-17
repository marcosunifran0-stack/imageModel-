import math

def eh_primo(n: int) -> bool:
    """
    Verifica se um número é primo.

    Um número primo é um inteiro maior que 1 que não tem divisores positivos
    além de 1 e ele mesmo.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se n for primo, False caso contrário.

    Raises:
        Nenhum. Assume que n é um inteiro.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    limite = math.isqrt(n)
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    try:
        numero = int(input("Digite um número para verificar se é primo: "))
        resultado = "primo" if eh_primo(numero) else "não primo"
        print(f"{numero}: {resultado}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
