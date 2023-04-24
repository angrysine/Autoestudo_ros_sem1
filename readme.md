# Primeira ponderada de programação
Criei um nó que controlava a tartaruga do exemplo turtle sim do ros para criar um losango.Para isso foi necessário realizar os seguintes passos:

1. Instalar o  wsl 
2. criei o repositório do git
3. usei o comando do ros2 para criar um package (ros2 pkg create)
4 criei meu código /src/my_turtle_controller/my_turtle_controller/draw_losango.py 
5. atualizei as dependências e rodei o comando colcon build
6. rodei meu publisher e o turtlesim

Para criar o código que desenha um losango foi necessário criar uma classe Draw que herdava do nodo rlcpy. Essa classe ao incializar cria um publisher para escreve rmensagens no tópico 'turtle1/cmd_vel' e manda uma informação do tipo twist. Usamos um timer para que o nodo mande uma informação a cada 1 segundo, essa informação pode ser de rotação ou translação dependendo da fase do desenho que nos encontramos. Como a velocidade angular está em radianos importamos o modulo math para fazer a tartaruga rodar e criar um losango composto de dois triângulos equiláteros.


link vídeo: https://drive.google.com/drive/folders/1nxwl0dmSbdywJfdFCEqSY1TMsjkazExP?usp=sharing