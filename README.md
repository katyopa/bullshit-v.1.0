# Tagcounter

Tagcounter is a program for counting html tags of a webpage.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tagcounter.

```bash
pip install tagcounter
```

## Usage

```bash

tagcounter --get yandex.ru  # downloads webpage, returns html tags and their counts, creates a new database, saves tags and counts into database
tagcounter --get ydx        # checks for synonyms of the urls in synonyms.yaml, feel free to add your own synonyms
tagcounter --view yandex.ru # returns html tags and their counts saved in database
tagcounter                  # starts GUI version: enter url or synonym (e.g. yandex.ru or ydx), press [Show From DB] or [Download From Internet] button
```

Thank you for reading this. Good luck!
