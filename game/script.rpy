﻿# Определение персонажей игры:

define r = Character('Рэндал', color="#c8ffc8")
define e = Character('Амариэ', color="#c800c8")
define l = Character('Мастер Сеймур', color="#0088c8")
define i = Character('Иган', color="#AA00FF")

# Настройки по умолчанию

default ClassesFirstVisit = 0
default BarracsFirstVisit = 0
default LibraryFirstVisit = 0
default LocalBookPagePointer = 1
default BookNameLocal = ""
default CallBackLocal = ""


# Служебные функции

init python:
    def GetBookLen (book_name):
        if book_name == "books/barracs_iomedae_":
            return 3
        else:
            return 0
        

# Игра начинается здесь:

screen monastry_map:
    imagemap:
        ground "images/map_ground.jpg"
        hover "images/map_hover.jpg"
        hotspot (353,140,157,56) action Jump ("start") # Гостевой дом
        hotspot (685,76,270,52) action Jump ("start") # Дом преподавателей
        hotspot (594,220,162,53) action Jump ("barracs_loc") # Спальни
        hotspot (323,326,116,51) action Jump ("classes_loc") # Классы
        hotspot (394,526,139,53) action Jump ("start") # Трапезная
        hotspot (352,703,102,52) action Jump ("start") # Кухня
        hotspot (552,757,115,52) action Jump ("start") # Склад
        hotspot (723,646,114,42) action Jump ("library_loc") # Библиотека
        hotspot (838,659,161,47) action Jump ("start") # Часовня
        hotspot (323,914,302,51) action Jump ("start") # Подсобное хозяйство
        hotspot (1263,768,154,51) action Jump ("start") # Больница
        hotspot (1028,113,105,54) action Jump ("start") # Храм
        hotspot (1067,209,124,56) action Jump ("start") # Конюшни
        hotspot (1212,201,159,52) action Jump ("start") # Мемориал
        hotspot (1491,105,104,50) action Jump ("start") # Мельница
        hotspot (1357,337,235,55) action Jump ("start") # Дом ректора

screen show_png(path):
    add path       
       
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

    $ BookNameLocal = book_name
    $ CallBackLocal = callback_loc
    
    call book_reading_loc(BookNameLocal, CallBackLocal)

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

    $ LocalBookPagePointer -= 1
    
    call book_reading_loc(BookNameLocal, CallBackLocal)
    
label page_right:

    $ LocalBookPagePointer += 1
    
    call book_reading_loc(BookNameLocal, CallBackLocal)
    
label page_close:

    $ LocalBookPagePointer = 1
    python:
        renpy.jump(CallBackLocal)
    
label start:

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
        
        # call screen hud_screen
        
        # show classes
        
        call screen monk_talk

        screen monk_talk():
            zorder 10
            add "classes"
            modal True
            
            imagebutton auto "classes_%s.png" focus_mask True action Jump ("talk_to_monk")
            
            imagebutton auto "classes_door_%s.png" focus_mask True action Jump ("monastry_map_loc")
            
        return
        
label talk_to_monk:
    
    scene monk0 with dissolve
    
    "Добрый день, брат Мэй!"
    
    menu:
        "Вы готовы к сдаче зачета?"
        
        "Да":
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
            
label book_show:

    return