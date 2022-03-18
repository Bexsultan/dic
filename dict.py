#problems1
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['drinks'] = {'Coca-Cola' : 1, 'Sprite' : 2, 'Fanta' : 3}
print(menu)

#problems2
a = {}
for i in range(3):
    n = input('name: ')
    p = input('password: ')
    a[n] = p

#problems3
d = {
    'Beksultan': 'programmer',
    'Kadyraly': 'security',
    'Usman': 'tester',
    'Damir': 'sporty man',
    'Islam': 'povar',
}
for a,b in d.items():
    print(f'Здравствуйте {a} Прекрасная профессия {b}')

#problems4
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['besh_barmak'] = 130
menu['lagman'] = 135
del menu['borsh']
for i,a in menu.items():
    print(i,a)

#problems5
a = {}
south_american_countries = list(frozenset(['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']))
for i in range (12):
    a[i+1]=south_american_countries[i]
print(a)