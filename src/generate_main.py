import ntpath
import os

victory_objectives_head = 'victory_objectives\n{\n'
victory_objectives_foot = '\n}\n'

victory_objectives = victory_objectives_head
victory_objectives_path = os.path.join(os.path.join(os.getcwd(), 'main'), 'victory_objectives.txt')

for faction_dir in os.walk(os.path.join(os.getcwd(), 'factions')):
    faction_name = ntpath.basename(faction_dir[0])
    faction_objectives_path = os.path.join(faction_dir[0], 'victory_objectives.txt')

    if faction_name == 'factions':
        continue

    with open(faction_objectives_path, 'r') as faction_objectives_file:
        faction_objectives = faction_objectives_file.read()

        victory_objectives += faction_objectives + '\n\n'

victory_objectives = victory_objectives[:-2] + victory_objectives_foot

with open(victory_objectives_path, 'w') as victory_objectives_file:
    victory_objectives_file.write(victory_objectives)
