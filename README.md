# Tibia Loot Scraper

This project is a tool to extract loot information of monsters from the game Tibia using the official wiki (https://tibia.fandom.com). It generates JSON files with the IDs and names of the items dropped by specific monsters.

## Project Structure

- **`loot_scrap.py`**: This script extracts all available items from the Tibia wiki and saves them in a JSON file called `items.json`. This file serves as a database for the game's items.
- **`get_items.py`**: This script takes a list of monster names, queries the Tibia wiki to retrieve the items they drop, and generates a JSON file with the item IDs that match the database.

## Requirements

- Python 3.x
- Required libraries:
    - `requests`
    - `beautifulsoup4`

You can install them by running:

```bash
pip install requests beautifulsoup4
```

## Usage

1. **Generate the item database**  
     Run the `loot_scrap.py` script to generate the `items.json` file:

     ```bash
     python loot_scrap.py
     ```

2. **Retrieve monster loot**  
     Modify the `get_items.py` file to include the monster names in the `monsterNames` list and the output file name in `nameOutputFile`. Then, run the script:

     ```bash
     python get_items.py
     ```

     This will generate a JSON file in the `outputs` folder with the items dropped by the specified monsters.

## Example

If you define the following monsters in `get_items.py`:

```python
monsterNames = ["Diabolic Imp", "Demon", "Demon Skeleton"]
nameOutputFile = "goroma_volcan.json"
```

The script will generate a file `goroma_volcan.json` with the items dropped by these monsters.

## Notes

- Ensure that the wiki structure does not change, as the scraper relies on the current structure of the pages.
- If you encounter issues with monster names, verify that they are spelled correctly and match the names on the wiki.

## Use with OTClient
- You can edit the loot by going to Target -> Edit -> and replacing the "items" list with the one generated in the output file.