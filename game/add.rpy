# Служебные функции

init python:

    r = Character("Рэндал", color="#c8ffc8")
    e = Character('Амариэ', color="#c800c8")
    l = Character('Мастер Сеймур', color="#0088c8")
    i = Character('Иган', color="#AA00FF")
    sbs = Character('Себастьян', color="#33DD00")
    ber = Character('Капитан Бер', color="#cfd483")
    heal = Character('Мастер медицины', color="#c3f243")
    ulm = Character('Ульм', color="#d3be53")
    ngrd = Character('Ночной стражник', color="#530bd3")
    cook = Character('Повар', color="#e95502")
    castellan = Character("Кастелян", color="#c80f08")
    templeguard = Character("Берн Кендрик", color="#142897")
    celsius = Character("Мастер Цельсий", color="#079634")
    tomash = Character("Мастер Томаш", color="#ff0000")

    # TO DO add descriptions from JSON & create data structures for locationinfo, questinfo etc.

    renpy.image("storage_storage_bg", Image("storage/storage_bg.png"))
    renpy.image("castellan_castellan_idle", Image("castellan/castellan_idle.png"))
    renpy.image("castellan_castellan_talk", Image("castellan/castellan_talk.png"))
    renpy.image("storage_castellan_coins_idle", Image("storage/castellan_coins_idle.png"))
    renpy.image("items_castellan_coins", Image("items/castellan_coins.png"))
    renpy.image("storage_go_back_idle", Image("storage/go_back_idle.png"))

    # Temple corridor
    renpy.image("temple_corridor_temple_corridor_bg", Image("temple_corridor/temple_corridor_bg.png"))
    renpy.image("temple_corridor_go_back_idle", Image("temple_corridor/go_back_idle.png"))
    renpy.image("temple_corridor_administration_enterance_idle", Image("temple_corridor/administration_enterance_idle.png"))
    renpy.image("temple_corridor_temple_entrance_idle", Image("temple_corridor/temple_entrance_idle.png"))
    renpy.image("celsius_celsius_idle", Image("celsius/celsius_idle.png"))
    renpy.image("celsius_celsius_talk", Image("celsius/celsius_talk.png"))
    renpy.image("guard_temple_guard_temple_talk", Image("guard_temple/guard_temple_talk.png"))
    renpy.image("guard_temple_guard_temple_idle", Image("guard_temple/guard_temple_idle.png"))

    # Temple
    renpy.image("temple_temple_bg", Image("temple/temple_bg.png"))
    renpy.image("temple_go_back_idle", Image("temple/go_back_idle.png"))
    renpy.image("temple_temple_altar_entrance_idle", Image("temple/temple_altar_entrance_idle.png"))
    renpy.image("tomash_tomash_idle", Image("tomash/tomash_idle.png"))
    renpy.image("tomash_tomash_talk", Image("tomash/tomash_talk.png"))
    
    # Altar
    renpy.image("altar_altar_bg", Image("altar/altar_bg.png"))
    renpy.image("altar_go_back_idle", Image("altar/go_back_idle.png"))
    renpy.image("altar_iomedae_grand_monument_idle", Image("altar/iomedae_grand_monument_idle.png"))
    renpy.image("items_iomedae_grand_monument", Image("items/iomedae_grand_monument.png"))

    def GetItemDescrText (ItemName):

        if ItemName == "alch_fire" :
            return AlchFireItemDescrText
        elif ItemName == "clothes_ofic" :
            return ClothesOficItemDescrText
        elif ItemName == "dagger" :
            return DaggerItemDescrText
        elif ItemName == "flask" :
            return FlaskItemDescrText
        elif ItemName == "harrow_deck" :
            return HarrowDeckDescrText
        elif ItemName == "heal" :
            return HealItemDescrText
        elif ItemName == "key_randal" :
            return KeyRandalItemDescrText
        elif ItemName == "kolbasa" :
            return KolbasaItemDescrText
        elif ItemName == "lamp" :
            return LampItemDescrText
        elif ItemName == "monk_robe" :
            return MonkRobeItemDescrText
        elif ItemName == "pouch" :
            return PouchItemDescrText
        elif ItemName == "rum_bottle" :
            return RumBottleItemDescrText
        elif ItemName == "water" :
            return WaterItemDescrText
        else :
            return "Хуй его еби что это такое."

    def GetBookLen (book_name):
        if book_name == "books/barracs_iomedae_":
            return 3
        if book_name == "classes/hexenhammer_":
            return 4
        else:
            return 0

    def GetQuestDescription (QuestName):
        if QuestName == "Сдать зачет по дьявольскому":
            return PassExamDevilLangDescrText
        elif QuestName == "Принести кастеляну масло":
            return BringOilToCastellanDescrText
        elif QuestName == "Найти Ульму пожрать":
            return FindFoodForUlmDescrText
        else:
            return "Эээм... хз че тут делать надо"

    def GetInvHLineNum(ItemsArray):
        if len(ItemsArray) // InventoryHSizeItems > 0:
            return len(ItemsArray) // InventoryHSizeItems + 1
        else:
            return len(ItemsArray) // InventoryHSizeItems



    class ItemClass():

        def __init__(self, **kwargs):
            self.hp = kwargs['hp']
            self.cost = kwargs['cost']
            self.magic = kwargs['magic']
            self.material = kwargs['material']
            self.owner = kwargs['owner']
            self.descr = kwargs['descr']
            self.name = kwargs['name']
            self.effect = kwargs['effect']
            self.effect_type = kwargs['effect_type']
            self.stat_req = kwargs['stat_req']
            self.abil_req = kwargs['abil_req']
            self.solidity = kwargs['solidity']
            self.fragile = kwargs['fragile']
            self.weight = kwargs['weight']
            self.icon = kwargs['icon']
            self.pic = kwargs['pic']
            self.latch = False
            self.can_be_taken = kwargs['can_be_taken']

        def IsBroken (self):
            if self.hp <= 0:
                return True
            else:
                return False

        def GetDamage (self, damage):
            if damage > self.solidity:
                self.hp = self.hp - damage

    class LocationClass:
        def __init__ (self,  **kwargs):
            self.name = kwargs['name']
            self.animals = kwargs['animals']
            self.npcs = kwargs['npcs']
            self.doors = kwargs['doors']
            self.objects = kwargs['objects']
            self.visited = False
            self.loc_description = kwargs['loc_description']
            self.pic = kwargs['pic']

        def RemoveObject (self, object):
            try:
                self.objects.remove(object)
            except ValueError:
                renpy.display_notify("Error! There is no " + object.name + " in " + self.name + "!")

    items_descr_dict = dict()
    work_energy_cost = dict()
    work_food_cost = dict()


    items_descr_dict['Alaric\'s sword'] = 'Well made one handed sword with sign "Alaric\'s property" on it'
    items_descr_dict['Longsword'] = 'Ordinary two handed longsword. VERY long'
    items_descr_dict['Healing potion'] = 'Ordinary healing potion'
    items_descr_dict['Golden coin'] = 'Обычная золотая монета'
    items_descr_dict['IomedaeAltarStatue'] = 'Охренительно большя статуя Иомедей'

    work_energy_cost["easy"] = 4
    work_energy_cost["hard"] = 10

    work_food_cost["easy"] = 4
    work_food_cost["hard"] = 10

    class WeaponClass(ItemClass):
        itemtype = "Weapon"
        def __init__(self, **kwargs):
            self.hands_req = kwargs['hands_req']
            super().__init__(**kwargs)

    class PotionClass(ItemClass):
        itemtype = "Potion"

    class TextClass(ItemClass):
        itemtype = "Text"

    class CoinClass(ItemClass):
        itemtype = "Coin"

    class ArmorClass(ItemClass):
        itemtype = "Armor"
        def __init__(self, **kwargs):
            self.value = kwargs['value']
            self.armor_type = kwargs['armor_type']
            super().__init__(**kwargs)

    class ItemBunchClass():
        itemtype = "Bunch"
        def __init__(self, item, number, pic):
            self.item = item
            self.num = number
            self.pic = pic
            self.latch = False
            if item.itemtype == "Weapon":
                _bunchtype = "Связка"
            elif item.itemtype == "Potion":
                _bunchtype = "Ящик с"
            elif item.itemtype == "Coin":
                _bunchtype = "Пригоршня"
            elif item.itemtype == "Text":
                _bunchtype = "Стопка"
            else:
                _bunchtype = "Куча"

            self.name =  _bunchtype + " c " + str(number) + " " + item.name



    class InvetoryClass():

        items = []

        def __init__(self, initial_items):
            self.items.extend(initial_items)

        def AddItem(self, item):

            if item.itemtype != "Bunch":
                self.items.append(item)
                renpy.display_notify(item.name, 'added in inventory')
            else:
                for i in range (item.num):
                    self.items.append(item)
                    _notify_text = str(item.num) + " " + item.item.name +  's added in inventory'
                    renpy.display_notify(_notify_text)

        def PrintItems(self):
            print("Invetory contains:")
            for i in range(len(self.items)):
                print(self.items[i].name)

        def RemoveItem(self, item):

            try:
                self.items.remove(item)
                print(item.name, 'removed from inventory')
            except ValueError:
                print('There is no', item.name, 'in inventory')

    class StatClass():

        def __init__(self, value):
            self.statvalue = value

        def DecreaseStat(self, value):
            if self.statvalue > value:
                self.statvalue -= value
            else:
                self.statvalue = 0

        def IncreaseStat(self, value):
            self.statvalue += value

    class ForceClass(StatClass):
        stattype = "Force"

    class DexterityClass(StatClass):
        stattype = "Dexterity"

    class CharismaClass(StatClass):
        stattype = "Charisma"

    class IntellectClass(StatClass):
        stattype = "Charisma"


    class CreatureClass():

        def __init__(self, **kwargs):
            self.hp = kwargs['hp']
            self.magic = kwargs['magic']
            self.material = kwargs['material']
            self.descr = kwargs['descr']
            self.name = kwargs['name']
            self.force = ForceClass(kwargs['force'])
            self.dexterity = DexterityClass(kwargs['dexterity'])
            self.charisma = CharismaClass(kwargs['charisma'])
            self.intellect = IntellectClass(kwargs['intellect'])
            self.abils = kwargs['abils']
            self.weight = kwargs['weight']
            self.size = kwargs['size']
            self.hands = kwargs['hands']
            self.legs = kwargs['legs']
            self.heads = kwargs['heads']
            self.tails = kwargs['tails']
            self.nat_armor = kwargs['nat_armor']
            self.speed = kwargs['speed']
            self.age = kwargs['age']
            self.alignment = kwargs['alignment']
            self.cheerfulness = kwargs['cheerfulness']
            self.satiety = kwargs['satiety'],
            self.alias = kwargs['alias']
            self.pic = kwargs['pic']

        def GetDamage (self, damage):
            if damage > self.nat_armor:
                self.hp -= damage

        def GetRest (self, comfort, time):
            if comfort == "bad":
                self.cheerfulness += time*8
            elif comfort == "middle":
                self.cheerfulness += time * 10
            else:
                self.cheerfulness += time * 12

            if self.cheerfulness > 100:
                self.cheerfulness = 100

        def GetFood (self, food_finess):
            if food_finess == "bad":
                self.satiety += 50
            elif food_finess == "middle":
                self.satiety += 70
            else:
                self.satiety += 100

            if self.satiety > 120:
                self.satiety = 120

        def SpendFood (self, spend):
            self.satiety -= spend
            if self.satiety < 0:
                self.satiety = 0

        def DoWork (self, work_type, time):
                _energy_estimate = self.cheerfulness - time * work_energy_cost[work_type]
                if _energy_estimate < 0:
                    return 1
                else:
                    self.cheerfulness -= time * work_energy_cost[work_type]
                    return 0

    class CharClass(CreatureClass):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.inventory = InvetoryClass(kwargs['inventory'])
            self.hat = kwargs['hat']
            self.clothes = kwargs['clothes']
            self.armor = kwargs['armor']
            self.left_hand_item = kwargs['left_hand_item']
            self.right_hand_item = kwargs['right_hand_item']
            self.religion = kwargs['religion']
            self.questlist = kwargs['questlist']
            self.textcolor =  kwargs['textcolor']
            self.charobject = kwargs['charobject']
            self.latch = False

        def GetDamage (self, damage):
            if damage > self.nat_armor + self.armor.value:
                self.hp -= damage - self.armor.value

#     class ProtagonistClass(CharClass):
#
#         def __init__(self, **kwargs):
#             super().__init__(**kwargs)

    class DoorObjectClass():
        def __init__(self, **kwargs):
            self.way_to = kwargs['way_to']
            self.closed = kwargs['closed']
            self.locked = kwargs['locked']
            self.lock_difficulty = kwargs['lock_difficulty']
            self.strength = kwargs['strength']
            self.descr = kwargs['descr']
            self.pic = kwargs['pic']

    def ShowLocationPic (location):
        renpy.scene()
        _text_buffer = location.pic + "_" + location.pic +  "_bg"
        renpy.show(_text_buffer)
        if location.doors != []:
            for i in range(len(location.doors)):
                _text_buffer = location.pic + "_" + location.doors[i].pic + "_idle"
                renpy.show(_text_buffer, zorder = 2)

        if location.npcs != []:
            for i in range(len(location.npcs)):
                _text_buffer = location.npcs[i].pic + "_" + location.npcs[i].pic + "_idle"
                renpy.show(_text_buffer, zorder = 2)

        if location.objects != []:
            for i in range(len(location.objects)):
                _text_buffer = location.pic + "_" + location.objects[i].pic + "_idle"
                renpy.show(_text_buffer, zorder = 4)

        return 0

label time_forward_h(delay):

    $ TimeCounter += delay
    if delay > 24:
        $ renpy.display_notify("Error!To much time hop in hours!")

    if TimeCounter > 24:
        $ TimeCounter -= 24
        $ DayCounter += 1
    return

label night_patrol_check:

    if TimeCounter < 6:
        jump night_patrol_catch
    else:
        return

label night_patrol_catch:

    scene monastry_yard_night_catched

    $ renpy.pause(.5)

    show quard_night_catched

    ngrd "Ты чего тут бродишь?! А ну марш в казарму, щенок!"

    call set_time_h(8) from _call_set_time_h

    jump barracs_loc

label set_time_h (time):

    $ TimeCounter = time

    return

label interloc_time_advance(NextLocation):

    call time_forward_h(1) from _call_time_forward_h

    call night_patrol_check from _call_night_patrol_check

    $ renpy.jump(NextLocation)

screen monastry_map:

    add "map_ground.jpg"

    $ TimeCounter12 = TimeCounter

    if TimeCounter >= 12:
        $ TimeCounter12 = TimeCounter - 12
    if TimeCounter12 == 12:
        $ TimeCounter12 = 0


    imagemap:
        ground "images/map_ground.jpg"
        hover "images/map_hover.jpg"
        hotspot (594,220,162,53) action Call ("interloc_time_advance", "barracs_loc") # Спальни
        hotspot (323,326,116,51) action Call ("interloc_time_advance", "classes_loc") # Классы
        hotspot (352,703,102,52) action Call ("interloc_time_advance", "kitchen_loc") # Кухня
        hotspot (723,646,114,42) action Call ("interloc_time_advance", "library_loc") # Библиотека
        hotspot (838,659,161,47) action Call ("interloc_time_advance", "chapel_loc") # Часовня
        hotspot (323,914,302,51) action Call ("interloc_time_advance", "main_gates_loc") # Подсобное хозяйство
        hotspot (1263,768,154,51) action Call ("interloc_time_advance", "hopital_loc") # Больница
        hotspot (1491,105,104,50) action Call ("interloc_time_advance", "main_gates_loc") # Мельница
        hotspot (552,757,115,52):
            action [SetVariable("location_object", StorageLocation), Call("location_abstract")] # Склад
        hotspot(1028,113,105,54):
            action [SetVariable("location_object", TempleCorridorLocation), Call("location_abstract")]  # Храм
        # hotspot (353,140,157,56) action Jump ("start") # Гостевой дом
        # hotspot (685,76,270,52) action Jump ("start") # Дом преподавателей
        # hotspot (394,526,139,53) action Jump ("start") # Трапезная

        # hotspot (1028,113,105,54) action Jump ("start") # Храм
        # hotspot (1067,209,124,56) action Jump ("start") # Конюшни
        # hotspot (1212,201,159,52) action Jump ("start") # Мемориал
        # hotspot (1357,337,235,55) action Jump ("diary_main_loc") # Дом ректора


    add "clock_" + str(TimeCounter12) + ".png" xzoom 0.25 yzoom 0.25 xpos 1700

    imagebutton:
            auto "diary_%s.png"
            focus_mask True
            action Jump ("diary_main_loc")



screen hud_screen:
    zorder 100
    frame:
        background None
        right_padding 8
        top_padding 8
        xpos 1.0
        xanchor 1.0
        vbox:
            hbox:
                imagebutton:
                    xoffset 7
                    yoffset -7
                    idle "icons/map_icon2_idle.png"
                    hover "icons/map_icon2_hover.png"
                    action [
                        Return(["monastry_map_loc"])
                    ]

label book_pre_reading_loc(book_name, callback_loc):

    $ BookNameLocal = book_name # store context
    $ CallBackLocal = callback_loc

    call book_reading_loc(BookNameLocal, CallBackLocal) from _call_book_reading_loc

label book_reading_loc(book_name, callback_loc):

    call screen book_reading(book_name, callback_loc, LocalBookPagePointer)

    screen book_reading(book_name, callback_loc, cur_page):
        modal True
        add (book_name + str(cur_page) + ".png")
        imagebutton:
            auto "books/exit_%s.png"
            focus_mask True
            action Jump ("page_close")
        if LocalBookPagePointer > 1:
            imagebutton:
                auto "books/left_arrow_%s.png"
                focus_mask True
                action Jump ("page_left")
        if LocalBookPagePointer < GetBookLen(book_name):
            imagebutton:
                auto "books/right_arrow_%s.png"
                focus_mask True
                action Jump ("page_right")

label page_left:
    play sound "audio/page_flip.wav" volume 1.0

    $ LocalBookPagePointer -= 1

    call book_reading_loc(BookNameLocal, CallBackLocal) from _call_book_reading_loc_1

label page_right:
    play sound "audio/page_flip.wav" volume 1.0

    $ LocalBookPagePointer += 1

    call book_reading_loc(BookNameLocal, CallBackLocal) from _call_book_reading_loc_2

label page_close:

    play sound "audio/book_close.wav" volume 1.0

    $ LocalBookPagePointer = 1
    python:
        renpy.jump(CallBackLocal)

style diary_button_text:
    color "#000000"
    hover_color "#FF0000"
    size 40
    font "AmadeusAP.ttf"

style diary_detailed_text:
    size 40
    font "AmadeusAP.ttf"

label quest_complete_label(closed_quest_name):

    $ QuestListPassed.append(closed_quest_name)
    $ QuestListActive.remove(closed_quest_name)

label diary_main_loc:

    call screen quest_list_scene

    screen quest_list_scene:
        modal True
        add ("diary_blank.png")
        vbox:
            xalign .2
            yalign .1
            for x in QuestListActive:
                textbutton x text_style "diary_button_text":
                    action Call ("quest_descr_label", x)
        imagebutton:
            auto "books/exit_%s.png"
            focus_mask True
            action Jump ("monastry_map_loc")
        imagebutton:
            auto "books/bag_%s.png"
            focus_mask True
            action Jump ("pic_inventory_label")

label inventory_show:

    call screen items_list_scene

    screen items_list_scene:
        modal True
        add ("diary_blank.png")
        vbox:
            xalign .2
            yalign .1
            for x in InventoryList:
                text x style "diary_detailed_text" color "000000"
        imagebutton:
            auto "books/exit_%s.png"
            focus_mask True
            action Jump ("monastry_map_loc")
        imagebutton:
            auto "books/left_arrow_%s.png"
            focus_mask True
            action Jump ("diary_main_loc")


label quest_descr_label(QuestName):


    call screen quest_descr_screen

    screen quest_descr_screen:
        modal True
        add ("diary_blank.png")
        vbox:
            text GetQuestDescription(QuestName) color "000000" area (265, 122, 625, 752) italic True style "diary_detailed_text"
        imagebutton:
            auto "books/left_arrow_%s.png"
            focus_mask True
            action Jump ("diary_main_loc")
        imagebutton:
            auto "books/exit_%s.png"
            focus_mask True
            action Jump ("monastry_map_loc")

label pic_inventory_label:
    scene paper_bg

    call screen show_inventory_icons

    screen show_inventory_icons:

        vbox:
            xanchor -1300
            yanchor -250

            add 'icons/gold.png' zoom .5
            text "     " + str(RandalGoldAmnt) + " золотых" color "#000000" font "AmadeusAP.ttf" size 60

        vbox:
            xanchor -200
            yanchor -50

            for y in range(InventoryHSizeItems):
                hbox:
                    for x in range(InventoryHSizeItems):
                        add 'icons/item_frame.png'
        vbox:
            xanchor -200
            yanchor -50
            $ VBuf = GetInvHLineNum(InventoryItemDict)
            $ ItemsListBuf = InventoryItemDict.keys()
            for y in range(VBuf):
                hbox:
                    if y < VBuf - 1:
                        for x in range(InventoryHSizeItems):
                            imagebutton:
                                auto 'icons/' + ItemsListBuf[y*InventoryHSizeItems + x] + '_icon_%s.png'
                                focus_mask True
                                action Call ("inventory_item_deteiled", ItemsListBuf[y*InventoryHSizeItems + x])
                    elif y == VBuf - 1:
                        for x in range(len(ItemsListBuf) % InventoryHSizeItems):
                            imagebutton:
                                auto 'icons/' + ItemsListBuf[y*InventoryHSizeItems + x] + '_icon_%s.png'
                                focus_mask True
                                action Call ("inventory_item_deteiled", ItemsListBuf[y*InventoryHSizeItems + x])

        imagebutton:
            auto "books/exit_%s.png"
            focus_mask True
            action Jump ("monastry_map_loc")


label inventory_item_deteiled(ItemKey):

    scene paper_bg

    call screen show_inventory_detailed_stats

    screen show_inventory_detailed_stats:

        add 'items/' + ItemKey + '.png' xpos 1000 zoom 0.75

        # text InventoryItemDict.get(ItemKey) color "000000" area (265, 122, 625, 752) italic True style "diary_detailed_text"
        text GetItemDescrText(ItemKey) color "000000" area (265, 122, 625, 752) italic True style "diary_detailed_text"

        imagebutton:
            auto "books/exit_%s.png"
            focus_mask True
            action Jump ("monastry_map_loc")

        imagebutton:
            auto "books/left_arrow_%s.png"
            focus_mask True
            action Jump ("pic_inventory_label")

label inventory_item_add(AddItemKey):

    $ InventoryItemDict [str(AddItemKey)] = GetItemDescrText(AddItemKey)

    return

label inventory_item_del(RmItemKey):

    $ del InventoryItemDict[str(RmItemKey)]

    return

label location_abstract:

    # Temp hack
    python:
        if location_object == StubLocation:
            renpy.call("monastry_map_loc")

    $ ShowLocationPic(location_object)

    if location_object.visited  == False:
        $ location_object.visited = True
        $ loc_visit_speech = location_object.loc_description
        r "[location_object.loc_description]"

    call screen show_location_items

    screen show_location_items:
        if location_object.npcs != []:
            for i in range(len(location_object.npcs)):
                imagebutton auto (location_object.npcs[i].pic + "/" + location_object.npcs[i].pic + "_%s.png") focus_mask True action [SetVariable("person_to_interact", location_object.npcs[i]), Jump ("dialoge_abstract")]

        if location_object.objects != []:
            for i in range(len(location_object.objects)):
                $ object_to_interact = location_object.objects[i]
                imagebutton auto (location_object.pic + "/" + location_object.objects[i].pic + "_%s.png") focus_mask True action [SetVariable("object_to_interact", location_object.objects[i]), Jump ("object_interact_abstract")]

        if location_object.doors != []:
            for i in range(len(location_object.doors)):
                $ doorway = location_object.doors[i].way_to
                imagebutton auto (location_object.pic + "/" + location_object.doors[i].pic + "_%s.png") focus_mask True action [SetVariable("location_object", LocDict[location_object.doors[i].way_to]), Call("location_abstract")]

        imagebutton auto "ui/map_button_%s.png" focus_mask True action Jump ("monastry_map_loc")

    return

label object_interact_abstract:

    $ itempic = object_to_interact.pic
    $ renpy.show(itempic, zorder = 6)

    python:
        if object_to_interact.latch == False:
            object_to_interact.latch = True
            "[object_to_interact.name]"

    menu:
        "Рассмотреть":
            "[object_to_interact.name]"
            jump object_interact_abstract
        "Украсть":
            $ randal.inventory.AddItem(object_to_interact)
            $ location_object.RemoveObject(object_to_interact)
            jump location_abstract
        "Сломать":
            r "Это как?"
            jump object_interact_abstract
        "Ну и хрен с ним":
            jump location_abstract
label dialoge_abstract():

    python:
        ShowLocationPic(location_object)
        renpy.hide (person_to_interact.pic + "_" +  person_to_interact.pic + "_idle")
        renpy.show (person_to_interact.pic + "_" +  person_to_interact.pic + "_talk", zorder = 6)

    # r "Добрый день!"
    python:
        if person_to_interact.latch == False:
            person_to_interact.latch = True
            renpy.say(person_to_interact.charobject, "Здравствуй, Рэндал!")

    menu:
        "Обокрасть":
            r "Не хочу красть у [person_to_interact.name]"
            jump dialoge_abstract
        "Напасть":
            r "Да меня [person_to_interact.name] отпиздит!"
            jump dialoge_abstract
        "Оценить отношение":
            $ renpy.say(person_to_interact.charobject, "Ты даже не даже!")
            jump location_abstract
        "Прокрастья мимо":
            $ renpy.say(person_to_interact.charobject, "Куда это ты собрался?")
            jump location_abstract
        "Ну пошел я":
            jump location_abstract
    return