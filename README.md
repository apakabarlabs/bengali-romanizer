[![Tests](https://github.com/apakabarlabs/bengali-romanizer/actions/workflows/test.yml/badge.svg)](https://github.com/apakabarlabs/bengali-romanizer/actions/workflows/test.yml)
[![Documentation](https://github.com/apakabarlabs/bengali-romanizer/actions/workflows/documentation.yml/badge.svg)](https://apakabarlabs.github.io/bengali-romanizer/bengali_romanizer.html)

# Bengali Romanizer

A learner-facing romanizer for standard Bangladeshi Bengali. It uses an
expert-built pronunciation dictionary instead of deriving pronunciation from
spelling alone.

## Installation

```bash
pip install bengali-romanizer
```

## Usage

```python
>>> import bengali_romanizer
>>> bengali_romanizer.romanize('বাংলা')
'bangla'
>>> bengali_romanizer.romanize('নমস্কার')
'nômoshkar'
>>> bengali_romanizer.romanize('ধন্যবাদ')
'dhonnobad'
>>> bengali_romanizer.romanize('ভক্তি')
'bhokti'
>>> bengali_romanizer.romanize('আন্দোলন')
'andolon'
>>> bengali_romanizer.romanize('প্রাচীন')
'prachin'

```

The library romanizes a word only when its pronunciation is unambiguous in the
bundled dictionary. It leaves unknown words and context-dependent homographs in
Bengali rather than teaching a guessed pronunciation.

## Reading the output

Most letters have their familiar Latin values. `ô` is the vowel in British
English *lot*, `æ` is the vowel in *cat*, `ng` is the final sound in *sing*,
and `sh`, `ch`, and `chh` distinguish Bengali consonants. Dots under `ṭ` and
`ḍ` mark retroflex consonants. `a` never implies a long vowel.

Pronunciations come from Google's native-speaker-transcribed
[Bengali pronunciation dictionary](https://github.com/google/language-resources/blob/master/bn/data/lexicon.tsv),
licensed under CC BY 4.0. The dictionary targets the standard language used in
Bangladesh and was built for accurate pronunciation by beginning learners and
speech systems.

## Documentation

The [API reference](https://apakabarlabs.github.io/bengali-romanizer/bengali_romanizer.html) is generated from the public Python API and deployed by GitHub Actions.

## Lines of Code

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/loc-history-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset=".github/loc-history-light.svg">
  <img alt="Lines of Code graph" src=".github/loc-history-light.svg">
</picture>
