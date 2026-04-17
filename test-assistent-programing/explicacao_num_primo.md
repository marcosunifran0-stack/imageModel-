### Explicação Técnica e Didática do Código em num_primo.py (Versão Otimizada com Clean Code)

Vou explicar o código linha por linha de forma técnica (usando conceitos de programação Python) e didática (explicando o propósito e o raciocínio por trás de cada parte). O código foi refatorado aplicando técnicas de clean code, como: importações no topo, type hints, docstring detalhada, nomes de variáveis descritivos e separação de responsabilidades. Aqui vai a análise:

1. **`import math`**  
   Importa o módulo `math` da biblioteca padrão do Python no topo do arquivo. Isso segue boas práticas de clean code, evitando importações dentro de funções e garantindo que dependências sejam claras desde o início. O módulo fornece funções matemáticas, como `isqrt` (raiz quadrada inteira).

2. **`def eh_primo(n: int) -> bool:`**  
   Define uma função chamada `eh_primo` com type hints: `n: int` indica que o parâmetro é um inteiro, e `-> bool` especifica que a função retorna um booleano. Isso melhora a legibilidade e permite verificações de tipo em IDEs modernas. A função verifica se `n` é primo.

3. **`"""`**  
   Início da docstring (documentação da função). Docstrings detalhadas são essenciais para clean code, explicando o que a função faz, seus parâmetros e retorno.

4. **`Verifica se um número é primo.`**  
   Descrição geral da função.

5. **`Um número primo é um inteiro maior que 1 que não tem divisores positivos`**  
   **`além de 1 e ele mesmo.`**  
   Explicação conceitual do que é um primo, tornando a docstring educativa.

6. **`Args:`**  
   Seção da docstring para argumentos.

7. **`    n (int): O número a ser verificado.`**  
   Descrição do parâmetro `n`.

8. **`Returns:`**  
   Seção para o retorno.

9. **`    bool: True se n for primo, False caso contrário.`**  
   Descrição do valor de retorno.

10. **`Raises:`**  
    Seção para exceções (neste caso, nenhuma).

11. **`    Nenhum. Assume que n é um inteiro.`**  
    Indica que a função assume entrada válida, evitando complexidade desnecessária.

12. **`"""`**  
    Fim da docstring.

13. **`if n <= 1:`**  
    Condição para casos base: números ≤ 1 não são primos.

14. **`    return False`**  
    Retorna `False` para n ≤ 1.

15. **`if n <= 3:`**  
    Condição para 2 e 3, que são primos.

16. **`    return True`**  
    Retorna `True` para n = 2 ou 3.

17. **`if n % 2 == 0:`**  
    Verifica se n é par (exceto 2, já tratado).

18. **`    return False`**  
    Retorna `False` para pares > 2.

19. **`limite = math.isqrt(n)`**  
    Calcula a raiz quadrada inteira de n para otimizar o loop, limitando verificações a √n.

20. **`for i in range(3, limite + 1, 2):`**  
    Loop sobre divisores ímpares de 3 até limite.

21. **`    if n % i == 0:`**  
        Verifica se n é divisível por i.

22. **`        return False`**  
        Retorna `False` se divisor encontrado.

23. **`return True`**  
    Se nenhum divisor encontrado, retorna `True`.

24. **`if __name__ == '__main__':`**  
    Bloco para execução direta, separando teste do código principal. Agora interativo, solicitando entrada do usuário.

25. **`    try:`**  
        Inicia um bloco try-except para capturar erros de entrada, como digitar algo que não seja um número.

26. **`        numero = int(input("Digite um número para verificar se é primo: "))`**  
        Solicita ao usuário um número via input, converte para inteiro. `input()` lê uma string, e `int()` a converte.

27. **`        resultado = "primo" if eh_primo(numero) else "não primo"`**  
        Calcula o resultado como string, melhorando legibilidade.

28. **`        print(f"{numero}: {resultado}")`**  
        Imprime o resultado formatado.

29. **`    except ValueError:`**  
        Captura exceções se a conversão para int falhar (e.g., usuário digita letras).

30. **`        print("Por favor, digite um número inteiro válido.")`**  
        Mensagem de erro amigável para entrada inválida.

### Observações Gerais
- **Clean Code Aplicado**: Importações no topo, type hints, docstring completa, nomes descritivos (e.g., `casos_teste` em vez de `exemplos`), separação de lógica de teste.
- **Eficiência**: Mantida (O(√n)), com otimizações para pares e limite de √n.
- **Manutenibilidade**: Código mais legível, documentado e estruturado para futuras alterações.
- **Execução**: Rode o arquivo para ver os testes; a função pode ser importada em outros módulos.

Se precisar de mais ajustes, é só pedir!
