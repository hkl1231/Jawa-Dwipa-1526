from header_factions import *


####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "{!}culture_sunda", 0, 0.9, [], []),
  ("culture_2",  "{!}culture_caruban_dermayu", 0, 0.9, [], []),
  ("culture_3",  "{!}culture_sunda_islam", 0, 0.9, [], []),
  ("culture_4",  "{!}culture_banyuwangian", 0, 0.9, [], []),
  ("culture_5",  "{!}culture_mataraman", 0, 0.9, [], []),
  ("culture_6",  "{!}culture_demak", 0, 0.9, [], []),
  ("culture_7",  "{!}culture_pajang", 0, 0.9, [], []),
  ("culture_8",  "{!}culture_wirasari", 0, 0.9, [], []),
  ("culture_9",  "{!}culture_kadirimajapahit", 0, 0.9, [], []),
  ("culture_10",  "{!}culture_singasari", 0, 0.9, [], []),
  ("culture_11",  "{!}culture_giri", 0, 0.9, [], []),
  ("culture_12",  "{!}culture_banyuwangi", 0, 0.9, [], []),
  ("culture_13",  "{!}culture_madura", 0, 0.9, [], []),
#additional_culture
  ("culture_portugal",  "{!}culture_portugal", 0, 0.9, [], []),
  ("culture_ming",  "{!}culture_ming", 0, 0.9, [], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
  ("kingdom_1",  "Mandala Pajajaran", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x185c13),
  ("kingdom_2",  "Kasultanan Cirebon",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x16205c),
  ("kingdom_3",  "Kadipaten Banten", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xffca1c),
  ("kingdom_4",  "Kedu",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xfc7e7e),
  ("kingdom_5",  "Mataram",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xab5120),
  ("kingdom_6",  "Kasultanan Demak",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xe80505),
  ("kingdom_7",  "Pajang",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x8EE366),
  ("kingdom_8",  "Wirasari",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x635034),
  ("kingdom_9",  "Mandala Wilwatikta",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x414a45),
  ("kingdom_10",  "Tumapel",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xdac3e8),
  ("kingdom_11",  "Janggala",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xa89e7e),
  ("kingdom_12",  "Karajaan Blambangan",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xa2a2a2),
  ("kingdom_13",  "Madura",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xc74236),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("portuguese","Portuguese Expeditionaries", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
  ("ccoop_all_stars","All Stars", 0, 0.5,[], []), #INVASION MODE (because renaming an existing one is so hard)
]

##diplomacy start+ Define these for convenience
dplmc_factions_begin = 1 #As mentioned in the notes above, this is hardcoded and shouldn't be altered.  Deliberately excludes "no faction".
dplmc_non_generic_factions_begin = [x[0] for x in enumerate(factions) if x[1][0] == "merchants"][0] + 1
dplmc_factions_end   = len(factions)
##diplomacy end+
# modmerger_start version=201 type=4
try:
    component_name = "factions"
    var_set = { "factions":factions,"default_kingdom_relations":default_kingdom_relations, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
