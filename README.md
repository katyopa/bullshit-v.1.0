# Tagcounter

Tagcounter is a program for counting html tags of a webpage.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tagcounter.

```bash
pip install tagcounter
```

## Usage

```bash

tagcounter --get yandex.ru  # downloads webpage, returns html tags and their counts, saves into database
tagcounter --get ydx        # for synonyms of the urls go to synonyms.py, feel free to add synonyms
tagcounter --view yandex.ru # returns html tags and their counts saved in database
tagcounter                  # starts GUI version: enter url or synonym (e.g. yandex.ru or ydx), press [Show From DB] or [Download From Internet] button
```

Thank you for reading this. Good luck!
