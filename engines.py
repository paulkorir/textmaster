import random

from models import Engine, Score


class SentenceLengthEngine(Engine):
    """Heuristic to analyse sentence length"""
    name = 'mean sentence length'

    def _calc(self, file):
        sentences = self.get_sentences(file)
        sentence_lengths = list()
        for sentence in sentences:
            sentence_lengths.append(len(sentence.split(' ')))
        import statistics
        mean = statistics.mean(sentence_lengths)
        score = Score(self, value=mean)
        return score


class NominalisationRatioEngine(Engine):
    """The proportion of words ending in -ion"""
    name = 'nominalisation ratio'

    def _calc(self, file):
        # for each word, check if it is nominalised
        words = self.get_words(file)
        print(f"{words = }")
        nominalisation_words = list(filter(lambda w: w.endswith('ion'), words))
        nominalisation_ratio = len(nominalisation_words) / len(words)
        score = Score(self, value=nominalisation_ratio)
        return score
