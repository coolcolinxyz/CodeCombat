def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


summonTypes = ['paladin']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'paladin':
            CommandPaladin(friend)
        elif friend.type == 'soldier':
            CommandSoldier(friend)
        elif friend.type == 'peasant':
            CommandPeasant(friend)


def CommandSoldier(soldier):
    target = hero.findNearest(hero.findEnemies())
    if target:
        hero.command(soldier, "attack", target)


def CommandPeasant(soldier):
    item = soldier.findNearestItem()
    if item:
        hero.command(soldier, "move", item.pos)


def CommandPaladin(paladin):
    if (paladin.canCast("heal")):
        hero.command(paladin, "cast", "heal", self)
    else:
        hero.command(paladin, "shield")


def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def attack(target):
    if target:
        if (hero.distanceTo(target) < 10 and hero.isReady("bash")):
            hero.bash(target)


buildTypes = ["fire-trap"]


def buildTroops():
    enemy = hero.findNearest(hero.findEnemies())
    items = hero.findItems()
    paladins = hero.findByType('paladin')
    if len(items) > 0:
        pickUpNearestItem(items)
    elif len(paladins) > 0:
        hero.shield()
    elif enemy and hero.distanceTo(enemy) < 10:
        type = buildTypes[len(hero.built) % len(buildTypes)]
        if hero.gold > hero.costOf(type):
            hero.buildXY(type, enemy.pos.x, enemy.pos.y)
            hero.shield()
            hero.shield()
            hero.shield()
            hero.shield()
            hero.shield()
        else:
            pickUpNearestItem(items)
    else:
        pickUpNearestItem(items)


while True:
    commandTroops()
    buildTroops()
    if hero.health < hero.maxHealth * 0.6:
        paladins = hero.findByType('paladin')
        if len(paladins) == 0:
            summonTroops()
            summonTroops()
