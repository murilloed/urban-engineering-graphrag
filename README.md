# Conhecimento urbano conectado

Recuperação de documentos com evidências e relações entre ativos.

**Status: MVP de pesquisa, v0.1.0.** Estudo de caso independente inspirado
em desafios dos setores relacionados à trajetória do autor (ANA · BiomaData).
Não representa entrega contratada, resultado real ou endosso dessas organizações.
Todos os exemplos desta versão são sintéticos e reproduzíveis.

## Executar

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e .
python -m urbanrag.demo --query "rede de água do bairro cerrado"
python -m unittest discover -s tests -v
```

## Implementado

Corpus sintético com IDs e proveniência; índice vetorial TF-IDF/cosseno; expansão de grafo; resposta extrativa com citações e abstinência; adapter MongoDB opcional. Nenhuma chamada a LLM nesta versão.

## Próximas etapas

Embeddings semânticos, banco vetorial e grafo persistentes; LLM com citações verificadas; avaliação de recuperação; ingestão de PDFs públicos licenciados; controle de versões.

## Reprodutibilidade e avaliação

A demonstração grava `artifacts/report.json`, com parâmetros e métricas.
Resultados de dados sintéticos validam o fluxo; não demonstram desempenho em produção.
Use a mesma semente e orçamento computacional para comparar abordagens.
Consulte `docs/design.md` para decisões e limitações.

## Contribuição

Abra uma issue com objetivo e critério de aceite. Entregue mudanças pequenas,
revisadas e acompanhadas de testes de comportamento. Não inclua dados de clientes,
credenciais ou resultados sem proveniência. Licença MIT para código e dados sintéticos próprios.
