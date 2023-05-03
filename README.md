# dwm-wip
A python script for identifying potential breeding combinations that can be made in [*Dragon Warrior Monsters*](https://en.wikipedia.org/wiki/Dragon_Warrior_Monsters). This monster battling/breeding game was originally released for the GameBoy Color in 1998 and is a spin-off of the hit, Dragon Quest series.

Inb4: I've never met anyone else who's played this game and am aware that this repo is useful to virtually nobody, other than myself.
But on the chance that you are currently playing this right now-
\
\
Are you tired of running back and forth between Pulio's farm/the Starry Night chambers and individually comparing the breeding combinations that each of your monsters might produce? :D
Well look no further! I too grew tired of this and to no one's benefit but my own, dug up the official walkthrough for this game, condensed the offspring combinations into a dataset and wrote this script for just that exact, noble purpose! ᕕ(ᐛ)ᕗ

### Usage

Simply replace the contents of the `./config.csv` with the following information for each of the monsters in your party/farm:
* Nickname
 * The monster's given nickname
 * This can be left as an empty string (`''`), but including info increases readability
* Name
 * The actual name of the monster (`'DragonKid'`, `'Slime'`, etc)
* Gender
 * The sex of the monster, dictating breeding patterns
* Generation
 * The generation (or "amount of plusses" for a given monster)
* Party Status
 * This would be `True/False` as to whether this monster is in your current party
 * This value is not currently used, but was initially intended to affect how the output is sorted

Then run `python main.py`

### Example 
Using the following, example `config.csv`:
```
"Nickname","Name","Gender","Generation","In_Party"
"Abul","GiantWorm","male",9,True
"Fera","LizardMan","male",8,True
"Vadr","RogueNite","male",11,True
"Onyn","Oniono","male",0,False
"Ebi","Digster","female",0,False
"Yuni","Unicorn","female",2,False
```

```
rstallworthjr dwm-wip % ./main.py

Abul(bug+9) + Ebi(bug+0) = GiantWorm(bug+9)
Ebi(bug+0) + Abul(bug+9) = Digster(bug+9)
Abul(bug+9) + Yuni(beast+2) = Gophecada(bug+11)
Yuni(beast+2) + Abul(bug+9) = Saccer(beast+11)
Fera(dragon+8) + Ebi(bug+0) = FairyDrak(dragon+8)
Ebi(bug+0) + Fera(dragon+8) = Catapila(bug+8)
Fera(dragon+8) + Yuni(beast+2) = Tortragon(dragon+10)
Yuni(beast+2) + Fera(dragon+8) = Almiraj(beast+10)
Vadr(material+11) + Ebi(bug+0) = SpikyBoy(material+11)
Ebi(bug+0) + Vadr(material+11) = StagBug(bug+11)
Vadr(material+11) + Yuni(beast+2) = MadCandle(material+13)
Yuni(beast+2) + Vadr(material+11) = WindBeast(beast+13)
Onyn(plant+0) + Ebi(bug+0) = CactiBall(plant+0)
Ebi(bug+0) + Onyn(plant+0) = WeedBug(bug+0)
Onyn(plant+0) + Yuni(beast+2) = FloraMan(plant+2)
Yuni(beast+2) + Onyn(plant+0) = PillowRat(beast+2)
```


> **_NOTE:_**  There are a few other features I had initially planned on adding:
> * passing the input filename via an argument
> * allow sorting output by value of generation
> * adding feature to only include/exclude breeds involving party monsters
> * interactive prompt for updating config.csv
> * making monsters name case-insensitive
> But as of uploading this repo, I've already used the existing version to beat the game and probably won't be coming back to make changes lol ¯\\\_(ツ)_/¯
