![readmFIRSTsurvey](https://user-images.githubusercontent.com/76967004/115037682-1d1a7e00-9ea5-11eb-8294-7ac5353e7196.png)
![sprintpann_product](https://user-images.githubusercontent.com/76967004/115057336-4db8e280-9eba-11eb-80d7-188667170782.png)

# Base de dados A, B e C :
### Conectado à AWS com permisões ADM para a criação das bases A, B e C, escolhi o MySQL como o sistema de gerenciamento para os bancos de dados.
### Após criar o database na RDS da AWS, fiz alterações na VPC configurando o Inbound rules para estabelecer conexão ON-PREMISES ao MySQL Workbench através do end point, porta padrão do MySQL, usuário e senha definidos na AWS.

![33](https://user-images.githubusercontent.com/76967004/115065062-0e8f8f00-9ec4-11eb-9a31-f6086a6a633a.png)

# Criação das telas :
### Para a criação das telas usei a IDE-multiplataforma QT Creator / QtDesigner, que receberam conexão no Algoritmo main.py através da biblioteca PyQT5.


# Backend (Algoritmo em Python):
### O Código: No Algoritmo main.py busquei aplicar as boas práticas seguindo o padrão de Orientação a Objetos, com marcações e comentários sempre que foi necessário, mantendo um clean code para uma fácil interpretação do código a qualquer momento.
### As funções: Ao conectar a base de dados e fazer a extração dos dados críticos para a inserção das informações no frontend, criei funções as quais separam os dados ao extraí-los e faz requisições distintas.
### Para uma maior segurança dos dados críticos desenvolvi uma base de dados on-premises com relacionamento Foreign Key e Join que faz a mediação na conexão das bases A, B e C que estão em cloud na AWS.


# Machine Learning (Cálculo Score) :
### Para o cálculo do SCORE eu usei a biblioteca Sckit-learn como a principal no desenvolvimento do algoritmo Decison tree, filtrando os melhores dados das bases para treinar o algoritmo.


## :small_red_triangle_down: CLICK PARA ASSISTIR O VÍDEO (ACESSANDO AS TELAS): :small_red_triangle_down :
[![FIRSTsurvey](http://img.youtube.com/vi/AprmWjlHKO8/0.jpg)](http://www.youtube.com/watch?v=AprmWjlHKO8 "FIRSTsurvey")

### Conclusão: Nos últimos anos vimos a crescente dos dados em todo o mundo, muitos dizem que é o “novo petróleo”, mas acredito que eles vão muito além disso, não é uma tarefa fácil protegê-los. Temos que inovar e melhorar a cada dia, mas mesmo com tantos desafios nós somos capazes.

![email_entrevista_tec](https://user-images.githubusercontent.com/76967004/115035846-5eaa2980-9ea3-11eb-856b-27e11b992aeb.png)
