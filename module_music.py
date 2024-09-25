from header_music import *


####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
##  ("losing_battle", "alosingbattle.mp3", sit_calm|sit_action),
##  ("reluctant_hero", "reluctanthero.mp3", sit_action),
##  ("the_great_hall", "thegreathall.mp3", sit_calm),
##  ("requiem", "requiem.mp3", sit_calm),
##  ("silent_intruder", "silentintruder.mp3", sit_calm|sit_action),
##  ("the_pilgrimage", "thepilgrimage.mp3", sit_calm),
##  ("ambushed", "ambushed.mp3", sit_action),
##  ("triumph", "triumph.mp3", sit_action),

##  ("losing_battle", "alosingbattle.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("reluctant_hero", "reluctanthero.mp3", mtf_sit_attack),
##  ("the_great_hall", "thegreathall.mp3", mtf_sit_map_travel),
##  ("requiem", "requiem.mp3", mtf_sit_map_travel),
##  ("silent_intruder", "silentintruder.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("the_pilgrimage", "thepilgrimage.mp3", mtf_sit_map_travel),
##  ("ambushed", "ambushed.mp3", mtf_sit_attack),
##  ("triumph", "triumph.mp3", mtf_sit_attack),
  ("bogus", "cant_find_this.ogg", 0, 0),
  ("mount_and_blade_title_screen", "main_menu_1.ogg", mtf_sit_main_title|mtf_start_immediately, 0),
  ("mount_and_blade_title_screen_2", "main_menu_2.ogg", mtf_sit_main_title|mtf_start_immediately, 0),

  ("ambushed_by_neutral", "battle_1.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight),
  ("ambushed_by_khergit", "battle_2.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_nord",    "gusti_patih_udara.ogg", mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_rhodok",  "gusti_patih_udara.ogg", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_swadian", "battle_4.ogg", mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_vaegir",  "battle_4.ogg", mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_sarranid", "battle_1.ogg", mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  
  ("arena_1", "arena.ogg", mtf_sit_arena, 0),
  ("arena_2", "battle_4.ogg", mtf_sit_arena, 0),
  ("armorer", "armorer.ogg", mtf_sit_travel, 0),
  ("bandit_fight", "battle_4.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),

  ("calm_night_1", "calm_night_2.ogg", mtf_sit_night, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  ("captured", "capture.ogg", mtf_persist_until_finished, 0),
  ("defeated_by_neutral", "defeated_by_neutral.ogg",mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_2", "defeated_by_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_3", "defeated_by_neutral_3.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),

  ("empty_village", "empty_village.ogg", mtf_persist_until_finished, 0),
  ("encounter_hostile_nords", "gusti_patih_udara.ogg", mtf_persist_until_finished|mtf_sit_encounter_hostile, 0),
  ("escape", "escape.ogg", mtf_persist_until_finished, 0),

  ("fight_1", "battle_1.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_2", "gusti_patih_udara.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_3", "battle_3.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_as_khergit", "battle_1.ogg", mtf_culture_3|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_4", "battle_2.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),  
  ("fight_as_nord", "gusti_patih_udara.ogg", mtf_culture_4|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_as_rhodok", "gusti_patih_udara.ogg", mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_as_swadian", "battle_1.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight, mtf_culture_all),
  ("fight_as_vaegir", "battle_4.ogg", mtf_culture_2|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_while_mounted_1", "gusti_patih_udara.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_while_mounted_2", "battle_1.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_while_mounted_3", "battle_4.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  
  ("infiltration_khergit", "infiltration_khergit.ogg", mtf_culture_3|mtf_sit_town_infiltrate, mtf_culture_all),

  ("killed_by_khergit", "killed_by_khergit.ogg", mtf_persist_until_finished|mtf_culture_3|mtf_sit_killed, 0),
  ("killed_by_swadian", "killed_by_swadian.ogg", mtf_persist_until_finished|mtf_culture_1|mtf_sit_killed, 0),
  
  ("lords_hall_khergit", "lords_hall_khergit.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),
  ("lords_hall_nord", "lords_hall_nord.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_swadian", "lords_hall_swadian.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_rhodok", "lords_hall_rhodok.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_vaegir", "lords_hall_vaegir.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  ("mounted_snow_terrain_calm", "sunda_travel_1.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  ("neutral_infiltration", "neutral_infiltration.ogg", mtf_sit_town_infiltrate, 0),
  ("outdoor_beautiful_land", "jawa_travel_2.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  ("retreat", "retreat.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),

  ("seige_neutral", "battle_1.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  ("enter_the_juggernaut", "gusti_patih_udara.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  
  ("siege_attempt", "battle_1.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  
  ("crazy_battle_music", "gusti_patih_udara.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  
  ("tavern_1", "tavern_1.ogg", mtf_sit_tavern|mtf_sit_feast, 0),
  ("tavern_2", "tavern_2.ogg", mtf_sit_tavern|mtf_sit_feast, 0),

  ("town_neutral", "town_neutral.ogg", mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  ("town_khergit", "jawa_town_1.ogg", mtf_culture_3|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_nord", "jawa_town_1.ogg", mtf_culture_4|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_rhodok", "jawa_town_1.ogg", mtf_culture_5|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_swadian", "sunda_town_1.ogg", mtf_culture_1|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_swadian2", "sunda_town_2.ogg", mtf_culture_1|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_vaegir", "jawa_town_1.ogg", mtf_culture_2|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_sarranid", "jawa_town_1.ogg", mtf_culture_6|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("travel_khergit", "jawa_travel_1.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_neutral", "travel_neutral.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("travel_nord",    "jawa_travel_1.ogg",    mtf_culture_4|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok",  "jawa_travel_2.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_swadian", "sunda_travel_1.ogg", mtf_culture_1|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_swadian2", "sunda_travel_2.ogg", mtf_culture_1|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_vaegir",  "jawa_travel_2.ogg",  mtf_culture_2|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_sarranid",  "jawa_travel_1.ogg",  mtf_culture_6|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("uncertain_homestead", "sunda_travel_1.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("hearth_and_brotherhood", "sunda_travel_2.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("tragic_village", "jawa_travel_1.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  ("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished, 0),
  ("victorious_neutral_1", "victorious_neutral_1.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_2", "victorious_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_3", "victorious_neutral_3.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),

  ("victorious_swadian", "victorious_swadian.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir", "victorious_vaegir.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir_2", "victorious_vaegir_2.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),

  ("coronation", "coronation.ogg", mtf_persist_until_finished, 0),



  
]
# modmerger_start version=201 type=4
try:
    component_name = "music"
    var_set = { "tracks":tracks, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
