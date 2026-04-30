# 🐛 Debug - Análise de Erros no Código

## Resumo
O código contém **5 erros** que causariam falhas na execução. Abaixo está a análise detalhada de cada um.

---

## ❌ ERRO 1: Aspas Faltando na String (Linha 5)

### Identificação
```python
item1 = float(input(Preço do item 1? ))
```

### Causa
A string `"Preço do item 1? "` está faltando as aspas (duplas ou simples). Sem aspas, o Python tenta interpretar `Preço` como uma variável, o que não existe.

### Resultado
```
SyntaxError: invalid syntax
```

### Correção
```python
item1 = float(input("Preço do item 1? "))
```

---

## ❌ ERRO 2: Tipo de Dado Incorreto (Linha 23)

### Identificação
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

### Causa
A função `input()` retorna uma **string**, não um número. Na linha 24, o código tenta dividir essa string por 100, o que é impossível. Além disso, a linha 42 tenta comparar uma string com o número 0 (`if desconto_cupom > 0`), outra operação inválida.

### Resultado
```
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

### Correção
Converter a entrada para `float`:
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

---

## ❌ ERRO 3: F-String Sem o Prefixo 'f' (Linha 37)

### Identificação
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

### Causa
A string contém a variável entre chaves `{}`, mas falta o prefixo `f` que ativa a formatação de f-string. Sem ele, Python trata isso como uma string literal comum.

### Resultado
Será impresso literalmente: `" Item 2:        R$ {total_item2:.2f}"` ao invés do valor real.

### Correção
Adicionar o prefixo `f`:
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

---

## ❌ ERRO 4: Indentação Incorreta (Linhas 42-43)

### Identificação
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

### Causa
O bloco `print` dentro do `if` está sem indentação. Em Python, todo código dentro de um bloco condicional, loop ou função **deve** estar indentado com 4 espaços.

### Resultado
```
IndentationError: expected an indented block
```

### Correção
Adicionar 4 espaços de indentação:
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

## ✅ CÓDIGO CORRIGIDO

```python
#                                      CÓDIGO CORRIGIDO                           
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```

---

## 📊 Tabela Resumida

| # | Linha | Erro | Causa | Solução |
|---|-------|------|-------|---------|
| 1 | 5 | Falta aspas | `input(Preço do item 1? )` sem aspas | Adicionar `"` e `"` |
| 2 | 23 | Tipo string | `input()` retorna string | Usar `float(input(...))` |
| 3 | 37 | Falta 'f' | String literal sem formatação | Adicionar `f` antes das aspas |
| 4 | 42-43 | Indentação | Bloco if sem identação | Adicionar 4 espaços |

