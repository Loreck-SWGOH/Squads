# Introduction

This document lays out the requirements for a web application to help users to
decide on using defense vs. health vs. protection mods for individual SWGOH
characters.

SWGOH is divided into groups of events. Some of these events are
always present, some events are guild driven, and other events are started by 
the game. Within each event category, there are specific events that allow 
players to interact with other players or the game. Players interact via teams.

Teams in SWGOH are comprised of different characters which can be obtained 
via shards earned during game play. All characters have a series of attributes,
such as speed and health that are used in game play to define both attacks and
defense against attacks. Characters increase these attributes applying different
types of gears and different types of mods.

Application of gear to a character allows a character to reach different gear
levels with different increases in attributes for each character. Gear levels
are numbered one (1) to thirteen (13). An addition to the game allows characters
to equip relics that allow characters even greater attributes. Relics are 
numbered one to nine (9).

Along with the gear and relics, characters can increase their attributes via mods. 
Unlike gear, mods can be added or removed from characters at will. Hence, 
the use of mods allow players to fine-tune the strengths of their characters.

Each character can have six different mods applied, denoted by their shape.
The six types are square, arrow, diamond, triangle, circle, and cross. Each type
of mod is part of a mod set, health, defense, critical chance, critical damage,
tenacity, offense, potency, and speed. Mods also have a primary stat and four
secondary stats.

The primary stats are accuracy, critical avoidance, critical
chance, critical damage, defense, health, offense, potency, protection, speed,
and tenacity. Secondary stats can be critical chance, flat defense, defense,
flat health, health, flat offense, offense, potency, flat protection, protection,
speed, and tenacity.

The primary and secondary stats are affected by the mod rarity, the mod level,
and the mod tier. The rarity of a mod cannot be changed, but the mod level and 
the mod tier can be increased. Mod levels range from level one (1) to level
fifteen (15). Mod tiers increase from tier E, the lowest, to tier A, the highest.
Increasing a mod's level or its tier causes primary stats and random secondary
stats to increase.

The suggested types of applied mods depend on a large number of factors,
including the allies in the team, the enemies being faced, and the event. A
recent addition to the conversation is the use of defense mod sets in place
of health mods sets and the use of defense primaries in place of health and
protection primaries.

In order to compare the relative effects of these types of mods, an effective
health statistic is calculated. Effective health combines the health and protection
statistics and scales it by the armor percentage.

---

# Usage

