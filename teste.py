import pytest
from principal import somar
from principal import subtrair

##Primeiro teste

def teste_somar():
	assert somar(2,4)==6

def teste_subtrair():
	assert subtrair(10,4)==6

