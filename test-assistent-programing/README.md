# 🎓 Projeto de Assistência de Programação

Um projeto educacional com exemplos práticos de código Python, demonstrando boas práticas de programação, debugging e refatoração.

## 📋 Visão Geral

Este projeto contém três módulos principais focados em conceitos fundamentais de programação:

1. **Verificação de Números Primos** - Algoritmo otimizado com boas práticas de código
2. **Debugging** - Identificação e correção de erros comuns
3. **Refatoração** - Transformação de código legado em código limpo

## 📁 Estrutura do Projeto

```
test-assistent-programing/
├── num_primo.py                      # Função para verificar primalidade
├── debug.py                          # Código com erros para debugar
├── refatoracao.py                    # Código legado para refatorar
├── explicacao_num_primo.md           # Análise detalhada do algoritmo de primos
├── explicacao-debug.md               # Identificação e correção de erros
├── eexplicacao_refatoracao.md        # Guia de refatoração
└── README.md                         # Este arquivo
```

## 🚀 Como Usar

### 1. Verificação de Números Primos

**Arquivo:** `num_primo.py`

**Descrição:** Implementa uma função otimizada para verificar se um número é primo, utilizando:
- Type hints para melhor legibilidade
- Docstring detalhada (padrão Google)
- Algoritmo eficiente com raiz quadrada
- Validação de entrada

**Como executar:**

```bash
python num_primo.py
```

**Entrada esperada:**
```
Digite um número para verificar se é primo: 17
```

**Saída esperada:**
```
17: primo
```

**Conceitos abordados:**
- ✅ Type hints (`n: int -> bool`)
- ✅ Docstrings profissionais
- ✅ Otimização de algoritmos
- ✅ Tratamento de exceções
- ✅ Clean Code

---

### 2. Debugging - Cálculo de Preços

**Arquivo:** `debug.py`

**Descrição:** Um programa de cálculo de preços com carrinho de compras. Inclui:
- Entrada de dados (cliente e 3 itens)
- Cálculo de subtotal e imposto (10%)
- Aplicação de desconto via cupom
- Formatação de saída

**Como executar:**

```bash
python debug.py
```

**Entrada esperada:**
```
Qual é seu nome? João Silva
Quantidade do item 1: 2
Preço do item 1? 50.00
Quantidade do item 2: 1
Preço do item 2? 100.00
Quantidade do item 3: 3
Preço do item 3? 25.00
Você tem um cupom de desconto? (Digite o percentual ou 0): 10
```

**Saída esperada:**
```
===============================
 Cliente: João Silva
===============================
 Item 1:        R$ 100.00
 Item 2:        R$ 100.00
 Item 3:        R$ 75.00
-------------------------------
 Subtotal:      R$ 275.00
 Imposto (10%): R$ 27.50
 Desconto (10%): -R$ 27.50
===============================
 TOTAL:         R$ 275.00
===============================
```

**Erros corrigidos:**
- ❌ Aspas faltando em strings (SyntaxError)
- ❌ Tipos de dados incorretos (TypeError)
- ❌ Lógica de comparação errada
- ❌ Formatação inadequada

Para análise detalhada dos erros, consulte [explicacao-debug.md](explicacao-debug.md)

---

### 3. Refatoração - Cálculo de Estatísticas

**Arquivo:** `refatoracao.py`

**Descrição:** Um programa que demonstra como transformar código legado em código limpo:

**Antes (Código legado):**
```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    # ... mais código confuso
```

**Depois (Código refatorado):**
```python
def calcular_estatisticas(numeros: list[float]) -> dict:
    """Calcula estatísticas de uma lista de números."""
    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    return {
        "total": total,
        "media": media,
        "maximo": maximo,
        "minimo": minimo
    }
```

**Como executar:**

```bash
python refatoracao.py
```

**Melhorias aplicadas:**
- ✅ Nomes de variáveis descritivos
- ✅ Type hints completos
- ✅ Docstrings
- ✅ Uso de funções built-in (`sum()`, `max()`, `min()`)
- ✅ Retorno estruturado (dicionário)
- ✅ Formatação PEP 8

Para análise detalhada da refatoração, consulte [eexplicacao_refatoracao.md](eexplicacao_refatoracao.md)

---

## 📚 Documentação Detalhada

Cada módulo possui um arquivo de explicação técnica e didática:

### `explicacao_num_primo.md`
Análise linha por linha do algoritmo de verificação de primalidade, incluindo:
- Explicação técnica de cada linha
- Conceitos de otimização
- Boas práticas aplicadas

### `explicacao-debug.md`
Identificação e correção de 5 erros comuns:
- Erros de sintaxe
- Problemas de tipo de dados
- Lógica incorreta

### `eexplicacao_refatoracao.md`
Guia completo de refatoração com:
- Identificação de problemas
- Passos de melhoria
- Comparação antes/depois
- Benefícios de cada mudança

---

## 💡 Conceitos Principais

### 1. Type Hints
Indicam o tipo esperado dos parâmetros e retornos:
```python
def eh_primo(n: int) -> bool:
    ...
```

### 2. Docstrings (Padrão Google)
Documentação profissional em formato padronizado:
```python
def funcao(parametro: tipo) -> tipo_retorno:
    """Descrição breve.
    
    Descrição detalhada.
    
    Args:
        parametro: Descrição do parâmetro.
    
    Returns:
        Descrição do retorno.
    """
```

### 3. Clean Code
Práticas de código limpo:
- Nomes descritivos e significativos
- Funções com uma única responsabilidade
- Tratamento adequado de erros
- Documentação clara

### 4. Debugging
Técnicas para encontrar e corrigir erros:
- Leitura cuidadosa de mensagens de erro
- Verificação de tipos de dados
- Testes com diferentes entradas

### 5. Refatoração
Processo de melhorar código existente:
- Melhor legibilidade
- Desempenho aprimorado
- Manutenção facilitada

---

## 🛠️ Requisitos

- **Python 3.7+** (para type hints compatíveis)
- Nenhuma dependência externa

---

## 📝 Exemplos de Uso

### Exemplo 1: Testando Números Primos

```bash
$ python num_primo.py
Digite um número para verificar se é primo: 2
2: primo

$ python num_primo.py
Digite um número para verificar se é primo: 1
1: não primo

$ python num_primo.py
Digite um número para verificar se é primo: 100
100: não primo
```

### Exemplo 2: Testando o Cálculo de Preços

Execute `debug.py` e teste com diferentes combinações de itens e cupons.

### Exemplo 3: Rodando o Cálculo de Estatísticas

```bash
$ python refatoracao.py
```

---

## 🎯 Objetivos de Aprendizado

Ao explorar este projeto, você aprenderá:

- ✅ Como escrever funções com type hints
- ✅ Como documentar código com docstrings
- ✅ Como identificar e corrigir erros comuns
- ✅ Como refatorar código legado
- ✅ Boas práticas de Python (PEP 8)
- ✅ Algoritmos eficientes
- ✅ Tratamento de exceções

---

## 📞 Estrutura para Estudos

**Recomendação de ordem de aprendizado:**

1. Comece com `explicacao_num_primo.md` para entender boas práticas
2. Execute `num_primo.py` e teste com diferentes números
3. Estude `explicacao-debug.md` para aprender a identificar erros
4. Corrija os erros em `debug.py`
5. Finalize com `eexplicacao_refatoracao.md` para dominar refatoração
6. Aplique as técnicas ao `refatoracao.py`

---

## 🔗 Recursos Adicionais

- [PEP 8 - Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Type Hints Documentation](https://docs.python.org/3/library/typing.html)

---

**Versão:** 1.0  
**Última atualização:** Abril 2026  
**Autor:** Assistente de Programação
