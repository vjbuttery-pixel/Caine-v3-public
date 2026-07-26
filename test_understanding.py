from knowledge.knowledge_base import KnowledgeBase
from search.researcher import Researcher


memory = KnowledgeBase()

researcher = Researcher(memory)


result = researcher.research(
[
    "castle",
    "magic",
    "forest"
]
)


print(result)