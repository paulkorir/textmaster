# `textmaster`
<hr>

## Introduction

`textmaster` is a text quality engine that analyses written text to generate a set of statistics indicating writing quality. The author can thus focus on structuring the message while `textmaster` can focus on elevating *stylometry* to make for a clear and engaging read. To accomplish this, `textmaster` relies on a set of heuristics, each of which estimates a particular measure of writing quality. For example, one of the measures of writing quality is the presence of *strong verbs* therefore, `textmaster` runs a check on the diversity of verbs used thoughout the text and offers suggestions on where repetition occurs and which parts can benefit from improvements.

Using `textmaster` is simple. Simply save your text as a `TEXT` (`.txt`) file then run `texmaster` on it.

```shell
tm analyse file.txt
```

Overall, `textmaster` gives a quality score on a scale of 0 to 100, with 100 being perfect text.

```shell
tm analyse file.txt
Quality score: 87.3%
```
Ask `textmaster` for more information by passing the `-v/--verbose` flag.

```shell
tm analyse --verbose file.txt
# a lot more information about your text
```

## Architecture
All heuristics are run concurrently over the text and are managed by an `EngineManager`, which takes an `TextMasterConfig` object and an iterable of `Engine` subclasses.

```python
with EngineManager(TextMasterConfig(args)) as engine_manager:
    # or engine_manager.configure(TextMasterConfig(config_file))
    from . import engines

    engine_manager.load(engines.all)
    result = engine_manager.analyse(args.filename)
    print(result)
```
