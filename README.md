# ML_final_project# Projeto Final de Aprendizagem de Máquina

Repositório para o projeto de Aprendizagem de Máquina envolvendo Redes Neurais, Árvore de Decisão e SVM.
Tema do projeto: Classificação de Projetos de Leis da Câmara dos Deputados.

## Desenvolvedores
- [@kamilyassis](https://www.github.com/kamilyassis)
- [@adriel1ft](https://github.com/adriel1ft)

## Estrutura do Projeto
- `collecting_data/`: Contém os arquivos com os códigos responsáveis pelas requisições do projeto.
- `data/`: Contém os datasets gerados com os dados das requisições após limpeza e analise.
- `img/`: Guarda uma imagem oficial do governo que ilustra o processo de aprovação de uma Lei. Além de imagens que foram usadas para o entendimento do cenário politico do país.

## Etapas

- Coleta de dado 
* Scrapping em API's do GOV para coleta de Proposições

- Processamento dos dados
* Remoção das Preposições != PL
* Remoção das PL != (Arquivada ou Tramitada)
* Medir a inclinação politica dos partidos (é_oposicao, é_aliado)
* influência dos partidos (porcentagem_da_bancada_do_partid_q_propos a lei)
