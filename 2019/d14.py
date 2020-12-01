import math
import re


reactions = [
    "5 HLJD, 1 QHSZD, 13 SKZX => 8 MQPH",
    "10 LSLV => 4 JNJHW",
    "1 MQGF, 4 ZWXDQ, 1 GNSZ => 9 DGDH",
    "1 SKZX, 3 DJSP => 1 MCHV",
    "6 TWSR, 10 ZHDFS, 10 LQZXQ => 9 LXQNX",
    "1 FRVW, 1 CJTW => 9 BRCB",
    "20 ZHVNP => 8 XMXL",
    "7 JQJXP => 1 ZGZDW",
    "13 KRCM => 6 KXPQ",
    "4 ZWXDQ, 4 KFKQF, 1 DZDX => 2 MQGF",
    "8 DZDX, 2 ZKGM => 3 KFKQF",
    "3 FXFTB => 8 KVDGP",
    "10 MVGLF, 3 MWFBW, 13 XMXL, 1 CJTW, 2 ZSXJZ, 2 TNCZH, 3 MPFKN, 6 LXQNX => 2 MZMZQ",
    "5 FRVW => 3 NWBTP",
    "1 MVGLF, 2 NLXD, 6 KVDGP, 2 MQPH, 4 FXTJ, 10 TKXKF, 2 FRWV => 2 CSNS",
    "13 TWSR => 9 BNWT",
    "2 KRCM => 7 LSLV",
    "1 ZHDFS, 11 NTVZD, 1 JQJXP => 6 ZHVNP",
    "2 MCHV, 1 JNJHW => 6 NDQNH",
    "32 SMHJH, 6 KXPQ => 1 CJTW",
    "15 FXFTB, 1 MVGLF => 9 MPFKN",
    "119 ORE => 9 KRCM",
    "3 TNCZH => 9 BFQLT",
    "5 MPFKN, 7 TKXKF, 6 JQJXP, 2 DZDX, 16 LCQJ, 4 DGDH, 4 ZGZDW => 7 WVXW",
    "1 ZHDFS, 1 LXQNX => 3 TNCZH",
    "4 ZMVKM, 1 BRQT => 3 QHSZD",
    "24 FRVW, 1 KVDGP, 2 ZLNM => 3 FGLNK",
    "2 KXPQ, 1 LSLV, 22 HNRQ => 5 ZWXDQ",
    "6 ZWXDQ => 1 FRVW",
    "1 FXFTB, 2 MWFBW => 6 ZHDFS",
    "32 FRVW => 5 FRWV",
    "6 FXFTB, 6 NDQNH, 2 MWFBW => 1 JQJXP",
    "9 ZMVKM, 6 QHSZD, 5 LSLV => 4 SMHJH",
    "3 CHKZ => 6 HLJD",
    "21 BFQLT => 6 FXTJ",
    "1 SMHJH, 4 FXFTB => 6 CHKZ",
    "13 FRVW, 13 JQJXP, 1 GNSZ => 8 ZSXJZ",
    "2 NDQNH => 8 NTVZD",
    "3 KRCM => 2 ZKGM",
    "13 ZHDFS, 14 ZWXDQ, 1 CHKZ => 7 LQZXQ",
    "2 BNWT, 3 CHKZ => 7 ZLNM",
    "167 ORE => 1 BRQT",
    "1 LSLV => 3 DZDX",
    "8 MZMZQ, 7 NWBTP, 3 WVXW, 44 MQPH, 3 DJSP, 1 CSNS, 3 BRCB, 32 LQZXQ => 1 FUEL",
    "8 ZLNM => 2 NLXD",
    "30 JQJXP, 9 FGLNK => 7 LCQJ",
    "1 ZKGM, 19 KXPQ => 8 DJSP",
    "4 DJSP => 6 FXFTB",
    "25 NFTPZ => 6 ZMVKM",
    "14 ZHVNP, 1 MVGLF => 9 TKXKF",
    "1 BRQT => 2 SKZX",
    "6 ZKGM => 7 HNRQ",
    "3 DZDX => 5 TWSR",
    "1 SMHJH => 7 MVGLF",
    "3 NDQNH => 1 GNSZ",
    "153 ORE => 9 NFTPZ",
    "14 MCHV, 4 JNJHW, 2 DJSP => 4 MWFBW"
]


def extract_composant(string):
    composant_regex = re.compile("(\d+) ([A-Z]+)")
    matches = composant_regex.match(string)
    quantity, composer = int(matches.group(1)), matches.group(2)
    return quantity, composer


def extract_reaction(string):
    separator = string.index(" => ")
    reactives_str = string[0:separator]
    product = string[(separator+4):]
    reactives = reactives_str.split(", ")
    return extract_composant(product), [extract_composant(reactive) for reactive in reactives]


def get_ore_quantity(qty, product, reactions_composers, composers_rest):

    if qty == 0:
        return 0, composers_rest
    if product == "ORE":
        return qty, composers_rest

    product_available = composers_rest.get(product, 0)
    if product_available > 0:
        qty -= product_available
        if qty >= 0:
            composers_rest[product] = 0
        else:
            composers_rest[product] = -qty
            return 0, composers_rest

    product_qty, composers = reactions_composers[product]
    nb_reactions_needed = math.ceil(qty / product_qty)
    remaining_qty = (product_qty * nb_reactions_needed) - qty
    sum = 0
    for comp_qty, composer in composers:
        qty_needed = nb_reactions_needed * comp_qty
        ore_quantity, composers_rest = get_ore_quantity(qty_needed, composer, reactions_composers, composers_rest)
        sum += ore_quantity
    if remaining_qty > 0:
        composers_rest[product] = remaining_qty
    return sum, composers_rest


def run_14():
    reactions_composers = {
        prdct_comp: (prdct_qty, reactives)
        for (prdct_qty, prdct_comp), reactives in [extract_reaction(reaction) for reaction in reactions]}
    return reactions_composers


def run_14a():
    reactions_composers = run_14()
    ore_qty, _ = get_ore_quantity(1, "FUEL", reactions_composers, {})
    print(ore_qty)


def run_14b():
    reactions_composers = run_14()
    available_ore = 1000000000000
    total_fuel = 0
    composers_rest = {}
    previous_rests = {}
    while True:
        if total_fuel % 10000 == 0:
            print(f"Ore left : {available_ore} ({total_fuel} produced)")
        needed_ore, composers_rest = get_ore_quantity(1, "FUEL", reactions_composers, composers_rest)
        if needed_ore > available_ore:
            print("No more ORE avaialable.")
            break
        available_ore -= needed_ore
        total_fuel += 1
        rest_hash = hash(frozenset(composers_rest.items()))
        if rest_hash in previous_rests:
            print("Loop detected !")
            previous_ore, previous_fuel = previous_rests[rest_hash]
            print(f"Previous ore : {previous_ore}, previous fuel : {previous_fuel}")
            print(f"Current ore : {available_ore}, current fuel : {total_fuel}")
            break
        else:
            previous_rests[rest_hash] = (available_ore, total_fuel)
    print(f"Total fuel : {total_fuel}")
