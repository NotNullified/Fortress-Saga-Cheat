# Fortress-Saga-Cheat
Cheat for the popular mobile game Fortress Saga.

### Summary:
This cheat is completely open source, and I am open to contributions from anyone. Currently it only supports maxing out your cannonball and kit levels.
The only required files here are main.py and all_sigs.json, the rest was just used in development.
The use of the term AOB and sig are used interchangably, sorry to anyone who tries to modify this mess lol.

### Guide:
1. Install LDPlayer and Python 3 (any version compatible with pymem)
2. Open your terminal and type `python -m pip install pymem`
3. Open ldplayer and run fortress saga
4. Run main.py in your terminal
5. Enjoy your new stats.

### Sig/AOB info
Cannon sig:
    First byte determines rarity and depth into rarity.
    1001 is normal cannon 1, 1002 is normal cannon 2
    2001 is elite cannon 1, and so on.
    Second byte is level, a dynamic value, hence the ?? wild card.
    third byte is always 256
    fourth byte is always 1

Kit sig:
    First byte same as cannon but 1101, 1102, 2101, and so on.
    Second byte is level
    Third is always 256
    Fourth is always 2

Stats:
    Fortress stats do not have a reliable signature to follow, but they are very easy to find.
    Simply scan a 4byte value equal to your stat, such as ATK, then level up attack and search the new lvl.
    Repeat until stats are found. I may be able to find a reliable signature in the future but I'm tired rn.

Heros:
    Currently unable to control hero XP, but this sig may be used to find the hero lvl, the hero lvl will be the last 4byte int of the sig
    00 EE BF 21 38 76 00 00 00 00 00 00 00 00 00 00 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 01 00 00 00 ?? ?? ?? ??
    I suspect XP is stored at an offset, but I cannot use detect what writes to address
    due to me being too lazy to run ceserver in a rooted ldplayer, when I'm unsure of if Fortress Saga has root detection, though there are other methods.
