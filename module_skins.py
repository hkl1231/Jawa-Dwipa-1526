from header_skins import *
from ID_particle_systems import *


####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

man_face_keys = [
(20,0, 0.7,-0.6, "Chin Size"),
(260,0, -0.6,1.4, "Chin Shape"),
(10,0,-0.5,0.9, "Chin Forward"),
(240,0,0.9,-0.8, "Jaw Width"),
(210,0,-0.5,1.0, "Jaw Position"),
(250,0,0.8,-1.0, "Mouth-Nose Distance"),
(200,0,-0.3,1.0, "Mouth Width"),
(50,0,-1.5,1.0, "Cheeks"),

(60,0,-0.4,1.35, "Nose Height"),
(70,0,-0.6,0.7, "Nose Width"),
(80,0,1.0,-0.1, "Nose Size"),
(270,0,-0.5,1.0, "Nose Shape"),
(90,0,-0.2,1.4, "Nose Bridge"),

(100,0,-0.3,1.5, "Cheek Bones"),
(150,0,-0.2,3.0, "Eye Width"),
(110,0,1.5,-0.9, "Eye to Eye Dist"),
(120,0,1.9,-1.0, "Eye Shape"),
(130,0,-0.5, 1.1, "Eye Depth"),
(140,0,1.0,-1.2, "Eyelids"),

(160,0,1.3,-0.2, "Eyebrow Position"),
(170,0,-0.1,1.9, "Eyebrow Height"),
(220,0,-0.1,0.9, "Eyebrow Depth"),
(180,0,-1.1,1.6, "Eyebrow Shape"),
(230,0,1.2,-0.7, "Temple Width"),

(30,0,-0.6,0.9, "Face Depth"),
(40,0,0.9,-0.6, "Face Ratio"),
(190,0,0.0,0.95, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]
# Face width-Jaw width Temple width
woman_face_keys = [
(230,0,0.8,-1.0, "Chin Size"), 
(220,0,-1.0,1.0, "Chin Shape"), 
(10,0,-1.2,1.0, "Chin Forward"),
(20,0, -0.6, 1.2, "Jaw Width"), 
(40,0,-0.7,1.0, "Jaw Position"),
(270,0,0.9,-0.9, "Mouth-Nose Distance"),
(30,0,-0.5,1.0, "Mouth Width"),
(50,0, -0.5,1.0, "Cheeks"),

(60,0,-0.5,1.0, "Nose Height"),
(70,0,-0.5,1.1, "Nose Width"),
(80,0,1.5,-0.3, "Nose Size"),
(240,0,-1.0,0.8, "Nose Shape"),
(90,0, 0.0,1.1, "Nose Bridge"),

(100,0,-0.5,1.5, "Cheek Bones"),
(150,0,-0.4,1.0, "Eye Width"),
(110,0,1.0,0.0, "Eye to Eye Dist"),
(120,0,-0.2,1.0, "Eye Shape"),
(130,0,-0.1,1.6, "Eye Depth"),
(140,0,-0.2,1.0, "Eyelids"),


(160,0,-0.2,1.2, "Eyebrow Position"),
(170,0,-0.2,0.7, "Eyebrow Height"),
(250,0,-0.4,0.9, "Eyebrow Depth"),
(180,0,-1.5,1.2, "Eyebrow Shape"),
(260,0,1.0,-0.7, "Temple Width"),

(200,0,-0.5,1.0, "Face Depth"),
(210,0,-0.5,0.9, "Face Ratio"),
(190,0,-0.4,0.8, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]
undead_face_keys = []

euro_face_keys = [
#>>>hispania 1200
(240, 0, -0.4, 0.3, "Chin Size"),
(230, 0, -0.4, 0.8, "Chin Shape"),
(250, 0, -0.25, 0.55, "Chin Forward"),
(130, 0, -0.5, 1.0, "Jaw Width"),

(120, 0, -0.5, 0.6, "Lower Lip"),
(110, 0, -0.2, 0.6, "Upper Lip"),

#(40, 0, -0.7, 1.0, "Jaw Position"),
(100, 0, 0.2, -0.2, "Mouth-Nose Distance"),
(90, 0, 0.55, -0.55, "Mouth Width"),
(20, 0, 0.6, -0.25, "Cheeks"),

(30, 0, -0.3, 0.3, "Nostril Size"),

(60, 0, 0.25, -0.25, "Nose Height"),
(40, 0, -0.2, 0.3, "Nose Width"),
(70, 0, -0.3, 0.4, "Nose Size"),
(50, 0, 0.2, -0.3, "Nose Shape"),
(80, 0, -0.3, 0.65, "Nose Bridge"),

(260, 0, -0.6, 0.5, "Cheek Bones"),
(160, 0, -0.2, 0.25, "Eye Width"),
(190, 0, -0.25, 0.15, "Eye to Eye Dist"),
(170, 0, -0.85, 0.85, "Eye Shape"),
(200, 0, -0.3, 0.7, "Eye Depth"),
(180, 0, -1.5, 1.5, "Eyelids"),

# (20, 0, 0.6, -0.25, "Eyebrow Position"),
(220, 0, 0.8, -0.8, "Eyebrow Height"),
# (220, 0, -0.1, 0.9, "Eyebrow Depth"),
(210, 0, -0.75, 0.75, "Eyebrow Shape"),
(10, 0, -0.6, 0.5, "Temple Width"),

(270, 0, -0.3, -0.1, "Face Depth"),
(150, 0, -0.25, 0.45, "Face Ratio"),
(140, 0, -0.4, 0.5, "Face Width"),

(280, 0, 0.0, 1.0, "Post-Edit"),
#<<<hispania 1200
]


chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26

comp_less_than = -1;
comp_greater_than = 1;

skins = [
  (
    "man", 0,
    "man_body", "man_calf_l", "m_handL",
    "male_head", man_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    ["beard_e","beard_d","beard_k","beard_l","beard_i","beard_j","beard_z","beard_m","beard_n","beard_y","beard_p","beard_o",   "beard_v", "beard_f", "beard_b", "beard_c","beard_t","beard_u","beard_r","beard_s","beard_a","beard_h","beard_g",], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_midage",0xffdfefe1,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff120808, 0xff007080c]),     
#     ("manface_old",0xffd0d0d0,["hair_white","hair_brunette","hair_red","hair_blonde"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ("manface_young_3",0xffdceded,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff120808, 0xff007080c]),
#     ("manface_young_4",0xffe0e8e8,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("manface_african",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
#     ("manface_old_2",0xffd5d5c5,["hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),

  (
    "woman", 1,
    "woman_body", "woman_calf_l", "f_handL",
    "female_head",
    [
      (40, 0, -1, 0, "Caucassian 2"),
      (30, 0, 0, 1, "Caucassian 1"),
      (10, 0, 0, 1, "Forehead"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    ["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s"],
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    [],
    [
      ("womanface_young", 0xFFE3E8EF, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("womanface_b", 0xFFDFDFDF, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("womanface_a", 0xFFE8DFE5, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("womanface_brown", 0xFFAF9F7E, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("womanface_african", 0xFF808080, ["hair_blonde"], [0xff120808, 0xff007080c]),
#      ("womanface_c_gaolu", 0xFFE3E8EF, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
    ],
    [(voice_die, "snd_woman_die"),(voice_hit, "snd_woman_hit"),(voice_yell, "snd_woman_yell")],
    "skel_human", 0.950000,
    psys_game_blood, psys_game_blood_2,
  ),

  (
    "no_head", 0,
    "man_body", "man_calf_l", "m_handL",
    "nomesh", man_face_keys,
    [],
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_midage",0xffdfefe1,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff120808, 0xff007080c]),     
#     ("manface_old",0xffd0d0d0,["hair_white","hair_brunette","hair_red","hair_blonde"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ("manface_young_3",0xffdceded,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff120808, 0xff007080c]),
#     ("manface_young_4",0xffe0e8e8,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("manface_african",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
#     ("manface_old_2",0xffd5d5c5,["hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),

  (
    "man_portugal", 0,
    "euro_body", "euro_calf_l", "euro_handL",
    "male_head_euro", euro_face_keys,
    ["pricha_akuratnaya_a","pricha_akuratnaya_short_a","man_hair_euro_t","man_hair_euro_s",     "man_hair_euro_q",     "man_hair_euro_p",     "man_hair_euro_r",     "man_hair_euro_n",     "man_hair_euro_v",     "man_hair_euro_y9",     "man_hair_euro_y7",     "man_hair_euro_m",     "pricha_gorshok_a",     "man_hair_euro_o",     "pricha_zachesanaya_a",     "man_hair_euro_u",     "man_hair_euro_y10",     "man_hair_euro_y11",     "man_hair_euro_y12",     "man_hair_euro_y2",     "man_hair_euro_y3",     "man_hair_euro_y4",     "man_hair_euro_y5",     "man_hair_euro_y6",     "man_hair_euro_y7","man_hair_euro_y8","man_hair_euro_y9"     ],
    ["beard_euro_e","beard_euro_d","beard_euro_k","beard_euro_l","beard_euro_i","beard_euro_j","beard_euro_z","beard_euro_m","beard_euro_n","beard_euro_y","beard_euro_p","beard_euro_o",   "beard_euro_v", "beard_euro_f", "beard_euro_b", "beard_euro_c","beard_euro_t","beard_euro_r","beard_euro_s","beard_euro_a","beard_euro_h","beard_euro_g",],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white",], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("europeanface_8",0xffcbe0e0,["hair_brunette"],[0xff120808, 0xff007080c]),
     ("europeanface_9",0xffdfefe1,["hair_brunette"],[0xff120808, 0xff007080c]),
     ("europeanface_10",0xffd0e0e0,["hair_brunette"],[0xff120808, 0xff007080c]),     
     ("europeanface_11",0xffdceded,["hair_brunette"],[0xff120808, 0xff007080c]),
     ("europeanface_12",0xffc0c8c8,["hair_brunette"],[0xff120808, 0xff007080c]),
     ("europeanface_13",0xfde4c8d8,["hair_brunette"],[0xff120808, 0xff007080c]),
     ("europeanface_14",0xffb0aab5,["hair_brunette"],[0xff120808, 0xff007080c]),
     ("europeanface_15",0xffe0e8e8,["hair_brunette"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("europeanface_16",0xff807c8a,["hair_brunette"],[0xff120808, 0xff007080c]),     
     ("europeanface_17",0xff807c8a,["hair_brunette"],[0xff120808, 0xff007080c]),     
     ("europeanface_18",0xff807c8a,["hair_brunette"],[0xff120808, 0xff007080c]),     
     ("europeanface_19",0xff807c8a,["hair_brunette"],[0xff120808, 0xff007080c]),     
     ("europeanface_20",0xffcbe0e0,["hair_brunette"],[0xffffffff, 0xffb04717, 0xff502a19]),     
     ("europeanface_21",0xff807c8a,["hair_brunette"],[0xff120808, 0xff007080c]),     
     ("europeanface_22",0xff807c8a,["hair_brunette"],[0xffffffff, 0xffb04717, 0xff502a19]),     
     ("europeanface_23",0xff807c8a,["hair_brunette"],[0xffffffff, 0xffb04717, 0xff502a19]),     
     ("europeanface_24",0xff807c8a,["hair_brunette"],[0xffffffff, 0xffb04717, 0xff502a19]),     
     ("europeanface_25",0xff807c8a,["hair_brunette"],[0xff120808, 0xff007080c]),     
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell2"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory2")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.6, comp_greater_than, (1.0,eye_to_eye_dist), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width) #hispania 1200
     [0.6, comp_less_than, (1.0,eye_to_eye_dist), (1.0,temple_width)], #hispania 1200
     [1.5, comp_greater_than, (1.0,face_ratio), (1.0,mouth_width)], #hispania 1200
	 [0.6, comp_greater_than, (-1.0,nose_width), (1.0,mouth_width)], #hispania 1200
     [-1.0, comp_less_than, (-1.0,nose_width), (1.0,mouth_width)], #hispania 1200
     # [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)], #hispania 1200
     # [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)], #hispania 1200
     # [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)], #hispania 1200
     # [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)], #hispania 1200
     ]
  ),

  (
    "man_chinese", 0,
    "euro_body", "euro_calf_l", "euro_handL",
    "chinese_head", man_face_keys,
    ["chinese_hair_a"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    ["chinese_beard_a","chinese_beard_b"], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("DaMing_face",0xffcbe0e0,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("DaMing_face_01",0xffdfefe1,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("DaMing_face_02",0xffd0e0e0,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("DaMing_face_03",0xffdceded,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("DaMing_face_04",0xffc0c8c8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("DaMing_face_05",0xfde4c8d8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("DaMing_face_06",0xffb0aab5,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("DaMing_face_07",0xffe0e8e8,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("DaMing_face_08",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("DaMing_face_09",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("DaMing_face_10",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("DaMing_face_11",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("DaMing_face_12",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("DaMing_face_13",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("DaMing_face_14",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("DaMing_face_15",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("DaMing_face_16",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("DaMing_face_17",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell3"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2
  ),
  (
    "sunda", 0,
    "man_body", "man_calf_l", "m_handL",
    "male_head", man_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    ["beard_e","beard_d","beard_k","beard_l","beard_i","beard_j","beard_z","beard_m","beard_n","beard_y","beard_p","beard_o",   "beard_v", "beard_f", "beard_b", "beard_c","beard_t","beard_u","beard_r","beard_s","beard_a","beard_h","beard_g",], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_midage",0xffdfefe1,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff120808, 0xff007080c]),     
#     ("manface_old",0xffd0d0d0,["hair_white","hair_brunette","hair_red","hair_blonde"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ("manface_young_3",0xffdceded,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff120808, 0xff007080c]),
#     ("manface_young_4",0xffe0e8e8,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("manface_african",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
#     ("manface_old_2",0xffd5d5c5,["hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell4"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),

  (
    "unique_1", 0,
    "man_body", "man_calf_l", "nomesh",
    "nomesh", man_face_keys,
    [],
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_midage",0xffdfefe1,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff120808, 0xff007080c]),     
#     ("manface_old",0xffd0d0d0,["hair_white","hair_brunette","hair_red","hair_blonde"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ("manface_young_3",0xffdceded,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff120808, 0xff007080c]),
#     ("manface_young_4",0xffe0e8e8,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("manface_african",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
#     ("manface_old_2",0xffd5d5c5,["hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt_unique_1"),(voice_grunt_long,"snd_man_grunt_unique_1"),(voice_yell,"snd_man_yell_unique_1"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),
  (
    "arab", 0,
    "arab_body", "arab_calf_l", "arab_handL",
    "male_head", man_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q",
     "man_hair_y9","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4"],
    ["beard_e","beard_d","beard_k","beard_l","beard_i","beard_j","beard_z","beard_m","beard_n","beard_y","beard_p","beard_o",   "beard_v", "beard_f", "beard_b", "beard_c","beard_t","beard_u","beard_r","beard_s","beard_a","beard_h","beard_g",], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("musulman_face_1",0xffcbe0e0,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("musulman_face_2",0xffdfefe1,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("musulman_face_3",0xffd0e0e0,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_4",0xffdceded,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("musulman_face_5",0xffc0c8c8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("musulman_face_6",0xfde4c8d8,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("musulman_face_7",0xffb0aab5,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("musulman_face_8",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_9",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_10",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_11",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_12",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_13",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_14",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_15",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_16",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_17",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_18",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_19",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_20",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("musulman_face_21",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),

]

# modmerger_start version=201 type=2
try:
    component_name = "skins"
    var_set = { "skins" : skins }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
