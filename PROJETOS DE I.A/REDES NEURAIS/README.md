# Projeto 1 - Classificação com TensorFlow Playground

Este repositório documenta o uso do **TensorFlow Playground** para realizar uma tarefa de classificação simples utilizando uma rede neural com uma camada oculta.

## Objetivo

O objetivo deste projeto é utilizar uma rede neural simples, com apenas um neurônio, para classificar dois conjuntos de dados (azul e laranja). O treinamento é feito usando o **TensorFlow Playground**, uma interface web interativa.

## Configuração Utilizada no TensorFlow Playground

- **Taxa de Aprendizado**: 0,03
- **Função de Ativação**: ReLU
- **Regularização**: Nenhuma
- **Proporção de Treinamento/Teste**: 50%
- **Ruído**: 0
- **Tamanho do Lote**: 10
- **Número de Neurônios na Camada Oculta**: 1

## Como Visualizar o Projeto

O código foi feito no **TensorFlow Playground**, e não em um ambiente local, por isso não há código Python diretamente no repositório. O repositório contém imagens que mostram a configuração e os resultados do treinamento.

## Resultados

Após o treinamento, a rede neural foi capaz de classificar com sucesso os dois grupos de dados (azul e laranja). Abaixo estão as imagens que mostram a configuração da rede e o gráfico de perda durante o treinamento.

### Configuração da Rede
![image](https://github.com/user-attachments/assets/9265be9c-b346-40b1-ba35-3d746b7ce139)

## Aparência da Rede com 1 neurônio
![image](https://github.com/user-attachments/assets/20b8156a-7c56-4264-a94b-4312a79a5dc8)


### Resultado do Treinamento
![image](https://github.com/user-attachments/assets/0cf570f2-65fe-47c2-a417-06ebd108faeb)



## Documentação Detalhada

Este rede neural busca demonstrar que é possível dividir dois grupos por uma linha com apenas um neurônio.

## Objetivo

O projeto tem como objetivo utilizar uma rede neural simples para resolver um problema de classificação binária (dois conjuntos de dados: azul e laranja). A tarefa é treinar a rede para que ela consiga classificar corretamente os dados.

## Arquitetura da Rede Neural

A rede neural criada no **TensorFlow Playground** possui os seguintes componentes:

- **Entrada**: 2 características (X1 e X2).
- **Camada Oculta**: 1 neurônio, com a função de ativação **ReLU**.
- **Saída**: 1 neurônio de saída, que decide se a entrada pertence à classe azul ou laranja.

## Configuração no TensorFlow Playground

A seguir, estão os parâmetros de configuração definidos para a rede:

- **Taxa de Aprendizado**: 0,03 (determinando a rapidez com que os pesos são ajustados).
- **Função de Ativação**: ReLU (para evitar o problema do desaparecimento do gradiente).
- **Proporção de Treinamento/Teste**: 50% para cada.
- **Ruído**: 0 (sem ruído nos dados para facilitar a classificação).
- **Tamanho do Lote**: 10 (quantidade de amostras utilizadas por vez durante o treinamento).

## Resultados

Após o treinamento, o modelo conseguiu separar com sucesso os dois grupos de dados. A curva de perda do treinamento e do teste se estabilizou em valores baixos, mostrando que o modelo aprendeu a fazer a classificação.

