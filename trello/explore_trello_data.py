"""'Hello, World' like Trello data file reading."""
import json
import pathlib

TRELLO_DATA_FILE = './data/2021-01-18_1205.json'

if __name__ == "__main__":
    dump_file = pathlib.Path(TRELLO_DATA_FILE)
    assert dump_file.exists() == True, f'File not found: "{dump_file}"'

    with dump_file.open(encoding='utf-8') as fh:
        d = json.load(fh)
    # "cards" branch stores all the cards. Current list is in "idList" attribute.
    print(
        'Card example'
        f"\n\tname={d['cards'][0]['name']}"
        f"\n\tlist id={d['cards'][0]['idList']}"
    )
    # So lists are located in "lists" branch.
    print(
        'List example'
        f"\n\tname={d['lists'][0]['name']}"
        f"\n\tid={d['lists'][0]['id']}"
    )
    
    print('Done')
