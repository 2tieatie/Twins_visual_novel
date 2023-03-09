import pygame
from settings import *
import sys
import textwrap
from pygame import mixer
pygame.init()
mixer.init()
info = pygame.display.Info()
h, w = info.current_h, info.current_w
sc = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
menu_image = pygame.image.load(MAIN_MENU_FILE)
text_image = pygame.image.load('test.png')
main_char = pygame.image.load(MAIN_CHAR_FILE)
pause_image = pygame.image.load(PAUSE_FILE)
vlas = pygame.image.load(VLAS_FILE)
small_erika = pygame.image.load(SMALL_ERIKA)
erika = pygame.image.load(ERIKA_FILE)
police = pygame.image.load(POLICE_FILE)
psyco = pygame.image.load(PSYCHO_FILE)
piere = pygame.image.load(PIERE_FILE)
dead_boy = pygame.image.load(DEAD_BOT_FILE)
boy = pygame.image.load(BOY_FILE)
dead_teen_erika = pygame.image.load(DEAD_TEEN_ERIKA_FILE)
dead_kid_erika = pygame.image.load(DEAD_KID_ERIKA_FILE)
marta = pygame.image.load(MARTA_FILE)
font_s_menu = int(h / 25.7)
STORY_FONT_SIZE = int(h / 25.7)
menu_image = pygame.transform.scale(menu_image, (w, h))
pause_image = pygame.transform.scale(pause_image, (w, h))
main_char = pygame.transform.scale(main_char, (w // 4.8, h // 3.08))
vlas = pygame.transform.scale(vlas, (w // 4.8, h // 3.08))
erika = pygame.transform.scale(erika, (w // 4.8, h // 3.08))
small_erika = pygame.transform.scale(small_erika, (w // 4.8, h // 3.08))
piere = pygame.transform.scale(piere, (w // 4.8, h // 3.08))
police = pygame.transform.scale(police, (w // 4.8, h // 3.08))
psyco = pygame.transform.scale(psyco, (w // 4.8, h // 3.08))
dead_boy = pygame.transform.scale(dead_boy, (w // 4.8, h // 3.08))
boy = pygame.transform.scale(boy, (w // 4.8, h // 3.08))
marta = pygame.transform.scale(marta, (w // 4.8, h // 3.08))
dead_teen_erika = pygame.transform.scale(dead_teen_erika, (w // 4.8, h // 3.08))
dead_kid_erika = pygame.transform.scale(dead_kid_erika, (w // 4.8, h // 3.08))
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.QUIT])
text_images_ = []
sc_rect = sc.get_rect()
font = pygame.font.SysFont(FONT, font_s_menu)
story_font = pygame.font.SysFont(FONT, STORY_FONT_SIZE)
save_pause_button = font.render(SAVE_TEXT, True, WHITE, None)
main_menu_button = font.render(MAIN_MENU, True, WHITE, None)
exit_text = font.render(EXIT, True, WHITE, None)
agr_text = font.render(AGR, True, WHITE, None)
dagt_text = font.render(DAGR, True, WHITE, None)
n_game_text = font.render(NEW_GAME, True, WHITE, None)
cont_text = font.render(CONTINUE, True, WHITE, None)
sett_text = font.render(SETTINGS, True, WHITE, None)
ex_menu_text = font.render(EXIT_MENU, True, WHITE, None)
final_text = []
bg_l = []
atr_l = []
wid_4 = w / 4
sc.set_alpha(None)
exit_b = False
exit_button_closing = False
main_menu = True
main_story = False
pause_ = False
show_exit_button = False
alpha = 0
set_alpa = True
alpha_s = 0
set_alpha_s = True
set_alpha_t = False
alpha_t = 0
show_atr = False
volume_change = False
sec_s = 0
sec_s_1 = 0
tabl_text = []
t_t = []
show_tabl = False
but_color = BLACK
pause_rect = pygame.Surface((w, h))
pause_rect.set_alpha(150)
pause_rect.fill((0, 0, 0))
clock = pygame.time.Clock()
exit_button_paramrters = [w / 2, h, 0, 0]
x_frame = w / 2
change_m = False
final = False
volume_c = 0

choise = {118: ['Сара:', 'Намагатися розтлумачити сон|1 1', 'Випити заспокійливе|13 0'],
          153: ['Сара:', 'Спробувати відволіктись|1 0', 'Намагатися відчути Еріку|6 1'],
          194: ['Сара: «Гаразд,..»', 'Піду прямо|1 0', 'Піду праворуч|8 0', 'Піду ліворуч|16 0'],
          222: ['Сара: «Що робити далі?»', 'Піти по дорозі праворуч|1 0', 'Піти по дорозі ліворуч|3 0', 'Чекати на автомобіль|5 0'],
          260: ['Сара:', 'Ні, ці сни щось значать|1 1', 'Сниться маячня через хвилювання|7 0'],
          358: ['Сара:', 'Розказати про сни|1 1', 'Розказати свої підозри, щодо версії поліції|13 0'],
          525: ['Cара:', 'Спробувати зрозуміти|1 1', 'Розлютитися|8 0'],
          557: ['Сара:', 'Надати сну значення|1 1', 'Промовчати про сон|8 0'],
          827: ['Сара:', 'Підбігти до сестри|2 0', 'Озирнутися уважніше|5 0'],
          861: ['Сара:', 'Сховати Еріку і побігти по підмогу|2 0', 'Тягнути її що є сили|66 0'],
          1162: ['Сара:', 'Побігти викликати поліцію|1 0', 'Йти в ліс, не гаючи часу|73 0']}
chsg = False
with open(SAVE_FILE) as s:
    saves = s.read().split()
    bg = int(saves[1])
    save = int(saves[0])
    atr = int(saves[2])
    steps = int(saves[3])
    volume = float(saves[4])
    m = int(saves[5])
with open(story_file, encoding='utf-8') as text_1:
    text = text_1.read().split('\n')

for i in range(2, 50):
    text_images_.append(pygame.transform.scale(text_image, (w / 2, STORY_FONT_SIZE * i)))

text_images_ = tuple(text_images_)
tabl = text_images_[0]

for i in BG_FILES_LIST:
    bg_l.append(pygame.transform.scale(pygame.image.load(i).convert(), (w, h)))

for i in ATR_FILES_LIST:
    atr_l.append(pygame.transform.scale(pygame.image.load(i), (h / 1.1, h / 1.1)))

atrib = atr_l[atr]
backg = bg_l[bg]
for index, i in enumerate(text):
    if i == '':
        text.pop(index)

for index, i in enumerate(text):
    t_1 = []
    for line in textwrap.wrap(i, width=TEXT_WIDTH):
        t_1.append(line)
    final_text.append(t_1)

exit_b_s = (wid_4, h / 3.2)

print('SUCCESFUL LOADING!')


def detection(x, y, size_x, size_y):
    mouse_pos = pygame.mouse.get_pos()
    m_x = mouse_pos[0]
    m_y = mouse_pos[1]
    rect_top = y
    rect_bottom = y + size_y
    rect_left = x
    rect_right = x + size_x
    if rect_bottom >= m_y >= rect_top and rect_left <= m_x <= rect_right:
        return True
    else:
        return False


def events():
    global show_exit_button, exit_button_showing, exit_b, exit_button_closing, \
        n_game_text, cont_text, sett_text, ex_menu_text, main_story, main_menu, save, bg, pause_, steps, atr, sec_s_1,\
        volume_change, volume, final
    for event in pygame.event.get():
        if event.type == pygame.QUIT and not exit_b:
            show_exit_button = True
            exit_button_showing = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_story and not exit_b and not pause_:
                if not final:
                    if not chsg:
                        save += 1
                    else:
                        for i in range(len(choise[save]) - 1):
                            if detection(wid_4 - w / 384, h / 2 + STORY_FONT_SIZE * 2 * i , x_frame + w / 192, STORY_FONT_SIZE * 2):
                                steps += int(choise[save][i + 1].split('|')[1].split(' ')[1])
                                save += int(choise[save][i + 1].split('|')[1].split(' ')[0])
                                sec_s_1 = 0

            if exit_b:
                if detection(sc_rect.centerx + exit_b_s[0] / 4.1, sc_rect.centery + exit_b_s[1] / 4.2,
                             font_s_menu * 1.2, font_s_menu * 1):
                    exit_b = False
                    exit_button_closing = True
                elif detection(sc_rect.centerx - exit_b_s[0] / 3, sc_rect.centery + exit_b_s[1] / 4.2,
                               font_s_menu * 1.7, font_s_menu * 1):
                    with open('save.txt', 'w') as s:
                        s.write(f'{save} {bg} {atr} {steps} {volume} {m}')
                    with open('save.txt', 'r') as s:
                        saves = s.read().split(' ')
                        bg_1 = int(saves[1])
                        save_1 = int(saves[0])
                        if bg_1 == bg and save_1 == save:
                            sys.exit()
            if main_menu or main_story and pause_ or volume_change:
                x = w / 12.6
                if detection(x, h / 2, font_s_menu * 4.25, font_s_menu):
                    if main_menu:
                        bg = 0
                        save = 0
                        atr = 0
                        steps = 0
                        main_story = True
                        main_menu = False
                        final = False
                    else:
                        pause_ = False
                elif detection(x, h / 1.7, font_s_menu * 6, font_s_menu):
                    if main_menu:
                        mixer.music.load(MUSIC_FILES_LIST[m - 1])
                        mixer.music.set_volume(volume)
                        mixer.music.play(loops=-1, fade_ms=1000)
                        main_story = True
                        main_menu = False
                    else:
                        with open('save.txt', 'w') as s:
                            s.write(f'{save} {bg} {atr} {steps} {volume} {m}')
                elif detection(x, h / 1.46, font_s_menu * 6.75, font_s_menu):
                    if main_menu:
                        volume_change = True
                        main_menu = False
                    else:
                        pause_ = False
                        main_story = False
                        main_menu = True
                        pass
                elif detection(x, h / 1.29, font_s_menu * 6.85, font_s_menu):
                    if not volume_change:
                        show_exit_button = True
                        exit_button_showing = True
                    else:
                        volume_change = False
                        main_menu = True
            if volume_change:
                if detection(w / 12.6, h / 3.29, w - w / 12.6 * 2, h // 10):
                    mouse_pos = pygame.mouse.get_pos()
                    m_x = mouse_pos[0]
                    volume = (m_x - w / 12.6) * 100 / (w - w / 12.6 * 2) / 100
                    mixer.music.set_volume(volume)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if main_menu and not exit_b:
                    show_exit_button = True
                    exit_button_showing = True
                elif main_story:
                    if pause_:
                        pause_ = False
                    else:
                        pause_ = True


def exit_button():
    global init, exit_button_paramrters, exit_button_showing, exit_b, exit_button_closing, agr_text, dagt_text
    ebp = exit_button_paramrters
    if exit_button_showing and not exit_b:
        if ebp[1] > sc_rect.centery - exit_b_s[1] / 2:
            fps_t = clock.get_fps() / 1
            pygame.draw.rect(sc, D_BLUE, ebp, 10, 10)
            pygame.draw.rect(sc, D_BLUE, (ebp[0] + 5, ebp[1] + 5, ebp[2] - 10, ebp[3] - 10))
            exit_button_paramrters = [ebp[0] - 0.577 * fps_t / 2,
                                      ebp[1] - fps_t,
                                      ebp[2] + 1.154 * fps_t / 2,
                                      ebp[3] + 0.77 * fps_t / 2]
        else:
            exit_button_showing = False
            exit_b = True
    elif exit_b:
        pygame.draw.rect(sc, D_BLUE, (sc_rect.centerx - exit_b_s[0] / 2,
                                      sc_rect.centery - exit_b_s[1] / 2, exit_b_s[0], exit_b_s[1]), 10, 10)
        pygame.draw.rect(sc, D_BLUE, (sc_rect.centerx - exit_b_s[0] / 2 + 5,
                                      sc_rect.centery - exit_b_s[1] / 2 + 4, exit_b_s[0] - 10, exit_b_s[1] - 10))
        sc.blit(exit_text, (sc_rect.centerx - exit_b_s[0] / 3, sc_rect.centery - exit_b_s[1] / 4.2,))
        sc.blit(agr_text, (sc_rect.centerx - exit_b_s[0] / 3, sc_rect.centery + exit_b_s[1] / 4.2,))
        sc.blit(dagt_text, (sc_rect.centerx + exit_b_s[0] / 4.1, sc_rect.centery + exit_b_s[1] / 4.2,))
        if detection(sc_rect.centerx + exit_b_s[0] / 4.1, sc_rect.centery + exit_b_s[1] / 4.2, font_s_menu * 1.2,
                     font_s_menu * 1):
            dagt_text = font.render(DAGR, True, GREEN, None)
        elif detection(sc_rect.centerx - exit_b_s[0] / 3, sc_rect.centery + exit_b_s[1] / 4.2, font_s_menu * 1.7,
                       font_s_menu * 1):
            agr_text = font.render(AGR, True, RED, None)
        else:
            agr_text = font.render(AGR, True, WHITE, None)
            dagt_text = font.render(DAGR, True, WHITE, None)
    elif exit_button_closing:
        if ebp[1] < 1080:
            fps_t = clock.get_fps() / 1
            pygame.draw.rect(sc, D_BLUE, ebp, 10, 10)
            pygame.draw.rect(sc, D_BLUE, (ebp[0] + 5, ebp[1] + 5, ebp[2] - 10, ebp[3] - 10))
            exit_button_paramrters = [ebp[0] + 0.577 * fps_t / 2,
                                      ebp[1] + fps_t,
                                      ebp[2] - 1.154 * fps_t / 2,
                                      ebp[3] - 0.77 * fps_t / 2]
        else:
            exit_button_paramrters = [w / 2, h, 0, 0]
            exit_button_closing = False
            exit_b = False


def pause():
    global save_pause_button, main_menu_button, cont_text
    sc.blit(pause_rect, (0, 0))
    x = w / 12.6
    if detection(x, h / 2, font_s_menu * 6, font_s_menu):
        cont_text = font.render(CONTINUE, True, GREEN, None)
    elif detection(x, h / 1.7, font_s_menu * 4.25, font_s_menu):
        save_pause_button = font.render(SAVE_TEXT, True, GREEN, None)
    elif detection(x, h / 1.46, font_s_menu * 6, font_s_menu):
        main_menu_button = font.render(MAIN_MENU, True, GREEN, None)
    else:
        cont_text = font.render(CONTINUE, True, WHITE, None)
        save_pause_button = font.render(SAVE_TEXT, True, WHITE, None)
        main_menu_button = font.render(MAIN_MENU, True, WHITE, None)
    sc.blit(cont_text, (x, h / 2))
    sc.blit(save_pause_button, (x, h / 1.7))
    sc.blit(main_menu_button, (x, h / 1.46))


def main_menu_func():
    global menu_image, n_game_text, cont_text, sett_text, ex_menu_text
    x = w / 12.6

    if not exit_b:
        if detection(x, h / 2, font_s_menu * 4.25, font_s_menu):
            n_game_text = font.render(NEW_GAME, True, GREEN, None)
        elif detection(x, h / 1.7, font_s_menu * 6, font_s_menu):
            cont_text = font.render(CONTINUE, True, GREEN, None)
        elif detection(x, h / 1.46, font_s_menu * 2.45, font_s_menu):
            sett_text = font.render(SETTINGS, True, GREEN, None)
        elif detection(x, h / 1.29, font_s_menu * 2.85, font_s_menu):
            ex_menu_text = font.render(EXIT_MENU, True, GREEN, None)
        else:
            n_game_text = font.render(NEW_GAME, True, WHITE, None)
            cont_text = font.render(CONTINUE, True, WHITE, None)
            sett_text = font.render(SETTINGS, True, WHITE, None)
            ex_menu_text = font.render(EXIT_MENU, True, WHITE, None)
    sc.blit(menu_image, (0, 0))
    sc.blit(n_game_text, (x, h / 2))
    sc.blit(cont_text, (x, h / 1.7))
    sc.blit(sett_text, (x, h / 1.46))
    sc.blit(ex_menu_text, (x, h / 1.29))


def settings():
    global main_menu, volume, main_menu_button
    x = w / 12.6
    a = bg_l[0].copy()
    a.set_alpha(100)
    sc.blit(a, (0, 0))
    if detection(x, h / 1.29, font_s_menu * 6.75, font_s_menu):
        main_menu_button = font.render(MAIN_MENU, True, GREEN, None)
    elif detection(w / 12.6, h / 3.29, w - w / 12.6 * 2, h // 10):
        mouse_pos = pygame.mouse.get_pos()
        m_x = mouse_pos[0]
        volume = (m_x - w / 12.6) * 100 / (w - w / 12.6 * 2) / 100
        mixer.music.set_volume(volume)
    else:
        main_menu_button = font.render(MAIN_MENU, True, WHITE, None)
    volume_text = font.render(f'Гучність: {int(volume * 100 + 0.5)}%', True, WHITE, None)
    pygame.draw.rect(sc, MILK_WHITE, (w / 12.6, h / 3.29, w - w / 12.6 * 2, h // 10), border_radius=h // 100)
    pygame.draw.rect(sc, (58, 40, 36), (w / 12.6, h / 3.29, (w - w / 12.6 * 2) * volume + 5, h // 10),
                     border_radius=h // 100)
    sc.blit(volume_text, (w / 12.6, h / 3.29 - volume_text.get_rect().height - h / 100))

    sc.blit(main_menu_button, (x, h / 1.29))


def main_story_():
    global save, bg, alpha, set_alpa, backg, atr, sec_s, show_atr, alpha_s, atrib, set_alpha_s, tabl_text, show_tabl, \
        alpha_t, set_alpha_t, tabl, t_t, steps, but_color, chsg, sec_s_1, change_m, m, final, volume_c
    text_1 = final_text[save]
    show_text = True
    char_n = ''
    sc.blit(backg, (0, 0))
    show_atr = False
    if volume > volume_c:
        volume_c += volume/100
        mixer.music.set_volume(volume_c)
    if '//фон' in text_1[0].lower():
        bg = int(text_1[0].lower().replace('//фон ', '').replace('//фон', '')) - 1
        save += 1
        set_alpa = True
        backg = bg_l[bg].copy()
        alpha = 0
    elif '//атр' in text_1[0].lower():
        atr = int(text_1[0][-1]) - 1
        atrib = atr_l[atr].copy()
        show_atr = True
        show_text = False
        sec_s = save
    elif 'табл/' in text_1[0].lower():
        tabl_text = []
        t_t = text_1
        t_t[0] = text_1[0].replace('табл/', '')
        save += 1
        sec_s = save
        show_tabl = True
        set_alpha_t = True
        tabl = text_images_[len(t_t) - 1].copy()
        for i in t_t:
            tabl_text.append(story_font.render(i, True, BLACK, None))
    elif '//skip' in text_1[0]:
        show_text = False
        save += int(text_1[0].split(' ')[1])
        if show_tabl:
            sec_s = save
        else:
            sec_s = 0
    elif '//back' in text_1[0]:
        save -= int(text_1[0].split(' ')[1])
        text_1 = final_text[save]
    elif '//финал' in text_1[0].lower():
        if steps in (0, 1):
            save += 1
        elif steps in (2, 3, 4):
            save += 140
        elif steps in (5, 6):
            save += 424
    elif '//кінець' in text_1[0]:
        final = True
        sc.blit(bg_l[0], (0, 0))
        kinec = font.render('КІНЕЦЬ', True, WHITE, None)
        sc.blit(kinec, (w / 2 - kinec.get_rect().width, h / 2 - kinec.get_rect().height))
    if '//music' in text_1[0].lower():
        save += 1
        volume_c= 0
        if 'stop' not in text_1[0].lower():
            m = int(text_1[0].split(' ')[1])
            if 'once' in text_1[0].lower():
                mixer.music.load(MUSIC_FILES_LIST[m - 1])
                mixer.music.play(loops=-1, fade_ms=1000)
            else:
                change_m = True
                if change_m:
                    mixer.music.load(MUSIC_FILES_LIST[m - 1])
                    mixer.music.play(loops=-1, fade_ms=1000)
                    change_m = False
        else:
            mixer.music.stop()

    text_1 = final_text[save]
    hei = len(text_1) - 1
    y_frame = STORY_FONT_SIZE * (2 + hei)
    if save in choise.keys():
        chsg = True
        char_n = choise[save][0]
        show_text = False
        sec_s_1 = save
        hei = len(choise[save])
        char = story_font.render(choise[sec_s_1][0], True, BLACK, None)
        y_frame = STORY_FONT_SIZE * (2 + hei - 1)
        if hei < 4:
            sc.blit(text_images_[hei], (wid_4, h / 2 - h / 21.6))
            sc.blit(text_images_[hei - 1], (wid_4, h / 2))
        else:
            sc.blit(text_images_[hei + 1], (wid_4, h / 2 - h / 21.6))
            sc.blit(text_images_[hei], (wid_4, h / 2))
        for index, i in enumerate(choise[save]):
            if index != 0:
                if detection(wid_4 - w / 384, h / 2 + STORY_FONT_SIZE * 2 * (index - 1), x_frame + w / 192, STORY_FONT_SIZE * 2):
                    text = story_font.render(i.split('|')[0], True, GREEN, None)
                    pygame.draw.rect(sc, GREEN, (wid_4 - w / 384, h / 2 + STORY_FONT_SIZE * 2 * (index - 1), x_frame + w / 192, STORY_FONT_SIZE * 2),
                                     h // 104, h // 144)
                else:
                    text = story_font.render(i.split('|')[0], True, BLACK, None)
                    pygame.draw.rect(sc, BLACK, (wid_4 - w / 384, h / 2 + STORY_FONT_SIZE * 2 * (index - 1), x_frame + w / 192,
                                     STORY_FONT_SIZE * 2),h // 104, h // 144)
                sc.blit(text, (wid_4 + w / 38.4, h / 2 + h / 45.6 + (index - 1) * STORY_FONT_SIZE * 2))
        sc.blit(char, (wid_4 + w / 38.4, h / 2 - h / 24))
        sc.blit(main_char, (w / 1.75, h / 2 - h // 3.08))
    c_b = True
    if alpha < 200 and set_alpa:
        backg.set_alpha(alpha)
        alpha += 10
    else:
        set_alpa = False
        backg = bg_l[bg]

    small_g = 0
    if show_text and '/' not in text_1[0] and '\\' not in text_1[0]:
        if chsg:
            chsg = False
        sc.blit(text_images_[hei + 1], (wid_4, h / 2 - h / 21.6))
        sc.blit(text_images_[hei], (wid_4, h / 2))
        pygame.draw.rect(sc, BLACK, (wid_4 - w / 384, h / 2, x_frame + w / 192, y_frame), h // 104, h // 144)
        for index, i in enumerate(text_1):
            if ': ' in i:
                if c_b:
                    char_n = i.split(': ')[0]
                text = story_font.render(i.split(': ')[1], True, BLACK, None)
            else:
                text = story_font.render(i, True, BLACK, None)
                if c_b:
                    char_n = '...'
            sc.blit(text, (wid_4 + w / 38.4, h / 2 + h / 45.6 + index * STORY_FONT_SIZE))
            sc.blit(text, (wid_4 + w / 38.4, h / 2 + h / 45.6 + index * STORY_FONT_SIZE))
            c_b = False

        if 'Сара' in char_n:
            sc.blit(main_char, (w / 1.75, h / 2 - h // 3.08))
        elif 'Влас' in char_n:
            sc.blit(vlas, (wid_4 - w / 384, h / 2 - vlas.get_rect().height))
        elif 'маленька дівчинка' in char_n.lower():
            sc.blit(small_erika, (wid_4 + w / 284, h / 2 - small_erika.get_rect().height))
        elif 'Еріка' in char_n and 'ниЕріка' not in char_n and 'смЕріка' not in char_n and 'маленька еріка' not in char_n.lower() :
            sc.blit(erika, (wid_4 + w / 284, h / 2 - erika.get_rect().height))
        elif 'Поліцейський' in char_n:
            sc.blit(police, (wid_4 + w / 284, h / 2 - police.get_rect().height))
        elif 'Психолог' in char_n:
            sc.blit(psyco, (wid_4 + w / 284, h / 2 - psyco.get_rect().height))
        elif 'П\'єр Шиліне' in char_n:
            sc.blit(piere, (wid_4 + w / 284, h / 2 - piere.get_rect().height))
        elif 'Марта Шиліне' in char_n:
            sc.blit(marta, (wid_4 + w / 284, h / 2 - marta.get_rect().height))
        elif 'Маленька Еріка' in char_n:
            sc.blit(small_erika, (wid_4 + w / 284, h / 2 - small_erika.get_rect().height))
        elif 'Хлопець' in char_n:
            sc.blit(boy, (wid_4 + w / 284, h / 2 - boy.get_rect().height))
        elif 'Мертвий хлопець' in char_n:
            sc.blit(dead_boy, (wid_4 + w / 284, h / 2 - dead_boy.get_rect().height))
        if 'ниЕріка' in char_n:
            sc.blit(dead_teen_erika, (wid_4 + w / 284, h / 2 - dead_teen_erika.get_rect().height))
            char_n = 'Еріка'
        elif 'смЕріка' in char_n:
            sc.blit(dead_kid_erika, (wid_4 + w / 284, h / 2 - dead_kid_erika.get_rect().height))
            char_n = 'Маленька Еріка'
            small_g = 1
        if 'маленька дівчинка' in char_n.lower() or 'маленька еріка' in char_n.lower():
            small_g = 1
        char = story_font.render(char_n, True, BLACK, None)
        sc.blit(char, (wid_4 + (w / 384 + x_frame + w / 192) / 2 - char.get_rect().width / 2 + small_g *
                       char.get_rect().width / 2, h / 2 - h / 24))
    if sec_s == save:
        if show_atr:
            if alpha_s < 255 and set_alpha_s:
                atrib.set_alpha(alpha_s)
                alpha_s += 10
            else:
                set_alpha_s = False
                atrib.set_alpha(255)
            sc.blit(atrib, (sc.get_rect().centerx - atrib.get_rect().width / 2,
                            sc.get_rect().centery - atrib.get_rect().height / 2))
        elif show_tabl:
            if show_tabl:
                if alpha_t < 255 and set_alpha_t:
                    tabl.set_alpha(alpha_t)
                    for i in tabl_text:
                        i.set_alpha(alpha_t)
                    alpha_t += 10
                else:
                    set_alpha_t = False
                    tabl.set_alpha(255)
                    for i in tabl_text:
                        i.set_alpha(255)
            sc.blit(tabl, (sc.get_rect().centerx - tabl.get_rect().width / 2,
                           tabl.get_rect().height))
            for index, i in enumerate(tabl_text):
                sc.blit(i, (sc.get_rect().centerx - i.get_rect().width / 2,
                                    tabl.get_rect().height + h / 45.6 + index * STORY_FONT_SIZE))
    else:

        show_atr = False
        show_tabl = False
        sec_s = 0
        alpha_s = 0
        alpha_t = 0


def main():
    while True:
        events()
        if main_menu:
            main_menu_func()
        elif main_story:
            main_story_()
        if volume_change:
            settings()
        if pause_:
            pause()
        if show_exit_button:
            exit_button()
        pygame.display.set_caption('Twins')
        pygame.display.set_icon(erika)
        clock.tick(60)
        pygame.display.flip()


if __name__ == "__main__":
    main()
