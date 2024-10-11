# Exercícios Práticos de TDD

Linguagem de Programação:
 - Python com framework unittest ou pytest

<br>

**JUnit e TDD**

<br/>

<details>
<summary>Exercício 1</summary>

### :pencil: Sobre
<br/>

Especifique um conjunto de casos de teste para testar o programa a seguir:

O programa lê três valores inteiros que representam os lados de um triângulo. 
O programa informa se os lados formam um triângulo:
 - Escaleno;
 - Isósceles;
 - Equilátero.

<br/>

### ✏️

1. Defina o esqueleto de uma classe Java|TypeScript|Python que resolva o problema acima.
2. Escreva os casos de teste para a linguagem de programação adotada, para as seguintes situações:
    1. Triângulo escaleno válido
    2. Triângulo isósceles válido
    3. Triângulo equilatero válido
    4. Pelo menos 3 casos de teste (CTs) para isósceles válido contendo a permutação dos mesmos valores
    5. Um valor zero
    6. Um valor negativo
    7. A soma de 2 lados é igual ao teceiro lado
    8. Para o item acima, um CT para cada permutação de valores
    9. CT em que a soma de 2 lados é menor que o terceiro lado
    10. Para o item acima, um CT para cada permutação de valores
    11. Um CT para os três valores iguais a zero

</details>

<br>

<details>
<summary>Exercício 2</summary>

### :pencil: Sobre
<br/>

Considerando o conjunto de classes abaixo. Utilizando a ténica de TDD, implemente o método **isValidToInclude()**. Esse método deve retornar uma lista de erros com base no objeto Person passado como parâmetro. Deve ser validado:

 - O nome é composto por ao menos 2 partes e deve ser composto de letras
 - A idade deve estar no intervalo [1, 200]
 - O objeto Person deve ter pelo menos um objeto da classe Email associado
 - O nome da classe Email deve ter @ e . sendo que cada parte deve ter ao menos um caractere

</details>

<br>

<details>
<summary>Exercício 3</summary>

### :pencil: Sobre
<br/>

Seguindo a técnica de Test Driven Development (TDD), desenvolva as classes necessárias para resolver o problema descrito abaixo:

O participante deve implementar uma calculadora de salário de funcionários. Um funcionário contem nome, email, salário-base e cargo. De acordo com seu cargo, a regra para cálculo do salário líquido é diferente:

 - Caso o cargo seja DESENVOLVEDOR, o funcionário terá desconto de 20% caso o salário seja maior ou igual que 3.000,00, ou apenas 10% caso o salário seja menor que isso;
 - Caso o cargo seja DBA, o funcionário terá desconto de 25% caso o salário seja maior ou igual que 2.000,00, ou apenas 15% caso o salário seja menor que isso;
 - Caso o cargo seja TESTADOR, o funcionário terá desconto de 25% caso o salário seja maior ou igual que 2.000,00, ou apenas 15% caso o salário seja menor que isso; 
 - Caso o cargo seja GERENTE, o funcionário terá desconto de 30% caso o salário seja maior ou igual que 5.000,00, ou apenas 20% caso o salário seja menor que isso.

</details>

<br>

## :scroll: Procedimentos para Executação
<br/>

1. Precisa ter instalado o Python e o `pytest`, para instalá-lo:

  ```
  pip install pytest
  ```

2. Entre na pasta coerente do exercício, tipo:

  ```
  cd exerc3
  ```

3. Para rodar os testes, execute o comando:

  ```
  pytest test.py
  ```