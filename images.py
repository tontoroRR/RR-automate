class BtnImage:
    menu = 'images/menuBtn.png'
    menuWithInfo = 'images/menuBtnInfo.png'
    backArrow = 'images/backarrowBtn.png'
    leaderBoards = 'images/leaderboards.png'
    close = 'images/closeBtn.png'
    maxCritTab = 'images/maxCritTab.png'
    totalTrophyTab = 'images/totalTrophyTab.png'

class LabelImage:
    totalTrophy = 'images/totaltrophies.png'
    totalTrophyBadge1st = 'images/totalTrophyBadge1st.png'
    maxCrit = 'images/maxCrit.png'
    maxCritBadge1st = 'images/maxCrit1stBadge.png'


class HeroImage:
    zeus = 'images/heroZeus.png'
    necro = 'images/heroNecro.png'
    mari = 'images/heroMari.png'
    mermaid = 'images/heroMermaid.png'
    jay = 'images/heroJay.png'
    snowflake = 'images/heroSnowflake.png'
    gadget = 'images/heroGadget.png'
    all = [zeus, necro, mari, mermaid, jay, snowflake, gadget]

class UnitImage:
    # Common
    common = []

    # Rare
    chemist = 'images/unitChemist.png'
    rare = [ chemist ]

    # Epic
    mime = 'images/unitMime.png'
    portalMageMax = 'images/unitPortalMageMax.png'

    epic = [ mime, portalMageMax ]

    # Legendary
    # bruiser = ''
    cultist = 'images/unitCultist.png'
    # demonHunter = ''
    demonHunterMax = 'images/unitDemonHunterMax.png'
    dryad = 'images/unitDryad.png'
    dryadMax = 'images/unitDryadMax.png'
    frostMax = 'images/unitFrostMax.png'
    harleyquin = 'images/unitHQ.png'
    knightStatusMax = 'images/unitKnightStatusMax.png'
    monk = 'images/unitMonk.png'
    monkMax = 'images/unitMonkMax.png'
    meteorMax = 'images/unitMeteorMax.png'
    ridingHood = 'images/unitRidingHood.png'
    ridingHoodMax = 'images/unitRidingHoodMax.png'
    scrapper = 'images/unitScrapper.png'
    seadogMax = 'images/unitSeadogMax.png'
    spiritMasterMax = 'images/unitSpiritMasterMax.png'
    summoner = 'images/unitSummoner.png'
    summonerMax = 'images/unitSummonerMax.png'
    swordMax = 'images/unitSwordMax.png'
    witchMax = 'images/unitWitchMax.png'

    legendary = [
            cultist, demonHunterMax, dryad, dryadMax, frostMax, harleyquin, knightStatusMax,
            monk, monkMax, meteorMax, ridingHood, ridingHoodMax, scrapper, seadogMax,
            spiritMasterMax, summoner, summonerMax, swordMax, witchMax
            ]

    all = common + rare + epic + legendary

class Converter:
    __DICT: dict = {
            'images/': '',
            'unit' : '',
            'hero' : '',
            '.png' : '',
            'Max' : '(Max)',
            'HQ' : 'Harleyquin',
            }
    @staticmethod
    def convert(_name: str):
        name = _name
        for k, v in Converter.__DICT.items():
            name = name.replace(k, v)
        return name
