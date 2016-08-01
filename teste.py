import pytest
from principal import soma
from principal import subtrair

##Primeiro teste

def teste_soma():
	assert soma(2,4)==6

def teste_subtrair():
	assert subtrair(10,4)==6

