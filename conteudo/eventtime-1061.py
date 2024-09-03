i,dia_com = input().split()
h_com,m_com,s_com = map(int,input().split(" : "))
i,dia_fim = input().split()
h_fim,m_fim,s_fim = map(int,input().split(" : "))

#converter dias em int
dia_com = int(dia_com)
dia_fim = int(dia_fim)

#print(m_com)

#coverter em segundos o tempo de começo, e depois o total
h_com *= 3600
m_com *= 60
total_com = 86400 - (h_com + m_com + s_com)


#converter em segundos o tempo do fim, e depois o total
h_fim *= 3600
m_fim *= 60
total_fim = h_fim + m_fim + s_fim

#achar a diferença em dias, e depois converter em segundos

total_dia = (dia_fim - dia_com)

#somar tudo, e converter de volat em dias minutos e segundos
total = total_fim + total_com
anw_dia = total % 86400
print(f"{anw_dia}")





