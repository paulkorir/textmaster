import asyncio
import pathlib
import unittest

import managers
import ui
from engines import SentenceLengthEngine, NominalisationRatioEngine

TEST_DATA_PATH = pathlib.Path('.')


class TestManagers(unittest.TestCase):
    def test_analyse_default(self):
        """Test that we can analyse some text"""
        args = ui.cli(f"tm {TEST_DATA_PATH / 'pickwick.txt'}")
        print(f"{args = }")
        managers.analyse(args)

    def test_engine_basic(self):
        """Test that we can run a simple engine"""
        sentence_length_engine = SentenceLengthEngine(TEST_DATA_PATH / 'pickwick.txt')
        score = asyncio.run(sentence_length_engine.run())
        print(f"{score}")

    def test_multiple_engines(self):
        """Test that we can run more than one engine"""
        async def gather(file):
            awaitables = [
                SentenceLengthEngine(file).run(),  # fixme: here is an example of repetition
                NominalisationRatioEngine(file).run(),
            ]
            _scores = await asyncio.gather(*awaitables)
            return _scores

        scores = asyncio.run(gather(TEST_DATA_PATH / 'pickwick.txt'))
        for score in scores:
            print(score)
