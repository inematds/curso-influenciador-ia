from pathlib import Path
from html import escape as E
import json
R=Path(__file__).resolve().parent
css='''body{margin:0;background:#f5f1e9;color:#292b2a;font:17px/1.65 system-ui}main,header,footer{max-width:850px;margin:auto;padding:22px}h1,h2,h3{font-family:Georgia,serif;line-height:1.2}h1{font-size:clamp(32px,6vw,52px)}a{color:#325550}section,article{border:1px solid #cdc9c0;background:#fffdf8;border-radius:12px;padding:22px;margin:18px 0}input,select,textarea,button{font:inherit;box-sizing:border-box;max-width:100%}input,textarea,select{width:100%;padding:10px;border:1px solid #797e77;border-radius:6px;background:#fff;color:#242824}label{display:block;margin:12px 0}button,.button{display:inline-block;padding:10px 16px;background:#325550;color:white;border:0;border-radius:6px;cursor:pointer;margin:6px 4px 6px 0}button:focus-visible,a:focus-visible{outline:3px solid #a75428;outline-offset:3px}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#ede9e1;padding:14px;font:15px/1.6 system-ui}img{width:100%;height:auto;border-radius:8px}nav{display:flex;gap:18px;flex-wrap:wrap}.muted{color:#535952}*{box-sizing:border-box}output{font-weight:700}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px}@media(max-width:500px){main,header,footer{padding:16px}section,article{padding:16px}}details{border:1px solid #cdc9c0;border-radius:12px;padding:16px;margin:14px 0;background:#fffdf8}summary{cursor:pointer;font-weight:700}input[type=checkbox]{width:auto;margin-right:8px}.check{display:flex;align-items:flex-start;gap:8px}.check input{margin-top:8px}.stats{background:#e9e3f0;padding:18px;border-radius:10px}small{display:block}.grid>*,details{min-width:0}@media print{nav,button{display:none}section{break-inside:avoid}}'''
def page(name,title,body,script=''):
 (R/name).write_text(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)} · Influenciador IA v6.2</title><style>{css}</style></head><body><header><nav><a href="curso.html#trilha">Curso</a><a href="caderno.html">Fichas</a><a href="sprint.html">21 dias</a><a href="recurso.html">Recurso aberto</a><a href="galeria.html">Galeria</a></nav></header><main><p>INEMA.CLUB · Influenciador IA v6.2</p><h1>{E(title)}</h1>{body}</main><footer><a href="https://inema.club">Voltar ao portal INEMA.CLUB</a></footer><script>{script}</script></body></html>')
body='''<p>Uma ficha aberta para planejar sua própria mesa criativa. Sem cadastro, coleta de contatos ou promessa de produtividade. Use objetos reais e confira suas condições; ilustrações não provam estabilidade ou resistência.</p><section><h2>Uma mudança possível</h2><ol><li>Escolha uma atividade que você realiza nessa mesa.</li><li>Liste três materiais que precisa alcançar durante a atividade.</li><li>Observe o espaço disponível sem bloquear circulação, cabos ou ventilação.</li><li>Escolha um objeto íntegro e estável para organizar um grupo de materiais.</li><li>Teste com cuidado no espaço real e ajuste o que não funcionar.</li></ol><pre>Minha atividade:
Três materiais necessários:
O que ocupa espaço sem ajudar:
Uma mudança que quero testar:
Condições do objeto real a conferir:
O que observei depois do teste:
O que vou manter ou ajustar:</pre><button id="imprimir">Imprimir ou salvar em PDF</button><p>Preencha nas suas notas ou no papel. Esta página não armazena respostas. Você pode adaptar a ficha para uso próprio, citando INEMA.CLUB quando redistribuir este modelo.</p></section>'''
page('recurso.html','Planeje uma pequena mudança na sua mesa',body,"document.getElementById('imprimir').addEventListener('click',()=>window.print());")
body='''<p>Referências didáticas da personagem adulta original Lia Lume. Imagens criadas no recurso nativo do Codex. Elas ilustram escolhas de identidade, sem comprovar animação ou publicação em rede. Para seu desafio, crie uma personagem própria.</p>'''
for n,title in [(1,'Apresentação da personagem'),(6,'Vistas de identidade'),(7,'Referência de corpo inteiro'),(8,'Três cenas com a mesma base'),(9,'Preparação de movimento'),(14,'Sequência ilustrada'),(15,'Um desvio deliberado para revisar')]:
 body+=f'<section><h2>{E(title)}</h2><img src="assets/img/aula-{n}.webp" width="1280" height="720" alt="{E(title)} de Lia Lume" loading="lazy"><p>'+('O broche vermelho é um erro proposital de identidade. A referência aprovada usa broche dourado em semicírculo.' if n==15 else 'Compare rosto, cabelo, roupa e broche. O resultado de cada geração precisa de conferência humana.')+'</p></section>'
page('galeria.html','Uma identidade, escolhas observáveis',body)
body='''<p>Fichas autorais do caso Lia Lume, personagem adulta fictícia. Copie para suas notas. Nenhuma conta social foi operada ou campanha executada na criação deste material.</p><section><h2>Antes do dia 1</h2><ul><li>Identidade adulta original e sete referências analisadas.</li><li>Imagem-base aprovada e três cenas reais.</li><li>Vídeo de movimento real revisado.</li><li>Carrossel de quatro páginas exportado e legível.</li><li>Conta acessível com apresentação de personagem virtual.</li><li>Três pilares, sete ideias e pelo menos três peças editoriais prontas.</li><li>Fontes, permissões, legendas e identificação conferidas.</li><li>Calendário com datas viáveis e cópia exportada.</li></ul><p>A reserva pode aproveitar as imagens, o vídeo e o carrossel produzidos nas aulas. Uma peça pronta só conta como publicação quando estiver acessível na rede e conferida.</p></section>
<section><h2>Ficha de sete referências</h2><pre>1. Paleta — autor/endereço, observação, decisão própria:
2. Luz — autor/endereço, observação, decisão própria:
3. Roupa — autor/endereço, observação, decisão própria:
4. Cenário — autor/endereço, observação, decisão própria:
5. Enquadramento — autor/endereço, observação, decisão própria:
6. Linguagem — autor/endereço, observação, decisão própria:
7. Formato — autor/endereço, observação, decisão própria:
Materiais apenas para análise:
Materiais autorizados para enviar ao gerador:</pre></section>
<section><h2>DNA do exemplo e pedido de cena</h2><pre>Lia Lume — personagem adulta fictícia, aparência de 32 anos.
Pele morena; cabelo preto curto com mecha azul-esverdeada; olhos escuros.
Jaqueta ameixa; camiseta e calça creme; broche dourado em semicírculo.
Estilo de ilustração 3D com textura de papel e argila.
Fixar rosto, cabelo, roupa, broche e estilo.
Variar pose, objeto e cenário coerente.
Cena: mantenha a personagem da referência e mostre-a segurando um caderno.
Fundo simples, luz suave, mãos e rosto legíveis. Sem texto na imagem.</pre><p>Escreva uma identidade própria para seu projeto. A descrição não garante resultado; compare cada arquivo com a referência aprovada.</p></section>
<section><h2>Roteiro do carrossel · quatro páginas</h2><ol><li><b>Pergunta:</b> Onde ficam seus lápis? Personagem virtual criada com IA.</li><li><b>Opção:</b> Uma composição ilustrada para reunir os materiais.</li><li><b>Critério:</b> Confira espaço, integridade e estabilidade no objeto real.</li><li><b>Convite:</b> Abra a ficha gratuita e planeje uma mudança possível.</li></ol><p>Use texto legível no editor; não dependa de letras geradas dentro da imagem. As quatro páginas formam uma publicação editorial.</p></section>
<section><h2>Identificações separadas</h2><pre>Editorial: personagem virtual criada com IA. Cena ilustrativa.
Estudo de oferta: personagem virtual criada com IA. Estudo fictício de oferta, sem parceria comercial.
Relação real: identificação de IA + publicidade e vínculo verdadeiro, conforme contexto e regras da plataforma.
Indicação remunerada real: informar que pode haver comissão, além da identificação publicitária aplicável.</pre><p>A regra editorial deste desafio identifica a personagem em todos os posts. Consulte também as exigências da rede. O aviso de IA não substitui a identificação comercial. O guia CONAR 2026 trata publicidade e responsabilidade, sem criar uma nova obrigação universal de rotular qualquer IA.</p></section>
<section><h2>Rotina de uma publicação</h2><pre>Tema e promessa:
Pilar e formato:
Roteiro ou sequência:
Materiais, origem e permissões:
Arquivo e versão:
[ ] Identidade e mensagem conferidas.
[ ] Leitura, som e movimento conferidos quando aplicáveis.
[ ] Legenda, direitos e identificação de IA conferidos.
[ ] Natureza comercial ou estudo corretamente identificados.
Situação: planejado / em produção / pronto / publicado
Endereço e data real após publicar:
Data da próxima consulta:
Minutos de trabalho ativo:
Filas, espera e pendências:</pre></section>
<section><h2>Cinco grupos de sinais</h2><ol><li><b>Exposição:</b> visualizações ou alcance, sem tratar definições diferentes como equivalentes.</li><li><b>Permanência:</b> tempo de exibição ou retenção, quando disponíveis.</li><li><b>Utilidade:</b> salvamentos ou compartilhamentos, conforme objetivo.</li><li><b>Interesse:</b> cliques ou perguntas pertinentes, com critério descrito.</li><li><b>Resultado:</b> conversas qualificadas ou transações reais; estudo pode ser não aplicável.</li></ol><pre>Fonte e definição:
Data e tempo desde a publicação:
Exposição:
Permanência:
Utilidade:
Interesse:
Resultado comercial:
O que observei:
O que ainda não sei:
Próxima consulta e ação:</pre><p><b>Exemplo fictício:</b>20 salvamentos em 1.000 visualizações = 2%. A razão usa essas contagens, não pessoas únicas. Sem visualizações disponíveis, não existe taxa calculável. Comparar exige mesma definição e intervalo; uma taxa não prova receita.</p></section>
<section><h2>Três ofertas para estudar</h2><article><h3>Serviço</h3><p>Um vídeo curto de produto com escopo, revisão, prazo e uso definidos. Só anuncie como disponível se você consegue produzir e cumprir as condições.</p></article><article><h3>Produto próprio</h3><p>Um conjunto autoral de modelos de planejamento, existente e revisado. Não revenda material de terceiros ou cursos gratuitos INEMA como se fossem seus.</p></article><article><h3>Indicação remunerada</h3><p>Um produto pertinente num programa que você realmente integra. Confira regras, direitos, adequação e identificação da comissão. Não existe afiliação INEMA presumida neste curso.</p></article></section>
<section><h2>Encerramento com evidências</h2><p>21 editoriais  + 1 oferta adicional = 22 publicações. Guarde arquivos e endereços. Confira três revisões semanais e a última consulta prevista após a publicação final. Uma lacuna diária deve aparecer como calendário estendido, sem alterar datas reais.</p><pre>Arquivos e referências conferidos:
Perfil e endereço:
Quantidade editorial publicada:
Post de oferta adicional:
Sequência diária ou lacunas:
Revisões de 7, 14 e 21 dias realizadas:
Última consulta realizada ou pendente:
O que observei:
O que ainda não sei:
Decisão e próximo passo:</pre><p>O resumo do acompanhamento usa declarações suas. Ele não acessa as redes nem certifica que um endereço corresponde à publicação.</p></section>'''
for i,d in enumerate(json.loads((R/'context/aulas-editoriais.json').read_text()),1):body+=f'<section id="aula-{i}"><h2>Aula {i} · {E(d["titulo"])}</h2><pre>{E(d["molde"])}</pre></section>'
body+='<section><h2>Fontes oficiais · consulta em 25/09/2026</h2><ul>'+''.join(f'<li><a href="{E(u)}" target="_blank" rel="noopener">{E(t)}</a></li>' for u,t in json.loads((R/'context/fontes.json').read_text()))+'</ul></section>'
page('caderno.html','Fichas para preparar e executar',body)
body='''<p>21 registros editoriais e uma oferta adicional. Preencher temas não conclui o desafio. O painel usa suas declarações; não acessa, publica ou agenda conteúdo nas redes. Os dados ficam neste navegador. Exporte cópias e não guarde senhas ou dados pessoais de contatos.</p><div class="stats" aria-live="polite"><p id="contagem"></p><p id="sequencia"></p><p id="revisao-resumo"></p><p id="pendencias"></p></div><p id="status" role="status">Pronto para preencher.</p><section><h2>Seu plano</h2><label>Projeto<input id="projeto" maxlength="200"></label><label>Início planejado<input id="inicio" type="date"></label><button id="datas" type="button">Preencher apenas datas vazias</button><p>O botão sugere 21 dias seguidos e revisões. Não altera datas já preenchidas. Depois de publicar, registre a data real.</p><button id="exportar" type="button">Exportar cópia JSON</button><label>Importar cópia JSON<input id="importar" type="file" accept="application/json,.json"></label><p>Importar substitui os campos atuais. Exporte antes para preservar outra versão. Arquivo inválido é rejeitado sem substituir os registros.</p></section><h2>Publicações editoriais</h2><p>Para entrar na contagem, um registro precisa de situação publicado, tema, data real, endereço HTTP/HTTPS único, nome do arquivo e conferências marcadas. Isso é uma conferência dos campos, não uma verificação externa.</p><div id="dias"></div><h2>Oferta adicional · publicação 22</h2><div id="oferta"></div><h2>Revisões semanais</h2><div id="revisoes"></div><section id="ultima"><h2>Última consulta</h2><p>Registre a consulta prevista após a publicação final. Ela pode acontecer depois do dia 21.</p></section>'''
script=(R/'assets/sprint.js').read_text()
page('sprint.html','Acompanhe o que realmente aconteceu',body,script)
