import json
import networkx as nx
import matplotlib.pyplot as plt

# Kavram dosyasını oku
with open("endüstri_evreni_çekirdek_kavramlar.json", "r", encoding="utf-8") as f:
    concepts = json.load(f)

# İlişki dosyasını oku
with open("veri/concept_relations.json", "r", encoding="utf-8") as f:
    relations = json.load(f)

# Kavram ID -> etiket eşlemesi
labels = {c["concept_id"]: c["label_en"] for c in concepts}

# Graph oluştur
G = nx.DiGraph()

# Düğümleri ekle
for c in concepts:
    G.add_node(c["concept_id"], label=c["label_en"], layer=c["layer"], axis=c["axis"])

# Kenarları ekle
for r in relations:
    G.add_edge(r["source"], r["target"], relation=r["relation"])

# Küçük demo alt kümesi seç
sub_nodes = list(G.nodes())[:25]
H = G.subgraph(sub_nodes)

# Çiz
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(H, seed=42)

nx.draw(
    H,
    pos,
    with_labels=True,
    labels={n: labels.get(n, n) for n in H.nodes()},
    node_size=1800,
    font_size=8,
    arrows=True
)

plt.title("Industry Universe Knowledge Graph Demo")
plt.tight_layout()
plt.show()
