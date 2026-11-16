ROOMS = {"L'ingresso":"The hall","Il soggiorno":"The living room","La sala da pranzo":"The dining room","La cucina":"The kitchen","La lavanderia":"The utility room","Il garage":"The garage","La cantina":"The cellar","La terrazza":"The patio","Il giardino":"The garden","La piscina":"The pool","La soffitta":"The loft","La cameretta":"The children's room","Il bagno":"The bathroom","La camera da letto":"The bedroom","Lo studio":"The study","Il gabinetto":"The loo"}
OBJ = """coat stand|console table|front door|shoe rack|grandfather clock|doormat|parcel|umbrella stand|ceiling light|smoke alarm
sofa|fireplace|telly|houseplant|bookcase|pouffe|coffee table|rug|chandelier|fan
sideboard|china cabinet|window|vase of flowers|serving trolley|chairs|table laid for dinner|bench|pendant light|garland
fridge|microwave|sink|bin|cooker|dishwasher|kitchen island|stools|cooker hood|hanging pans
washing machine|washing powder|tumble dryer|laundry basket|boiler|iron|washing-up bowl|broom|clothes horse|clothes pegs
tool board|petrol can|garage door|stepladder|car|toolbox|workbench|tyres|strip light|bike on the wall
wine rack|barrel|boiler|bucket|shelves|packs of water|crate of apples|mousetrap|hanging ham|bare light bulb
lemon tree in a pot|hammock|railing|lantern|swing seat|cushions|little table|watering can|awning|moon
hedge|kennel|tree|garden gnome|barbecue|flower bed|garden table|wheelbarrow|sun|cloud
outdoor shower|towel|diving board|rubber ring|deckchair|lilo|pool|pool ladder|parasol|seagull
trunk|boxes|skylight|rocking chair|tailor's dummy|gramophone|rolled-up rug|doll|beam|cobweb
toy box|teddy bear|doll's house|rocking horse|bunk beds|ball|foam play mat|train set|mobile|stars
bath|towel rail|washbasin|toothbrush|shower|scales|bath mat|laundry basket|strip light|shower curtain
wardrobe|bedside table|headboard|dressing table|chest of drawers|slippers|double bed|bedside rug|chandelier|mosquito net
desk|printer|shelves|globe|filing cabinet|swivel chair|rug|wastepaper basket|spotlights|air conditioner
toilet|loo roll|flush|toilet brush|hand basin|magazines|air freshener|mat|light bulb|little window""".split("\n")
import re, json
def apply(t):
    a = t.index("const HOMES = ["); b = t.index("];", a)
    block = t[a:b]
    for k, v in ROOMS.items(): block = block.replace(f'it: "{k}"', f'it: "{v}"')
    rows = OBJ; ri = -1; out = []; pos = 0
    homes = re.split(r'(\{ k: ")', block)
    # parcourir les maisons dans l'ordre
    parts = block.split('{ k: "')
    newparts = [parts[0]]
    for i, p in enumerate(parts[1:]):
        words = rows[i].split("|"); j = 0
        def sub(m):
            nonlocal j
            r = f'["the {words[j]} · {m.group(1)}"'; j += 1; return r
        p2 = re.sub(r'\["[^"·]+ · ([^"]+)"', sub, p)
        assert j == 10, (i, j)
        newparts.append(p2)
    return t[:a] + '{ k: "'.join(newparts) + t[b:]
