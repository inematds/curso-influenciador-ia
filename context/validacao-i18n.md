# Validação EN/ES — 2026-09-27

Conteúdo 6.3.0; formato OSWork v6.2 preservado.
- EN: 24/24 aulas aprovadas; média 10/10. Ver auditoria-en.json.
- ES: 24/24 aulas aprovadas; média 9.958333333333334/10. Ver auditoria-es.json.
- Auditor adaptado ao idioma EN: download/upload/login/backup/setup/input/output/script são vocabulário nativo, não empréstimos ingleses no português. Sentinelas técnicas (API, CLI, JSON, Git, terminal etc.) e demais critérios permanecem ativos. A adaptação é local ao verificador; a skill global não foi alterada.
- Motor: 26/26 comportamentos em PT, EN e ES; logs i18n-motor-*.log.
- Estrutura, links, IDs, respostas de quiz, arquivos locais e sintaxe JS verificados.
- Navegador: todas as aulas em celular, imagens, troca de idioma preservando a aula, exportação/importação e rejeição de outra edição; nenhum erro JS.
- Planejadores interativos, quando presentes: campos de estado, persistência e exportação/importação por edição testados.
- Revisão textual simulada nos relatórios revisao-i18n-*.md. Não houve teste com alunos externos.
- Todos os testes de navegador bloquearam HTTP externo; fontes de fallback locais. Nenhuma API de tradução usada.
- Capturas locais: /home/nmaldaner/projetos/output/cursos-v62-traducao/curso-influenciador-ia. A inspeção visual é registrada separadamente após abrir as capturas.

## Inspeção visual — 27/09/2026

Capturas abertas: en-desktop-papel.png, es-desktop-escuro.png, en-mobile-review.png (aula12) e es-mobile-review.png (acompanhamento21dias). Textos, imagens e controles legíveis, sem cortes observados nas amostras. Suíte passou em24 aulas por idioma e apoios em390px, nos3 temas desktop, com persistência/exportação/importação, rejeição de outra edição,21 registros, lacunas, duplicações e campos pendentes. Não houve teste em aparelhos físicos nem execução real de21dias de publicações.

Ajustes finais Luna: substituição de workflow por instruções simples em8 unidades e redução fiel de3 respostas corretas de quiz, preservando gabarito. Auditoria EN final24/24, média10; static e browser repetidos com êxito.
