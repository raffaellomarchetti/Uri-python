from datetime import datetime
from datetime import timedelta
h1,m1,h2,m2=input().split()
while h1+m1+h2+m2 != '0000':
    hora_inicio = datetime.strptime(h1+':'+m1, '%H:%M')
    hora_fim = datetime.strptime(h2+':'+m2, '%H:%M')
    if hora_inicio <= hora_fim:
        print(int((hora_fim-hora_inicio).total_seconds()/60))
    else:
        print(int(((hora_fim+ timedelta(days=1))-hora_inicio).total_seconds()/60))
    h1,m1,h2,m2 = input().split()