"""Learner-facing romanization of standard Bangladeshi Bengali."""

from __future__ import annotations

import gzip
from functools import cache
from importlib.resources import files

_PHONEMES = {
    "O": "ô",
    "a": "a",
    "i": "i",
    "u": "u",
    "e": "e",
    "E": "æ",
    "o": "o",
    "k": "k",
    "kh": "kh",
    "g": "g",
    "gh": "gh",
    "N": "ng",
    "c": "ch",
    "ch": "chh",
    "j": "j",
    "jh": "jh",
    "T": "ṭ",
    "Th": "ṭh",
    "D": "ḍ",
    "Dh": "ḍh",
    "t": "t",
    "th": "th",
    "d": "d",
    "dh": "dh",
    "n": "n",
    "p": "p",
    "f": "f",
    "b": "b",
    "bh": "bh",
    "m": "m",
    "r": "r",
    "l": "l",
    "sh": "sh",
    "s": "s",
    "h": "h",
}
_BENGALI_START = "\u0980"
_BENGALI_END = "\u09ff"
_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")


def _romanize_phonemes(transcription: str) -> str:
    result: list[str] = []
    for phoneme in transcription.replace(".", "").split():
        if phoneme == "i^":
            result.append("y" if not result else "i")
        elif phoneme == "u^":
            result.append("u")
        elif phoneme == "e^":
            result.append("y")
        elif phoneme == "o^":
            result.append("w" if not result else "o")
        else:
            result.append(_PHONEMES[phoneme])
    return "".join(result)


@cache
def _pronunciations() -> dict[str, tuple[str, ...]]:
    variants: dict[str, set[str]] = {}
    resource = files("bengali_romanizer").joinpath("data/lexicon.tsv.gz")
    with (
        resource.open("rb") as compressed,
        gzip.open(compressed, "rt", encoding="utf-8") as lexicon,
    ):
        for line in lexicon:
            if line.startswith("#") or not line.strip():
                continue
            spelling, transcription, *_ = line.rstrip("\n").split("\t")
            variants.setdefault(spelling, set()).add(_romanize_phonemes(transcription))
    return {word: tuple(sorted(readings)) for word, readings in variants.items()}


def _is_bengali(character: str) -> bool:
    return _BENGALI_START <= character <= _BENGALI_END


def romanize(text: str) -> str:
    """Return verified learner-facing readings while preserving uncertain words.

    Words with one pronunciation in the bundled expert-built lexicon are
    romanized. Unknown words and context-dependent homographs stay in Bengali,
    making missing coverage visible instead of presenting a guess as fact.

    >>> romanize("বাংলা নববর্ষ")
    'bangla nôbobôrsho'
    >>> romanize("বাংলায়")
    'banglay'
    """
    lexicon = _pronunciations()
    result: list[str] = []
    position = 0

    while position < len(text):
        if _is_bengali(text[position]) and not text[position].isdigit():
            end = position + 1
            while end < len(text) and _is_bengali(text[end]):
                end += 1
            word = text[position:end]
            readings = lexicon.get(word, ())
            result.append(readings[0] if len(readings) == 1 else word)
            position = end
        else:
            result.append(text[position].translate(_DIGITS))
            position += 1

    return "".join(result)
