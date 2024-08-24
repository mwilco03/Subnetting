#import pandas as pd
def print_table(data):
    widths = {k: max(len(k), *(len(str(d[k])) for d in data)) for k in data[0]}
    print(" ".join(f"{k:{widths[k]}}" for k in widths))
    print("-" * sum(widths.values()))
    for row in data:
        print(" ".join(f"{str(row[k]):{widths[k]}}" for k in widths))

MAGIC = 8
mgk_net = [["/" + str(MAGIC * (j - 1) + i) for j in range(1, int(MAGIC / 2) + 1)] for i in range(1, MAGIC + 1)]
nets, adrs = zip(*[(2 ** (i + 1), 2 ** (MAGIC - i - 1)) for i in range(MAGIC)])
networks = []
for i in range(MAGIC):
    n = {}
    n['index'] = i + 1
    n['cidr'] = mgk_net[i]
    n['last_subnet'] = MAGIC * int(MAGIC * MAGIC / 2) - adrs[i]
    n['nets'] = nets[i]
    n['addresses'] = adrs[i]
    n['range'] = f'[1:{adrs[i] - 2}]'
    n['gateway'] = adrs[i] - 1
    n['next_network'] = [x for x in range(0, 256, adrs[i])][1:11]
    n['network_calc'] = f'{adrs[i]}*(n<={nets[i] - 1})'
    networks.append(n)
#df_networks = pd.DataFrame(networks)
#print(df_networks)
print_table(networks)
