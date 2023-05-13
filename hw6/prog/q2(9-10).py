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
        print("Results are empty")

counts = Counter(name_list)
top_10 = counts.most_common(10)

total_count = len(name_list)

for name, count in top_10:
    percentage = (count / total_count) * 100
    print(f"{name}: {count} ({percentage:.2f}%)")

names = [name for name, _ in top_10]
counts = [count for _, count in top_10]

plt.bar(names, counts)
plt.xlabel('Организмы')
plt.ylabel('Количество')
plt.title('Топ 10 организмов')
plt.xticks(rotation=45)

for i, count in enumerate(counts):
    percentage = (count / total_count) * 100
    plt.text(i, count, f"{percentage:.2f}%", ha='center', va='bottom')

plt.show()
