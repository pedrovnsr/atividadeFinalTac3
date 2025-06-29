
# Integração com APIs e Testes Automatizados

Este projeto realiza testes de API para os sites Jsonplaceholder e Dummy Rest API. Além disso, também executa testes de ponta a ponta na interface web dos sites citados.

## Ferramentas utilizadas

 - Pytest: Ferramenta utilizada para escrita e execução de testes
 - Unittest: Biblioteca padrão do python para escrita de testes unitários no estilo JUnit
 - Selenium: Automatização de tarefas no navegador.
 - Playwright: Escrita de testes de ponta a ponta em navegador web.
 - APIdog: interface gráfica para desenvolvimento e testes de API.

## Instalação de dependências

Antes de instalar as bibliotecas a cima pode-se utilizar um ambiente virtual, para que as bibliotecas e os testes tenham um ambiente isolado no sistema.

Caso seja optado por utilizar um ambiente virtual utilizando a biblioteca venv é necessário executar os comandos:

```sh
python -m venv <venv>
source <venv>/bin/activate
```

Para instalar as bibliotecas, execute:

```sh
pip install -r requirements.txt
```

### Instalação do Playwright

Além das dependências listadas no arquivo de requerimentos, é necessário instalar o navegador utilizado pelo Playwright, isso pode ser feito utilizando o comando: 

```sh
playwright install chrome
```

### Instalação do Selenium

A instalação do navegador e do driver utilizado pela biblioteca é feito de forma automática ao executar os testes pela primeira vez.

### Instalação do API Dog

A ferramenta pode ser utilizado sem instalação através do site [app.apidog.com](app.apidog.com).

## Execução dos testes

Após instalação das bibliotecas os testes podem ser executados com o comando:

```sh
pytest

# Para executar os testes imprimindo logs:
pytest --log-cli-level=INFO

# Para executar os testes e gerar relatório
pytest --html report.html

# Para executar os testes da biblioteca unittest
python -m unittest
```

