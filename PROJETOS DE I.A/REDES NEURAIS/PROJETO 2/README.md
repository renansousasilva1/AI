![image](https://github.com/user-attachments/assets/4a840e7d-0c33-4460-afbc-1a01e77f456b)## Projeto 2: Classificação com Rede Neural para Dados Circulares

Este repositório contém a implementação do **Projeto 2**, que usa o **TensorFlow Playground** para resolver um problema de **classificação não linear**. O objetivo é classificar pontos distribuídos em uma forma **circular**, onde a classe azul está dentro de um círculo e a classe laranja está fora dele.

## Objetivo
No Projeto 2, o objetivo é classificar dois conjuntos de dados que possuem uma distribuição circular. O desafio aqui é que os dados azuis estão dentro do círculo, e os dados laranjas estão fora, o que impossibilita o uso de uma simples linha reta para separá-los. Vamos ver o processo de como a rede neural foi configurada e como a complexidade aumentou à medida que novos neurônios foram adicionados.

### Desafio:
- Não é possível separar os dados de forma simples usando uma **linha reta**, pois a separação entre as classes segue uma forma **circular**. 
![image](https://github.com/user-attachments/assets/4e6257e5-b45b-4719-add6-2fc29cbb01e9)

- A rede neural precisa aprender representações não lineares para resolver esse problema.
![image](https://github.com/user-attachments/assets/d709ba6d-dfe3-4d83-b066-6a9271fb4fb3)

## Estrutura do Modelo
![image](https://github.com/user-attachments/assets/d6272ce7-b2c6-4a28-81d8-d617e97981f4)

### Camadas da Rede Neural

- **Camada de Entrada**: Recebe as coordenadas dos pontos como entradas (\(X_1\) e \(X_2\)).
- **Camada Oculta**: Inicialmente, com um neurônio, depois aumentada para 2 e 3 neurônios.
- **Camada de Saída**: Com um único neurônio para classificar os pontos em duas classes: azul e laranja.

### Função de Ativação

A função de ativação usada na camada oculta é a **ReLU (Rectified Linear Unit)**, que permite à rede aprender padrões não lineares.


### Processo de Treinamento

1. **Início com 1 neurônio**:
   - Com 1 neurônio, a rede tenta separar os dados com uma linha reta, mas falha devido à separação circular dos dados.

![image](https://github.com/user-attachments/assets/74e1ab65-516b-4a8c-b935-deaa0b2fb0d7)


2. **Adicionando neurônios**:
   ![image](https://github.com/user-attachments/assets/b2c5fc35-b9cc-4cb0-af8f-ea7089350bda)

   - Ao adicionar mais neurônios à camada oculta (2 neurônios), a rede melhora a capacidade de separação, mas ainda há falhas na classificação, pois a linha de decisão não consegue separar todos os pontos.

   ![image](https://github.com/user-attachments/assets/39a1b49f-3a2e-41c6-a4c0-77fbc8f0a566)


4. **Com 3 neurônios**:
   ![image](https://github.com/user-attachments/assets/8b6b9eb2-c1ac-4a78-8e4b-dcf7c2ebbad8)

   - Agora, com **3 neurônios**, a rede consegue separar os dados corretamente, atingindo uma classificação precisa.

   ![image](https://github.com/user-attachments/assets/4c3c3680-bb9f-4667-929c-be14e0c025a6)


### Configurações Utilizadas

- **Taxa de Aprendizado**: 0,03
- **Função de Ativação**: ReLU
- **Tamanho do Lote**: 10
- **Proporção de Dados de Treinamento e Teste**: 50%
- **Ruído**: 0 (para facilitar a localização da solução)
- **Regularização**: Não foi aplicada (não necessária para este problema simples)

## Como Executar

Este projeto foi desenvolvido no **TensorFlow Playground**, uma plataforma web que permite a criação e treinamento de redes neurais de forma interativa. Para replicar o experimento:

1. Acesse o **[TensorFlow Playground](https://playground.tensorflow.org/)**.
2. Selecione as configurações conforme descrito:
   - **Taxa de Aprendizado**: 0,03
   - **Função de Ativação**: ReLU
   - **Tamanho do Lote**: 10
   - **Proporção de Dados de Treinamento e Teste**: 50%
   - **Ruído**: 0
3. Selecione o **conjunto de dados circular**.
![image](https://github.com/user-attachments/assets/fccd7ab8-6451-4bfa-a26d-b52f72b1e9fa)

4. Adicione neurônios na camada oculta para experimentar com 1, 2 e 3 neurônios.
5. Observe os resultados de **perda de treinamento** e **perda de teste** para diferentes números de neurônios.

## Conclusão

O **Projeto 2** ilustra a importância de usar redes neurais com **múltiplos neurônios** na camada oculta para resolver problemas de **classificação não linear**, como a separação circular dos dados. Com a adição de neurônios, a rede consegue compreender e aprender padrões mais complexos e realizar uma classificação precisa.

Este experimento demonstra como redes neurais podem ser ajustadas e configuradas para resolver problemas que não podem ser resolvidos com simples operações lineares.


