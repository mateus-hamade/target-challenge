## Target Challenge - Estágio 2024

1- Observe o trecho de código abaixo:

  int INDICE = 13, SOMA = 0, K = 0;
  
  enquanto K < INDICE faça
  
  {
  
  K = K + 1;
  
  SOMA = SOMA + K;
  
  }
  
  imprimir(SOMA);
  
  
  Ao final do processamento, qual será o valor da variável SOMA?
  `ao final do processamento do valor da variável soma será 91`


2- Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
   
  
  IMPORTANTE:
  
  Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

  [resposta](https://github.com/mateus-hamade/target-challenge/blob/master/contains_fibonnaci.py)

3- Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, `9`

b) 2, 4, 8, 16, 32, 64, `128`

c) 0, 1, 4, 9, 16, 25, 36, `49`

d) 4, 16, 36, 64, `100`

e) 1, 1, 2, 3, 5, 8, `13`

f) 2,10, 12, 16, 17, 18, 19, `20`



4- Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

1. Ligo o interruptor, deixo por um tempo e desligo
2. ligo um segundo interruptor.
3. Vou a uma das 3 salas. (1ª ida)
4. Se a lâmpada estiver *apagada e quente* siginifica que o interruptor que ficou ligado por mais tempo é resposável por esta lâmpada.
5. Se a lâmpada estiver *acesa* significa que o interruptor que ficou ligado é resposável por ela.
6. Se a lâmpada estiver *apagada e fria* significa que é o interruptor que não foi alterado.
7. Volto até a sala dos interruptores.
8. Sabendo que um interruptor é responsável por uma das salas, basta ligar 1 dos 2 restantes.
9. Vou até uma outra sala e vejo se ela está acesa ou apagada. (2ª ida)
10. Por consequencia do passo 9, é possível descobrir qual interruptor é responsável por sua lâmpada.

 

5- Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
[resposta](https://github.com/mateus-hamade/target-challenge/blob/master/string_reverse.py)
