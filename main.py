s = 'Бритва Оккама (иногда лезвие Оккама) — методологический принцип, в кратком виде гласящий: Не следует множить сущее без необходимости, либо не следует привлекать новые сущности без крайней на то необходимости.'
s = s.lower()
sp_simvol = []
sp_count = []
for i in range(len(s)):
    if s[i] in sp_simvol:
        index = sp_simvol.index(s[i])
        sp_count[index] += 1
    else:
        sp_simvol.append(s[i])
        sp_count.append(1)
t = []
for i in range(len(sp_simvol)):
    t.append([sp_count[i], sp_simvol[i]])
print(sorted(t))



