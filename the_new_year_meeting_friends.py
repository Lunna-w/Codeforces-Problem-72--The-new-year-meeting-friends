n,m,o=map(int,input().split())

ao=[]

m_n = abs(m - n)
n_o = abs(n - o)
m_o = abs(m - o)

ao.append(m_n)
ao.append(n_o)
ao.append(m_o)

ao.sort()
print(ao[0]+ao[1])

