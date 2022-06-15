print('''
    You go over to the main terminal again. You see the options displayed across the screen.
    ''')
proceed = ''
while proceed != 'y':
    choice2 = input('''
        What option do you select?
            1. Escape Pod Diagnostics
            2. Escape Pod Logs
            3. Escape Pod Functions
        ''')
    if choice2 == "1":
        print('''
        OCCUPANTS: 2
        OXYGEN LEVELS: 46%
        LIFE SUPPORT STATUS: Stable
        FUEL LEVEL: 5%
        MANEUVERABILITY: Disabled
        HYDERDRIVE: Decomissioned
        SIGNAL TO PLURNING STAR: ---
        ''')
    if choice2 == "2":
        print('''
        NO LOGS TO DISPLAY.
        ''')
    if choice2 == "3":
        print('''
        ESCAPE POD FUNCTIONS:
        - Self Destruct
        - Engine Thrust
        - Jetison Fuel
        ''')
        proceed = 'y'