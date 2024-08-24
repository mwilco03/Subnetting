function subnetting(MAGIC=8) {
   const mgk_net = Array.from({ length: MAGIC }, (_, i) => Array.from({ length: Math.floor(MAGIC / 2) }, (_, j) => `/${(j + 1) * MAGIC - MAGIC + i + 1}`));
   const [nets, adrs] = Array.from({ length: MAGIC }, (_, i) => [2 ** (i + 1), 2 ** (MAGIC - i - 1)]).reduce(([nets, adrs], [net, adr]) => [[...nets, net], [...adrs, adr]], [[], []]);

   const networks = Array.from({ length: MAGIC }, (_, i) => ({
      index: i + 1,
      cidr: mgk_net[i],
      last_subnet: MAGIC * Math.floor(MAGIC * MAGIC / 2) - adrs[i],
      nets: nets[i],
      addresses: adrs[i],
      range: `[1:${adrs[i] - 2}]`,
      gateway: adrs[i] - 1,
      next_network: Array.from({ length: Math.floor((MAGIC * Math.floor(MAGIC * MAGIC / 2)-1) / adrs[i]) }, (_, j) => (j + 1) * adrs[i]).slice(0, 10),
      network_calc: `${adrs[i]}*(n<=${nets[i] - 1})`,
   }));
   console.table(networks);
}; subnetting();
