computer_parts = ["키보드", "키보드","키보드", "모니터","모니터","마우스", "사운드바",]
d = {}

for c in computer_parts:    # c안에 computer_parts들을 하나씩 대입    
    
    if c in d:              # c의 key가 딕셔너리 안에 있어?
        d[c] = d[c] + 1     # 있다면 value 값에 1을 더해줘
    else:
        d[c] = 1            # 그게 아니라면 d(부품)을 딕셔너리에 넣어주고 value값을 1로 만들어줘

print(d)                    # 딕셔너리의 key 와 value 값을 출력해줘