'''
If you were on the moon now, your weight will be 16,5% of your earth weight.
To calculate it you have to multiple to 0,165. If next 15 years your weight will
increase 1 kg each year. What will be your weight each year on the moon next
15 years?
'''
weight_now = int(input('Какой Ваш вес сейчас: '))
weight_on_moon = weight_now * 0.165
print(f"Ваш вес на луне был бы: {weight_on_moon}")
i=0
for kg in range(weight_now, weight_now+15):
    i+=1
    kg_on_moon = kg * 0.165
    print(f"Год: {i} вес на луне: {kg_on_moon} ")


