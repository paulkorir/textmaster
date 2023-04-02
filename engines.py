from models import Engine, Score


class SentenceLengthEngine(Engine):
    """Heuristic to analyse sentence length"""

    def __init__(self, name='mean sentence length'):
        self._name = name

    def proc(self, file):
        score = self._calculate_mean_sentence_length(file)
        return score

    def _calculate_mean_sentence_length(self, file):
        sentences = self.get_sentences(file)
        sentence_lengths = list()
        for sentence in sentences:
            sentence_lengths.append(len(sentence.split(' ')))
        import statistics
        mean = statistics.mean(sentence_lengths)
        score = Score(self, value=mean)
        return score
