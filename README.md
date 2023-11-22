# Projeto: Gerando Planilhas Tabeladas e Títulos para Resumos de Manuscritos

## Visão Geral

Este projeto tem como objetivo organizar relatórios por colunas na planilha Excel e gerar títulos para resumos de manuscritos usando o modelo GPT-3.5 Turbo da OpenAI. Os script 'geraPlanilha' lê um arquivo Excel e o organiza em colunas capturando os títulos das colunas no texto e seus valores respectivos, já o script 'geraTitulo' gera um título para cada resumo e, em seguida, escreve os títulos de volta para o arquivo Excel.

## Erros a serem Corrigidos


### Erro 1: Requisições em Excesso

O script está fazendo requisições excessivas para a API OpenAI, o que está impedindo a geração de títulos com base nos resumos. Isso precisa ser tratado implementando o controle de limites de taxa e otimizando as requisições.

### Erro 2: Colunas Não Necessárias

O script deve incluir uma função que remove colunas não necessárias que não serão necessárias para o Rossio. Isso precisa ser adicionado ao script.

### Erro 3: Compatibilidade com Diferentes Tipos de Relatórios

O script precisa ser testado com diferentes tipos de relatórios, como relatórios audiovisuais e entrevistas, para garantir que funcione corretamente com esses tipos de dados.

## Referências

- [API OpenAI](https://www.openai.com/api)
- [Pandas read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)
- [Pandas DataFrame.to_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html)
- [Dicas de Limite de Taxa OpenAI](https://help.openai.com/en/articles/6891753-rate-limit-advice)
- [Exemplo de Limite de Taxa OpenAI](https://cookbook.openai.com/examples/how_to_handle_rate_limits)