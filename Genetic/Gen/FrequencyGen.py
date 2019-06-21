from Genetic.Gen import BaseGen

class FrequencyGen(BaseGen):
    def __init__(self, frequency_score: float, content: str):
        super().__init__(content)
        self.frequency_score = frequency_score