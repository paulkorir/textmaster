import models

applied_engines = [
    'SentenceLengthEngine',
]


def analyse(args: models.CLIParser) -> int:
    # initialise the set of engines to be run
    models.EngineManager.applied_engines = applied_engines
    # start your engines...
    with models.EngineManager(models.TextMasterConfig(args.config_file)) as engine_manager:
        result = engine_manager.analyse(args.filename)
        print(result)
    return 0
