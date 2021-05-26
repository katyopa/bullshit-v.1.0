# Tagcounter

Tagcounter is a program for counting htmltags of a webpage.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tagcounter.

```bash
pip install tagcounter
```

## Usage

```bash
import foobar

tagcounter --get yandex.ru  # downloads webpage, returns html tags and their counts,    saves into database
tagcounter --get ydx        # for synonyms of the urls go to synonyms.py
tagcounter --view yandex.ru # returns html tags and their counts saved in database
tagcounter                  # starts GUI version: enter yandex.ru / ydx, press button
```

Thank you for reading this. Good luck!
