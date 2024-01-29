class BtnImage:
    menu = 'images/menuBtn.png'
    menuWithInfo = 'images/menuBtnInfo.png'
    backArrow = 'images/backarrowBtn.png'
    leaderBoards = 'images/leaderboards.png'
    close = 'images/closeBtn.png'
    maxCritTab = 'images/maxCritTab.png'
    totalTrophyTab = 'images/totalTrophyTab.png'
    bottomBattle = 'images/bottomBattleBtn.png'

class LabelImage:
    totalTrophy = 'images/totaltrophies.png'
    totalTrophyBadge1st = 'images/totalTrophyBadge1st.png'
    maxCrit = 'images/maxCrit.png'
    maxCritBadge1st = 'images/maxCrit1stBadge.png'


class HeroImage:
    zeus = 'images/heroZeus.png'
    zeus_ALT =  'images/heroZeus_ALT_.png'
    necro = 'images/heroNecro.png'
    mari = 'images/heroMari.png'
    mermaid = 'images/heroMermaid.png'
    jay = 'images/heroJay.png'
    snowflake = 'images/heroSnowflake.png'
    gadget = 'images/heroGadget.png'
    all = [zeus, zeus_ALT, necro, mari, mermaid, jay, snowflake, gadget]

class UnitImage:
    # Common
    common = []

    # Rare
    chemist = 'images/unitChemist.png'
    sharpshooterMax = 'images/unitSharpshooterMax.png'
    rare = [ chemist, sharpshooterMax ]

    # Epic
    mime = 'images/unitMime.png'
    portalMageMax = 'images/unitPortalMageMax.png'

    epic = [ mime, portalMageMax ]

    # Legendary
    # bruiser = ''
    cultist = 'images/unitCultist.png'
    # demonHunter = ''
    bansheeMax = 'images/unitBansheeMax.png'
    clock = 'images/unitClock.png'
    corsair = 'images/unitCorsair.png'
    cultist = 'images/unitCultist.png'
    demonHunterMax = 'images/unitDemonHunterMax.png'
    dryad = 'images/unitDryad.png'
    dryadMax = 'images/unitDryadMax.png'
    frostMax = 'images/unitFrostMax.png'
    harleyquin = 'images/unitHQ.png'
    inquisitorMax = 'images/unitInquisitorMax.png'
    knightStatueMax = 'images/unitKnightStatueMax.png'
    meteorMax = 'images/unitMeteorMax.png'
    minotaurMax = 'images/unitMinotaurMax.png'
    monk = 'images/unitMonk.png'
    monkMax = 'images/unitMonkMax.png'
    ridingHood = 'images/unitRidingHood.png'
    ridingHoodMax = 'images/unitRidingHoodMax.png'
    scrapper = 'images/unitScrapper.png'
    seadogMax = 'images/unitSeadogMax.png'
    shaman = 'images/unitShaman.png'
    spiritMasterMax = 'images/unitSpiritMasterMax.png'
    summoner = 'images/unitSummoner.png'
    summonerMax = 'images/unitSummonerMax.png'
    swordMax = 'images/unitSwordMax.png'
    trapper = 'images/unitTrapper.png'
    witchMax = 'images/unitWitchMax.png'

    legendary = [
            # banshee,
            bansheeMax,
            # bruiser, bruiserMax, bladeDancer, bladeDancerMax, boreas, boreasMax,
            clock, corsair, cultist,
            # cultistMax, demonHunter,
            demonHunterMax,
            # demonologist, demonologistMax,
            dryad, dryadMax,
            # frost,
            frostMax, harleyquin,
            # harleyquinMax, inquisitor,
            inquisitorMax,
            # genie, genieMax, unithex, unithexMax, knightStatue,
            knightStatueMax,
            # meteor,
            meteorMax,
            # minotaur,
            minotaurMax, monk, monkMax,
            ridingHood, ridingHoodMax,
            # robot, robotMax,
            scrapper,
            # stasis, seadog,
            seadogMax, shaman,
            # spiritMaster,
            spiritMasterMax, summoner, summonerMax,
            # tesla, teslaMax,
            trapper,
            # sword,
            swordMax,
            # witch,
            witchMax
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
            '_ALT_' : '',
            }
    @staticmethod
    def convert(_name: str):
        name = _name
        for k, v in Converter.__DICT.items():
            name = name.replace(k, v)
        return name
