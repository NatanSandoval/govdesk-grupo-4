"""Gera o BPMN 2.0 editável e a prévia SVG do processo de reposição."""
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
      'bpmndi': 'http://www.omg.org/spec/BPMN/20100524/DI',
      'dc': 'http://www.omg.org/spec/DD/20100524/DC',
      'di': 'http://www.omg.org/spec/DD/20100524/DI'}
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)


def element(parent, prefix, tag, **attrs):
    return ET.SubElement(parent, '{' + NS[prefix] + '}' + tag, {k: str(v) for k, v in attrs.items()})


lanes = [('po', 'Product Owner / CIO', 60), ('dev', 'Dev Lead', 250), ('qa', 'QA / Auditoria', 460)]
nodes = [
    ('inicio', 'startEvent', 'qa', ['Necessidade'], 130, 530, 36, 36),
    ('identificar', 'task', 'qa', ['Identificar mínimo', 'ou necessidade'], 200, 500, 150, 80),
    ('priorizar', 'task', 'po', ['Definir prioridade'], 390, 110, 150, 80),
    ('registrar', 'task', 'dev', ['Registrar solicitação', 'e validar campos'], 590, 280, 150, 70),
    ('valido', 'exclusiveGateway', 'dev', ['Válida?'], 790, 290, 50, 50),
    ('corrigir', 'task', 'dev', ['Corrigir campos'], 590, 375, 150, 60),
    ('atender', 'task', 'dev', ['Iniciar atendimento', 'Em andamento'], 900, 280, 150, 70),
    ('receber', 'task', 'qa', ['Conferir recebimento', 'integral dos itens'], 1100, 500, 160, 80),
    ('concluir', 'task', 'dev', ['Confirmar recebimento', 'Concluída e entrada'], 1300, 280, 160, 70),
    ('verificar', 'task', 'qa', ['Verificar saldo', 'e indicadores'], 1500, 500, 150, 80),
    ('revisar', 'task', 'po', ['Revisar conclusão'], 1500, 110, 150, 80),
    ('fim', 'endEvent', 'po', ['Fim'], 1740, 130, 36, 36),
]
flows = [
    ('f1', 'inicio', 'identificar', '', [(166, 548), (200, 548)]),
    ('f2', 'identificar', 'priorizar', '', [(275, 500), (275, 150), (390, 150)]),
    ('f3', 'priorizar', 'registrar', '', [(540, 150), (665, 150), (665, 280)]),
    ('f4', 'registrar', 'valido', '', [(740, 315), (790, 315)]),
    ('f5', 'valido', 'corrigir', 'Não', [(815, 340), (815, 405), (740, 405)]),
    ('f6', 'corrigir', 'registrar', '', [(665, 375), (665, 350)]),
    ('f7', 'valido', 'atender', 'Sim', [(840, 315), (900, 315)]),
    ('f8', 'atender', 'receber', '', [(1050, 315), (1180, 315), (1180, 500)]),
    ('f9', 'receber', 'concluir', '', [(1260, 540), (1380, 540), (1380, 350)]),
    ('f10', 'concluir', 'verificar', '', [(1460, 315), (1575, 315), (1575, 500)]),
    ('f11', 'verificar', 'revisar', '', [(1650, 540), (1690, 540), (1690, 220), (1575, 220), (1575, 190)]),
    ('f12', 'revisar', 'fim', '', [(1650, 150), (1740, 150)]),
]

definitions = ET.Element('{' + NS['bpmn'] + '}definitions', id='ProntoEstoqueDefinitions', targetNamespace='https://github.com/NatanSandoval/govdesk-grupo-4')
process = element(definitions, 'bpmn', 'process', id='ProcessoReposicao', name='Reposição de estoque TO BE', isExecutable='false')
lane_set = element(process, 'bpmn', 'laneSet', id='Raias')
for lane_id, name, y in lanes:
    lane = element(lane_set, 'bpmn', 'lane', id=lane_id, name=name)
    for node in nodes:
        if node[2] == lane_id:
            element(lane, 'bpmn', 'flowNodeRef').text = node[0]
for node_id, kind, lane, labels, x, y, w, h in nodes:
    node = element(process, 'bpmn', kind, id=node_id, name=' '.join(labels))
    for flow in flows:
        if flow[2] == node_id:
            element(node, 'bpmn', 'incoming').text = flow[0]
        if flow[1] == node_id:
            element(node, 'bpmn', 'outgoing').text = flow[0]
for fid, source, target, label, points in flows:
    element(process, 'bpmn', 'sequenceFlow', id=fid, sourceRef=source, targetRef=target, name=label)
diagram = element(definitions, 'bpmndi', 'BPMNDiagram', id='DiagramaReposicao')
plane = element(diagram, 'bpmndi', 'BPMNPlane', id='PlanoReposicao', bpmnElement='ProcessoReposicao')
for lane_id, name, y in lanes:
    shape = element(plane, 'bpmndi', 'BPMNShape', id=lane_id + '_di', bpmnElement=lane_id, isHorizontal='true')
    element(shape, 'dc', 'Bounds', x=30, y=y, width=1800, height=190)
for node_id, kind, lane, labels, x, y, w, h in nodes:
    shape = element(plane, 'bpmndi', 'BPMNShape', id=node_id + '_di', bpmnElement=node_id)
    element(shape, 'dc', 'Bounds', x=x, y=y, width=w, height=h)
for fid, source, target, label, points in flows:
    edge = element(plane, 'bpmndi', 'BPMNEdge', id=fid + '_di', bpmnElement=fid)
    for x, y in points:
        element(edge, 'di', 'waypoint', x=x, y=y)
ET.indent(definitions)
ET.ElementTree(definitions).write(ROOT / 'docs/processo-estoque.bpmn', encoding='utf-8', xml_declaration=True)

svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1860" height="720" viewBox="0 0 1860 720" role="img" aria-labelledby="titulo descricao">',
       '<title id="titulo">Processo de reposição do ProntoEstoque TO BE</title>',
       '<desc id="descricao">Três raias com os papéis da RACI e tarefas de priorização, cadastro, validação, atendimento, recebimento e revisão.</desc>',
       '<rect width="1860" height="720" fill="white"/>',
       '<defs><marker id="seta" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#334155"/></marker></defs>',
       '<g font-family="Arial,sans-serif" fill="#111827"><text x="30" y="35" font-size="24" font-weight="bold">ProntoEstoque   Processo de reposição TO BE</text>']
for lane_id, name, y in lanes:
    svg += [f'<rect x="30" y="{y}" width="1800" height="190" fill="#f8fafc" stroke="#94a3b8"/>',
            f'<text x="62" y="{y+95}" font-size="18" text-anchor="middle" transform="rotate(-90 62 {y+95})">{escape(name)}</text>']
for fid, source, target, label, points in flows:
    svg.append('<polyline points="' + ' '.join(f'{x},{y}' for x, y in points) + '" fill="none" stroke="#334155" stroke-width="2" marker-end="url(#seta)"/>')
    if label:
        x, y = points[0]
        svg.append(f'<text x="{x+8}" y="{y-8}" font-size="15">{label}</text>')
for node_id, kind, lane, labels, x, y, w, h in nodes:
    if kind in ['startEvent', 'endEvent']:
        svg.append(f'<circle cx="{x+w/2}" cy="{y+h/2}" r="18" fill="white" stroke="#1e2761" stroke-width="{4 if kind == "endEvent" else 2}"/>')
        svg.append(f'<text x="{x+w/2}" y="{y+h+22}" text-anchor="middle" font-size="15">{escape(labels[0])}</text>')
    elif kind == 'exclusiveGateway':
        svg.append(f'<polygon points="{x+w/2},{y} {x+w},{y+h/2} {x+w/2},{y+h} {x},{y+h/2}" fill="white" stroke="#1e2761" stroke-width="2"/>')
        svg.append(f'<text x="{x+w/2}" y="{y+h/2+6}" text-anchor="middle" font-size="24">×</text><text x="{x+w/2}" y="{y-12}" text-anchor="middle" font-size="15">Válida?</text>')
    else:
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="white" stroke="#1e2761" stroke-width="2"/>')
        for i, label in enumerate(labels):
            yy = y+h/2 + (i-(len(labels)-1)/2)*21+5
            svg.append(f'<text x="{x+w/2}" y="{yy}" text-anchor="middle" font-size="15">{escape(label)}</text>')
svg.append('<text x="30" y="690" font-size="16">Raias representam responsabilidades da equipe. Conferência de entrega e revisão da PO são atividades humanas externas ao app.</text></g></svg>')
(ROOT / 'docs/processo-estoque.svg').write_text('\n'.join(svg), encoding='utf-8')
print('BPMN e SVG gerados.')
