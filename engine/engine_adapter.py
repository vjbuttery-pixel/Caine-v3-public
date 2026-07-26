from abc import ABC, abstractmethod


class EngineAdapter(ABC):
    """
    Base interface for every supported game engine.

    Concrete implementations will translate
    Caine's abstract projects into engine-
    specific scenes, assets and scripts.
    """

    @abstractmethod
    def initialise(self):
        pass


    @abstractmethod
    def create_project(self, project):
        pass


    @abstractmethod
    def import_model(self, model):
        pass


    @abstractmethod
    def import_material(self, material):
        pass


    @abstractmethod
    def import_animation(self, animation):
        pass


    @abstractmethod
    def import_audio(self, audio):
        pass


    @abstractmethod
    def import_vfx(self, effect):
        pass


    @abstractmethod
    def create_scene(self, scene):
        pass


    @abstractmethod
    def save_project(self):
        pass


    @abstractmethod
    def build(self):
        pass


    @abstractmethod
    def play(self):
        pass