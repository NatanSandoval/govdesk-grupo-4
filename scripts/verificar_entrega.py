"""Verificações de consistência para ensaiar a entrega, sem dependências externas."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
erros = []
obrigatorios = ['README.md', '.replit', 'docs/PETI.md', 'docs/lgpd.md', 'docs/raci.md',
               'docs/template-mudanca.md', 'docs/backlog.md', 'docs/wbs.md',
               'docs/processo-chamados.md', 'docs/processo-estoque.bpmn', 'docs/processo-estoque.svg',
               'docs/melhoria-continua.md', 'docs/encerramento.md', 'docs/licoes-aprendidas.md',
               'docs/sustentacao.md', 'docs/autoavaliacao.md', 'docs/apresentacao.md',
               'docs/apresentacao/prontoestoque-semana10.pptx', 'docs/testes-semana10.md',
               'docs/respostas-semana10.md']
for arquivo in obrigatorios:
    if not (ROOT / arquivo).is_file():
        erros.append('Arquivo ausente: ' + arquivo)
for arquivo in [ROOT / 'README.md', *sorted((ROOT / 'docs').glob('*.md'))]:
    for link in re.findall(r'\]\(([^)]+)\)', arquivo.read_text(encoding='utf-8')):
        if '://' in link or link.startswith('#'):
            continue
        destino = link.split('#')[0]
        if destino and not (arquivo.parent / destino).exists():
            erros.append(f'Link quebrado em {arquivo.name}: {link}')
raci = (ROOT / 'docs/raci.md').read_text(encoding='utf-8')
atividades = 0
for linha in raci.splitlines():
    if not linha.startswith('|'):
        continue
    celulas = [c.strip() for c in linha.strip('|').split('|')]
    if len(celulas) == 6 and any(c in ('A', 'A/R') for c in celulas[1:]):
        atividades += 1
        if sum(c in ('A', 'A/R') for c in celulas[1:]) != 1:
            erros.append('Linha RACI sem um único A: ' + celulas[0])
    elif len(celulas) == 6 and any(c in ('R', 'C', 'I') for c in celulas[1:]):
        erros.append('Linha RACI sem A: ' + celulas[0])
if atividades == 0:
    erros.append('RACI sem atividades reconhecidas.')
ns = {'b': 'http://www.omg.org/spec/BPMN/20100524/MODEL'}
xml = ET.parse(ROOT / 'docs/processo-estoque.bpmn').getroot()
raias = xml.findall('.//b:lane', ns)
papeis = set(re.findall(r'\(([^)]+)\)', next(l for l in raci.splitlines() if l.startswith('| Atividade'))))
if {r.get('name') for r in raias} != papeis:
    erros.append('Raias BPMN divergem dos papéis da RACI.')
ids = [e.get('id') for e in xml.iter() if e.get('id')]
if len(set(ids)) != len(ids):
    erros.append('BPMN contém IDs duplicados.')
for fluxo in xml.findall('.//b:sequenceFlow', ns):
    if fluxo.get('sourceRef') not in ids or fluxo.get('targetRef') not in ids:
        erros.append('BPMN com sequência inválida: ' + fluxo.get('id', ''))
nos = {e.get('id') for e in xml.iter() if e.tag.split('}')[-1] in ('task', 'startEvent', 'endEvent', 'exclusiveGateway')}
referencias = [ref.text for raia in raias for ref in raia.findall('b:flowNodeRef', ns)]
if set(referencias) != nos or len(referencias) != len(set(referencias)):
    erros.append('Cada nó BPMN precisa pertencer a uma única raia.')
licoes = (ROOT / 'docs/licoes-aprendidas.md').read_text(encoding='utf-8')
for pessoa in ['Isabella Jacques', 'Guilherme Cimino', 'Ruan Bauer', 'Natan Correa', 'Max Iago']:
    if not any(l.startswith('|') and pessoa in l for l in licoes.splitlines()):
        erros.append('Lição de referência ausente para ' + pessoa)
if erros:
    raise SystemExit('\n'.join(erros))
print(f'Entrega consistente: {len(obrigatorios)} arquivos, links locais, {atividades} atividades RACI, 3 raias BPMN e lições dos 5 integrantes.')
