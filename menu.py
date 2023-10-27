import curses

def centralizar_mensagem(stdscr, mensagem):
    altura, largura = stdscr.getmaxyx() # Altura e Largura da Janela
    coluna = (largura - len(mensagem)) // 2
    return coluna

def centralizar_opcoes(stdscr, menu_opcoes):
    altura, largura = stdscr.getmaxyx()
    linha = altura // 2 - len(menu_opcoes) // 2
    coluna_inicial = largura // 2
    return linha, coluna_inicial

def main(stdscr):
    curses.curs_set(0) 
    stdscr.nodelay(1)  
    stdscr.timeout(100) 
    stdscr.keypad(1)  

    # Cores 
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  

    # Aumenta o tamanho da fonte
    curses.curs_set(0)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  
    curses.curs_set(0)
 

    # Opções do menu
    menu_opcoes = ["Novo Jogo", "Opções", "Sair do Jogo"]
    selecionado = 0

    while True:
        stdscr.clear()

        linha, coluna_inicial = centralizar_opcoes(stdscr, menu_opcoes)

        # Imprime as opções do menu com destaque nas opções selecionadas e tamanho de fonte maior
        for i, opcao in enumerate(menu_opcoes):
            if i == selecionado:
                stdscr.addstr(linha + i, coluna_inicial, opcao, curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.addstr(linha + i, coluna_inicial, opcao, curses.color_pair(2) | curses.A_BOLD)

        # Captura a tecla que o usuário está digitando
        key = stdscr.getch()

        if key == curses.KEY_UP and selecionado > 0:
            selecionado -= 1
        elif key == curses.KEY_DOWN and selecionado < len(menu_opcoes) - 1:
            selecionado += 1
        elif key == ord("\n"):
            if selecionado == 0:
                mensagem = "Jogo roda"
                coluna = centralizar_mensagem(stdscr, mensagem)
                stdscr.addstr(linha + len(menu_opcoes) + 1, coluna, mensagem)
                stdscr.refresh()
                stdscr.getch()
            elif selecionado == 1:
                mensagem = "Ideias de opção"
                coluna = centralizar_mensagem(stdscr, mensagem)
                stdscr.addstr(linha + len(menu_opcoes) + 1, coluna, mensagem)
                stdscr.refresh()
                stdscr.getch()
            elif selecionado == 2:
                break  # Sair do jogo se a opção "Sair do Jogo" for selecionada

    curses.endwin()  # Restaura a configuração do terminal

if __name__ == "__main__":
    curses.wrapper(main)
