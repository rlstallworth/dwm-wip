class Monster:
    def __init__(self, nickname, name, generation):
        self.name = name
        self.nickname = nickname if nickname else name
        self.generation = generation
        self.family = self.get_family()

    def get_family(self):
        family = None
        for key in families:
            for name in families[key]:
                if name.lower() == self.name.lower():
                    family = key
                    break
        if family == None:
            print(f"Could not find family of {self.name}")
        return family
    
    def __str__(self):
        return f"{self.nickname}({self.family}+{self.generation})"

    def breed(self, mate):
        generation = self.generation + mate.generation

        if self.family == mate.family:
            return Monster(None, self.name, generation)

        ped_key=self.name
        if ped_key in matches:
            mate_key=mate.name
            if mate_key in matches[ped_key]:
                return Monster(None, matches[ped_key][mate_key], generation)
            mate_key=f"Any {mate.family}"
            if mate_key in matches[ped_key]:
                return Monster(None, matches[ped_key][mate_key], generation)

        ped_key=f"Any {self.family}"
        if ped_key in matches:
            mate_key=mate.name
            if mate_key in matches[ped_key]:
                return Monster(None, matches[ped_key][mate_key], generation)
            mate_key=f"Any {mate.family}"
            if mate_key in matches[ped_key]:
                return Monster(None, matches[ped_key][mate_key], generation)

        print(f"No offspring of {self.name} + {mate.name}")

families = {
	"slime":["DrakSlime", "SpotSlime", "WingSlime", "TreeSlime", "Snaily", "SlimeNite", "Babble", "BoxSlime", "Slime", "Healer", "FangSlime", "RockSlime", "SlimeBorg", "Slabbit", "SpotKing", "KingSlime", "Metaly", "Metabble", "MetalKing", "GoldSlime"],
	"dragon":["DragonKid", "Tortragon", "Pteranod", "Gasgon", "FairyDrak", "LizardMan", "Poisongon", "Swordgon", "Dragon", "MiniDrak", "MadDragon", "Rayburn", "Chamelgon", "LizardFly", "Andreal", "KingCobra", "Spikerous", "GreatDrak", "Crestpent", "WingSnake", "Coatol", "Orochi", "BattleRex", "SkyDragon", "Divinegon"],
	"beast":["Tonguella", "Almiraj", "CatFly", "PillowRat", "Saccer", "GulpBeast", "Skullroo", "WindBeast", "Anteater", "SuperTen", "IronTurt", "Mommonja", "HammerMan", "Grizzly", "Yeti", "MadGopher", "FairyRat", "Unicorn", "Goategon", "WildApe", "Trumpeter", "KingLeo", "DarkHorn", "MadCat", "BigEye"],
	"bird":["Picky", "Wyvern", "BullBird", "Florajay", "DuckKite", "MadPecker", "MadRaven", "MistyWing", "Dracky", "BigRoost", "StubBird", "LandOwl", "MadGoose", "MadCondor", "Blizzardy", "Phoenix", "ZapBird", "WhipBird", "FunkyBird", "RainHawk"],
	"plant":["MadPlant", "FireWeed", "FloraMan", "WingTree", "CactiBall", "Gulpple", "Toadstool", "AmberWeed", "Stubsuck", "Oniono", "DanceVegi", "TreeBoy", "FaceTree", "HerbMan", "BeanMan", "EvilSeed", "ManEater", "Snapper", "Rosevine", "Watabou"],
	"bug":["GiantSlug", "Catapila", "Gophecada", "Butterfly", "WeedBug", "GiantWorm", "Lipsy", "StagBug", "ArmyAnt", "GoHopper", "TailEater", "ArmorPede", "Eyeder", "GiantMoth", "Droll", "ArmyCrab", "MadHornet", "HornBeet", "Armorpion", "Digster"],
	"devil":["Pixy", "ArcDemon", "AgDevil", "Demonite", "DarkEye", "EyeBall", "SkulRider", "EvilBeast", "1EyeClown", "Gremlin", "MedusaEye", "Lionex", "GoatHorn", "Orc", "Ogre", "GateGuard", "ChopClown", "Grendal", "Akubar", "MadKnight", "Gigantes", "Centasaur", "EvilArmor", "Jamirus", "Durran"],
	"zombie":["Spooky", "Skullgon", "PutrePup", "RotRaven", "Mummy", "DarkCrab", "DeadNite", "Shadow", "Hork", "Mudron", "NiteWhip", "MadSpirit", "WindMerge", "Reaper", "DeadNoble", "WhiteKing", "BoneSlave", "Skeletor", "Servant", "CopyCat"],
	"material":[ "JewelBag", "EvilWand", "MadCandle", "CoilBird", "Facer", "SpikyBoy", "MadMirror", "RogueNite", "Goopi", "Voodoll", "MetalDrak", "Balzak", "SabreMan", "CurseLamp", "Roboster", "EvilPot", "Gismo", "LavaMan", "IceMan", "Mimic", "MudDoll", "Golem", "StoneMan", "BombCrag", "GoldGolem"],
	"boss":["DracoLord", "DracoLord", "Hargon", "Sidoh", "Baramos", "Zoma", "Pizzaro", "Esterk", "Mirudraas", "Mirudraas", "Mudou", "DeathMore", "DeathMore", "DeathMore", "Darkdrium"]
}

matches = {
  "Any beast" : {
    "Any bird": "CatFly",
    "Any boss": "DarkHorn",
    "Any bug": "Saccer",
    "Any devil": "Grizzly",
    "Any dragon": "Almiraj",
    "Any material": "WindBeast",
    "Any plant": "PillowRat",
    "Any slime": "Tonguella",
    "Any zombie": "Skullroo",
    "Dragon": "MadCat",
    "DrakSlime": "Goategon",
    "DuckKite": "Mommonja",
    "EyeBall": "BigEye",
    "FangSlime": "Unicorn",
    "LizardFly": "FairyRat",
    "MadPecker": "WildApe",
    "Mudron": "SuperTen",
    "Orc": "Yeti",
    "SabreMan": "MadGopher",
    "StubSuck": "HammerMan",
    "Tortragon": "IronTurt"
  },
  "Any bird": {
    "Any beast": "BullBird",
    "Any boss": "ZapBird",
    "Any bug": "DuckKite",
    "Any devil": "MadPecker",
    "Any dragon": "Wyvern",
    "Any material": "MistyWing",
    "Any plant": "FloraJay",
    "Any slime": "Picky",
    "Any zombie": "MadRaven",
    "CoilBird": "MadCondor",
    "DanceVegi": "FunkyBird",
    "DrakSlime": "Phoenix",
    "Droll": "MadGoose",
    "IceMan": "Blizzardy",
    "Rayburn": "WhipBird",
    "RockSlime": "StubBird"
  },
  "Any bug": {
    "AmberWeed": "Eyeder",
    "Any beast": "Gophecada",
    "Any bird": "Butterfly",
    "Any boss": "Digster",
    "Any devil": "GiantWorm",
    "Any dragon": "Catapila",
    "Any material": "StagBug",
    "Any plant": "WeedBug",
    "Any slime": "GiantSlug",
    "Any zombie": "Lipsy",
    "DarkCrab": "ArmyCrab",
    "FairyRat": "MadHornet",
    "FloraMan": "TailEater",
    "IronTurt": "Armorpede",
    "Saccer": "GiantMoth",
    "Spooky": "Droll"
  },
  "Any devil": {
    "Any beast": "Gremlin",
    "Any bird": "Demonite",
    "Any boss": "ArcDemon",
    "Any bug": "EyeBall",
    "Any dragon": "MedusaEye",
    "Any material": "EvilBeast",
    "Any plant": "DarkEye",
    "Any slime": "Pixy",
    "Any zombie": "SkulRider",
    "Armorpede": "EvilArmor",
    "BeanMan": "Orc",
    "BigEye": "Gigantes",
    "DarkHorn": "GoatHorn",
    "HammerMan": "Ogre",
    "LizardMan": "Lionex",
    "MadDragon": "Grendal",
    "RogueNite": "MadKnight"
  },
  "Any dragon": {
    "Any beast": "Tortragon",
    "Any bird": "Pteranod",
    "Any bug": "FairyDrak",
    "Any devil": "LizardMan",
    "Any material": "Swordgon",
    "Any plant": "Gasgon",
    "Any slime": "DragonKid",
    "Any zombie": "Poisongon",
    "ArmyCrab": "Spikerous",
    "Babble": "KingCobra",
    "BigRoost": "Crestpent",
    "GoHopper": "LizardFly",
    "GulpBeast": "MadDragon",
    "Gulpple": "Andreal",
    "Lionex": "BattleRex",
    "MadCondor": "Rayburn",
    "Phoenix": "SkyDragon",
    "Picky": "MiniDrak",
    "SpotKing": "GreatDrak",
    "Voodoll": "Chamelgon"
  },
  "Any material": {
    "Andreal": "MetalDrak",
    "Any beast": "MadCandle",
    "Any bird": "CoilBird",
    "Any boss": "Balzak",
    "Any bug": "SpikyBoy",
    "Any devil": "MadMirror",
    "Any dragon": "EvilWand",
    "Any plant": "Facer",
    "Any slime": "JewelBag",
    "Any zombie": "RogueNite",
    "BoxSlime": "Mimic",
    "GiantWorm": "SabreMan",
    "Lipsy": "Voodoll",
    "SkulRider": "Roboster",
    "Snaily": "EvilPot",
    "WingTree": "CurseLamp"
  },
  "Any plant": {
    "Any beast": "FloraMan",
    "Any bird": "WingTree",
    "Any boss": "RoseVine",
    "Any bug": "CactiBall",
    "Any devil": "Gulpple",
    "Any dragon": "FireWeed",
    "Any material": "AmberWeed",
    "Any slime": "MadPlant",
    "Any zombie": "Toadstool",
    "Butterfly": "EvilSeed",
    "Facer": "DanceVegi",
    "FunkyBird": "HerbMan",
    "Gophecada": "Oniono",
    "NiteWhip": "FaceTree",
    "PillowRat": "BeanMan",
    "Pixy": "TreeBoy"
  },
  "Any slime": {
    "Almiraj": "FangSlime",
    "Any beast": "SpotSlime",
    "Any bird": "WingSlime",
    "Any bug": "Snaily",
    "Any devil": "SlimeNite",
    "Any dragon": "DrakSlime",
    "Any material": "BoxSlime",
    "Any plant": "TreeSlime",
    "Any zombie": "Babble",
    "BombCrag": "RockSlime",
    "MetalDrak": "Metaly",
    "Roboster": "SlimeBorg",
    "Skullroo": "Slabbit"
  },
  "Any zombie": {
    "Any beast": "PutrePup",
    "Any bird": "RotRaven",
    "Any boss": "WhiteKing",
    "Any bug": "DarkCrab",
    "Any devil": "DeadNite",
    "Any dragon": "MadSpirit",
    "Any material": "Shadow",
    "Any plant": "Mummy",
    "Any slime": "Spooky",
    "GiantSlug": "Mudron",
    "MistyWing": "NiteWhip",
    "Swordgon": "Skullgon",
    "WeedBug": "Reaper",
    "WindBeast": "WindMerge"
  },
  "1EyeClown": { "1EyeClown": "ChopClown" },
  "Akubar": { "RainHawk": "Jamirus" },
  "AntEater": { "Any beast": "AntEater" },
  "ArmyAnt": { "Any bug": "ArmyAnt" },
  "Baramos": { "DarkHorn": "Mudou" },
  "BigRoost": { "Any bird": "BigRoost" },
  "Blizzardy": { "Phoenix": "RainHawk" },
  "BoneSlave": { "BoneSlave": "Skeletor" },
  "BullBird": { "Any beast": "LandOwl" },
  "Centasaur": { "GoldGolem": "Durran" },
  "Copycat": { "Zombie": "CopyCat" },
  "Crestpent": { "Crestpent": "WingSnake" },
  "DeadNite": { "DeadNite": "DeadNoble" },
  "DeathMore1": { "Armorpion": "DeathMore2" },
  "DeathMore2": { "Mudou": "DeathMore3" },
  "DeathMore3": { "Watabou": "Darkdrium" },
  "Demonite": { "Demonite": "GateGuard" },
  "Dracky": { "Any bird": "Dracky" },
  "DracoLord1": {
    "Divinegon": "DracoLord2",
    "Sidoh": "Zoma"
  },
  "DragonKid": { "DragonKid": "Dragon" },
  "Durran": { "Divinegon": "Pizzaro" },
  "Esterk": { "GoldSlime": "Mirudraas1" },
  "EvilSeed": { "EvilSeed": "ManEater" },
  "GateGuard": { "Any beast": "Centasaur" },
  "GoHopper": { "Any bug": "GoHopper" },
  "Golem": { "Golem": "StoneMan" },
  "Goopi": {
    "Any material": "Goopi",
    "FireWeed": "Gismo",
    "Goopi": "MudDoll"
  },
  "GreatDrak": { "MedusaEye": "Orchi" },
  "Gremlin": { "Any dragon": "AgDevil" },
  "Grendal": { "Grendal": "Akubar" },
  "Grizzly": { "Any dragon": "GulpBeast" },
  "Hargon": { "Orochi": "Baramos" },
  "Hork": {
    "Any zombie": "Hork",
    "Hork": "BoneSlave"
  },
  "HornBeet": { "HornBeet": "Armorpion" },
  "IceMan": { "LavaMan": "GoldGolem" },
  "Jamirus": { "Rosevine": "Sidoh" },
  "ManEater": { "ManEater": "Snapper" },
  "Metabble": { "Metabble": "MetalKing" },
  "MetalDrak": {
    "ArcDemon": "LavaMan",
    "Skullgon": "IceMan"
    },
  "MetalKing": {
    "MadCondor": "SpotKing",
    "MetalKing": "GoldSlime"
  },
  "Metaly": { "Metaly": "Metabble" },
  "Mirudraas1": { "Spikerous": "Mirudraas2" },
  "MudDoll": { "MudDoll": "Golem" },
  "Pixy": { "Any slime": "1EyeClown" },
  "Pizzaro": { "KingLeo": "Esterk" },
  "Servant": { "GreatDrak": "DracoLord1" },
  "Skeletor": { "Skeletor": "Servant" },
  "SkyDragon": { "Orochi": "Divinegon" },
  "Slime": {
    "Any slime": "Slime",
    "PillowRat": "Healer"
  },
  "SpikyBoy": { "SpikyBoy": "BombCrag" },
  "SpotKing": { "MadCondor": "KingSlime" },
  "StagBug": { "StagBug": "HornBeet" },
  "StubSuck": { "Any plant": "StubSuck" },
  "Trumpeter": { "Trumpeter": "KingLeo" },
  "WhiteKing": { "MetalKing": "Hargon" },
  "WildApe": { "WildApe": "Trumpeter" },
  "WingSnake": { "WingSnake": "Coatol" },
  "Zoma": { "Mirudraas1": "DeathMore1" }
}
