import random
from autoclick import autoclick_regfreq
from click_timer import click_timer

password = input('Senha: ')

while True:
    t = random.randrange(1740, 1860)
    print(f'Random time: {t//60}:{t%60}')
    click_timer(t)
    autoclick_regfreq(password)