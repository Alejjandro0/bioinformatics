import json
import matplotlib.pyplot as plt
from collections import Counter

with open('blast_results.json') as f:
    data = json.load(f)

name_list = []

for result in data['BlastOutput2']:
    try:
        hits = result['report']['results']['search']['hits']
        for hit in hits:
            description = hit['description'][0]
            sciname = description['sciname']
            name_list.append(sciname)
    except:
        print("emtpy")

counts = Counter(name_list)

for name, count in counts.items():
    print(f"{name}: {count}")

names = list(counts.keys())
counts = list(counts.values())

plt.bar(names, counts)
plt.xlabel('Организмы')
plt.ylabel('Количество')
plt.title('Распределение организмов')
plt.xticks(rotation=45)
plt.show()
