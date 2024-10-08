scripts = [
###WSE - Warband Script Enhancer 2 v1.0.8.4 by K700
#script_wse_multiplayer_message_received
# Called each time a composite multiplayer message is received
# INPUT
# script param 1 = sender player no
# script param 2 = event no
("wse_multiplayer_message_received", [
	#(store_script_param, ":player_no", 1),
	#(store_script_param, ":event_no", 2),
]),

#script_wse_game_saved
# Called each time after game is saved successfully
("wse_game_saved", [
]),

#script_wse_savegame_loaded
# Called each time after savegame is loaded successfully
("wse_savegame_loaded", [
]),

#script_wse_chat_message_received
# Called each time a chat message is received (both for servers and clients)
# INPUT
# script param 1 = sender player no
# script param 2 = chat type (0 = global, 1 = team)
# s0 = message
# OUTPUT
# trigger result = anything non-zero suppresses default chat behavior. Server will not even broadcast messages to clients.
# result string = changes message text for default chat behavior (if not suppressed).
("wse_chat_message_received", [
	#(store_script_param, ":player_no", 1),
	#(store_script_param, ":chat_type", 2),
]),

#script_wse_console_command_received
# Called each time a command is typed on the dedicated server console or received with RCON (after parsing standard commands)
# INPUT
# script param 1 = command type (0 - local, 1 - remote)
# script param 2 = num parts if bAutoSplitModuleConsoleCommands enabled
# s0 = text
# OUTPUT
# trigger result = anything non-zero if the command succeeded
# result string = message to display on success (if empty, default message will be used)
("wse_console_command_received", [
	#(store_script_param, ":command_type", 1),
	#(store_script_param, ":num_parts", 2),
]),

#script_wse_get_agent_scale
# Called each time an agent is created
# INPUT
# script param 1 = troop no
# script param 2 = horse item no
# script param 3 = horse item modifier
# script param 4 = player no
# OUTPUT
# trigger result = agent scale (fixed point)
("wse_get_agent_scale", [
	#(store_script_param, ":troop_no", 1),
	#(store_script_param, ":horse_item_no", 2),
	#(store_script_param, ":horse_item_modifier", 3),
	#(store_script_param, ":player_no", 4),
]),

#script_wse_window_opened
# Called each time a window (party/inventory/character) is opened
# INPUT
# script param 1 = window no
# script param 2 = window param 1
# script param 3 = window param 2
# OUTPUT
# trigger result = presentation that replaces the window (if not set or negative, window will open normally)
("wse_window_opened", [
	#(store_script_param, ":window_no", 1),
	#(store_script_param, ":window_param_1", 2),
	#(store_script_param, ":window_param_2", 3),
]),
                                                         
 

#script_game_missile_dives_into_water
# Called each time a missile dives into water
# INPUT
# script param 1 = missile item no
# script param 2 = missile item modifier
# script param 3 = launcher item no
# script param 4 = launcher item modifier
# script param 5 = shooter agent no
# script param 6 = missile no
# pos1 = water impact position and rotation
("game_missile_dives_into_water", [
	#(store_script_param, ":missile_item_no", 1),
	#(store_script_param, ":missile_item_modifier", 2),
	#(store_script_param, ":launcher_item_no", 3),
	#(store_script_param, ":launcher_item_modifier", 4),
	#(store_script_param, ":shooter_agent_no", 5),
	#(store_script_param, ":missile_no", 6),
]),

#script_wse_get_server_info
# Called each time a http request for server info received (http://server_ip:server_port/)
# OUTPUT
# trigger result = anything non-zero replace message text for response info 
# result string =  message text for response info 
("wse_get_server_info", [
]),

#script_wse_initial_window_start
# Called each time after initial window started with bMainMenuScene=true (requires WSE2)
("wse_initial_window_start", [
]),
###WSE - Warband Script Enhancer 2 v1.0.8.4 by K700 - end
]

def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1171 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "scripts"
		orig_scripts = var_set[var_name_1]
		
		modmerge_pbod_scripts(orig_scripts)
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)

from util_scripts import *
def modmerge_pbod_scripts(orig_scripts):
	add_scripts(orig_scripts, scripts, True)