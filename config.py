import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = "-5256631062"

CHECK_INTERVAL = 10

# ----------------------------------
# Vyhledávání
# ----------------------------------

SEARCH_URLS = [

    (
        "https://www.vinted.cz/catalog"
        "?search_text=pokemon"
        "&order=newest_first"
        "&status_ids[]=1"
        "&status_ids[]=6"
    ),

    (
        "https://www.vinted.cz/catalog"
        "?search_text=lorcana"
        "&order=newest_first"
        "&status_ids[]=1"
        "&status_ids[]=6"
    ),

]

# ----------------------------------
# Oblíbené Pokémon sety
# ----------------------------------

FAVORITE_SETS = [

    "151",
    "prismatic evolutions",
    "destined rivals",
    "journey together",
    "surging sparks",
    "evolving skies",

]

# ----------------------------------
# Pokémon sety
# ----------------------------------

SETS = [

    "151",
    "prismatic evolutions",
    "destined rivals",
    "journey together",
    "surging sparks",
    "twilight masquerade",
    "stellar crown",
    "paldean fates",
    "obsidian flames",
    "paradox rift",
    "temporal forces",
    "shrouded fable",
    "crown zenith",
    "lost origin",
    "silver tempest",
    "astral radiance",
    "fusion strike",
    "brilliant stars",
    "evolving skies",
    "battle styles",
    "vivid voltage",

]

# ----------------------------------
# Produkty
# ----------------------------------

PRODUCTS = [

    {
        "name": "Elite Trainer Box",
        "aliases": [
            "elite trainer box",
            "elite trainer",
            "trainer box",
            "etb",
        ],
        "limit": 3800,
        "priority": 100,
    },

    {
        "name": "Booster Box",
        "aliases": [
            "booster box",
            "display box",
            "booster display",
            "sealed display",
            "36 booster",
            "36 packs",
            "booster x36",

            "lorcana booster box",
            "lorcana booster display",
            "lorcana display",
            "display lorcana",
        ],
        "limit": 6500,
        "priority": 100,
    },

    {
        "name": "Booster Bundle",
        "aliases": [
            "booster bundle",
            "bundle",
            "6 pack",
            "6-pack",
            "six pack",
            "6 boosters",
            "bundle box",
        ],
        "limit": 1400,
        "priority": 90,
    },

    {
        "name": "Ultra Premium Collection",
        "aliases": [
            "ultra premium collection",
            "ultra premium",
            "upc",
        ],
        "limit": 5500,
        "priority": 100,
    },
        {
        "name": "Collection Box",
        "aliases": [
            "collection",
            "collection box",
            "premium collection",
            "illustration collection",
            "figure collection",
            "premium figure collection",
            "premium figure",
            "figure box",
            "premium box",
            "gift box",
            "pokemon box",
            "collector box",
            "box set",
            "pin collection",
            "pin box",
            "ex box",
            "pokemon ex box",
            "v box",
            "v-box",
            "vstar box",
            "vstar collection",
            "vmax box",
            "gx box",
            "box pokemon",
            "collection premium",
            "mega evolution",
            "mega heroes",
            "kolekcja",
            "kolekcja pokemon"
        ],
        "limit": 1800,
        "priority": 90,
    },

    {
        "name": "Mini Tin",
        "aliases": [
            "mini tin",
            "mini collector tin",
            "mini collector",
            "mini puszka",
        ],
        "limit": 900,
        "priority": 70,
    },

    {
        "name": "Tin",
        "aliases": [
            "tin",
            "collector tin",
            "stacking tin",
            "hidden potential tin",
            "pokeball tin",
            "poke ball tin",
            "puszka",
            "pokemon puszka"
        ],
        "limit": 800,
        "priority": 70,
    },

    {
        "name": "Collector Chest",
        "aliases": [
            "collector chest",
            "collector's chest",
            "collectors chest",
            "lunch box",
            "treasure chest",
        ],
        "limit": 1200,
        "priority": 80,
    },

    {
        "name": "Build & Battle",
        "aliases": [
            "build & battle",
            "build battle",
            "build-and-battle",
            "build battle box",
        ],
        "limit": 700,
        "priority": 70,
    },

    {
        "name": "Battle Deck",
        "aliases": [
            "battle deck",
            "league battle deck",
            "theme deck",
            "league deck",
        ],
        "limit": 600,
        "priority": 50,
    },

    {
        "name": "Trainer Toolkit",
        "aliases": [
            "trainer toolkit",
            "toolkit",
        ],
        "limit": 900,
        "priority": 60,
    },
        {
        "name": "Blister",
        "aliases": [
            "blister",
            "checklane blister",
            "single blister",
            "sleeved booster",
            "booster blister",
        ],
        "limit": 500,
        "priority": 40,
    },

    {
        "name": "Triple Blister",
        "aliases": [
            "3 pack",
            "3-pack",
            "3pack",
            "three pack",
            "triple blister",
        ],
        "limit": 1000,
        "priority": 60,
    },

    {
        "name": "Pokemon Center",
        "aliases": [
            "pokemon center",
        ],
        "limit": 6000,
        "priority": 120,
    },

]
    # ----------------------------------
    # Jackpot ceny
    #----------------------------------

JACKPOT_LIMITS = {

    "Booster Box": 4000,

    "Elite Trainer Box": 1600,

    "Ultra Premium Collection": 3000,

    "Collection Box": 1000,

    "Booster Bundle": 700,

    "Mini Tin": 300,

    "Tin": 350,

}
# ----------------------------------
# Blacklist
# ----------------------------------

BLOCKED_WORDS = [

    # Singles
    "karta",
    "karty",
    "card",
    "cards",
    "single",
    "singles",

    # Rarity
    "reverse",
    "holo",
    "holofoil",
    "masterball",
    "pokeball reverse",

    # Card types
    "energy",
    "supporter",

    # Bulk
    "bulk",
    "lot kart",
    "bulk cards",

    # Binder
    "binder",
    "album",
    "portfolio",

    # Plush / Toys
    "pluszak",
    "maskotka",
    "figurka",
    "funko",
    "lego",

    # Clothing
    "koszulka",
    "bluza",
    "spodenki",
    "pościel",
    "shirt",
    "hoodie",
    "cap",
    "čepice",
    "šiltovka",

    # Empty products
    "empty",
    "pusty",
    "prázdný",
    "box only",
    "only box",
    "bez karet",
    "bez boosterů",
    "obal",
    "wrapper",

    # Pokémon GO
    "pokemon go level",
    "pokemon go account",
    "konto pokemon go",

    # Empty tins / empty boxes

    "empty tin",
    "empty mini tin",
    "tin only",
    "mini tin only",

    "prázdný tin",
    "prázdný mini tin",
    "prázdná plechovka",
    "jen tin",
    "pouze tin",
    "bez obsahu",

    "pusta puszka",
    "puszka po",
    "pusta puszeczka",
    "puste pudełko",
    "same pudełko",
    "sam box",
    "box bez kart",
    "bez zawartości",
    "bez zawartosci",

    "same opakowanie",
    "opakowanie po",
    "opakowanie",

    "without boosters",
    "no boosters",
    "bez boostera",
]