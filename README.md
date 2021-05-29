# Tagcounter

Tagcounter is a program for counting html tags of a webpage.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tagcounter.

```bash
pip install 
```

## Usage

```bash

tagcounter --get yandex.ru  # downloads webpage, returns html tags and their counts, saves them into database
tagcounter --get ydx        # checks for for synonyms of the urls in synonyms.py, feel free to add synonyms
tagcounter --view yandex.ru # returns html tags and their counts saved in database
tagcounter                  # starts GUI version: enter url or synonym (e.g. yandex.ru or ydx), press [Show From DB] or [Download From Internet] button
```

Thank you for reading this. Good luck!
