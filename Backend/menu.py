def display_menu(choices, title):
    print("-" * len(title))
    print(title)
    print("-" * len(title))
    
    for i, choice in enumerate(choices, start=1):
        print(i, choice)

def get_user_choice(choices, prompt):
    allowed_answers = [str(i) for i in range(1, len(choices) + 1)] + ['X', 'x']
    
    while True:
        choice = input(prompt)
        if choice in allowed_answers:
            return choice
        else:
            print(f'Введите номер от 1 до {len(choices)} или "X" для выхода.')

def menu(choices, title="Elon's delivery food:", prompt="Choose your food:"):
    display_menu(choices, title)
    
    choice = get_user_choice(choices, prompt)
    
    if choice in ['X', 'x']:
        return ''
    else:
        return choices[int(choice) - 1]
