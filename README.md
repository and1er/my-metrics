# my-metrics

A tool for my personal metrics visualization and analysis using python.

## Trello

I use [Trello](https://trello.com) for my reading and courses management. And I want to visualize my progress in each component someday.

Trello could dump a board to `.json` file (in a UI in a board menu _Print and export_). A data file includes following data branches I found useful:

* `lists`: a list of board columns, key field is `id`;
* `cards`: all the cards with `idList` is a foreign key to `lists`.

So this could help to start to analyze the data.

### Requirements

* Python 3.7+;
* a Trello account;
* some dumps from Trello stored to `./trello/data/*.json` in `yyyy-mm-dd_HHMM.json` files.

### Running

Simple "Hello, World!" like run.

1. `cd trello`
2. set a path to a single file in `TRELLO_DATA_FILE` in `explore_trello_data.py` (this is temporary solution)
3. run the python script

    ```bash
    $ python3 explore_trello_data.py 
    Card example
            name=My card
            list id=5f4b5951d586974d757ef62c
    List example
            name=My list (column)
            id=5f4b5951d586974d757ef62c
    Done
    ```
