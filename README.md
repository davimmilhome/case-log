
# case-log

Um programa de processamento de dados feito para um case de dados logísticos no meu portfólio

--- 
O programa é estruturado da seguinte forma: 

<pre>

│   .gitignore 
│    main.py 
│    requirements.txt
│    pre-commit-config.yaml
│    README.md
├───cfg
├───general_data_entry
    ├───input
    └───output
├───integration
├───logs
├───models
├───parsers
├───services
└───utils

</pre>

**Onde:**

cfg/ - responsável por configurações gerais do projeto (ex: setup de logs) </br>

geral_data_entry/ -  entrada e saída de dados local  </br>

integration/ -  onde os dados são integrados/mergeados para serem parseados  </br>

models/ -   guarda informações gerais da estrutura dos dados </br>

parsers/ -   onde o tratamento de dados é de fato executado </br>

services/ -   serviços onde os dados são resgatados de sua fonte e servidos ao resto da aplicação </br>

utils/ -   scripts com reaproveitamento geral na aplicação </br>

main.py - Ponto de partida do programa </br>

requirements.txt - setup de pacotes python </br>

.pre-commit-config.yaml - configuraçãs dos pre-commits (padronização) do projeto </br>

## Dependências

- Bibliotecas Built-in do python
- Bibliotecas Third Party python

## Usando

Clone o repositório. </br>

Crie um ambiente virtual e após criar e ativar (importante estar dentro do ambiente virtual criado)
instale as dependências: </br>

<pre>
pip install -r requirements.txt
pre-commit install
</pre>

Execute o main certificando que os arquivos de entrada de dados foram colocados corretamente em general_da_entry/input </br>
</br>
Nesse caso, é o arquivo de entrada de dados "general_data_entry/input/base_monitoramento_entregas.csv" </br>
</br>

Nesse caso, esse procedimento é feito em caso de execução local, no futuro es services podem ser adaptados para captar os dados diretamente do banco de dados sem a necessidade de exceução local. </br>

Salve e utilize os dados de acordo com o necessário (saída em general_data_entry/output/) </br>

## Funcionamento

Os dados são processados do arquivo original, gerando duas saídas: painel de erros parseado 
e monitoramento entregas parseado.

## Autores
Davi Milhome
