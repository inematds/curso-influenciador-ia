# Revisão simulada das traduções EN/ES — partes 1 e 3a

## Cobertura e integridade

- `en-1.json`: 554/554 unidades; cobertura exata e `validate()` sem erros.
- `es-1.json`: 554/554 unidades; cobertura exata e `validate()` sem erros.
- `en-3a.json`: 277/277 unidades; cobertura exata e `validate()` sem erros.
- `es-3a.json`: tradução concluída pelo agente B (277/277), integrada e validada pelo coordenador; revisão em revisao-i18n-2-3b.md.

As traduções mantêm a ordem e o conteúdo dos números, placeholders, URLs, nomes de arquivo, tags e atributos HTML. Textos de instrução entre `&lt;...&gt;` foram traduzidos; o atributo `data-def` foi mantido exatamente como na fonte, pois o montador trata esse atributo separadamente. A Lia Lume continua descrita como personagem adulta fictícia. O texto não afirma que alunos publicaram, venderam ou obtiveram resultados reais.

## Revisão simulada

A leitura por amostragem cobriu navegação, fichas operacionais, aulas, escolhas de atividade, chamadas para a próxima aula e instruções de preparação e execução. Os avisos distinguem origem por IA de relação comercial; as tarefas continuam no imperativo dirigido ao aluno; os estados de calendário e acompanhamento não apresentam planejamento como execução. Não identifiquei contradição material entre a fonte e os três catálogos concluídos.

A amostragem paralela de `en/es-2.json` e `en/es-3b.json` não encontrou mudança de sentido material nos exemplos lidos. As ocorrências em espanhol do título `Influenciador IA v6.2` foram confirmadas como nome do curso/marca da coleção e podem permanecer sem localização. Nenhum catálogo de B foi alterado.

Esta é uma revisão simulada durante a produção, sem avaliador humano externo. Ela não substitui leitura final após a integração dos quatro arquivos.

## Ajuste final após auditoria EN

Foram criados 11 overrides em `i18n/en-overrides.json`: as oito unidades que diziam “workflow” agora usam termos cotidianos como “approach”, “process”/“steps”, e as alternativas corretas dos quizzes 3, 12 e 16 foram encurtadas para 9, 7 e 11 palavras, respectivamente. O gabarito e a mensagem foram preservados; `validate()` passou para as 11 unidades, sem divergências de tags, atributos, números, placeholders ou URLs. Causa registrada em `FALHAS.md` como prompt.
