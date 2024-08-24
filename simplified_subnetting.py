import pandas as pd
"""
def print_table(data):
    widths = {k: max(len(k), *(len(str(d[k])) for d in data)) for k in data[0]}
    print(" ".join(f"{k:{widths[k]}}" for k in widths))
    print("-" * sum(widths.values()))
    for row in data:
        print(" ".join(f"{str(row[k]):{widths[k]}}" for k in widths))
"""
nets=[]
adrs=[]
networks=[]
magic_cidr=[]
##Cidr nets
#Create 4x8 matrix
#adding 8 to the (i)ndex
#starting @ 1
for i in range(1,8+1):
    k=[]
    for j in range(1,4+1):
        k.append("/"+str(8*(j-1)+i))
    magic_cidr.append(k)
##Nets&Addresses
#loop over range
#+1 for networks
#-1 for addresses
for i in range(8):
    nets.append(2**(i+1))
    adrs.append(2**(8-1-i))
for i in range(8):
    n={}
    n['index'] = i+1
    n['cidr'] = magic_cidr[i]
    #256-addresses == last subnet
    n['last_subnet'] = 256-adrs[i]
    n['networks'] = nets[i]
    n['addresses'] = adrs[i]
    ##Usable range
    #addresses-2
    n['use_range'] = '[1:'+str(adrs[i]-2)+']'
    ##Gateway
    #addresses-1
    n['gateway'] = adrs[i]-1
    ##Network ranges
    #for range 0..256 step over number of addresses
    #only display 10 iterations [1:11]
    n['next_networks'] = [i for i in range(0,256,adrs[i])][1:11]
    ##Net calc
    #given the problem:
    #whats the first usabe ip of 12.190.185.10/18
    #We know /18 is in the 3rd column
    #So we examine 3rd octet 185
    #So /18 has 4 options for ranges
    #[1,64,128,192] 185>128 and 185<192
    #So selecting 12.190.128.1 as the first usable address
    n['network_calc'] = str(adrs[i]) + '*(n<=' + str(nets[i]-1) + ')'
    networks.append(n)

print(pd.DataFrame(networks))
#print_table(networks)
