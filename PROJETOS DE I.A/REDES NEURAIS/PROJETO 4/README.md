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

-- **Output 1**:
![image](https://github.com/user-attachments/assets/6151c4cd-8a5b-4515-9a87-aaddf86d2ffd)


## Conclusão 2

Através de alguns ajustes no projeto foi possível observer como construir redes neurais não é tão simples quanto parece, deixando claro, mais uma vez que, entender a importância da arquitetura e como as diferentes configurações podem impactar diretamente nos resultados.


**Arquitetura utilizada**:
![image](https://github.com/user-attachments/assets/9a0cef00-7377-431c-92e9-2e51a05f251e)



**Resultado**:
![image](https://github.com/user-attachments/assets/aeffc1bb-16a8-48ef-aad1-31cf99c8ad38)



-- **OUTPUT 2**:

![image](https://github.com/user-attachments/assets/b2f26f6a-f65e-4da9-bf08-b2e31a254337)

## OBSERVAÇÕES

Mesmo que você tente reproduzir a rede neural que eu criei, usando as mesmas configurações... Você vai ver que ainda assim, não vai ficar igual a minha rede neural. Isso acontece pois cada rede neural comece com pesos diferentes e outros pontos importantes. O comportamento de redes neurais, como você observou no TensorFlow Playground, pode gerar resultados diferentes mesmo quando a configuração parece ser a mesma. Isso acontece por causa de vários fatores estocásticos e variabilidade nos processos de treinamento. Aqui estão as principais razões pelas quais isso ocorre:

## 1. Inicialização Aleatória dos Pesos
Quando você cria uma rede neural, os pesos das conexões entre os neurônios são inicializados aleatoriamente antes do início do treinamento. Essa inicialização aleatória é um dos principais fatores que causam a variabilidade nos resultados entre execuções. Mesmo com a mesma arquitetura e configuração, a rede começará com diferentes valores de pesos, o que pode levar a diferentes trajetórias de treinamento e, portanto, resultados diferentes.

Impacto: A rede pode aprender caminhos diferentes para minimizar a função de perda devido à inicialização aleatória dos pesos.
Solução: Para garantir consistência nos resultados, pode-se usar técnicas de inicialização controlada (como inicialização de Xavier ou He), ou definir uma semente aleatória (random seed), o que ajuda a garantir que os pesos iniciais sejam sempre os mesmos.


## 2. Processo Estocástico de Otimização
A maioria dos algoritmos de otimização usados em redes neurais (como o Adam, SGD, etc.) tem uma natureza estocástica. Isso significa que durante o treinamento, as atualizações dos pesos não são determinísticas e podem ser influenciadas por mini-batches aleatórios ou por variações nas iterações de treinamento.

Impacto: Mesmo com os mesmos dados de entrada e arquitetura de rede, a ordem em que os dados são apresentados para a rede pode influenciar o treinamento, resultando em um caminho de aprendizado diferente.
Solução: Algumas plataformas permitem configurar a semente aleatória para o processo de treinamento, garantindo que a ordem dos dados e as atualizações dos pesos sejam as mesmas em diferentes execuções.

## 3. Tamanho do Mini-Batch
Alguns algoritmos de otimização, como o Stochastic Gradient Descent (SGD), dividem o conjunto de dados em pequenos lotes (mini-batches). A maneira como esses mini-batches são formados pode ser diferente entre execuções, o que pode afetar o treinamento.

Impacto: A variabilidade no tamanho dos mini-batches e na ordem dos dados pode levar a diferentes resultados.
Solução: Controlar a semente aleatória ajuda a garantir que os mini-batches sejam formados de maneira consistente.


## 4. Funções de Ativação e Gradientes
Algumas funções de ativação, como sigmoid e tanh, podem ser mais suscetíveis ao problema de gradientes desaparecendo ou explodindo, dependendo da inicialização dos pesos. Isso pode levar a convergências mais lentas ou a resultados que não são tão precisos em algumas execuções.

Impacto: Pequenas variações na inicialização dos pesos ou nas atualizações do gradiente podem fazer com que o treinamento alcance diferentes mínimos locais ou se desvie para soluções subótimas.
Solução: Usar funções de ativação como ReLU pode ajudar a mitigar esses problemas, pois elas são menos propensas ao desaparecimento de gradientes.

## 5. Diferentes Caminhos de Convergência
As redes neurais podem ter múltiplos mínimos locais na função de perda, o que significa que podem convergir para soluções diferentes dependendo de como o treinamento evolui. Mesmo com a mesma configuração, a rede pode "decidir" por diferentes caminhos durante o treinamento, chegando a soluções diferentes.

Impacto: O algoritmo de otimização pode encontrar diferentes mínimos locais em diferentes execuções.
Solução: É possível tentar configurar a semente aleatória para garantir que o treinamento comece sempre no mesmo ponto e siga o mesmo caminho de otimização.

## 6. Regularização
Se você estiver usando regularização (como Dropout ou L2 Regularization), esses métodos podem introduzir um comportamento estocástico adicional, pois Dropout, por exemplo, desativa aleatoriamente neurônios durante o treinamento.

Impacto: Isso introduz aleatoriedade na rede, e o treinamento pode ser afetado de maneiras diferentes entre execuções.
Solução: Desmarcar o Dropout ou garantir que a semente aleatória esteja configurada pode ajudar a obter resultados mais consistentes.

## 7. Ambiente de Execução
A execução da rede neural pode depender de vários fatores do ambiente de execução, como a versão do TensorFlow Playground, a máquina em que está sendo executado (local ou em nuvem) e até mesmo pequenas variações no hardware que podem afetar os cálculos de precisão flutuante.

Impacto: Diferentes execuções podem ser feitas em ambientes levemente diferentes, resultando em pequenas variações nos resultados.
Solução: Para garantir a consistência, é importante tentar rodar em um ambiente controlado ou usar o TensorFlow local com seeds e configurações específicas.


