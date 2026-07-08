def calculate_score(result):

    score = 0

    # Základ produktu
    score += result["priority"]

    # Oblíbený set
    if result["favorite"]:
        score += 100

    # Rozpoznaný set
    if result["set"]:
        score += 40

    # Typ produktu
    PRODUCT_BONUS = {

        "Booster Box": 70,

        "Ultra Premium Collection": 65,

        "Elite Trainer Box": 55,

        "Pokemon Center": 55,

        "Collection Box": 35,

        "Collector Chest": 30,

        "Booster Bundle": 25,

        "Tin": 20,

        "Mini Tin": 15,

        "Build & Battle": 15,

        "Triple Blister": 12,

        "Blister": 8,

        "Battle Deck": 5,

        "Trainer Toolkit": 5,

    }

    score += PRODUCT_BONUS.get(result["product"], 0)

    return score