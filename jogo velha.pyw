import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.root.geometry("270x305")  # Define o tamanho fixo da janela
        self.root.resizable(False, False)  # Impede que a janela seja redimensionada
        self.player = 'X'
        self.board = [''] * 9
        self.buttons = []
        self.reset_button = None
        self.show_start_screen()  # Exibe a tela inicial

    # Função para criar a tela inicial
    def show_start_screen(self):
        self.clear_window()  # Limpa a janela
        title = tk.Label(self.root, text="Jogo da Velha", font=('Arial', 24))
        title.pack(pady=20)

        play_button = tk.Button(self.root, text="Jogar", font=('Arial', 18), width=10, command=self.start_game)
        play_button.pack(pady=10)

        exit_button = tk.Button(self.root, text="Sair", font=('Arial', 18), width=10, command=self.root.quit)
        exit_button.pack(pady=10)

        created_by = tk.Label(self.root, text="Criado por: Kleber Klaar", font=('Arial', 12))
        created_by.pack(pady=20)

    # Função para limpar a janela atual
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Função para iniciar o jogo
    def start_game(self):
        self.clear_window()  # Limpa a tela inicial
        self.create_buttons()  # Cria os botões do jogo

    # Função para criar os botões do tabuleiro
    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text='', font=('Arial', 20), width=5, height=2,
                               command=lambda i=i: self.play(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    # Função executada ao clicar em um botão do tabuleiro
    def play(self, i):
        if self.board[i] == '' and not self.check_winner():
            self.board[i] = self.player
            self.buttons[i].config(text=self.player)
            if self.check_winner():
                self.end_game(f"Jogador {self.player} venceu!")
            elif '' not in self.board:
                self.end_game("Empate!")
            else:
                self.switch_player()

    # Função para alternar o jogador
    def switch_player(self):
        self.player = 'O' if self.player == 'X' else 'X'

    # Função para verificar o vencedor
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]              # Diagonais
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                return True
        return False

    # Função chamada quando o jogo termina (vitória ou empate)
    def end_game(self, message):
        messagebox.showinfo("Fim de jogo", message)
        self.disable_buttons()
        self.create_reset_button()

    # Função para desabilitar os botões após o fim do jogo
    def disable_buttons(self):
        for button in self.buttons:
            button.config(state='disabled')

    # Função para criar o botão de reiniciar
    def create_reset_button(self):
        if not self.reset_button:
            self.reset_button = tk.Button(self.root, text="Jogar Novamente", font=('Arial', 14),
                                          command=self.reset_game)
            self.reset_button.grid(row=3, column=0, columnspan=3)

    # Função para reiniciar o jogo
    def reset_game(self):
        self.player = 'X'
        self.board = [''] * 9
        for button in self.buttons:
            button.config(text='', state='normal')
        if self.reset_button:
            self.reset_button.destroy()
            self.reset_button = None

if __name__ == "__main__":
    root = tk.Tk()
    jogo_da_velha = JogoDaVelha(root)
    root.mainloop()
