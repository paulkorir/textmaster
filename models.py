import abc
import argparse
import io
import string
from threading import Lock


class AnalysisResults:
    def __str__(self):
        results_string = ''
        return results_string


class TextMasterConfig:
    def __init__(self, config_file: str):
        self._config_file = config_file


class Score:
    """The class representing the score returned by running an engine on some text"""

    # todo: perform statistical analysis over scores
    def __init__(self, engine, value=0):
        self._engine = engine
        self._value = value

    def __str__(self):
        score_string = f"{self._engine.name} = {self._value}"
        return score_string


class EngineManager:
    applied_engines = list()  # a list of strings; each an engine name

    def __init__(self, tmconfig: TextMasterConfig):
        self._config = tmconfig

    def analyse(self, filename) -> AnalysisResults:
        """This is where the event loop occurs"""
        print(f"Analysing {filename}...")
        result = AnalysisResults()
        return result

    def __enter__(self):
        """Enter the context manager"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager"""


class Engine(abc.ABC):
    """An engine has two main interfaces:

    - the `proc()` interface takes an `io.TextIOBase` subclass through which it can access the text data; it returns
    a `Score` object
    - the `run()` interface is an asynchronous coroutine run on the `EngineManager`'s event loop which internally
    invokes `proc()` interface

    """
    lock = Lock()  # shared lock
    name = 'abstract engine'

    def __init__(self, file):
        self._file = file

    def proc(self) -> Score:
        """Run the heuristic"""
        with open(self._file) as file:
            score = self._calc(file)
        return score

    @abc.abstractmethod
    def _calc(self, file) -> Score:
        """Abstract method for calculating the actual score"""
        score = Score(self)
        return score

    async def run(self):
        score = self.proc()
        return score

    @staticmethod
    def get_sentences(file: io.TextIOBase):
        """Get the sentences in the file"""
        with Engine.lock:
            file.seek(0)  # rewind the file handle
            raw_sentences = list(map(lambda s: s.strip(), file.read().split('.')))
        return raw_sentences

    @staticmethod
    def get_words(file: io.TextIOBase):
        """Get all words as an iterable"""
        with Engine.lock:
            file.seek(0)
            text = file.read().lower()
            # split any hyphenated words
            # text = list(map(lambda w: w.split('-')))
            # remove punctuation
            for char in string.punctuation:
                text = text.replace(char, '')
            words = text.split(' ')
        return words


class CLIParser(argparse.ArgumentParser):
    def parse(self):
        return super().parse_args()
