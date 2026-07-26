from knowledge.graph import KnowledgeGraph



graph = KnowledgeGraph()



graph.add_concept(
    "castle",
    "architecture"
)


graph.add_feature(
    "castle",
    "towers"
)


graph.add_material(
    "castle",
    "stone"
)


graph.add_relationship(
    "castle",
    "uses",
    "stone"
)



print(
    graph.describe()
)