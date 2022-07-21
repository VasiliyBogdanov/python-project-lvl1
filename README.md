### Hexlet tests and linter status:
[![Actions Status](https://github.com/VasiliyBogdanov/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/VasiliyBogdanov/python-project-lvl1/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/e6d4dd8a3232a22f4482/maintainability)](https://codeclimate.com/github/VasiliyBogdanov/python-project-lvl1/maintainability)
[![linter](https://github.com/VasiliyBogdanov/python-project-lvl1/actions/workflows/linter.yml/badge.svg)](https://github.com/VasiliyBogdanov/python-project-lvl1/actions/workflows/linter.yml)
### Description:
This is 1st project in Hexlet's 'Python developer' course, Brain Games, a collection of 5 mathematical games, with simple CLI.

### Requirements: 
- Python ^3.8;
- poetry;
### Installation:
```
pip install git+https://github.com/VasiliyBogdanov/python-project-lvl1.git
```
or:
- Clone this repo;
- If you have 'make' utility:
```
make install
make build
make publish
make package-install
```
- If you don't:
    - get one 🧐 http://gnuwin32.sourceforge.net/packages/make.htm (It's not actually required, read on);
```
poetry install
poetry build
poetry publish --dry-run
python3 -m pip install --user dist/*.whl
```
! Use `python` instead of `python3`, if you're using Windows

### Commands list:
- `brain-even`: answer if number in question is even;
- `brain-calc`: calculate simple expression;
- `brain-gcd`: calculate the greatest common divisor of two numbers;
- `brain-progression`: insert missing number in mathematical progression;
- `brain-prime`: answer if number if question is prime or not;
## Demo:
### brain-even
[![asciicast](https://asciinema.org/a/vAII6SGUdUEqq2DAomTypoHkc.svg)](https://asciinema.org/a/vAII6SGUdUEqq2DAomTypoHkc)
### brain-calc
[![asciicast](https://asciinema.org/a/esVrPezRjUkAeI5C69wFnQLuJ.svg)](https://asciinema.org/a/esVrPezRjUkAeI5C69wFnQLuJ)
### brain-gcd
[![asciicast](https://asciinema.org/a/DVtZw5yxAqKY3juKkgSLE46iQ.svg)](https://asciinema.org/a/DVtZw5yxAqKY3juKkgSLE46iQ)
### brain-progression
[![asciicast](https://asciinema.org/a/k4poHH7yOIIFHrJeM8JzgNN8S.svg)](https://asciinema.org/a/k4poHH7yOIIFHrJeM8JzgNN8S)
### brain-prime
[![asciicast](https://asciinema.org/a/FZyL0d1GrSZnhpDa204K5FQAa.svg)](https://asciinema.org/a/FZyL0d1GrSZnhpDa204K5FQAa)
