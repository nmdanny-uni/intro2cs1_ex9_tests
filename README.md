# Tests for exercise 9 - Rush Hour

## Description

These are tests for the rush hour game.

Note that these tests aren't guaranteed to be correct, it's very likely that I've
made mistakes, misunderstood some parts of the exercise or added unnecessary
constraints. If so, please 
[open up an issue](https://github.cs.huji.ac.il/danielkerbel/intro2cs1_ex9_tests/issues)
or correct them and make a pull request.

If you don't understand why a test failed, open up the test file and see what's
going on. I've tried to keep the tests somewhat simple and descriptive.

## Contributing
If you found a mistake or want to add your own tests, feel free to do so (via basic git usage
and a pull request, see tutorials on the web)


## What is/isn't covered
Covered:
* API of Car
* API of Board
* A pretty simple test of one valid playthrough of the game

Not covered:
* More interesting playthroughs or edge-cases
* Doesn't enforce correct usage of the API - e.g by replacing your own class
  implementations with alternative ones.
  
## Usage

Place the tests within the ex9 project folder(either directly or within
a nested directory within the main folder.)

Requires 'pytest' to be available in your environment. Can be installed via 
`python -m pip install pytest`,
then you can run the tests via `python -m pytest -vv` or via
PyCharm

# Note 
Requires python 3.6.
 
 On some systems you may have to type `python3` 
instead of `python` in the above commands.

If there happen to be multiple 'game.py' files within your project root,
it will use the topmost(most nested) one. 

(If you run `python -m pytest -k "test_ensure_tests_configured_corrrectly" -s` 
 it will tell you which python executable and game.py file is being used)