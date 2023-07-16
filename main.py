import json
import os
from datetime import datetime

# load Data
with open("/home/kinet/Desktop/Kinetikus/notesApp/notes.json", "r") as f:
    data = json.load(f)
    data: dict


# save Data
def save():
    with open("notes.json", "w") as f:
        json.dump(data, f, indent=3)


def comLine():
    clear = lambda :os.system('clear')
    clear()
    def line(pos):
        com = input(f"\n\n[*] commandLine [pos:{pos}]> ").split(" ")
        command = com[0]
        if command == 'select':
            select(com[1])
        if command == 'create':
            create(' '.join(com[1:]))
        if command == 'delete':
            del data['notes'][list(data['notes'].keys())[int(com[1])]]
            save()
            clear()
            comLine()


    def select(n):
        clear()
        n = int(n)
        key = list(data['notes'].keys())[n] # Title
        print(f"Title: {key}\n")
        t = data['notes'][key]
        [print(f"\t[{num}] {i[0]}: {i[1]}") for num, i in enumerate(list(t.items()))]
        
        com = input(f"\n\n[*] commandLine [pos:{key}]> ").split(" ")
        command = com[0]
        if command == 'add':
            add(com[1:], key)
        if command == 'delete':
            del data['notes'][key][list(t.keys())[int(com[1])]]
            # del data['notes'][key][t[int(com[1])]]
            save()
            clear()
            select(n)
        if command == 'back':
            clear()
            comLine()

    def create(title):
        data['notes'][title] = {}
        save()
        clear()
        select(str(len(data['notes'].keys())-1))
        line("create")
    
    def add(item, pos):
        item = ' '.join(item).split(', ')
        title = item[0]
        val = item[1]
        data['notes'][pos][title] = val
        save()
        clear()
        select(list(data['notes'].keys()).index(pos))
        
    
    print("KinetiNotes 0.1.0\n")
    for num, i in enumerate(data['notes']):
        print(f"\t[{num}] {i}")

    menu = f"\n(help)\n(exit)\n"
    print(menu)
    
    line("main")
    


if __name__ == "__main__":
    comLine()
