# travis_trainning [![Build Status](https://travis-ci.org/cs-bruno-novo/travis_trainning.svg?branch=master)](https://travis-ci.org/cs-bruno-novo/travis_trainning)

Olá, aqui faremos uma integração do nosso código, em python, nossos testes, em python, utilizando o travis para nos ajudar a visualizar e gerenciar melhor nosso código.


## Pré-requisitos

Antes de começarmos,precisamos configurar nosso ambiente para testarmos nosso código antes de commitá-lo no github e termos certeza de que está funcionando.

Instale o pytest, um pacote do python para testarmos nosso código em python. Digite o comando abaixo:
´´´sh
  pip install -U pytest
´´´
Depois teste a versão que instalada:
´´´sh
  pytest --version
´´´
 :warning: Se você estiver utilizando o OpenSuse, utilize py.test para instalar e testarmos

 Agora podemos testar nossos códigos sem problemas. Vamos colocar as mãos na massa:

 Depois de ja ter criado os arquivos de testes, por exemplo teste.py, vamos testá-los:

 ´´´sh
  pytest teste.py
 ´´´

Se o resultado foi ok, maravilha! Caso contrário, revise seu código ou os passos da instalação acima.
