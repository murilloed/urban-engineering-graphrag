# Decisões de engenharia

## Escopo
Recuperação de documentos com evidências e relações entre ativos. O cenário é um benchmark sintético independente.

## Entregas atuais
Corpus sintético com IDs e proveniência; índice vetorial TF-IDF/cosseno; expansão de grafo; resposta extrativa com citações e abstinência; adapter MongoDB opcional. Nenhuma chamada a LLM nesta versão.

## Evolução
Embeddings semânticos, banco vetorial e grafo persistentes; LLM com citações verificadas; avaliação de recuperação; ingestão de PDFs públicos licenciados; controle de versões.

## Qualidade e colaboração
CI executa testes de comportamento. Revisões devem conferir contratos de entrada,
invariantes, divisão de dados e métricas. Evoluções de infraestrutura exigem avaliação
de custo, autorização e observabilidade. Não há recursos cloud provisionados.

## Limitações
Validar a hipótese com dados públicos licenciados ou dados autorizados antes de uso
operacional. Relatar baseline, várias sementes, intervalos de incerteza, consumo
de recursos e resultados negativos. O backlog não constitui funcionalidade implementada.
