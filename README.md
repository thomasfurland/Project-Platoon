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

# Run
```bash
python3 map_generater.py
```