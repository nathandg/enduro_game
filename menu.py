import curses
from utils.ascii_art import title
from utils.ascii_art import new_game_art
from utils.ascii_art import score_art
from utils.ascii_art import exit_art
from utils.ascii_art import noob_art
from utils.ascii_art import expert_art
from utils.ascii_art import car_art

from game import Game
from Player.PlayerInfo import PlayerInfo
from utils.Enums import Difficulty

import pygame
from pygame import mixer


def centralizar_ascii_art(stdscr, texto):
    _, largura = stdscr.getmaxyx()
    x = (largura - len(texto[0])) // 3
    y = 0  # Define y como 0 para posicionar o texto no topo da tela
    return x, y


def draw(stdscr, x, y, lst, background=False):
    """ Exibe texto na tela """
    for i, line in enumerate(lst):
        if 0 <= y + i < curses.LINES and 0 <= x < curses.COLS:
            if background:
                stdscr.addstr(y + i, x, line, curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.addstr(y + i, x, line)
    stdscr.refresh()


def centralizar_opcoes_vertical(stdscr, menu_opcoes):
    altura, largura = stdscr.getmaxyx()

    altura_opcoes = len(menu_opcoes) * 2
    linha_inicial = altura // 2 - altura_opcoes // 2
    coluna_inicial = largura // 3 - len(menu_opcoes[0][0]) // 2

    # Lista para armazenar as coordenadas das opções
    coordenadas_opcoes = []

    # Calcula as coordenadas para cada opção
    for i in range(len(menu_opcoes)):
        linha_opcao = linha_inicial + i * 3  # Ajuste conforme necessário
        coordenadas_opcoes.append((linha_opcao, coluna_inicial))

    return coordenadas_opcoes

def centralizar_opcoes_horizontal(stdscr, menu_opcoes):
    altura, largura = stdscr.getmaxyx()

    # Calcula a largura total das opções
    largura_total = sum(len(opcao[0]) for opcao in menu_opcoes) + len(menu_opcoes) - 1  # Considera espaços entre as opções

    # Calcula a coluna inicial para centralizar as opções
    coluna_inicial = largura // 2 - largura_total // 2

    # Lista para armazenar as coordenadas das opções
    coordenadas_opcoes = []

    # Calcula as coordenadas para cada opção
    for i, opcao in enumerate(menu_opcoes):
        coluna_opcao = coluna_inicial + sum(len(menu_opcoes[j][0]) + 1 for j in range(i))  # Adiciona 1 para o espaço entre as opções
        linha_opcao = altura // 2
        coordenadas_opcoes.append((linha_opcao, coluna_opcao))

    return coordenadas_opcoes

def main(stdscr):
    mixer.init()
    pygame.init()
    pop = pygame.mixer.Sound("sounds/pop.wav")

    # Cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Aumenta o tamanho da fonte
    curses.curs_set(0)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.curs_set(0)

    # Opções do menu
    menu_opcoes = [new_game_art, score_art, exit_art]
    titulo = [title]
    etapa = 0
    selecionado = 0
    altura, largura = stdscr.getmaxyx()

    while True:
        stdscr.clear()

        if etapa == 0:
            coordenadas_opcoes = centralizar_opcoes_vertical(stdscr, menu_opcoes)
            draw(stdscr, *centralizar_ascii_art(stdscr, title[0]), titulo[0])

            for i, (y, x) in enumerate(coordenadas_opcoes):
                opcao = menu_opcoes[i]
                if selecionado == i:
                    draw(stdscr, x + 35, y + 5, opcao, True)
                else:
                    draw(stdscr, x + 35, y + 5, opcao, False)

        elif etapa == 1:
            coordenadas_opcoes = centralizar_opcoes_horizontal(stdscr, menu_opcoes)
            draw(stdscr, *centralizar_ascii_art(stdscr, title[0]), titulo[0])
            if selecionado == 0:
                draw(stdscr, x + 44, y + 5, menu_opcoes[0])
                draw (stdscr, x + 40, y - 5, car_art[1])
            else:
                draw(stdscr, x + 42, y + 5, menu_opcoes[1])
                draw (stdscr, x + 40, y - 3, car_art[0])

        key = stdscr.getch()

        if etapa == 0:
            pop.play()
            if key == curses.KEY_UP and selecionado > 0:
                selecionado -= 1
            elif key == curses.KEY_DOWN and selecionado < len(menu_opcoes) - 1:
                selecionado += 1
            elif key == ord("\n"):
                if selecionado == 0:
                    stdscr.clear()
                    etapa = 1
                    titulo = [title]
                    menu_opcoes = [noob_art, expert_art]
                elif selecionado == 1:
                    exit()
                elif selecionado == 2:
                    exit()
        elif etapa == 1:
            pop.play()
            if key == curses.KEY_LEFT and selecionado > 0:
                selecionado -= 1
            elif key == curses.KEY_RIGHT and selecionado < len(menu_opcoes) - 1:
                selecionado += 1
            elif key == ord("\n"):
                if selecionado == 0:
                    # Lógica para escolher "Noob"
                    PlayerInfo.difficulty = Difficulty.NOOB
                    break
                elif selecionado == 1:
                    # Lógica para escolher "Expert"
                    PlayerInfo.difficulty = Difficulty.EXPERT
                    break

        stdscr.refresh()
    Game(stdscr)


if __name__ == "__main__":
    curses.wrapper(main)
