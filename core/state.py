from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CaineState:

    """
    The complete runtime state of Caine.

    Every major system reads from here.

    Every major system writes here.

    This is effectively Caine's "brain state".
    """

    running: bool = False

    paused: bool = False

    game_mode: str = "singleplayer"

    current_project: str | None = None

    active_goal: str | None = None

    mood: str = "curious"

    energy: float = 100.0

    focus: float = 100.0

    creativity: float = 1.0

    reasoning_depth: int = 5

    created_objects: int = 0

    solved_problems: int = 0

    learned_concepts: int = 0

    last_update: datetime = field(default_factory=datetime.utcnow)

    def tick(self):

        self.last_update = datetime.utcnow()

    def describe(self):

        return {

            "running": self.running,

            "paused": self.paused,

            "game_mode": self.game_mode,

            "project": self.current_project,

            "goal": self.active_goal,

            "mood": self.mood,

            "energy": self.energy,

            "focus": self.focus,

            "creativity": self.creativity,

            "reasoning_depth": self.reasoning_depth,

            "created_objects": self.created_objects,

            "solved_problems": self.solved_problems,

            "learned_concepts": self.learned_concepts,

            "last_update": self.last_update.isoformat()

        }