from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Initialize global game state
game_state = {
    'faction1': None,
    'faction2': None,
    'unit1': None,
    'unit2': None,
    'unit1_health': 0,
    'unit2_health': 0,
    'turn': 1,
    'battle_report': [],
    'message': ''
}

# Data for units and factions
UNITS = {
    'Space Marines': ['Space Marine', 'Assault Marine', 'Devastator'],
    'Orks': ['Boyz', 'Shoota Boyz', 'Warboss'],
    'Eldar': ['Guardian', 'Dire Avenger', 'Farseer']
}

FACTIONS = ['Space Marines', 'Orks', 'Eldar']

# Unit stats, including threshold for each unit
UNIT_STATS = {
    'Space Marine': {'health': 10, 'attack': 4, 'strength': 4, 'armor_save': 3, 'hit_threshold': 4},
    'Assault Marine': {'health': 8, 'attack': 5, 'strength': 4, 'armor_save': 3, 'hit_threshold': 3},
    'Devastator': {'health': 7, 'attack': 3, 'strength': 5, 'armor_save': 3, 'hit_threshold': 5},
    'Boyz': {'health': 8, 'attack': 4, 'strength': 5, 'armor_save': 6, 'hit_threshold': 5},
    'Shoota Boyz': {'health': 8, 'attack': 4, 'strength': 5, 'armor_save': 5, 'hit_threshold': 4},
    'Warboss': {'health': 12, 'attack': 5, 'strength': 6, 'armor_save': 4, 'hit_threshold': 2},
    'Guardian': {'health': 6, 'attack': 3, 'strength': 3, 'armor_save': 5, 'hit_threshold': 4},
    'Dire Avenger': {'health': 6, 'attack': 4, 'strength': 3, 'armor_save': 4, 'hit_threshold': 3},
    'Farseer': {'health': 5, 'attack': 3, 'strength': 3, 'armor_save': 4, 'hit_threshold': 5}
}

@app.route('/')
def index():
    return render_template('index.html', factions=FACTIONS)

@app.route('/start_game', methods=['POST'])
def start_game():
    faction1 = request.form['faction1']
    faction2 = request.form['faction2']
    unit1 = request.form['unit1']
    unit2 = request.form['unit2']
    
    # Initialize units and their health
    game_state['faction1'] = faction1
    game_state['faction2'] = faction2
    game_state['unit1'] = unit1
    game_state['unit2'] = unit2
    game_state['unit1_health'] = UNIT_STATS[unit1]['health']
    game_state['unit2_health'] = UNIT_STATS[unit2]['health']
    game_state['battle_report'] = []
    game_state['turn'] = 1
    game_state['message'] = ''
    
    return redirect(url_for('game'))

@app.route('/game')
def game():
    unit1 = game_state['unit1']
    unit2 = game_state['unit2']
    
    # Simulate the turn
    battle_result = simulate_turn(unit1, unit2)
    game_state['battle_report'].append(battle_result)
    
    # Check if the game has ended (one unit is destroyed)
    if game_state['unit1_health'] <= 0 or game_state['unit2_health'] <= 0:
        winner = unit1 if game_state['unit1_health'] > 0 else unit2
        game_state['message'] = f"{winner} wins the battle!"
        return render_template('game.html', game_state=game_state, unit1=unit1, unit2=unit2, UNIT_STATS=UNIT_STATS)
    
    return render_template('game.html', game_state=game_state, unit1=unit1, unit2=unit2, UNIT_STATS=UNIT_STATS)

def simulate_turn(unit1, unit2):
    # Get unit stats for both units
    unit1_stats = UNIT_STATS[unit1]
    unit2_stats = UNIT_STATS[unit2]
    
    # Simulate dice rolls for both units to determine if the attack hits
    attack1_roll = random.randint(1, 6) + unit1_stats['attack']
    attack2_roll = random.randint(1, 6) + unit2_stats['attack']
    
    # Get the individual hit thresholds for each unit
    hit_threshold1 = unit1_stats['hit_threshold']
    hit_threshold2 = unit2_stats['hit_threshold']

    # Initialize damage
    damage1 = 0
    damage2 = 0
    
    # Store the dice rolls for the battle report
    dice_rolls = {
        'unit1_attack': attack1_roll,
        'unit2_attack': attack2_roll
    }

    battle_report = f"Turn {game_state['turn']}:\n"
    
    # Unit 1 attacks Unit 2
    if attack1_roll >= hit_threshold1:
        # Successful hit: roll for damage
        damage1 = random.randint(1, 6)
        game_state['unit2_health'] -= damage1
        battle_report += f"Unit 1 ({unit1}) successfully attacks Unit 2 ({unit2}) with a roll of {attack1_roll} (hit threshold: {hit_threshold1}) causing {damage1} damage.\n"
    else:
        battle_report += f"Unit 1 ({unit1}) misses the attack on Unit 2 ({unit2}) with a roll of {attack1_roll} (hit threshold: {hit_threshold1}).\n"

    # Unit 2 attacks Unit 1
    if attack2_roll >= hit_threshold2:
        # Successful hit: roll for damage
        damage2 = random.randint(1, 6)
        game_state['unit1_health'] -= damage2
        battle_report += f"Unit 2 ({unit2}) successfully attacks Unit 1 ({unit1}) with a roll of {attack2_roll} (hit threshold: {hit_threshold2}) causing {damage2} damage.\n"
    else:
        battle_report += f"Unit 2 ({unit2}) misses the attack on Unit 1 ({unit1}) with a roll of {attack2_roll} (hit threshold: {hit_threshold2}).\n"

    # Display the remaining health in the report
    battle_report += f"\nRemaining Health:\n"
    battle_report += f"Unit 1 ({unit1}) HP: {game_state['unit1_health']} / {UNIT_STATS[unit1]['health']}\n"
    battle_report += f"Unit 2 ({unit2}) HP: {game_state['unit2_health']} / {UNIT_STATS[unit2]['health']}\n"
    
    return battle_report

@app.route('/get_units/<faction>')
def get_units(faction):
    units = UNITS.get(faction, [])
    return {'units': units}

@app.route('/restart_game')
def restart_game():
    # Reset the game state to the initial values
    game_state.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
