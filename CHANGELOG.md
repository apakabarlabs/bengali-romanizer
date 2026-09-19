# Changelog

## 0.2.0

### Changed

- Python 3.10 is now the minimum supported version; CI covers Python 3.10
  through 3.14 on Linux and macOS.
- Romanization now follows an expert-transcribed pronunciation lexicon for
  standard Bangladeshi Bengali instead of inferring pronunciation from
  spelling.
- Unknown words and context-dependent homographs remain in Bengali instead of
  receiving a guessed reading.
- Bengali digits are converted to Latin digits, while punctuation and other
  scripts remain unchanged.
- The bundled dictionary contains 65,000 entries and retains its CC BY 4.0
  attribution.

### Distribution

- The package is published to PyPI by the release workflow.
- Generated API documentation and a lines-of-code history are published by
  GitHub Actions.

## 0.1.2

Last release before the test corpus and packaging were reorganized.
