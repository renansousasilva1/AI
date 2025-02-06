# Projeto 3: Classificação com 4 Quadrantes

Este projeto utiliza o **TensorFlow Playground** para resolver um problema de **classificação não linear**, onde os dados estão distribuídos em 4 quadrantes dentro de um quadrado. O objetivo é classificar corretamente os pontos azuis e laranja que estão localizados nesses quadrantes.

## Desafio

A tarefa é classificar pontos com base em sua posição dentro de um quadrante. Como a separação entre as classes não é linear, não podemos resolver o problema com uma única linha reta.
![image](https://github.com/user-attachments/assets/9ce2b15c-a3c4-4c9f-bfe2-d2c07a95ecf1)

## Configurações do Modelo
![image](https://github.com/user-attachments/assets/8c8f2e81-9375-4c69-a09c-d2b6ece353c0)

- **Taxa de Aprendizado**: 0,03
- **Função de Ativação**: ReLU
- **Tamanho do Lote**: 10
- **Proporção de Dados de Treinamento e Teste**: 50%

## Resultados do Experimento

### 1. Inicialização Inadequada com 3 Neurônios

Com **3 neurônios**, a rede não conseguiu classificar corretamente os pontos, especialmente nas partes superiores dos quadrantes.

![image](https://github.com/user-attachments/assets/1ba06bf8-c6fc-463d-a463-5bde3f4f831b)


### 2. Inicialização Adequada com 3 Neurônios

Após a **inicialização adequada dos pesos**, a rede conseguiu classificar os pontos corretamente.

![image](https://github.com/user-attachments/assets/c8a2479f-5ec2-419b-b522-9747ed33f8e9)


### 3. Com 5 Neurônios

Com **5 neurônios**, a rede apresentou resultados estáveis e precisos, resolvendo o problema de classificação com alta confiabilidade.

![image](https://github.com/user-attachments/assets/c7144273-0890-4330-af03-478b9869eb80)


## Como Executar

Para replicar este experimento:

1. Acesse o **[TensorFlow Playground](https://playground.tensorflow.org/)**.
2. Selecione as configurações descritas acima.
3. Use o **conjunto de dados com 4 quadrantes**.
4. Teste a rede com 3 e 5 neurônios na camada oculta.
5. Observe os resultados de **perda de treinamento** e **perda de teste** para diferentes números de neurônios.

## Conclusão

O **Projeto 3** destaca a importância da **inicialização dos pesos** e como a adição de **neurônios na camada oculta** pode melhorar a capacidade da rede em resolver problemas de classificação não linear, tornando o modelo mais robusto e confiável.
![image](https://github.com/user-attachments/assets/feca531c-a1d2-4603-92f8-572e3ae3d597)
