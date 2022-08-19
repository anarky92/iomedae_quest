# Tech stuff

#define config.automatic_images = [ '\\', ':', '_', '-', '/' ]
define config.automatic_images = [ '/' ]
define config.automatic_images_strip = [ "images" ]

# Определение персонажей игры:

define r = Character("Рэндал", color="#c8ffc8")
define e = Character('Амариэ', color="#c800c8")
define l = Character('Мастер Сеймур', color="#0088c8")
define i = Character('Иган', color="#AA00FF")
define sbs = Character('Себастьян', color="#33DD00")
define ber = Character('Капитан Бер', color="#cfd483")
define heal = Character('Мастер медицины', color="#c3f243")
define ulm = Character('Ульм', color="#d3be53")
define ngrd = Character('Ночной стражник', color="#530bd3")
define cook = Character('Повар', color="#e95502")
#define castellan = Character(castellannpc.name, color="#c80f08")
define DEBUG = True

# Настройки по умолчанию

default ClassesFirstVisit = 0
default BarracsFirstVisit = 0
default LibraryFirstVisit = 0
default ChapelFirstVisit = 0
default KitchenFirstVisit = 0
default IomedaeStatueInfoFirstVisit = 0
default IomedaeOldFirstVisit = 0
default LocalBookPagePointer = 1
default BookNameLocal = ""
default CallBackLocal = ""
default MainGatesAccessDenied = True
default DayCounter = 1
default TimeCounter = 8 # Game starts at 8 am
# Skills

default RadalStr = 10
default RadalDex = 10
default RadalWiz = 10
default RadalInt = 10
default RadalStm = 10

default RandalDevilLangKnow = 0
default RandalReligKnow = 0
default RandalPlanKnow = 0
default RandalHistoryKnow = 0

default RandalGood = 50 # Neutral
default RandalLawful = 85 # Lawful


default RandalGoldAmnt = 10
default RandalStatus = "Испытательный срок"

default QuestListActive = ["Сдать зачет по дьявольскому", "Принести кастеляну масло"]
default QuestListPassed = []
                           
# UI settings
default InventoryHSizeItems = 8


# Игра начинается здесь:
                  
label start:

    python:

        location_object = None

        object_to_interact = None

        InventoryItemDict = {   'alch_fire' : AlchFireItemDescrText,
                                'clothes_ofic' : ClothesOficItemDescrText,
                                'dagger' : DaggerItemDescrText,
                                'flask' : FlaskItemDescrText,
                                'harrow_deck' : HarrowDeckDescrText,
                                'heal' : HealItemDescrText,
                                'key_randal' : KeyRandalItemDescrText,
                                'lamp' : LampItemDescrText,
                                'monk_robe' : MonkRobeItemDescrText,
                                'pouch' : PouchItemDescrText,
                                'rum_bottle' : RumBottleItemDescrText,
                                'water' : WaterItemDescrText}


        # Something strange here
        temDict = {   'alch_fire' : "blabla",
                           'clothes_ofic' : "blabla",
                           'dagger' : "blabla",
                           'flask' : "blabla",
                           'harrow_deck' : "blabla",
                           'heal' : "blabla",
                           'key_randal' : "blabla",
                           'lamp' : "blabla",
                           'monk_robe' : "blabla",
                           'pouch' : "blabla",
                           'rum_bottle' : "blabla",
                           'water' : "blabla"}

        castallanmonkeycreature = CreatureClass(
            hp = 100,
            magic = False,
            material = True,
            descr = "Кастелян монастыря  Йорген. Скупой, злопамятный, внимательный.",
            name = "Йорген",
            force = 10,
            dexterity = 15,
            charisma = 6,
            intellect = 8,
            abils = ["Ordinary weapon", "Heavy weapon"],
            weight = 80,
            size = "middle",
            hands = 2,
            legs = 2,
            heads = 1,
            tails = 0,
            nat_armor = 5,
            speed = 20,
            age = 45,
            alignment = [85, -10],
            cheerfulness = 100,
            satiety = 100,
            alias = None,
            pic = None
        )


        randomforce = ForceClass(1)

        castellannpc = CharClass(
            hp = 100,
            magic = False,
            material = True,
            descr = "Кастелян монастыря  Йорген. Скупой, злопамятный, внимательный.",
            name = "Йорген",
            force = 10,
            dexterity = 15,
            charisma = 6,
            intellect = 8,
            abils = ["Ordinary weapon", "Heavy weapon"],
            weight = 80,
            size = "middle",
            hands = 2,
            legs = 2,
            heads = 1,
            tails = 0,
            nat_armor = 5,
            speed = 20,
            age = 45,
            alignment = [85, -10],
            cheerfulness = 100,
            satiety = 100,
            inventory = [],
            hat = None,
            clothes = None,
            armor = None,
            left_hand_item = None,
            right_hand_item = None,
            religion = "Iomedae",
            alias = None,
            pic = "castellan"
        )

        randal = CharClass(
            hp = 100,
            magic = False,
            material = True,
            descr = "Главный герой собственно. Хотя как вы видите эту надпись я хз.",
            name = "Рэндал Мэй",
            force = 9,
            dexterity = 11,
            charisma = 16,
            intellect = 16,
            abils = ["Ordinary weapon"],
            weight = 70,
            size = "middle",
            hands = 2,
            legs = 2,
            heads = 1,
            tails = 0,
            nat_armor = 4,
            speed = 20,
            age = 25,
            alignment = [0, -26],
            cheerfulness = 100,
            satiety = 100,
            inventory = [],
            hat = None,
            clothes = None,
            armor = None,
            left_hand_item = None,
            right_hand_item = None,
            religion = None,
            alias = None,
            pic = None
        )


        GoldenCoin = CoinClass(
            hp = 10,
            cost = 100,
            magic = False,
            material = "gold",
            owner = None,
            descr = items_descr_dict["Golden coin"],
            name = "Golden coin",
            effect = 25,
            effect_type = "Phys damage",
            stat_req = [15, 6, 0, 0],
            abil_req = ["Ordinary weapon", "Heavy weapon"],
            solidity = 10,
            fragile = False,
            weight = 7,
            hands_req = 2,
            icon = "golden_coin_",
            pic = "golden_coin"
        )

        CastellanGoldenBunch = ItemBunchClass(GoldenCoin, 100, "castellan_coins")

        StorageLocation = LocationClass(
            name = "storage",
            animals = [],
            npcs = [castellannpc],
            doors = ["storage_exit"],
            objects = [CastellanGoldenBunch],
            loc_description = "Склад! Надо будет найти способ наведаться сюда без свидетелей..."
        )

    if DEBUG==True:
        call monastry_map_loc
        #call pic_inventory_label
        #call diary_main_loc from _call_diary_main_loc
        #call diary_main_loc from _call_diary_main_loc

    show castle_far_away

    "Добро пожаловать в монастырь Иомедэй"
    
    show castle_far_away
    
    call screen hud_screen

label monastry_map_loc:
    
    call screen monastry_map

label classes_loc:
        
        scene classes with dissolve
        if ClassesFirstVisit == 0:
            "Приятная тиниша и прохлада класса накрыли Рэндала"
            $ ClassesFirstVisit = 1
        
        call screen monk_talk

        screen monk_talk():
            zorder 10
            add "classes"
            modal True
            
            imagebutton auto "classes_%s.png" focus_mask True action Jump ("talk_to_monk")            
            imagebutton auto "classes_door_%s.png" focus_mask True action Jump ("monastry_map_loc")
            imagebutton auto "classes/table_%s.png" focus_mask True action Jump ("classes_study_loc")
            imagebutton auto "classes/hexenhammer_%s.png" focus_mask True action Call ("book_pre_reading_loc","classes/hexenhammer_","classes_loc")
            
        return
        
label talk_to_monk:
    
    scene monk0 with dissolve
    
    "Добрый день, брат Мэй!"
    
    menu:
        "Вы готовы к сдаче зачета?"
        
        "Да" if RandalDevilLangKnow >= 10:
            call quest_complete_label("Сдать зачет по дьявольскому") from _call_quest_complete_label
            call time_forward_h(1) from _call_time_forward_h_1
            jump monastry_map_loc
            
        "Нет":
            jump classes_loc
    
    return
            
        
label barracs_loc:
    
    scene barracs_bg with dissolve
    
    if BarracsFirstVisit == 0:
        r "Казарма. Как же тут воняет носками..."
        $ BarracsFirstVisit = 1

    call screen barracs_nav
    
    screen barracs_nav():
        zorder 11
        add "barracs_bg"
        modal True
        
        imagebutton auto "barracs_bg_exit_%s.png" focus_mask True action Jump ("monastry_map_loc")
        
        imagebutton auto "barracs_bg_elv_%s.png" focus_mask True action Jump ("elv_talk_loc")
        
        imagebutton auto "barracs/barracs_book_%s.png" focus_mask True action Call ("book_pre_reading_loc","books/barracs_iomedae_","barracs_loc")
        imagebutton auto "barracs/randal_bed_%s.png" focus_mask True action Jump ("barracs_sleep_loc")
        
    return

label elv_talk_loc:

    scene barracs_bg_empty
    
    show elf_inq
    
    e "Привет, Рэнадал! Чего не на занятиях?"
    
    menu:
    
        "Не твое дело":
            e "Ну и хуй ты Рэндал"
            jump barracs_loc
            
        "Да у меня тут одна мысль появилась.... *Хитрая ухмылка*":
            e "Ну давай рассказывай"
            r "Блаблабла"
            jump monastry_map_loc
            
    return
    
label library_loc:

    scene library_choice with dissolve

    if LibraryFirstVisit == 0:
        r "Храм знаний ёпта"
        $ LibraryFirstVisit = 1
    
    call screen library_nav
    
    screen library_nav():
        zorder 11
        add "library_choice"
        modal True
        
        imagebutton auto "library/librarian_%s.png" focus_mask True action Jump ("librarian_talk")
        imagebutton auto "library/boy_%s.png" focus_mask True action Jump ("boy_talk")
        imagebutton auto "library/away_%s.png" focus_mask True action Jump ("monastry_map_loc")
        imagebutton auto "library/restricted_%s.png" focus_mask True action Jump ("librarian_talk_restricted")
    
    
    return    
    
label librarian_talk:

    scene library_bg_boy
    
    show librarian_speech
    
    l "Зачем пришел? Необходимую литературу тебе уже выдали"
    
    menu:
    
        "*Очи в пол* Господин Сеймур, я бы хотел попросить вашего разрешения на изучение монографии о блаблабла":
            l "*Ворчливо* Черт с тобой, учись. Но только попробуй навести мне тут бардак!"
            hide librarian_speech
            jump library_loc
        "*Дерзко* Я теперь брат монастыря и имею право на доступ к учебным пособиям!":
            l "Вот и отправляйся к Норрису. Передай что тебе очень нужны учебные пособия!"
            hide librarian_speech
            jump monastry_map_loc
            
    return

label librarian_talk_restricted:

    scene library_bg_boy
    
    show librarian_speech
    
    l "Мэй! Совсем страх потерял?!"
    
    r "Извините мастер Сеймур, больше не повторится"
    
    l "А ну брысь отсюда!"
    
    hide librarian_speech
    jump monastry_map_loc
    
    
    return

label boy_talk:

    scene library_bg_librarian
    
    show boy_speech
    
    r "Эй, Иган, погоди, дело есть"
    
    i "Чего ты сюда приперся?"
    
    menu:
    
        "Слыш, шкет, зубы жмут?":
            i "Да пошел ты. Тут не твоя банда. Мастер Сеймур тебе сейчас покажет. МАСТЕР СЕЙМУУР!"
            jump librarian_talk_restricted
        
        "Иган, ты чего сразу пузыришься? Говорю же, дело есть *подмигнуть*":
            i "*Прищурившись* Что за дело?"
            r "Заход вечером в казарму, Уолтер расскажет"
            jump library_loc
    return
            
label main_gates_loc:

    scene gates_closed_guard
   
    $ renpy.pause(1.0)
    
    scene gates_closed_no_guard
    
    show guard_halt
    
    sbs "Ты куда это собрался, оборванец?"
    
    menu:
    
        "*Спокойно* Я по поручения кастеляна на ферму":
            sbs "Ты даже не послушник. Покажи пропуск и  накладную от кастеляна"
            menu:
                "Да чтоб тебя четри драли...":
                    jump monastry_map_loc
                "Спокой развернуться и уйти":
                    jump monastry_map_loc
        
        "*Раздрежнно* Иди дальше мух считай, с уменя дела. *Грубо оттолкнуть*":
            sbs "Тревога! Капитан Бер, этот висельник пытается сбежать!"
            jump cpatain_ber_gates_talk
            
    return
    
label cpatain_ber_gates_talk:

    scene gates_closed_guard
    
    show captain_ber

    ber "*Раздраженно* Слышь ублюдок! А ну быстро марш к завхозу. Скажешь 3 наряда вне очереди."
    menu:
            "Да чтоб тебя черти драли...":
                ber "Лови, ублюдок"
                hide captain_ber
                jump beaten_loc
            "Слушаюсь, господин капитан!":
                jump monastry_map_loc
   

    return
    
label beaten_loc:   
    
    show left_fist
    
    $ renpy.pause(.5)
    
    hide left_fist
    show right_fist
    
    $ renpy.pause(.5)
    
    hide right_fist
    show left_fist
    
    $ renpy.pause(.5)
    
    hide left_fist
    scene sky
    
    "Успокоился, урод? Тащите его в лазарет, пусть заштопают"
    
    call hopital_loc(True) from _call_hopital_loc

    return
    
label hopital_loc(injured=False):
    
    if injured==True:
        scene hospital_no_healer
        show healer
        heal "Ну все, залатали мы тебя. Освобождай койку и иди в казаму отлеживаться"
        jump barracs_loc
        show healer
    else:
        scene hospital_healer
        $renpy.pause (1.0)
        scene hospital_no_healer
        show healer
        heal "Ты чего приперся? Заболел?"
        menu:
            "Меня в наряд прислали":
                heal "Иди у завхоза отрабатывай, мне тут хулиганье не нужно"
                jump monastry_map_loc
            "Да чего-то неважно себя чувствую":
                heal "Давай поссмотрим..."
                $renpy.pause (1.0)
                heal "Вали отсюда, симулянт"
                jump monastry_map_loc
            "Уже хожу":
                jump monastry_map_loc
                
    return    
        
label chapel_loc:
    
    scene chapel_bg_monk

    if ChapelFirstVisit == 0:
        r "Фига себе! Чего это тут такое?"
        $ ChapelFirstVisit = 1
        
        
    call screen chapel_nav
        
    screen chapel_nav:    
        modal True
        imagebutton auto "chapel/chapel_monk_%s.png" focus_mask True action Jump ("chapel_monk_talk")
        imagebutton auto "chapel/chapel_exit_%s.png" focus_mask True action Jump ("monastry_map_loc")
        imagebutton auto "chapel/iomedae_statue_%s.png" focus_mask True action Jump ("chapel_statue_loc")
    
    return
        
label chapel_monk_talk:
    
    scene chapel_bg_no_monk
    
    $ renpy.pause(.5)
    
    show chapel_monk
    
    if IomedaeStatueInfoFirstVisit == 0:
        $ IomedaeStatueInfoFirstVisit = 1
        r "Эй, дружище, че это у вас тут за красотка стоит?"
        ulm "Ты чего?! *Удивленно* Это же наша знаменитая статуя Иомедэй после победы над Шепчущим Тираном! Первое из известных изображений Богини!"
        r "А чего её на всех остальных изображениях мужиком с сиськами рисуют?"
        ulm "*Рассерженно* Поряви почтение!"
        r "Да ладно тебе, я же тут новенький, помоги разобраться чего у вас тут как, брат"
        ulm "*Смутившись* Да, ты прав. Это тебя же неделю назад от крестьян спасали?"
        r "*Усмехнувшись* Ага"
        ulm "*Тоже усмехнувшись* Пересуды до сих пор ходят."
        ulm "А почему это изображение Богини не стало каноничным я не знаю. Может в воспитательных целях *пожал плечами*"
        r "Ну буду считать что она такая *Подмигнув* Тебя как звать то?"
        ulm "Ульм. А ты Рэндал?"
        r "Ага *протянул руку*"
        ulm "*Ответил на рукопожатие*"
        r "Ну бывай, пойду осмотрюсь"
        ulm "Удачи"
        jump chapel_loc
    else:
        r "Как дела, Ульм"
        ulm "Да все так же. Жду не дождусь пока послушание кончится, устал уже, сил нет тут торчать водиночку"
        menu:
            "Ну бывай":
                r "Ну бывай"
                ulm "*Мрачно* Ага"
                hide chapel_monk
                jump chapel_loc
                # TODO here we need quest exist check function
            "Тебе может помочь чем?" if "Найти Ульму пожрать" not in QuestListPassed and "Найти Ульму пожрать" not in QuestListActive:
                r "Тебе может помочь чем?"
                ulm "Пожрать бы чего-нибудь"
                r "Придумаю чего-нибудь"
                ulm "Спасибо, Рэндал"
                r "Бывай"
                $ QuestListActive.append("Найти Ульму пожрать")
                hide chapel_monk
                jump chapel_loc
            "Я тут тебе пожрать притаранил" if "Найти Ульму пожрать" in QuestListActive and "kolbasa" in InventoryItemDict:
                ulm "Спасибо, Рэндал!"
                r "Да незачто, бывай"
                $ QuestListPassed.append("Найти Ульму пожрать")
                $ QuestListActive.remove("Найти Ульму пожрать")
                call inventory_item_del("kolbasa")
                jump chapel_loc
    return
                
label chapel_statue_loc:
    
    scene chapel_statue_bg

    if IomedaeOldFirstVisit == 0 and IomedaeStatueInfoFirstVisit == 1:
        $ IomedaeOldFirstVisit = 1
        r "Ничего себе богиня. Хороша. Такой можно и послужить *Усмехнулся*"
        r "*Лицо стало серьёзней* Спасибо тебе, что приютила, прекрасная воительница."
        
    menu:
    
        "Помолиться" if IomedaeStatueInfoFirstVisit == 1:
            r "Солнце, купи мне гитару"
            r "Научи курить план"
            r "Не раскачивай Землю,"
            r "Не буди по-утру"
            r "Пивом проставь, да прокляни сушняк"
            r "Вобщем, сделай так чтобы всё было ништяк"
            jump chapel_loc
        "Просто полюбоваться прелестями богини" if IomedaeStatueInfoFirstVisit == 1:   
            $ renpy.pause(5)
            jump chapel_loc
        "Полюбоваться прелестями статуи" if IomedaeStatueInfoFirstVisit == 0:   
            $ renpy.pause(5)
            jump chapel_loc
        "В следующий раз" :
            jump chapel_loc

    return
    
label kitchen_loc:

    scene kitchen_bg_cook
    
    if KitchenFirstVisit == 0:
        $ KitchenFirstVisit = 1
        r " *Принюхивается* Аж слюнки потекли..."

    call screen kitchen_nav
        
    screen kitchen_nav:    
        modal True
        imagebutton auto "kitchen/kitchen_basket_%s.png" focus_mask True action Jump ("kitchen_steal_food_loc")
        imagebutton auto "kitchen/cook_%s.png" focus_mask True action Jump ("kitchen_cook_talk_loc")
        imagebutton auto "kitchen/exit_%s.png" focus_mask True action Jump ("monastry_map_loc")
        
label kitchen_steal_food_loc:

    scene kitchen_bg_cook
    
    menu :
        "Кажется я могу незаметно свистнуть колбасу..."
        
        "Ну нафиг":
            jump kitchen_loc
            
        "Было ваше стало наше" if "kolbasa" not in InventoryItemDict:
            call inventory_item_add("kolbasa")
            jump kitchen_loc
            
label kitchen_cook_talk_loc:

    scene kitchen_bg_no_cook
    
    show cook
    
    cook "Чего надо?"
    
    menu:
    
        "Можно у вас чего-нибудь попросить поесть?":
            cook "*Раздраженно* Вали отсюда. Есть будешь со всеми. Если заслужишь"
            jump kitchen_loc
            
        "Там в часовне послушник Ульм на дежурсве с голоду пухнет. Можно для него паек получить?":
            cook "*Раздраженно* Ты кого надурить вздумал? Вали отсюда, проходимец!"
            jump kitchen_loc

label classes_study_loc:

    menu:
    
        "Ботать дьявольский" if RandalDevilLangKnow < 10:
            call time_forward_h(8) from _call_time_forward_h_2
            $ RandalDevilLangKnow += 1
            with fade
            jump classes_loc
        "Да ну его нафиг, заебался в корень":
            jump classes_loc
    
    
label barracs_sleep_loc:

    menu:
    
        "Спать до утра":
            call time_forward_h(8 + (24 - TimeCounter)) from _call_time_forward_h_3
            scene randal_sleep with fade
            $ renpy.pause(1)
            jump barracs_loc
        "Спать 1 час":
            call time_forward_h(1) from _call_time_forward_h_4
            scene randal_sleep with fade
            $ renpy.pause(1)
            jump barracs_loc
        "Спать 8 часов":
            call time_forward_h(8) from _call_time_forward_h_5
            scene randal_sleep with fade
            $ renpy.pause(1)
            jump barracs_loc