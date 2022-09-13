# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'По закону подлости дождь не пошел. '
        'Утка дошла до бара в целости и сохранности, но уставшая от ноши зонтика. '
        'Что выпить утке, чтобы расслабиться?'
    )
    option = ''
    options = {'Лонг Айленд': True, 'Пряный Латте Макиато на кокосовом \N{nail polish}': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return drunk_duck()
    return sober_duck()


def step2_no_umbrella():
    print(
        'По закону подлости пошел дождь. '
        'Утка дошла до бара мокрая и замерзшая. '
        'Что выпить утке, чтобы согреться?'
    )
    option = ''
    options = {'Пару стопочек Царской': True, 'Имбирный чай': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return drunk_duck()
    return sober_duck()


def drunk_duck():
    print(
        'Так как день зарплаты был вчера, утка оставила все деньги в баре и слегка перебрала. '
        'На ее счастье в баре оказался ее друг Улитка - завсегдатай данного заведения, '
        'стабильно появляющийся раз в месяц. Улитка снова поругался с барменом и друзья поехали домой.'
          )


def sober_duck():
    print(
        'Чинно проведя остаток вечера, утра встретила своего друга Улитку - завсегдатая этого заведения, '
        'стабильно появляющегося раз в месяц. Улитка снова поругался с барменом и друзья поехали домой.'
          )


if __name__ == '__main__':
    step1()
