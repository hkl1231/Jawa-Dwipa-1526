from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *


####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main_Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17,52.50),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed","{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar","Kuta_Kidul",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-396.72,-18.15),[]),

  ("town_1","Pakuan",  icon_sunda_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-397.03,115.10),[],170),
  ("town_2","Kawali",  icon_sunda_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-226.79,12.09),[],170),
  ("town_3","Kutamaya",  icon_sunda_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-281.80,75.78),[],170),
  ("town_4","Pulasari",  icon_sunda_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-485.02,135.50),[],170),

  ("town_5","Cirebon",  icon_sunda_town_port_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-185.74,96.05),[],273),
  ("town_6","Cimanuk",  icon_sunda_town_port_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.35,154.27),[],-93),
  ("town_7","Cibuaya",  icon_sunda_town_port_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-335.66,193.01),[],170),
  ("town_8","Pamanukan",  icon_sunda_town_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-297.02,147.07),[],170),

  ("town_9","Banten_Girang",  icon_sunda_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-485.03,162.90),[],170),
  ("town_10","Pontang",  icon_sunda_town_port_b|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-460.94,198.84),[],4),
  ("town_11","Kalapa",  icon_sunda_town_port_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-402.71,179.03),[],-13),

  ("town_12","Budur",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.95,-37.03),[],170),
  ("town_13","Bagaluhan",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.40,-44.64),[],170),

  ("town_14","Mataram",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29.62,-68.20),[],170),

  ("town_15","Bintara",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.62,62.45),[],344),
  ("town_16","Jepara",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.70,103.38),[],85),
  ("town_17","Tuban",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(243.61,67.07),[],302),
  ("town_18","Trowulan",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(274,-55.19),[],170),
  ("town_19","Kembang_Jenar",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.85,68.35),[],340),
  ("town_20","Rembang",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150.14,91.50),[],-4),
  ("town_21","Pekalongan",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.43,62.40),[],-19),
  ("town_22","Paguhan",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.39,17.36),[],170),

  ("town_23","Pajang",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.11,-12.70),[],170),
  ("town_24","Klaten",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.32,-38.04),[],170),

  ("town_25","Wirasari",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(143.47,30.85),[],170),

  ("town_26","Bajanegara",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(190.59,30.69),[],170),

  ("town_27","Kudadu",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(276.61,-77.76),[],170),

  ("town_28","Wengker",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(177.16,-70.85),[],170),
  ("town_29","Pacitan",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(121.13,-118.17),[],170),

  ("town_30","Karanggayam",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(209.26,-103.96),[],170),

  ("town_31","Dahanapura",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(241.88,-76.65),[],170),

  ("town_32","Wulung",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(279.15,-120.99),[],170),

  ("town_33","Kanjuruhan",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325.08,-136.42),[],170),

  ("town_34","Kutaraja",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(323.57,-101.21),[],170),

  ("town_35","Gresik",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(317.15,28.02),[],-76),

  ("town_36","Kahuripan",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(326.78,9.15),[],95),

  ("town_37","Sidayu",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(298.31,50.97),[],270),
  ("town_38","Lamongan",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(274.92,26.81),[],170),
  ("town_39","Madyun",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(201.39,-40.54),[],170),
  ("town_40","Sadon",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(171.98,-31.72),[],170),

  ("town_41","Wirabhumi",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(521.53,-167.79),[],170),
  ("town_42","Pakembangan",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(444.40,-88.67),[],170),

  ("town_43","Lumajang",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(384.82,-121.51),[],170),
  ("town_44","Sugeneb",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(464.98,38.38),[],170),

  ("castle_1","Majalengka",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-222.34,83.60),[],50),
  ("castle_2","Tanjungbarat",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-359.08,130.65),[],50),
  ("castle_3","Bojong_Menje",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-322.46,65.64),[],50),
  ("castle_4","Cangkuang",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-263.69,25.01),[],50),
  ("castle_5","Tugu",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-373.08,148.86),[],50),
  ("castle_6","Pangandaran",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-176.95,-53.98),[],8),
  ("castle_7","Karang_Kamulyan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.26,-5.72),[],50),

  ("castle_8","Sindangsari",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-232.15,-69.28),[],50),
  ("castle_9","Garut",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-301.75,14.22),[],50),
  ("castle_10","Sindangbarang",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-355.33,-22.04),[],50),
  ("castle_11","Kadipaten",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-242.19,85.55),[],50),
  ("castle_12","Kebon_Kopi",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-420.28,133.57),[],50),
  ("castle_13","Jatibarang",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-217.75,117.61),[],50),
  ("castle_14","Babakan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.40,63.07),[],50),
  ("castle_15","Lohbener",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-228.58,128.38),[],50),
  ("castle_16","Batujaya",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-363.98,169.60),[],50),
  ("castle_17","Cieureup",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-530.91,119.06),[],50),
  ("castle_18","Pangguyangan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-454.11,74.05),[],50),
  ("castle_19","Cibadak",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-398.11,60.64),[],50),
  ("castle_20","Ujung_Kulon",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-563.80,76.37),[],50),
  ("castle_21","Tanjung_Kidul",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-440.33,9.06),[],50),
  ("castle_22","Kalibaya",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.77,26.62),[],50),
  ("castle_23","Brebes",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.20,45.36),[],50),
  ("castle_24","Mijen",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.65,36.03),[],50),
  ("castle_25","Pati",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.15,71.36),[],50),
  ("castle_26","Kudus",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.66,65.45),[],50),
  ("castle_27","Blora",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(187.57,47.02),[],50),
  ("castle_28","Matahun",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(230.67,14.87),[],50),
  ("castle_29","Gangsen",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(243.11,-17.66),[],50),
  ("castle_30","Sanggurah",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(256.12,-32.59),[],50),
  ("castle_31","Kranggan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-103.32,-8.17),[],50),
  ("castle_32","Talaga",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220.74,62.02),[],50),
  ("castle_33","Cilacap",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-138.86,-46.40),[],50),
  ("castle_34","Bobotsari",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.23,-2.07),[],50),
  ("castle_35","Purwokerto",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.04,-25.42),[],50),
  ("castle_36","Bayawulung",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.13,-49.88),[],50),
  ("castle_37","Temanggung",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.61,13.19),[],50),
  ("castle_38","Mamrati",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.66,-53.41),[],50),
  ("castle_39","Abhayagiri",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.81,-96.69),[],50),
  ("castle_40","Jatimalang",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.90,-78.23),[],50),
  ("castle_41","Plaosan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.71,-54.14),[],50),
  ("castle_42","Kalasan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.96,-85.22),[],50),
  ("castle_43","Prambanan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.56,-53.68),[],50),
  ("castle_44","Genteng",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159.81,-14.20),[],50),
  ("castle_45","Dieng",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.26,29.63),[],50),
  ("castle_46","Bojong_Kidul",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-518.40,144.90),[],50),
  ("castle_47","Tangarang",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-444,157.23),[],50),
  ("castle_48","Poh_Pitu",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.40,27.98),[],50),
  ("castle_49","Purwodadi",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.40,30.97),[],50),

  ("castle_50","Kertasura",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.50,-17.23),[],50),
  ("castle_51","Wonogiri",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.23,-49.78),[],50),
  ("castle_52","Karangasem",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(100.09,-37.34),[],50),
  ("castle_53","Pracimantoro",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.09,-84.61),[],50),

  ("castle_54","Tegalamba",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(152.04,-90.54),[],50),

  ("castle_55","Pamotan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(344.24,-33.25),[],50),
  ("castle_56","Sadeng",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(418.28,-145.17),[],50),
  ("castle_57","Bajrajinaparamitraputra",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(407.60,-70.23),[],50),
  ("castle_58","Prabalingga",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(372.86,-61.23),[],50),
  ("castle_59","Banyuwangi",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(533.98,-117.98),[],50),
  ("castle_60","Jember",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(455.33,-132.78),[],50),

  ("castle_61","Bangkalan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(326.38,41.60),[],50),
  ("castle_62","Pamekasan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(409.88,23.89),[],50),

  ("village_1","Situraja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-261.94,66.26),[],100),
  ("village_2","Wado",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-239.30,61.31),[],100),
  ("village_3","Cimalaka",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-260.64,93.24),[],100),
  ("village_4","Rancakalong",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-300.66,89.29),[],100),
  ("village_5","Cicalengka",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-288.98,42.17),[],100),
  ("village_6","Talagasari",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-237.48,121.79),[],100),
  ("village_7","Jatiwangi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-219.92,94.14),[],100),
  ("village_8","Palimanan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-203.39,97.69),[],100),
  ("village_9","Linggarjati",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192.52,78.85),[],100),
  ("village_10","Karangampel",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.36,115.62),[],100),
  ("village_11","Dermayu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-207.52,146.72),[],100),
  ("village_12","Cangkring",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-243.34,141.80),[],100),
  ("village_13","Kandanghaur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-270.23,144.01),[],100),
  ("village_14","Ciasem",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-318.91,152.40),[],100),
  ("village_15","Cijulang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.97,-60.48),[],100),
  ("village_16","Saunggalah",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206.44,35.07),[],100),
  ("village_17","Panjalu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-240.56,18.34),[],100),
  ("village_18","Ciamis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-245.94,-8.10),[],100),
  ("village_19","Babakananyar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170,-26.14),[],100),
  ("village_20","Kalipucang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159.21,-48.61),[],100),
  ("village_21","Cikalong",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192.90,-22.20),[],100),
  ("village_22","Cikatomas",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214.29,-43.47),[],100),
  ("village_23","Karanganyar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-269.52,-59.95),[],100),
  ("village_24","Pameungpeuk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-317.86,-29.75),[],100),
  ("village_25","Cilimus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-311.25,6.59),[],100),
  ("village_26","Pangalengan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-329.41,38.82),[],100),
  ("village_27","Cicatih",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-404.74,50.21),[],100),
  ("village_28","Cigombong",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-396.77,92),[],100),
  ("village_29","Citeureup",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-381.91,133.48),[],100),
  ("village_30","Ciaruteun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-412.75,129.49),[],100),
  ("village_31","Cadas_Ngampar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-308.96,107.55),[],100),
  ("village_32","Cibalong",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-264.76,-28.90),[],100),
  ("village_33","Arca_Domas",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-360.29,103.88),[],100),
  ("village_34","Binong",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-304.67,134.85),[],100),
  ("village_35","Sundapura",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-354.77,140.32),[],100),
  ("village_36","Sungaibuntu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-326.38,181.90),[],100),
  ("village_37","Cikeruh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-350.69,189.85),[],100),
  ("village_38","Cigede",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-426.17,189.93),[],100),
  ("village_39","Parung",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-410.54,159.32),[],100),
  ("village_40","Cileungsi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-383.18,157.96),[],100),
  ("village_41","Cilegon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-488.63,187.14),[],100),
  ("village_42","Tanara",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-448.88,187.21),[],100),
  ("village_43","Tunjung",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-462.87,164.84),[],100),
  ("village_44","Cikeuyeup",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-466.16,136.39),[],100),
  ("village_45","Cimanggu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-534.85,83.43),[],100),
  ("village_46","Hanjeli",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-412.11,22.09),[],100),
  ("village_47","Sajamerta",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.70,51.20),[],100),
  ("village_48","Tegal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.86,66.44),[],100),
  ("village_49","Kendungwuni",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.47,49.12),[],100),
  ("village_50","Klampak",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.92,46.84),[],100),
  ("village_51","Bulakamba",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.46,55.64),[],100),
  ("village_52","Kalirahayu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-126.48,70.94),[],100),
  ("village_53","Losan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.17,56.12),[],100),
  ("village_54","Ciseureuh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.65,31.94),[],100),
  ("village_55","Cipari",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-186.88,51.31),[],100),
  ("village_56","Kendal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.44,60.70),[],100),
  ("village_57","Semarang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.60,53.31),[],100),
  ("village_58","Karangawen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.78,34.91),[],100),
  ("village_59","Gubug",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.15,45.22),[],100),
  ("village_60","Sanggam",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91,29.80),[],100),
  ("village_61","Gedhang_Sanga",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.08,18.55),[],100),
  ("village_62","Jambean",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.71,23.36),[],100),
  ("village_63","Patiayam",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.53,83.13),[],100),
  ("village_64","Kedung",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.25,88.60),[],100),
  ("village_65","Keling",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.09,131.59),[],100),
  ("village_66","Genuk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(90.47,115.77),[],100),
  ("village_67","Muria",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.67,98.24),[],100),
  ("village_68","Mantingan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(186.88,59.69),[],100),
  ("village_69","Kalipang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(190.18,91.81),[],100),
  ("village_70","Lasem",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(167.81,92.11),[],100),
  ("village_71","Pamotan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(167.08,75.42),[],100),
  ("village_72","Tambak_Badya",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(222.86,75.51),[],100),
  ("village_73","Bektiharja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(240.95,51.25),[],100),
  ("village_74","Jatiraga",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(212.86,54.05),[],100),
  ("village_75","Lwaram",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(216.97,0.62),[],100),
  ("village_76","Gondang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(230.25,-26.44),[],100),
  ("village_77","Palah",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(275.71,-101.72),[],100),
  ("village_78","Canggu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(273.25,-46.23),[],100),
  ("village_79","Watugaluh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(257.25,-63.59),[],100),
  ("village_80","Losarang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-265.24,125.27),[],100),
  ("village_81","Karanganyar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-109.55,22.67),[],100),
  ("village_82","Magelang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.13,-17.57),[],100),
  ("village_83","Parakan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.69,15.09),[],100),
  ("village_84","Ajibarang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.23,-23.49),[],100),
  ("village_85","Cinangsi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-149.37,-23.20),[],100),
  ("village_86","Karangjati",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.43,5.65),[],100),
  ("village_87","Canggal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.73,-46.90),[],100),
  ("village_88","Pejagoan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.63,-49.31),[],100),
  ("village_89","Pangkalan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(327.97,35.79),[],100),
  ("village_90","Kebumen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.03,-56.05),[],100),
  ("village_91","Purbalingga",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.54,-19.24),[],100),
  ("village_92","Sokaraja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.37,-33.36),[],100),
  ("village_93","Kebasen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.97,-38.03),[],100),
  ("village_94","Binangun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.37,-54.15),[],100),
  ("village_95","Purwareja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.91,-62.20),[],100),
  ("village_96","Ngawen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.72,-42.53),[],100),
  ("village_97","Wirangunan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.47,-13.24),[],100),
  ("village_98","Janggala",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.77,-70.60),[],100),
  ("village_99","Bantul",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.63,-73.01),[],100),
  ("village_100","Semanu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.18,-73.32),[],100),
  ("village_101","Potrowangsan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.86,-82.30),[],100),
  ("village_102","Wanasari",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.28,-65.52),[],100),
  ("village_103","Imogiri",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.96,-80.76),[],100),
  ("village_104","Tlagawarak",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.23,-102.52),[],100),
  ("village_105","Pawon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.99,-27.92),[],100),
  ("village_106","Cidanghiyang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-501.56,95.69),[],100),
  ("village_107","Karanghawu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-446.77,51.81),[],100),
  ("village_108","Wangun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-479.29,115.48),[],100),
  ("village_109","Gunungsari",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-497.17,156),[],100),
  ("village_110","Ciruas",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-471.85,154.94),[],100),

  ("village_111","Grogol",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.04,-17.09),[],100),
  ("village_112","Sukaharja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.08,-26.19),[],100),
  ("village_113","Jambangan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.69,-4.73),[],100),
  ("village_114","Karangjati",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.96,-30.40),[],100),
  ("village_115","Gunungan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.17,-39.01),[],100),
  ("village_116","Cawas",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.30,-45.92),[],100),
  ("village_117","Kuangsan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.89,-39.32),[],100),
  ("village_118","Jatisrana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.31,-63.24),[],100),
  ("village_119","Wurjantara",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.28,-71.06),[],100),
  ("village_120","Danareja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.95,-103.17),[],100),
  ("village_121","Ponggok",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134.60,-109.40),[],100),
  ("village_122","Dringa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91.44,-124.42),[],100),
  ("village_123","Slahung",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(166.33,-83.64),[],100),
  ("village_124","Sumarata",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(163.92,-68.48),[],100),
  ("village_125","Jetis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(138,-88.04),[],100),
  ("village_126","Wwatan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(189.25,-80.08),[],100),
  ("village_127","Gethuk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(196.57,-126.83),[],100),
  ("village_128","Pulung",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(222.90,-83.62),[],100),
  ("village_129","Lor",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(231.14,-62.97),[],100),
  ("village_130","Anjukladang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(221.84,-45.65),[],100),
  ("village_131","Balareja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(210.27,-26.71),[],100),
  ("village_132","Krandengan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(192.78,-54),[],100),
  ("village_133","Gerih",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(186.61,-24.32),[],100),
  ("village_134","Dadapan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(157.88,-20.39),[],100),
  ("village_135","Kalang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(160.82,-47.47),[],100),
  ("village_136","Panunggalan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(145.57,23.32),[],100),
  ("village_137","Kajen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150.21,51.93),[],100),
  ("village_138","Prawata",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(130.71,44.43),[],100),
  ("village_139","Tamulang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(264.41,-47.98),[],100),
  ("village_140","Badal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(248.82,-87.98),[],100),
  ("village_141","Ngrawa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(236.49,-109.70),[],100),
  ("village_142","Kanigara",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(285.48,-125.84),[],100),
  ("village_143","Kedungreja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(303.38,-116.63),[],100),
  ("village_144","Kademangan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(268.16,-131.12),[],100),
  ("village_145","Malang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(326.18,-115.22),[],100),
  ("village_146","Danamulya",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(311.81,-152.22),[],100),
  ("village_147","Turen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(339.71,-140.86),[],100),
  ("village_148","Purwareja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(340.81,-67.60),[],100),
  ("village_149","Tumapel",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(310.51,-106.39),[],100),
  ("village_150","Lawang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(326.70,-82.33),[],100),
  ("village_151","Majakerta",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(290.26,-42.91),[],100),
  ("village_152","Majasari",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(320.30,-50.10),[],100),
  ("village_153","Jatikurung",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(279.74,-23.01),[],100),
  ("village_154","Kedungsana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(258.22,17.19),[],100),
  ("village_155","Kalimalang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(295.74,23.51),[],100),
  ("village_156","Dukuhagung",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(279.40,1.57),[],100),
  ("village_157","Pajaman",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(262.83,55.84),[],100),
  ("village_158","Petung",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(284.21,53.64),[],100),
  ("village_159","Karangreja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(296.62,58.04),[],100),
  ("village_160","Sampurnan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(296.49,37.24),[],100),
  ("village_161","Kandangan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(314.05,15.61),[],100),
  ("village_162","Benjing",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(297.23,10.87),[],100),
  ("village_163","Hujung_Galuh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(330.34,17.85),[],100),
  ("village_164","Karang_Plasa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(310.70,-1.10),[],100),
  ("village_165","Tawangalun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(340.64,0.44),[],100),
  ("village_166","Bangil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(330.03,-33.14),[],100),
  ("village_167","Semawut",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(308.40,-28.72),[],100),
  ("village_168","Janggaran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(326.44,-19.50),[],100),
  ("village_169","Gending",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(390.82,-74.76),[],100),
  ("village_170","Bandilan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(355.41,-50.05),[],100),
  ("village_171","Kertawana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(366.26,-110.26),[],100),
  ("village_172","Klakah",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(385.99,-102.64),[],100),
  ("village_173","Kunir",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(394.08,-135.99),[],100),
  ("village_174","Prajekan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(416.76,-121.82),[],100),
  ("village_175","Majang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(475.92,-144.83),[],100),
  ("village_176","Bangareja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(495.41,-176.25),[],100),

  ("village_177","Karangarja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(490.93,-155.45),[],100),
  ("village_178","Blimbing",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(524.24,-137.35),[],100),
  ("village_179","Wanasari",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(462.60,-92.34),[],100),
  ("village_180","Situbanda",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(460.14,-62.57),[],100),
  ("village_181","Sumberwaru",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(490.70,-64.98),[],100),
  ("village_182","Wangsareja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(526.83,-84.39),[],100),
  ("village_183","Paradaan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(463.41,46.49),[],100),
  ("village_184","Lombang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(486.06,55.26),[],100),
  ("village_185","Ngampar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(439.78,49.74),[],100),
  ("village_186","Sampang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(382.10,17.61),[],100),
  ("village_187","Burajeh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(350.02,42.87),[],100),
  ("village_188","Semar_Ngaringan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(171.12,35.88),[],100),
  ("village_189","Buloh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(197.75,25.40),[],100),
  ("village_190","Bluto",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(449.55,23.93),[],100),
  ("village_191","Sambongbangi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(170.32,18.31),[],100),

  
  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.74,-35.31),[]),
  ("four_ways_inn","Leuweung_Hideung",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-370.29,83.32),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.02,165.71),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.66,95.09),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.73,-2.97),[]),

  ("treasure_hunt_1","Abandoned_Temple",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(147.83,2.32),[]),
  ("treasure_hunt_2","Candi_Arjuna",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.79,25.77),[]),
  ("treasure_hunt_3","Candi_Sambisari",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.07,-62.48),[]),
  ("treasure_hunt_4","Jangkar_Bumi",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.23,-17),[]),
  ("treasure_hunt_5","Curug_Kahyangan",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-250.60,43.69),[]),
  ("treasure_hunt_6","Strange_Structure",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(448.98,-109.63),[]),
  ("treasure_hunt_7","Lawang_Swarga",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-392.78,26.34),[]),
  ("treasure_hunt_8","Curug_Naga",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-348.49,98.01),[]),
  ("treasure_hunt_9","Sumur_Pancasora",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.36,16.19),[]),
  ("treasure_hunt_10","Kraton_Kidul",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-127.68,-65.71),[]),

  ("training_ground","Training_Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.02,105.10),[]),

  ("training_ground_1","Training_Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99,106.71),[],100),
  ("training_ground_2","Training_Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(226.05,28.47),[],100),
  ("training_ground_3","Training_Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.44,79.10),[],100),
  ("training_ground_4","Training_Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.26,-31.29),[],100),
  ("training_ground_5","Training_Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.80,12.50),[],100),


#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-343.57,120.98),[],-87),
  ("Bridge_2","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.47,28.85),[],-65),
  ("Bridge_3","{!}3",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(94.09,-68.54),[],136),
  ("Bridge_4","{!}4",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(193.41,-4.43),[],56),
  ("Bridge_5","{!}5",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-357.16,139.75),[],109),
  ("Bridge_6","{!}6",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-245.09,85.26),[],-90),
  ("Bridge_7","{!}7",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-372.83,174.74),[],-58),
  ("Bridge_8","{!}8",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(264.88,-54.17),[],61),
  ("Bridge_9","{!}9",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(243.03,20.34),[],-111),
  ("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(323.49,-7.81),[],-117),
  ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-240.92,61.42),[],62),
  ("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(244.10,-100),[],-56),
  ("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.54,-42.72),[],62),
  ("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.07,-11.59),[],133),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(104.15,-55.05),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the_steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-270.15,-52.81),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the_tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(457.48,-114.81),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the_forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-448.44,121.95),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the_highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-338.09,58.16),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the_coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-76.66,160.06),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the_coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-410.43,236.50),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the_desert",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(118.53,84.94),[(trp_looter,15,0)]),
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[(trp_looter,15,0)]),
#Hispania 1200, barco, embarco/desembarco, viaje maritimo, ship, puertos
	("puerto_gresik"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(317.27,29.52),[]),
	("puerto_pamotan"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(344.90,-35.03),[]),
	("puerto_blambangan_1"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(466.92,-51.55),[]),
	("puerto_blambangan_2"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(536.02,-102.66),[]),
	("puerto_wulung"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(197.12,85.16),[]),
	("puerto_karanggayam"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(225.65,-141.72),[]),
	("puerto_kidul_1"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134.15,-140.21),[]),
	("puerto_kidul_2"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(181.92,99.87),[]),
	("puerto_kidul_3"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.56,106.68),[]),
	("puerto_kidul_4"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.42,129.11),[]),
	("puerto_kidul_5"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.25,91.16),[]),
	("puerto_kidul_6"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.54,61.04),[]),
	("puerto_muria_1"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.57,65.43),[]),
	("puerto_muria_2"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.92,77.76),[]),
	("puerto_muria_3"   ,"Balearic_Islands",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-409.28,181.37),[]),
	("puerto_end"   ,"Port",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
#Hispania 1200, barco, embarco/desembarco, viaje maritimo, ship, islas
	("isla_madura"   ,"Majorca_Island",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(331.98,32.24),[]),
#	("isla_menorca"   ,"Minorca Island",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(190, 50),[]),
#	("isla_ibiza"   ,"Ibiza Island",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134, -21),[]),

  ]
# modmerger_start version=201 type=2
try:
    component_name = "parties"
    var_set = { "parties" : parties }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
