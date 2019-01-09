def conv_min_seg(num):
    '''(number) -> number

    Converter Minutos em Segundos
       Converte o tempo informado em minutos para segundos
       Informa quantos segundos têm em X minutos

    >>> conv_min_seg(3)
    180 segundos
    >>> conv_min_seg(10)
    600 segundos   
    '''

    return print(num * 60 , 'segundos')


def conv_seg_min(num):
    '''(number) -> number

    Converter Segundos em Minutos
       Converte o tempo informado em segundos para minutos
       Informa quantos minutos têm em X segundos

    >>> conv_seg_min(60)
    1 minuto
    >>> conv_seg_min(181)
    3 minutos e 1 segundo    
    '''

    if num == 60:
        return print(num // 60 , 'minuto')

    if num < 60 and num % 60 == 1:
        return print('0 minutos e' , num % 60 , 'segundo')

    if num < 60:
        return print('0 minutos e' , num % 60 , 'segundos')
    
    if num > 60 and num < 120 and num % 60 == 1:
        return print(num // 60 , 'minuto e' , num % 60 , 'segundo')

    if num > 60 and num < 120:
        return print(num // 60 , 'minuto e' , num % 60 , 'segundos')

    if num >= 120 and num % 60 == 0:
        return print(num // 60 , 'minutos')

    if num >= 120 and num % 60 == 1:
        return print(num // 60 , 'minutos e' , num % 60 , 'segundo')
    
    elif num >= 120:
        return print(num // 60 , 'minutos e' , num % 60 , 'segundos')

    
def conv_hr_min(num):
    '''(number) -> number

    Converter Horas em Minutos
        Converte o tempo informado em horas para minutos
        Informa quantos minutos têm em X horas
        
    >>> conv_hr_min(5)
    300
    >>> conv_hr_min(12)
    720
    '''

    return print(num * 60 , 'minutos')


def conv_min_hr(num):
    '''(number) -> number

    Converter Minutos em Horas
        Converte o tempo informado em minutos para horas
        Informa quantas horas têm em X minutos
        
    >>> conv_min_hr(60)
    1 hora
    >>> conv_min_hr(300)
    5 horas
    '''

    if num == 60:
        return print(num // 60 , 'hora')

    if num < 60 and num % 60 == 1:
        return print('0 horas e' , num % 60 , 'minuto')

    if num < 60:
        return print('0 horas e' , num % 60 , 'minutos')
    
    if num > 60 and num < 120 and num % 60 == 1:
        return print(num // 60 , 'hora e' , num % 60 , 'minuto')

    if num > 60 and num < 120:
        return print(num // 60 , 'hora e' , num % 60 , 'minutos')

    if num >= 120 and num % 60 == 0:
        return print(num // 60 , 'horas')

    if num >= 120 and num % 60 == 1:
        return print(num // 60 , 'horas e' , num % 60 , 'minuto')

    elif num >= 120:
        return print(num // 60 , 'horas e' , num % 60 , 'minutos')




def conv_dias_horas(num):
    '''(number) -> number

    Converter Dias em Horas
       Converte o tempo informado em dias para horas
       Informa quantas horas têm em X dias

    >>> conv_dias_horas(1)
    24 horas
    >>> conv_dias_horas(7)
    168 horas
    '''

    return print(num * 24 , 'horas')


def conv_horas_dias(num):
    '''(number) -> number

    Converter Horas em Dias
       Converte o tempo informado em horas para dias
       Informa quantas dias têm em X horas

    >>> conv_horas_dias(24)
    1
    >>> conv_horas_dias(168)
    7
    '''

    if num == 24:
        return print(num // 24 , 'dia')

    if num < 24 and num % 24 == 1:
        return print('0 dias e' , num % 24 , 'hora')

    if num < 24:
        return print('0 dias e' , num % 24 , 'horas')
    
    if num > 24 and num < 48 and num % 24 == 1:
        return print(num // 24 , 'dia e' , num % 24 , 'hora')

    if num > 24 and num < 48:
        return print(num // 24 , 'dia e' , num % 24 , 'horas')

    if num >= 48 and num % 24 == 0:
        return print(num // 24 , 'dias')

    if num >= 48 and num % 24 == 1:
        return print(num // 24 , 'dias e' , num % 24 , 'hora')

    elif num >= 48:
        return print(num // 24 , 'dias e' , num % 24 , 'horas')


def conv_sem_dias(num):
    '''(number) -> number

    Converter Semanas em Dias
       Converte o tempo informado em semanas para dias
       Informa quantos dias têm em X semanas

    >>> conv_sem_dias(1)
    7 dias
    >>> conv_sem_dias(5)
    35 dias
    '''

    return print(num * 7 , 'dias')


def conv_dias_sem(num):
    '''(number) -> number

    Converter Dias em Semanas
       Converte o tempo informado em dias para semanas
       Informa quantas semanas têm em X dias

    >>> conv_dias_sem(7)
    1 semana
    >>> conv_dias_sem(35)
    5 semanas
    '''

    if num == 7:
        return print(num // 7 , 'semana')

    if num < 7 and num % 7 == 1:
        return print('0 semanas e' , num % 7 , 'dia')

    if num < 7:
        return print('0 semanas e' , num % 7 , 'dias')
    
    if num > 7 and num < 14 and num % 7 == 1:
        return print(num // 7 , 'semana e' , num % 7 , 'dia')

    if num > 7 and num < 14:
        return print(num // 7 , 'semana e' , num % 7 , 'dias')

    if num >= 14 and num % 7 == 0:
        return print(num // 7  , 'semanas')

    if num >= 14 and num % 7 == 1:
        return print(num // 7  , 'semanas e' , num % 7 , 'dia')
    
    elif num >= 14:
        return print(num // 7  , 'semanas e' , num % 7 , 'dias')


def conv_mes_sem(num):
    '''(number) -> number

    Converter Meses em Semanas
       Converte o tempo informado em meses para semanas
       Informa quantas semanas têm em X meses
       # essa conta não é exata

    >>> conv_mes_sem(1)
    4 semanas
    >>> conv_mes_sem(2)
    8 semanas
    '''

    return print(num * 4 , 'semanas')


def conv_sem_mes(num):
    '''(number) -> number

    Converter Semanas em Meses
       Converte o tempo informado em semanas para meses
       Informa quantos meses têm em X semanas
       ### X semanas são X meses e Y semanas

    >>> conv_sem_mes(4)
    1 mês
    >>> conv_sem_mes(8)
    2 meses
    '''

    if num == 4:
        return print(num // 4 , 'mês')

    if num < 4 and num % 4 == 1:
        return print('0 meses e' , num % 4 , 'semana')

    if num < 4:
        return print('0 meses e' , num % 4 , 'semanas')
    
    if num > 4 and num < 8 and num % 4 == 1:
        return print(num // 4 , 'mês e' , num % 4 , 'semana')

    if num > 4 and num < 8:
        return print(num // 4 , 'mês e' , num % 4 , 'semanas')

    if num >= 8 and num % 4 == 0:
        return print(num // 4 , 'meses')

    if num >= 8 and num % 4 == 1:
        return print(num // 4 , 'meses e' , num % 4 , 'semana')

    elif num >= 8:
        return print(num // 4 , 'meses e' , num % 4 , 'semanas')


def conv_anos_mes(num):
    '''(number) -> number

    Converter Meses em Anos
       Converte o tempo informado em anos para meses
       Informa quantos meses têm em X anos

    >>> conv_anos_mes(1)
    12 meses
    >>> conv_anos_mes(2)
    24 meses
    '''

    return print(num * 12 , 'meses')


def conv_mes_anos(num):
    '''(number) -> number

    Converter Anos em Meses
       Converte o tempo informado em meses para anos
       Informa quantos anos têm em X meses
       ### X meses são X anos e Y meses

    >>> conv_mes_anos(12)
    1 ano
    >>> conv_mes_anos(37)
    3 anos e 1 mês
    '''

    if num == 12:
        return print(num // 12 , 'ano')

    if num < 12 and num % 12 == 1:
        return print('0 anos e' , num % 12 , 'mês')

    if num < 12:
        return print('0 anos e' , num % 12 , 'meses')
    
    if num > 12 and num < 24 and num % 12 == 1:
        return print(num // 12 , 'ano e' , num % 12 , 'mês')

    if num > 12 and num < 24:
        return print(num // 12 , 'ano e' , num % 12 , 'meses')

    if num >= 24 and num % 12 == 0:
        return print(num // 12 , 'anos')

    if num >= 24 and num % 12 == 1:
        return print(num // 12 , 'anos e' , num % 12 , 'mês')

    elif num >= 24:
        return print(num // 12 , 'anos e' , num % 12 , 'meses')



