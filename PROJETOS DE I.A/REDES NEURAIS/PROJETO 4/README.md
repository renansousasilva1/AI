# Projeto 4 - Classificação com Redes Neurais no TensorFlow Playground

## Objetivo

O objetivo deste projeto é criar e treinar uma rede neural para classificar corretamente dois tipos de pontos (laranja e azul) dispostos de forma espiral. A tarefa é ajustar a arquitetura da rede neural, utilizando camadas ocultas e neurônios, para alcançar uma precisão alta na classificação.

## Descrição do Problema

O problema envolve a criação de uma rede neural capaz de classificar pontos distribuídos de forma espiral, com dois grupos distintos:
- **Pontos Laranja**
- **Pontos Azul**

O objetivo final é que a rede neural consiga traçar as fronteiras de decisão que separam esses dois grupos de pontos de forma eficiente.

## Como Resolver o Problema

A solução foi abordada utilizando o **TensorFlow Playground**, uma plataforma interativa para explorar redes neurais. A principal tarefa foi adicionar camadas ocultas e ajustar o número de neurônios para melhorar a capacidade de classificação da rede.

### Estratégia de Arquitetura
A arquitetura da rede neural foi ajustada da seguinte maneira:
- **Camada de Entrada**: 2 neurônios, correspondendo às duas dimensões dos dados (x, y).
- **Camada Oculta**: Iniciamos com uma camada oculta de 8 neurônios, mas foi necessário adicionar mais camadas ocultas para melhorar o desempenho.
- **Camadas Ocultas**: O modelo foi aprimorado com até **6 camadas ocultas**, com um máximo de **8 neurônios por camada**.


A meta foi atingir uma **perda de teste menor ou igual a 0,05** e uma **perda de treinamento menor ou igual a 0,02**.

## Resultados

Após a configuração da rede neural, o modelo alcançou os seguintes resultados:
- **Perda de Treinamento**: 0.007
- **Perda de Teste**: 0.006
- ![image](https://github.com/user-attachments/assets/66e8f588-608a-44b3-ae1e-fba03246f3a1)


A rede foi capaz de separar adequadamente os pontos laranja e azul, como mostrado na captura de tela abaixo.

![image](https://github.com/user-attachments/assets/865d9bb5-f53b-4750-a397-6dab8e59ece8)


## Dicas e Aprendizados

Aqui estão algumas dicas que podem ajudar a melhorar sua experiência ao usar o TensorFlow Playground:

1. **Aumento de Camadas e Neurônios**:
   Muitas vezes, é tentador aumentar o número de camadas ou neurônios esperando que isso melhore o desempenho. No entanto, **aumento excessivo pode não levar à melhoria do desempenho** e, em alguns casos, pode até piorar o modelo devido ao **overfitting**.

2. **A Base de Dados**:
   Aumentar a base de dados nem sempre resulta em uma melhoria direta no desempenho. O que realmente importa é a qualidade da rede neural e a arquitetura da rede para o problema em questão.

## Conclusão

Através deste projeto, foi possível aprender sobre como construir redes neurais eficazes, entender a importância da arquitetura e como as diferentes configurações podem impactar diretamente os resultados.
![image](https://github.com/user-attachments/assets/c0957d31-1a26-4e90-966f-857abe058529)


