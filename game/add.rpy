# Служебные функции

init python:
    # TO DO add descriptions from JSON & create data structures for locationinfo, questinfo etc.
    
    # InventoryItemDict = {   'alch_fire' : AlchFireItemDescrText, 
                            # 'clothes_ofic' : ClothesOficItemDescrText, 
                            # 'dagger' : DaggerItemDescrText, 
                            # 'flask' : FlaskItemDescrText, 
                            # 'harrow_deck' : HarrowDeckDescrText,
                            # 'heal' : HealItemDescrText,
                            # 'key_randal' : KeyRandalItemDescrText,
                            # 'lamp' : LampItemDescrText,
                            # 'monk_robe' : MonkRobeItemDescrText,
                            # 'pouch' : PouchItemDescrText,
                            # 'rum_bottle' : RumBottleItemDescrText,
                            # 'water' : WaterItemDescrText}
                            
                            
    # Something strange here                        
    InventoryItemDict = {   'alch_fire' : "blabla", 
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

        # hotspot (353,140,157,56) action Jump ("start") # Гостевой дом
        # hotspot (685,76,270,52) action Jump ("start") # Дом преподавателей
        # hotspot (394,526,139,53) action Jump ("start") # Трапезная
        # hotspot (552,757,115,52) action Jump ("start") # Склад
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