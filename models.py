import abc
import argparse
import io
from threading import Lock


class AnalysisResults:
    def __str__(self):
        results_string = ''
        return results_string


class EngineManager:
    applied_engines = list()  # a list of strings; each an engine name

    def __init__(self, tmconfig: TexMasterConfig):
        self._config = tmconfig

    def analyse(self) -> AnalysisResults:
        """This is where the event loop occurs"""
        result = AnalysisResults()
        return result


class TextMasterConfig:
    def __init__(self, config_file: str):
        self._config_file = config_file


class Engine:
    """An engine has two main interfaces:

    - the `proc()` interface takes an `io.TextIOBase` subclass through which it can access the text data; it returns
    a `Score` object
    - the `run()` interface is an asynchronous coroutine run on the `EngineManager`'s event loop which internally
    invokes `proc()` interface

    """
    lock = Lock()  # shared lock

    @abc.abstractmethod
    def __init__(self, *, name):
        self._name = name

    @abc.abstractmethod()
    def proc(self, file: io.TextIOBase) -> Score:
        """Run the heuristic"""

    async def run(self):
        score = self.proc()
        return score

    @staticmethod
    def get_sentences(file: io.TextIOBase):
        """Get the sentences in the file"""
        with self.lock.acquire():
            file.seek(0)  # rewind the file handle
            raw_sentences = list(map(lambda s: s.strip(), file.split('.')))
        return raw_sentences


class Score:
    """The class representing the score returned by running an engine on some text"""
    # todo: perform statistical analysis over scores
    def __init__(self, engine, value=0):
        self._engine = engine
        self._value = value

    def __str__(self):
        score_string = f"{engine.name} = {self._value}"
        return score_string


class CLIParser(argparse.ArgumentParser):
    def parse(self):
        return super().parse_args()
