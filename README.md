# Project-Platoon

Project repository for Catan-Risk Crossover Boardgame.

This ReadME can be used as a road map and history log to use as reference.

Apr.11, 2020 First Zoom Meeting
* Decided on Catan-Risk Hybrid Game.
  * Risk Style battling while being played on a Catan hex map with resources to compete for.
    * Tentative List of Resources.
      * Oil, Stone, Wheat, Wood.
      * Resources like oil can be hidden, adding an element of luck and risk to resource collection.
  * Battle mechanics based on number of soldiers and strength modifier via enhancements.
  * "Higher Level Warfare" with disease, famine and prostitutes. Possibly in the form of developer cards.

* Current Goals to work towards:
  * Creation of Ruleset for the game. 
    * What can we change about risk and catan to make it higher impact and have higher replayability?
    * What sort of in-game interactions do we provide? What out-of-game interactions do we enable?
      * eg) Temporary Alliances are integral to risk, but don't actually exist in the game. 

  * Create the Hex Map Generator in Python.
    * Fixed Size
    * Various Land and Sea Blocks

# Requirements
 * Install all pip requirements (Do this once):
```bash
$ pip install -r requirements.txt
```
 * Open up the pipenv environment:
```bash
$ pipenv shell
```
 * Install all requirements in the pipenv (Do this once):
```bash
$ pipenv install
```
 * To exit the pipenv into your main terminal use:
```bash
$ exit
```

# Run
From pipenv use this command to run the game:
```bash
python3 main.py
```

Apr.23, 2020 Dev Meeting
* Planned the next steps moving forward with making the game map.
  * Merge to and clean up main branch
  * Write code in view module to display map
  * Add Generation class to control module
  * Handle Tile Clicking logic in control module
  * Add players to models module for hex capture mario party style game

