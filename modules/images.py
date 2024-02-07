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
    cards = 'images/cardsLabel.png'
    bestPlayer = 'images/bestPlayer.png'
    top90 = 'images/top90.png'

class HeroImage:
    zeus = 'images/heroZeus.png'
    zeus_ALT =  'images/heroZeus_ALT_.png'
    necro = 'images/heroNecro.png'
    necro_ALT = 'images/heroNecro_ALT_.png'
    mari = 'images/heroMari.png'
    mari_ALT = 'images/heroMari_ALT_.png'
    mermaid = 'images/heroMermaid.png'
    jay = 'images/heroJay.png'
    snowflake = 'images/heroSnowflake.png'
    gadget = 'images/heroGadget.png'
    trickster = 'images/heroTrickster.png'
    all = [ zeus, zeus_ALT, necro, necro_ALT, mari, mari_ALT, 
           mermaid, jay, snowflake, gadget, trickster ]

class UnitImage:
    # Common
    hunterMax = 'images/unitHunterMax.png'
    rogueMax = 'images/unitRogueMax.png'
    common = [ hunterMax, rogueMax ]

    # Rare
    chemist = 'images/unitChemist.png'
    sharpshooterMax = 'images/unitSharpshooterMax.png'
    rare = [ chemist, sharpshooterMax ]

    # Epic
    engineerMax = 'images/unitEngineerMax.png'
    mime = 'images/unitMime.png'
    portalKeeper = 'images/unitPortalKeeper.png'
    portalMageMax = 'images/unitPortalMageMax.png'
    reaperMax = 'images/unitReaperMax.png'
    epic = [ engineerMax, mime, portalKeeper, portalMageMax, reaperMax]

    # Legendary
    bansheeMax = 'images/unitBansheeMax.png'
    bladeDancerMax = 'images/unitBladeDancerMax.png'
    bruiserMax = 'images/unitBruiserMax.png'
    cultist = 'images/unitCultist.png'
    # demonHunter = ''
    clock = 'images/unitClock.png'
    clock_ALT = 'images/unitClock_ALT_.png'
    corsair = 'images/unitCorsair.png'
    cultist = 'images/unitCultist.png'
    cultistMax = 'images/unitCultistMax.png'
    demonHunterMax = 'images/unitDemonHunterMax.png'
    demonHunterMax_ALT = 'images/unitDemonHunterMax_ALT_.png'
    dryad = 'images/unitDryad.png'
    dryadMax = 'images/unitDryadMax.png'
    dryadMax_ALT = 'images/unitDryadMax_ALT_.png'
    frostMax = 'images/unitFrostMax.png'
    genieMax = 'images/unitGenieMax.png'
    genie = 'images/unitGenieMax.png'
    harleyquin = 'images/unitHQ.png'
    harleyquin_ALT = 'images/unitHQ_ALT_.png'
    inquisitorMax = 'images/unitInquisitorMax.png'
    knightStatue = 'images/unitKnightStatue.png'
    knightStatueMax = 'images/unitKnightStatueMax.png'
    meteorMax = 'images/unitMeteorMax.png'
    minotaurMax = 'images/unitMinotaurMax.png'
    monk = 'images/unitMonk.png'
    monkMax = 'images/unitMonkMax.png'
    ridingHood = 'images/unitRidingHood.png'
    ridingHoodMax = 'images/unitRidingHoodMax.png'
    robotMax = 'images/unitRobotMax.png'
    scrapper = 'images/unitScrapper.png'
    seadog = 'images/unitSeadog.png'
    seadogMax = 'images/unitSeadogMax.png'
    shaman = 'images/unitShaman.png'
    spiritMasterMax = 'images/unitSpiritMasterMax.png'
    summoner = 'images/unitSummoner.png'
    summonerMax = 'images/unitSummonerMax.png'
    swordMax = 'images/unitSwordMax.png'
    teslaMax = 'images/unitTeslaMax.png'
    trapper = 'images/unitTrapper.png'
    trapper_ALT = 'images/unitTrapper_ALT_.png'
    witch = 'images/unitWitch.png'
    witchMax = 'images/unitWitchMax.png'
    legendary = [
            # banshee,
            bansheeMax,
            bladeDancerMax,
            # bladeDancer, boreas, boreasMax,
            # bruiser, 
            bruiserMax, clock, clock_ALT, corsair, cultist, cultistMax,
            # demonHunter,
            demonHunterMax, demonHunterMax_ALT,
            # demonologist, demonologistMax,
            dryad, dryadMax, dryadMax_ALT,
            # frost,
            frostMax, genie, genieMax, harleyquin, harleyquin_ALT,
            # harleyquinMax, inquisitor,
            inquisitorMax,
            # genie, genieMax, unithex, unithexMax,
            knightStatue, knightStatueMax,
            # meteor,
            meteorMax,
            # minotaur,
            minotaurMax, monk, monkMax, ridingHood, ridingHoodMax,
            # robot,
            robotMax, scrapper,
            # stasis,
            seadog, seadogMax, shaman,
            # spiritMaster,
            spiritMasterMax, summoner, summonerMax,
            # tesla,
            teslaMax, trapper, trapper_ALT,
            # sword,
            swordMax, witch, witchMax
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
