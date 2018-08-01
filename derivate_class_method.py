class Philosopher:
    def __init_subclass__(cls, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name
        print(cls.__name__)

class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass
