import numpy
import pygame
pygame.init()
from chess_piece import *
from chessgame import *
import math
import time

white_king = pygame.image.load('white_king.png')
white_queen = pygame.image.load('white_queen.png')
white_castle = pygame.image.load('white_rook.png')
white_bishop = pygame.image.load('white_bishop.png')
white_knight = pygame.image.load('white_horse.png')
white_pawn = pygame.image.load('white_pawn.png')

white_king_image = pygame.transform.scale(white_king, (80, 80))
white_queen_image = pygame.transform.scale(white_queen, (80, 80))
white_castle_image = pygame.transform.scale(white_castle, (65, 65))
white_bishop_image = pygame.transform.scale(white_bishop, (70, 70))
white_knight_image = pygame.transform.scale(white_knight, (65, 65))
white_pawn_image = pygame.transform.scale(white_pawn, (40, 40))

white_king_image_mini = pygame.transform.scale(white_king, (40, 40))
white_queen_image_mini = pygame.transform.scale(white_queen, (40, 40))
white_castle_image_mini = pygame.transform.scale(white_castle, (40, 40))
white_bishop_image_mini = pygame.transform.scale(white_bishop, (40, 40))
white_knight_image_mini = pygame.transform.scale(white_knight, (40, 40))
white_pawn_image_mini = pygame.transform.scale(white_pawn, (30, 30))

black_king = pygame.image.load('black_king.png')
black_queen = pygame.image.load('black_queen.png')
black_castle = pygame.image.load('black_rook.png')
black_bishop = pygame.image.load('black_bishop.png')
black_knight = pygame.image.load('black_knight.png')
black_pawn = pygame.image.load('black_pawn.png')

black_king_image = pygame.transform.scale(black_king, (80, 80))
black_queen_image = pygame.transform.scale(black_queen, (80, 80))
black_castle_image = pygame.transform.scale(black_castle, (65, 65))
black_bishop_image = pygame.transform.scale(black_bishop, (70, 70))
black_knight_image = pygame.transform.scale(black_knight, (65, 65))
black_pawn_image = pygame.transform.scale(black_pawn, (40, 40))

black_king_image_mini = pygame.transform.scale(black_king, (40, 40))
black_queen_image_mini = pygame.transform.scale(black_queen, (40, 40))
black_castle_image_mini = pygame.transform.scale(black_castle, (40, 40))
black_bishop_image_mini = pygame.transform.scale(black_bishop, (40, 40))
black_knight_image_mini = pygame.transform.scale(black_knight, (40, 40))
black_pawn_image_mini = pygame.transform.scale(black_pawn, (30, 30))

class chessboard:
    def __init__(self):
        # color creation
        self.green = (0, 225, 0)
        self.yellow = (225, 225, 10)
        self.brown = (31, 13, 4)
        self.black = (0, 0, 0)
        self.white = (255, 253, 209)
        self.blue = (30, 144, 255)
        self.red = (199, 21, 133)
        self.pink = (255, 192, 203)
        self.grey = (100, 100, 100)
        self.green_previous = (173, 255, 47)
        self.blue_previous = (135, 206, 250)
        self.red_previous = (250, 128, 114)

        # display size and square size
        self.top_line = 0
        self.gap = 5

        self.setup_text_gap_large = 130
        self.setup_text_gap_small = 70
        self.setup_text_gap = 50
        self.setup_click_width = 200
        self.setup_click_height = 50


        self.dis_width_input = 900
        self.panel_width = 370
        self.dis_width = round(self.dis_width_input / 8) * 8
        self.location_width = self.dis_width / 8
        self.block_width = self.location_width - self.gap

        # image sizes
        self.image_gap = self.dis_width_input / 45
        self.kq_image_gap = self.dis_width_input / 90
        self.pawn_image_gap = self.dis_width_input / 26

        # decision circles
        self.circle_width = self.block_width / 3.5


        # init display
        self.dis = pygame.display.set_mode((self.dis_width - self.gap + (self.panel_width * 2), self.dis_width - self.gap + self.top_line))
        pygame.display.set_caption("Chess")
        self.dis.fill(self.grey)

    def display_setup(self, white_human, white_computer, white_random, white_program, black_human, black_computer, black_random, black_program):
        self.dis.fill(self.black)

        if white_human == True:
            pygame.draw.rect(self.dis, self.grey, [(self.panel_width / 1.6) + self.setup_text_gap, (self.dis_width / 5) + self.setup_text_gap_large, 200, 50])

        if white_computer == True and white_random == True:
            pygame.draw.rect(self.dis, self.grey, [(self.panel_width / 1.6) + self.setup_text_gap, ((self.dis_width / 5) + self.setup_text_gap_large + self.setup_text_gap_small), 300, 50])

        if white_computer == True and white_program == True:
            pygame.draw.rect(self.dis, self.grey, [(self.panel_width / 1.6) + self.setup_text_gap, ((self.dis_width / 5) + self.setup_text_gap_large + (self.setup_text_gap_small * 2)), 300, 50])

        if black_human == True:
            pygame.draw.rect(self.dis, self.grey, [(self.panel_width / 1.6) + self.dis_width - self.setup_text_gap, ((self.dis_width / 5) + self.setup_text_gap_large), 200, 50])

        if black_computer == True and black_random == True:
            pygame.draw.rect(self.dis, self.grey, [(self.panel_width / 1.6) + self.dis_width - self.setup_text_gap, ((self.dis_width / 5) + self.setup_text_gap_large + self.setup_text_gap_small), 300, 50])

        if black_computer == True and black_program == True:
            pygame.draw.rect(self.dis, self.grey, [(self.panel_width / 1.6) + self.dis_width - self.setup_text_gap, ((self.dis_width / 5) + self.setup_text_gap_large + (self.setup_text_gap_small * 2)), 300, 50])

        font_player = pygame.font.SysFont("comicsansms", 60)
        font_settings = pygame.font.SysFont("comicsansms", 30)

        text_play = font_player.render("PLAY", True, self.yellow)
        text_white = font_player.render("WHITE", True, self.white)
        text_black = font_player.render("BLACK", True, self.white)
        text_computer = font_settings.render("Computer (random)", True, self.white)
        text_computer_program = font_settings.render("Computer (program)", True, self.white)
        text_human = font_settings.render("Human", True, self.white)

        self.dis.blit(text_play, ((self.panel_width - 70 + self.dis_width / 2), self.dis_width / 1.4))

        self.dis.blit(text_white, ((self.panel_width / 1.6) + self.setup_text_gap, self.dis_width / 5))
        self.dis.blit(text_human, ((self.panel_width / 1.6) + self.setup_text_gap, (self.dis_width / 5) + self.setup_text_gap_large))
        self.dis.blit(text_computer, ((self.panel_width / 1.6) + self.setup_text_gap, (self.dis_width / 5) + self.setup_text_gap_large + self.setup_text_gap_small))
        self.dis.blit(text_computer_program, ((self.panel_width / 1.6) + self.setup_text_gap, (self.dis_width / 5) + self.setup_text_gap_large + (self.setup_text_gap_small * 2)))

        self.dis.blit(text_black, ((self.panel_width / 1.6) + self.dis_width - self.setup_text_gap, self.dis_width / 5))
        self.dis.blit(text_human, ((self.panel_width / 1.6) + self.dis_width - self.setup_text_gap, (self.dis_width / 5) + self.setup_text_gap_large))
        self.dis.blit(text_computer, ((self.panel_width / 1.6) + self.dis_width - self.setup_text_gap, (self.dis_width / 5) + self.setup_text_gap_large + self.setup_text_gap_small))
        self.dis.blit(text_computer_program, ((self.panel_width / 1.6) + self.dis_width - self.setup_text_gap, (self.dis_width / 5) + self.setup_text_gap_large + (self.setup_text_gap_small * 2)))


    def display_init(self): # draws the squares:
        self.dis.fill(self.grey)
        pygame.draw.rect(self.dis, self.black, [0, 0, self.dis_width, self.top_line])
        pygame.draw.rect(self.dis, self.black, [0, 0, self.panel_width, self.dis_width])
        pygame.draw.rect(self.dis, self.grey, [self.panel_width - self.gap, 0, self.gap, self.dis_width])
        pygame.draw.rect(self.dis, self.black, [self.dis_width + self.panel_width, 0, self.panel_width, self.dis_width])

        font = pygame.font.SysFont("comicsansms", 40)
        small_font = pygame.font.SysFont("arial", 20)

        white_text = font.render("WHITE:", True, self.white)
        black_text = font.render("BLACK:", True, self.white)
        self.dis.blit(black_text, (10, (self.dis_width / 2) - 70))
        self.dis.blit(white_text, (self.panel_width + self.dis_width + 10, (self.dis_width / 2) - 70))

        white_text_take = small_font.render("Taken by black:", True, self.white)
        black_text_take = small_font.render("Taken by white:", True, self.white)
        self.dis.blit(white_text_take, (10, self.dis_width / 2))
        self.dis.blit(black_text_take, (self.panel_width + self.dis_width + 10, self.dis_width / 2))

        for a in range(0, 8):
            for b in range(0, 8):

                if a % 2 == 0:
                    if b % 2 == 0:
                        pygame.draw.rect(self.dis, self.white, [a * self.location_width + self.panel_width, b * self.location_width + self.top_line, self.block_width, self.block_width])
                    else:
                        pygame.draw.rect(self.dis, self.brown, [a * self.location_width + self.panel_width, b * self.location_width + self.top_line, self.block_width, self.block_width])

                else:
                    if b % 2 == 0:
                        pygame.draw.rect(self.dis, self.brown, [a * self.location_width + self.panel_width, b * self.location_width + self.top_line, self.block_width, self.block_width])
                    else:
                        pygame.draw.rect(self.dis, self.white, [a * self.location_width + self.panel_width, b * self.location_width + self.top_line, self.block_width, self.block_width])

        return True


    def circle_mod(self, y, x, golist):
        pygame.draw.rect(self.dis, self.green, [y * self.location_width + self.panel_width, x * self.location_width + self.top_line, self.block_width, self.block_width])
        for num in range(0, int(len(golist) / 2)):
            pygame.draw.circle(self.dis, self.blue, (golist[(num * 2) + 1] * self.location_width + (self.location_width / 2) + self.panel_width, golist[num * 2] * self.location_width + (self.location_width / 2) + self.top_line), self.circle_width)
            if array[golist[num * 2], golist[(num * 2) + 1]] in king_values:
                pygame.draw.circle(self.dis, self.yellow, (golist[(num * 2) + 1] * self.location_width + (self.location_width / 2) + self.panel_width, golist[num * 2] * self.location_width + (self.location_width / 2) + self.top_line), self.circle_width)
            if array[golist[num * 2], golist[(num * 2) + 1]] != board and array[golist[num * 2], golist[(num * 2) + 1]] not in king_values:
                pygame.draw.circle(self.dis, self.red, (golist[(num * 2) + 1] * self.location_width + (self.location_width / 2) + self.panel_width, golist[num * 2] * self.location_width + (self.location_width / 2) + self.top_line), self.circle_width)



    def piece_continue(self):

        wt_2 = 0
        wt_3 = 0
        wt_4 = 0
        wt_5 = 0
        wt_6 = 0
        bt_2 = 0
        bt_3 = 0
        bt_4 = 0
        bt_5 = 0
        bt_6 = 0


        for piece in listall:
            if piece.x == None:
                if piece.player == "white":
                    if piece.type == 2:
                        wt_2 += 1
                    if piece.type == 3:
                        wt_3 += 1
                    if piece.type == 4:
                        wt_4 += 1
                    if piece.type == 5:
                        wt_5 += 1
                    if piece.type == 6:
                        wt_6 += 1
                if piece.player == "black":
                    if piece.type == 2:
                        bt_2 += 1
                    if piece.type == 3:
                        bt_3 += 1
                    if piece.type == 4:
                        bt_4 += 1
                    if piece.type == 5:
                        bt_5 += 1
                    if piece.type == 6:
                        bt_6 += 1



        for piece in listall:
            if not piece.x == None:
                if piece.player == "white":
                    if piece.type == 1:
                        self.dis.blit(white_king_image, (piece.y * self.location_width + self.kq_image_gap + self.panel_width, piece.x * self.location_width + self.kq_image_gap + self.top_line))
                    if piece.type == 2:
                        self.dis.blit(white_queen_image, (piece.y * self.location_width + self.kq_image_gap + self.panel_width, piece.x * self.location_width + self.kq_image_gap + self.top_line))
                    if piece.type == 3:
                        self.dis.blit(white_bishop_image, (piece.y * self.location_width + self.image_gap + self.panel_width, piece.x * self.location_width + self.image_gap + self.top_line))
                    if piece.type == 4:
                        self.dis.blit(white_knight_image, (piece.y * self.location_width + self.image_gap + self.panel_width, piece.x * self.location_width + self.image_gap + self.top_line))
                    if piece.type == 5:
                        self.dis.blit(white_castle_image, (piece.y * self.location_width + self.image_gap + self.panel_width, piece.x * self.location_width + self.image_gap + self.top_line))
                    if piece.type == 6:
                        self.dis.blit(white_pawn_image, (piece.y * self.location_width + self.pawn_image_gap + self.panel_width, piece.x * self.location_width + self.pawn_image_gap + self.top_line))
                if piece.player == "black":
                    if piece.type == 1:
                        self.dis.blit(black_king_image, (piece.y * self.location_width + self.kq_image_gap + self.panel_width, piece.x * self.location_width + self.kq_image_gap + self.top_line))
                    if piece.type == 2:
                        self.dis.blit(black_queen_image, (piece.y * self.location_width + self.kq_image_gap + self.panel_width, piece.x * self.location_width + self.kq_image_gap + self.top_line))
                    if piece.type == 3:
                        self.dis.blit(black_bishop_image, (piece.y * self.location_width + self.image_gap + self.panel_width, piece.x * self.location_width + self.image_gap + self.top_line))
                    if piece.type == 4:
                        self.dis.blit(black_knight_image, (piece.y * self.location_width + self.image_gap + self.panel_width, piece.x * self.location_width + self.image_gap + self.top_line))
                    if piece.type == 5:
                        self.dis.blit(black_castle_image, (piece.y * self.location_width + self.image_gap + self.panel_width, piece.x * self.location_width + self.image_gap + self.top_line))
                    if piece.type == 6:
                        self.dis.blit(black_pawn_image, (piece.y * self.location_width + self.pawn_image_gap + self.panel_width, piece.x * self.location_width + self.pawn_image_gap + self.top_line))


            for num in range(0, wt_2):
                self.dis.blit(white_queen_image_mini, (20, (self.dis_width / 2) + 60))
                if num > 0:
                    self.dis.blit(white_queen_image_mini, (20 + ((num - 1) * 20), (self.dis_width / 2) + 180))

            for num in range(0, wt_3):
                self.dis.blit(white_bishop_image_mini, (60 + (num * 20), (self.dis_width / 2) + 60))

            for num in range(0, wt_4):
                self.dis.blit(white_knight_image_mini, (110 + (num * 20), (self.dis_width / 2) + 60))

            for num in range(0, wt_5):
                self.dis.blit(white_castle_image_mini, (160 + (num * 20), (self.dis_width / 2) + 60))

            for num in range(0, wt_6):
                self.dis.blit(white_pawn_image_mini, (20 + (num * 20), (self.dis_width / 2) + 120))



            for num in range(0, bt_2):
                self.dis.blit(black_queen_image_mini, (self.panel_width + self.dis_width + 20, (self.dis_width / 2) + 60))
                if num > 0:
                    self.dis.blit(black_queen_image_mini, (self.panel_width + self.dis_width + 20 + ((num - 1) * 20), (self.dis_width / 2) + 180))

            for num in range(0, bt_3):
                self.dis.blit(black_bishop_image_mini, (self.panel_width + self.dis_width + 60 + (num * 20), (self.dis_width / 2) + 60))

            for num in range(0, bt_4):
                self.dis.blit(black_knight_image_mini, (self.panel_width + self.dis_width + 110 + (num * 20), (self.dis_width / 2) + 60))

            for num in range(0, bt_5):
                self.dis.blit(black_castle_image_mini, (self.panel_width + self.dis_width + 160 + (num * 20), (self.dis_width / 2) + 60))

            for num in range(0, bt_6):
                self.dis.blit(black_pawn_image_mini, (self.panel_width + self.dis_width + 20 + (num * 20), (self.dis_width / 2) + 120))





    def clear(self): #clears of any take lines, and resets any taken values
        for a in range(0, 8):
            for b in range(0, 8):
                array[a, b] = board
        for piece in listall:
            if not piece.x == None:
                array[piece.x, piece.y] = piece.value


        #for a in range(0, 8):
        #    for b in range(0, 8):
        ##        if array[a, b] == white_move_only or array[a, b] == white_take_line or array[a, b] == black_move_only or array[a, b] == black_take_line or array[a, b] == white_take_only or array[a, b] == black_take_only:
        #            array[a, b] = board
        #        elif array[a, b] in white_taken or array[a, b] in black_taken:
        #            array[a, b] -= 40
        #        elif array[a, b] in white_star or array[a, b] in black_star:
        #            array[a, b] -= 80

    def clear_white_mod(self):
        for a in range(0, 8):
            for b in range(0, 8):
                if array[a, b] == white_move_only or array[a, b] == white_take_line or array[a, b] == black_move_only or array[a, b] == black_take_line or array[a, b] == white_take_only or array[a, b] == black_take_only:
                    array[a, b] = board
                elif array[a, b] in white_support or array[a, b] in black_support:
                    array[a, b] -= 80
                elif array[a, b] in white_taken:
                    array[a, b] -= 40
                #elif array[a, b] in white_star or array[a, b] in black_star:
                    #array[a, b] -= 80

    def clear_black_mod(self):
        for a in range(0, 8):
            for b in range(0, 8):
                if array[a, b] == white_move_only or array[a, b] == white_take_line or array[a, b] == black_move_only or array[a, b] == black_take_line or array[a, b] == white_take_only or array[a, b] == black_take_only:
                    array[a, b] = board
                elif array[a, b] in white_support or array[a, b] in black_support:
                    array[a, b] -= 80
                elif array[a, b] in black_taken:
                    array[a, b] -= 40
                #elif array[a, b] in white_star or array[a, b] in black_star:
                    #array[a, b] -= 80


    def previous_move(self, last_click_y, last_click_x, y, x, taking):
        pygame.draw.rect(self.dis, self.green_previous, [last_click_y * self.location_width + self.panel_width, last_click_x * self.location_width + self.top_line, self.block_width, self.block_width])
        if taking == True:
            pygame.draw.rect(self.dis, self.red_previous, [y * self.location_width + self.panel_width, x * self.location_width + self.top_line, self.block_width, self.block_width])
        if taking == False:
            pygame.draw.rect(self.dis, self.blue_previous, [y * self.location_width + self.panel_width, x * self.location_width + self.top_line, self.block_width, self.block_width])


    def check_black_checkmate(self):


        black_in_check = False
        total_golist = []

        for piece in whitelist:
            if piece.x != None:
                self.clear()
                piece.move()
                if array[kingb.x, kingb.y] == black_check:
                    black_in_check = True
                    break

        self.clear()
        if black_in_check == True:

            for piece in blacklist:
                if piece.x != None:

                    possible_x = None
                    possible_y = None
                    xx = piece.x
                    yy = piece.y
                    move_list_black = []
                    golist_black = []
                    piece.move()

                    # ALL LEGAL MOVES FOR A PARTICULAR PIECE
                    for a in range(0, 8):
                        for b in range(0, 8):
                            if array[a, b] in white_taken or array[a, b] == black_move_only or array[a, b] == black_take_line:
                                move_list_black.append(a)
                                move_list_black.append(b)


                    self.clear_black_mod()
                    if array[kingb.x, kingb.y] == black_castle_value:
                        array[kingb.x, kingb.y] -= 200



                    count = 0
                    for num in range(0, int(len(move_list_black) / 2)):

                        simulate_take = False

                        # If it's moving into a taken value, remove the taken value
                        if array[move_list_black[num * 2], move_list_black[(num * 2) + 1]] in white_taken:
                            simulate_take = True
                            for other_piece in whitelist:
                                if other_piece.x == move_list_black[num * 2] and other_piece.y == move_list_black[(num * 2) + 1]:
                                    other_piece.x = None
                                    other_piece.y = None
                                    revive_me = other_piece

                        # Move the piece, and save the last value for future clearing.
                        previous = array[move_list_black[num * 2], move_list_black[(num * 2) + 1]]
                        array[move_list_black[num * 2], move_list_black[(num * 2) + 1]] = piece.value
                        if count == 0:
                            array[piece.x, piece.y] = board

                        piece.x = move_list_black[num * 2]
                        piece.y = move_list_black[(num * 2) + 1]


                        # Check for check!! If it is a legal move, append it to the golist.
                        legal = True
                        for oppose_piece in whitelist:
                            if oppose_piece.x != None:
                                oppose_piece.move()

                                if array[kingb.x, kingb.y] == black_check:
                                    legal = False
                                    self.clear_black_mod()
                                    break
                                else:
                                    self.clear_black_mod()
                        if legal == True:
                            golist_black.append(move_list_black[num * 2])
                            golist_black.append(move_list_black[(num * 2) + 1])

                        # and now, reset the board to test for the next potential legal / illegal move
                        array[move_list_black[num * 2], move_list_black[(num * 2) + 1]] = previous
                        if simulate_take == True:
                            revive_me.x = move_list_black[num * 2]
                            revive_me.y = move_list_black[(num * 2) + 1]

                        count += 1

                    #break
                    piece.x = xx
                    piece.y = yy
                    array[piece.x, piece.y] = piece.value
                    self.clear()


                    if len(golist_black) != 0:
                        total_golist.append(1)
                        return total_golist
                        break

                #return total_golist
                #break

                # if list has length 1, it should have broken, and a move is possible, so not in check mate.
                # if list has length 0, it found no possible moves, so is therefore in check mate.
                #return total_golist

        if len(total_golist) == 0 and black_in_check == True:
            print("blackshould be checkmate")
            return total_golist

        elif black_in_check == False:
            total_golist.append(1)
            return total_golist



    def check_white_checkmate(self):

        white_in_check = False
        total_golist = []

        for piece in blacklist:
            if piece.x != None:
                self.clear()
                piece.move()
                if array[kingw.x, kingw.y] == white_check:
                    white_in_check = True
                    break
        self.clear()
        if white_in_check == True:

            for piece in whitelist:
                if piece.x != None:
                    possible_x = None
                    possible_y = None
                    xx = piece.x
                    yy = piece.y
                    re_move = False
                    move_list_white = []
                    golist_white = []
                    piece.move()

                    # ALL LEGAL MOVES FOR A PARTICULAR PIECE
                    for a in range(0, 8):
                        for b in range(0, 8):
                            if array[a, b] in black_taken or array[a, b] == white_move_only or array[a, b] == white_take_line or array[a, b] == white_castle_value:
                                castle_legal_white = True

                                if array[a, b] == white_castle_value:
                                    re_move = True
                                    self.clear()

                                    for oppose_piece_castle in blacklist:
                                        if oppose_piece_castle.x != None:
                                            oppose_piece_castle.move()
                                            if piece.value == 13:
                                                if array[kingw.x, kingw.y] == white_check or array[0, 2] == black_take_line or array[0, 2] == black_take_only or array[0, 3] == black_take_line or array[0, 3] == black_take_only:
                                                    self.clear_white_mod()
                                                    castle_legal_white = False
                                                    break
                                                else:
                                                    self.clear_white_mod()
                                            if piece.value == 14:
                                                if array[kingw.x, kingw.y] == white_check or array[0, 5] == black_take_line or array[0, 5] == black_take_only or array[0, 6] == black_take_line or array[0, 6] == black_take_only:
                                                    self.clear_white_mod()
                                                    castle_legal_white = False
                                                    break
                                                else:
                                                    self.clear_white_mod()

                                if castle_legal_white == True:
                                    move_list_white.append(a)
                                    move_list_white.append(b)

                                if re_move == True:
                                    piece.move()
                    self.clear_white_mod()


                    count = 0
                    for num in range(0, int(len(move_list_white) / 2)):

                        simulate_take = False

                        # If it's moving into a taken value, remove the taken value
                        if array[move_list_white[num * 2], move_list_white[(num * 2) + 1]] in black_taken:
                            simulate_take = True
                            for other_piece in blacklist:
                                if other_piece.x == move_list_white[num * 2] and other_piece.y == move_list_white[(num * 2) + 1]:
                                    other_piece.x = None
                                    other_piece.y = None
                                    revive_me = other_piece

                        # Move the piece, and save the last value for future clearing.
                        previous = array[move_list_white[num * 2], move_list_white[(num * 2) + 1]]
                        array[move_list_white[num * 2], move_list_white[(num * 2) + 1]] = piece.value
                        if count == 0:
                            array[piece.x, piece.y] = board

                        piece.x = move_list_white[num * 2]
                        piece.y = move_list_white[(num * 2) + 1]


                        # Check for check!! If it is a legal move, append it to the golist.
                        legal = True
                        for oppose_piece in blacklist:
                            if oppose_piece.x != None:
                                oppose_piece.move()
                                if array[kingw.x, kingw.y] == white_check:
                                    legal = False
                                    self.clear_white_mod()
                                    break
                                else:
                                    self.clear_white_mod()
                        if legal == True:
                            golist_white.append(move_list_white[num * 2])
                            golist_white.append(move_list_white[(num * 2) + 1])

                        # and now, reset the board to test for the next potential legal / illegal move
                        array[move_list_white[num * 2], move_list_white[(num * 2) + 1]] = previous
                        if simulate_take == True:
                            revive_me.x = move_list_white[num * 2]
                            revive_me.y = move_list_white[(num * 2) + 1]

                        count += 1

                    #break
                    piece.x = xx
                    piece.y = yy
                    array[piece.x, piece.y] = piece.value
                    self.clear()

                    if len(golist_white) != 0:
                        total_golist.append(1)
                        return total_golist
                        break

                #return total_golist
                #break

                # if list has length 1, it should have broken, and a move is possible, so not in check mate.
                # if list has length 0, it found no possible moves, so is therefore in check mate.
                #return total_golist

        if len(total_golist) == 0 and white_in_check == True:
            return total_golist

        elif white_in_check == False:
            total_golist.append(1)
            return total_golist



    # ----- GAME RUNNING ----- #
    def run(self):


        # ----- NECESSARY STARTING DEFINITIONS ----- #
        game_over = False
        player = "WHITE"
        golist = []
        golist_black = []
        move_list = []
        move_list_black = []
        just_selected_white = False
        just_selected_black = False
        white_piece_to_move = dummy_piece
        black_piece_to_move = dummy_piece
        last_click_y = None
        last_click_x = None
        saved_last_click_y = None
        saved_last_click_x = None
        saved_y = None
        saved_x = None
        saved_taking = None
        end_game = False
        initialise = True
        taken_list = []

        setup = True
        white_human = False
        white_computer = False
        white_random = False
        white_program = False
        black_human = False
        black_computer = False
        black_random = False
        black_program = False

        computer_moved = False

        y = None
        x = None
        timelist_white = []
        timelist_black = []



        # ----- GAME LOOP START ----- #
        while not game_over:

            start = time.time()
            #if end_game == False:
                #print("\n\n\n\n\n**********\n\nNEW TURN\n\n**********\n\n\n\n\n")

            # ----- RESETS ----- #
            delay = False
            computer_castle = False
            human_castle = False
            taking = False
            black_human_just_moved = False
            setup_delay = False

            # ----- SETUP ----- #
            if setup == True:
                self.display_setup(white_human, white_computer, white_random, white_program, black_human, black_computer, black_random, black_program)

            # ----- INITIALISE ----- #
            if initialise == True and setup == False:
                self.display_init()
                self.piece_continue()
                initialise = False



            # ----- EVENT FINDER ----- #
            if not (black_computer == True and player == "BLACK") or (white_computer == True and player == "WHITE") or (end_game == True):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True

                    if event.type == pygame.KEYDOWN:
                        print(array)

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        # ----- PIXEL CLICKED TO ARRAY COORDINATE CONVERSION ----- #
                        a = pygame.mouse.get_pos()
                        x = math.floor((a[0] - self.panel_width) / self.location_width) # round down these values.
                        y = math.floor((a[1] - self.top_line) / self.location_width)

                        if setup == True:

                            # WHITE HUMAN
                            if a[0] > ((self.panel_width / 1.6) + self.setup_text_gap) and a[0] < ((self.panel_width / 1.6) + self.setup_text_gap + self.setup_click_width):
                                if a[1] > ((self.dis_width / 5) + self.setup_text_gap_large)  and a[1] < ((self.dis_width / 5) + self.setup_text_gap_large + self.setup_click_height):
                                    white_human = True
                                    white_computer = False
                                    white_random = False
                                    white_program = False
                                    white_computer_setting = False

                            # WHITE COMPUTER RANDOM
                            if a[0] > ((self.panel_width / 1.6) + self.setup_text_gap) and a[0] < ((self.panel_width / 1.6) + self.setup_text_gap + self.setup_click_width + 100):
                                if a[1] > ((self.dis_width / 5) + self.setup_text_gap_large + self.setup_text_gap_small) and a[1] < ((self.dis_width / 5) + self.setup_text_gap_large + self.setup_text_gap_small + self.setup_click_height):
                                    white_computer = True
                                    white_human = False
                                    white_random = True
                                    white_program = False
                                    white_computer_setting = "RANDOM"

                            # WHITE COMPUTER PROGRAM
                            if a[0] > ((self.panel_width / 1.6) + self.setup_text_gap) and a[0] < ((self.panel_width / 1.6) + self.setup_text_gap + self.setup_click_width + 100):
                                if a[1] > ((self.dis_width / 5) + self.setup_text_gap_large + (self.setup_text_gap_small * 2)) and a[1] < ((self.dis_width / 5) + self.setup_text_gap_large + (self.setup_text_gap_small * 2) + self.setup_click_height):
                                    white_computer = True
                                    white_human = False
                                    white_program = True
                                    white_random = False
                                    white_computer_setting = "PROGRAM"



                            # BLACK HUMAN
                            if a[0] > ((self.panel_width / 1.6) + self.dis_width - self.setup_text_gap) and a[0] < ((self.panel_width / 1.6) + self.dis_width - self.setup_text_gap + self.setup_click_width):
                                if a[1] > ((self.dis_width / 5) + self.setup_text_gap_large) and a[1] < ((self.dis_width / 5) + self.setup_text_gap_large + self.setup_click_height):
                                    black_human = True
                                    black_computer = False
                                    black_random = False
                                    black_program = False
                                    black_computer_setting = False

                            # BLACK COMPUTER RANDOM
                            if a[0] > ((self.panel_width / 1.6) + self.dis_width - self.setup_text_gap - 50) and a[0] < ((self.panel_width / 1.6) + self.dis_width - self.setup_text_gap + self.setup_click_width + 100):
                                if a[1] > ((self.dis_width / 5) + self.setup_text_gap_large + self.setup_text_gap_small) and a[1] < ((self.dis_width / 5) + self.setup_text_gap_large + self.setup_text_gap_small + self.setup_click_height):
                                    black_computer = True
                                    black_human = False
                                    black_random = True
                                    black_program = False
                                    black_computer_setting = "RANDOM"

                            # BLACK COMPUTER PROGRAM
                            if a[0] > ((self.panel_width / 1.6) + self.dis_width - self.setup_text_gap - 50) and a[0] < ((self.panel_width / 1.6) + self.dis_width - self.setup_text_gap + self.setup_click_width + 100):
                                if a[1] > ((self.dis_width / 5) + self.setup_text_gap_large + (self.setup_text_gap_small * 2)) and a[1] < ((self.dis_width / 5) + self.setup_text_gap_large + (self.setup_text_gap_small * 2) + self.setup_click_height):
                                    black_computer = True
                                    black_human = False
                                    black_program = True
                                    black_random = False
                                    black_computer_setting = "PROGRAM"

                            # PLAY
                            if a[0] > (self.panel_width - 90 + (self.dis_width / 2)) and a[0] < (self.panel_width - 90 + (self.dis_width / 2) + self.setup_click_width):
                                if a[1] > (self.dis_width / 1.4) and a[1] < ((self.dis_width / 1.4) + 100):
                                    if white_human or white_computer == True:
                                        if black_human or black_computer == True:
                                            setup = False
                                            setup_delay = True
                                        else:
                                            pass
                                    self.display_init()
                                    self.piece_continue()

                        if end_game == True:
                            if a[0] > 0 and a[0] < 200:
                                if a[1] > 0 and a[1] < 200:
                                    for reset_piece in listall:
                                        reset_piece.reset()
                                    self.clear()
                                    setup_delay = True
                                    setup = True
                                    end_game = False
                                    taken_list = []
                                    golist = []
                                    golist_black = []
                                    move_list = []
                                    move_list_black = []
                                    just_selected_white = False
                                    just_selected_black = False
                                    white_piece_to_move = dummy_piece
                                    black_piece_to_move = dummy_piece
                                    last_click_y = None
                                    last_click_x = None
                                    saved_last_click_y = None
                                    saved_last_click_x = None
                                    saved_y = None
                                    saved_x = None
                                    saved_taking = None
                                    initialise = True
                                    timelist_white = []
                                    timelist_black = []

                        # only run the program if actually clicked on the board
                        if x <= 7 and y <= 7 and x >= 0 and y >= 0 and setup == False and setup_delay == False and end_game == False:


                            # ----- RESETS ----- #
                            self.display_init()         # draws the board
                            self.clear()                # makes the value of each piece original
                            if saved_last_click_x != None:
                                self.previous_move(saved_last_click_x, saved_last_click_y, saved_x, saved_y, saved_taking)
                            self.piece_continue()       # draws the pieces to the board
                            delay = False
                            castle_skip = False
                            castle_skip_black = False
                            re_move = False
                            same_click = False
                            taking = False

                            if just_selected_white == False: # so the piece only moves immediatly after it has been selected.
                                move_list = []
                                golist = []
                            just_selected_white = False
                            if just_selected_black == False:
                                move_list_black = []
                                golist_black = []
                            just_selected_black = False



                            # ----- WHITE TURNS ----- #
                            if player == "WHITE":

                                # ----- HUMAN TURNS ----- #
                                if white_human == True:

                                    # ----- PIECE SELECTION ----- #
                                    if array[y, x] in white_values:

                                        # affirm that the piece value you click is / isn't potentially a castling piece.
                                        for num in range(0, int(len(golist) / 2)):
                                            if y == golist[num * 2] and x == golist[(num * 2) + 1]:
                                                castle_skip = True
                                                break

                                        # if selecting board or same piece again, select it properly.
                                        if array[y, x] == white_piece_to_move.value and array[last_click_y, last_click_x] == white_piece_to_move.value:
                                            same_click = True
                                            self.display_init()
                                            if saved_last_click_x != None:
                                                self.previous_move(saved_last_click_x, saved_last_click_y, saved_x, saved_y, saved_taking)
                                            self.piece_continue()
                                            white_piece_to_move = dummy_piece


                                        # if not a potential castling piece, follow this:
                                        if castle_skip == False and same_click == False:

                                            for piece in whitelist:
                                                if piece.value == array[y, x]:
                                                    piece.move()
                                                    move_list = []
                                                    golist = []

                                                    # ----- CHECK FOR POSSIBLE LEGAL / ILLEGAL MOVES, AND CASTLING RESTRICTIONS ----- #
                                                    # looks for all possible legal, and illegal, moves the selected piece can make
                                                    # check that the king, and two spaces it moves during castling, are not in check
                                                    for a in range(0, 8):
                                                        for b in range(0, 8):

                                                            if array[a, b] in black_taken or array[a, b] == white_move_only or array[a, b] == white_take_line or array[a, b] == white_castle_value:
                                                                castle_legal = True

                                                                if array[a, b] == white_castle_value:
                                                                    re_move = True
                                                                    self.clear()

                                                                    for oppose_piece_castle in blacklist:
                                                                        if oppose_piece_castle.x != None:
                                                                            oppose_piece_castle.move()
                                                                            if piece.value == 13:
                                                                                if array[kingw.x, kingw.y] == white_check or array[7, 2] == black_take_line or array[7, 2] == black_take_only or array[7, 3] == black_take_line or array[7, 3] == black_take_only:
                                                                                    self.clear_white_mod()
                                                                                    castle_legal = False
                                                                                    break
                                                                                else:
                                                                                    self.clear_white_mod()
                                                                            if piece.value == 14:
                                                                                if array[kingw.x, kingw.y] == white_check or array[7, 5] == black_take_line or array[7, 5] == black_take_only or array[7, 6] == black_take_line or array[7, 6] == black_take_only:
                                                                                    self.clear_white_mod()
                                                                                    castle_legal = False
                                                                                    break
                                                                                else:
                                                                                    self.clear_white_mod()

                                                                if castle_legal == True:
                                                                    move_list.append(a)
                                                                    move_list.append(b)

                                                                if re_move == True:
                                                                    piece.move()
                                                    self.clear_white_mod() # needs to be adapted, so taken values remain.
                                                    if array[kingw.x, kingw.y] == white_castle_value:
                                                        array[kingw.x, kingw.y] -= 200


                                                    # ----- CHECK POSSIBLE LEGAL / ILLEGAL MOVES ARE IN FACT LEGAL ----- #
                                                    yy = y
                                                    xx = x
                                                    count = 0
                                                    for num in range(0, int(len(move_list) / 2)):

                                                        simulate_take = False

                                                        # If its moving into a taken value, remove the taken value
                                                        if array[move_list[num * 2], move_list[(num * 2) + 1]] in black_taken:
                                                            simulate_take = True
                                                            for other_piece in blacklist:
                                                                if other_piece.x == move_list[num * 2] and other_piece.y == move_list[(num * 2) + 1]:
                                                                    other_piece.x = None
                                                                    other_piece.y = None
                                                                    revive_me = other_piece

                                                        # Move the piece, and save the last value for future clearing.
                                                        previous = array[move_list[num * 2], move_list[(num * 2) + 1]]
                                                        array[move_list[num * 2], move_list[(num * 2) + 1]] = piece.value
                                                        if count == 0:
                                                            array[yy, xx] = board

                                                        piece.x = move_list[num * 2]
                                                        piece.y = move_list[(num * 2) + 1]


                                                        # check for check!! If it is a legal move, append it to the golist.
                                                        legal = True
                                                        for oppose_piece in blacklist:
                                                            if oppose_piece.x != None:
                                                                oppose_piece.move()
                                                                if array[kingw.x, kingw.y] == white_check:
                                                                    legal = False
                                                                    self.clear_white_mod()
                                                                    break
                                                                else:
                                                                    self.clear_white_mod()
                                                        if legal == True:
                                                            golist.append(move_list[num * 2])
                                                            golist.append(move_list[(num * 2) + 1])

                                                        # and now, reset the board to test for the next legal / illegal move
                                                        array[move_list[num * 2], move_list[(num * 2) + 1]] = previous
                                                        if simulate_take == True:
                                                            revive_me.x = move_list[num * 2]
                                                            revive_me.y = move_list[(num * 2) + 1]

                                                        count += 1
                                                    break


                                            # put the selected piece back on the board
                                            piece.x = y
                                            piece.y = x
                                            array[piece.x, piece.y] = piece.value
                                            self.clear()
                                            self.display_init()
                                            if saved_last_click_x != None:
                                                self.previous_move(saved_last_click_x, saved_last_click_y, saved_x, saved_y, saved_taking)
                                            self.circle_mod(x, y, golist)
                                            self.piece_continue()
                                            white_piece_to_move = piece
                                            just_selected_white = True
                                            computer_moved = False

                                    # ----- PIECE MOVE ----- #
                                    for num in range(0, int(len(golist) / 2)):
                                        if y == golist[num * 2] and x == golist[(num * 2) + 1]:
                                            white_piece_to_move.move()

                                            # if taking a piece, remove it from the game
                                            if array[y, x] in black_taken:
                                                for piece in listall:
                                                    if piece.x == y and piece.y == x:
                                                        piece.x = None
                                                        piece.y = None
                                                        piece.first_turn = None
                                                        taking = True

                                            # move piece if castling
                                            if array[y, x] == white_castle_value:
                                                human_castle = True
                                                if white_piece_to_move.y == 7:
                                                    array[white_piece_to_move.x, white_piece_to_move.y] = board
                                                    white_piece_to_move.y = 5
                                                    kingw.y = 6
                                                    array[y, x] = board
                                                if white_piece_to_move.y == 0:
                                                    array[white_piece_to_move.x, white_piece_to_move.y] = board
                                                    white_piece_to_move.y = 3
                                                    kingw.y = 2
                                                    array[y, x] = board

                                            # move piece if not castling
                                            if castle_skip == False:
                                                array[y, x] = white_piece_to_move.value
                                                array[white_piece_to_move.x, white_piece_to_move.y] = board
                                                white_piece_to_move.x = y
                                                white_piece_to_move.y = x

                                            # pawns turn to queens
                                            if white_piece_to_move.type == 6:
                                                if white_piece_to_move.x == 0:
                                                    white_piece_to_move.type = 2
                                                    white_piece_to_move.ranking = 9


                                            self.display_init()
                                            self.previous_move(last_click_x, last_click_y, x, y, taking)
                                            saved_last_click_x = last_click_x
                                            saved_last_click_y = last_click_y
                                            saved_x = x
                                            saved_y = y
                                            saved_taking = taking
                                            self.piece_continue()
                                            player = "BLACK"
                                            delay = True
                                            white_piece_to_move.first_turn = False
                                            if human_castle == True:
                                                kingw.first_turn = False
                                            computer_moved = False

                                            total_golist = self.check_black_checkmate()
                                            if len(total_golist) == 0:
                                                really_is_check = False
                                                for piece in whitelist:
                                                    if piece.x != None:
                                                        self.clear()
                                                        piece.move()
                                                        if array[kingb.x, kingb.y] == black_check:
                                                            font_win = pygame.font.SysFont("comicsansms", 30)
                                                            text_win = font_win.render("Black in checkmate", True, self.white)
                                                            self.dis.blit(text_win, (self.panel_width + self.dis_width, self.dis_width / 5))
                                                            end_game = True
                                                            really_is_check = True
                                                            break
                                                if really_is_check == False:
                                                    font_draw = pygame.font.SysFont("comicsansms", 30)
                                                    text_draw = font_draw.render("Black can't move.\nStalemate", True, self.white)
                                                    self.dis.blit(text_draw, (self.panel_width + self.dis_width, self.dis_width / 5))
                                                    end_game = True



                            # ----- BLACK TURNS ----- #
                            if player == "BLACK" and delay == False:

                                # ----- HUMAN TURNS ----- #
                                if black_human == True:

                                    # ----- PIECE SELECTION ----- #
                                    if array[y, x] in black_values:

                                        # affirm that the piece value you click is / isn't potentially a castling piece.
                                        for num in range(0, int(len(golist_black) / 2)):
                                            if y == golist_black[num * 2] and x == golist_black[(num * 2) + 1]:
                                                castle_skip_black = True
                                                break

                                        # if selecting board or same piece again, select it properly.
                                        if array[y, x] == black_piece_to_move.value and array[last_click_y, last_click_x] == black_piece_to_move.value:
                                            same_click = True
                                            self.display_init()
                                            if saved_last_click_x != None:
                                                self.previous_move(saved_last_click_x, saved_last_click_y, saved_x, saved_y, saved_taking)
                                            self.piece_continue()
                                            black_piece_to_move = dummy_piece

                                        # if not a potential castling piece, follow this:
                                        if castle_skip_black == False and same_click == False:

                                            for piece in blacklist:
                                                if piece.value == array[y, x]:
                                                    piece.move()
                                                    move_list_black = []
                                                    golist_black = []

                                                    # ----- CHECK FOR POSSIBLE LEGAL / ILLEGAL MOVES, AND CASTLING RESTRICTIONS ----- #
                                                    # looks for all possible legal, and illegal, moves the selected piece can make
                                                    # check that the king, and two spaces it moves during castling, are not in check
                                                    for a in range(0, 8):
                                                        for b in range(0, 8):
                                                            if array[a, b] in white_taken or array[a, b] == black_move_only or array[a, b] == black_take_line or array[a, b] == black_castle_value:
                                                                castle_legal_black = True

                                                                if array[a, b] == black_castle_value:
                                                                    re_move = True
                                                                    self.clear()

                                                                    for oppose_piece_castle in whitelist:
                                                                        if oppose_piece_castle.x != None:
                                                                            oppose_piece_castle.move()
                                                                            if piece.value == 33:
                                                                                if array[kingb.x, kingb.y] == black_check or array[0, 2] == white_take_line or array[0, 2] == white_take_only or array[0, 3] == white_take_line or array[0, 3] == white_take_only:
                                                                                    self.clear_black_mod()
                                                                                    castle_legal_black = False
                                                                                    break
                                                                                else:
                                                                                    self.clear_black_mod()
                                                                            if piece.value == 34:
                                                                                if array[kingb.x, kingb.y] == black_check or array[0, 5] == white_take_line or array[0, 5] == white_take_only or array[0, 6] == white_take_line or array[0, 6] == white_take_only:
                                                                                    self.clear_black_mod()
                                                                                    castle_legal_black = False

                                                                                    break
                                                                                else:
                                                                                    self.clear_black_mod()

                                                                if castle_legal_black == True:

                                                                    move_list_black.append(a)
                                                                    move_list_black.append(b)

                                                                if re_move == True:
                                                                    piece.move()

                                                    self.clear_black_mod()
                                                    if array[kingb.x, kingb.y] == black_castle_value:
                                                        array[kingb.x, kingb.y] -= 200


                                                    # ----- CHECK POSSIBLE LEGAL / ILLEGAL MOVES ARE IN FACT LEGAL ----- #
                                                    yy = y
                                                    xx = x
                                                    count = 0
                                                    for num in range(0, int(len(move_list_black) / 2)):

                                                        simulate_take = False

                                                        # If it's moving into a taken value, remove the taken value
                                                        if array[move_list_black[num * 2], move_list_black[(num * 2) + 1]] in white_taken:
                                                            simulate_take = True
                                                            for other_piece in whitelist:
                                                                if other_piece.x == move_list_black[num * 2] and other_piece.y == move_list_black[(num * 2) + 1]:
                                                                    other_piece.x = None
                                                                    other_piece.y = None
                                                                    revive_me = other_piece

                                                        # Move the piece, and save the last value for future clearing.
                                                        previous = array[move_list_black[num * 2], move_list_black[(num * 2) + 1]]
                                                        array[move_list_black[num * 2], move_list_black[(num * 2) + 1]] = piece.value
                                                        if count == 0:
                                                            array[yy, xx] = board

                                                        piece.x = move_list_black[num * 2]
                                                        piece.y = move_list_black[(num * 2) + 1]


                                                        # Check for check!! If it is a legal move, append it to the golist.
                                                        legal = True
                                                        for oppose_piece in whitelist:
                                                            if oppose_piece.x != None:
                                                                oppose_piece.move()
                                                                if array[kingb.x, kingb.y] == black_check:
                                                                    legal = False
                                                                    self.clear_black_mod()
                                                                    break
                                                                else:
                                                                    self.clear_black_mod()
                                                        if legal == True:
                                                            golist_black.append(move_list_black[num * 2])
                                                            golist_black.append(move_list_black[(num * 2) + 1])

                                                        # and now, reset the board to test for the next potential legal / illegal move
                                                        array[move_list_black[num * 2], move_list_black[(num * 2) + 1]] = previous
                                                        if simulate_take == True:
                                                            revive_me.x = move_list_black[num * 2]
                                                            revive_me.y = move_list_black[(num * 2) + 1]

                                                        count += 1

                                                    break


                                            # put the selected piece back on the board
                                            piece.x = y
                                            piece.y = x
                                            array[piece.x, piece.y] = piece.value
                                            self.clear()
                                            self.display_init()
                                            if saved_last_click_x != None:
                                                self.previous_move(saved_last_click_x, saved_last_click_y, saved_x, saved_y, saved_taking)
                                            self.circle_mod(x, y, golist_black)
                                            self.piece_continue()
                                            black_piece_to_move = piece
                                            just_selected_black = True
                                            computer_moved = False

                                    # ----- PIECE MOVE ----- #
                                    for num in range(0, int(len(golist_black) / 2)):
                                        if y == golist_black[num * 2] and x == golist_black[(num * 2) + 1]:
                                            black_piece_to_move.move()

                                            # if taking a piece, remove it from the game
                                            if array[y, x] in white_taken:
                                                for piece in listall:
                                                    if piece.x == y and piece.y == x:
                                                        piece.x = None
                                                        piece.y = None
                                                        piece.first_turn = None
                                                        taking = True

                                            # move piece if castling
                                            if array[y, x] == black_castle_value:
                                                human_castle = True
                                                if black_piece_to_move.y == 7:
                                                    array[black_piece_to_move.x, black_piece_to_move.y] = board
                                                    black_piece_to_move.y = 5
                                                    kingb.y = 6
                                                    array[y, x] = board
                                                if black_piece_to_move.y == 0:
                                                    array[black_piece_to_move.x, black_piece_to_move.y] = board
                                                    black_piece_to_move.y = 3
                                                    kingb.y = 2
                                                    array[y, x] = board

                                            # move piece if not castling
                                            if castle_skip_black == False:
                                                array[y, x] = black_piece_to_move.value
                                                array[black_piece_to_move.x, black_piece_to_move.y] = board
                                                black_piece_to_move.x = y
                                                black_piece_to_move.y = x

                                            # pawns turn to queens
                                            if black_piece_to_move.type == 6:
                                                if black_piece_to_move.x == 7:
                                                    black_piece_to_move.type = 2
                                                    black_piece_to_move.ranking = 9

                                            self.display_init()
                                            self.previous_move(last_click_x, last_click_y, x, y, taking)
                                            saved_last_click_x = last_click_x
                                            saved_last_click_y = last_click_y
                                            saved_x = x
                                            saved_y = y
                                            saved_taking = taking
                                            self.piece_continue()
                                            player = "WHITE"
                                            black_piece_to_move.first_turn = False
                                            if human_castle == True:
                                                kingb.first_turn = False
                                            computer_moved = False
                                            black_human_just_moved = True

                                            total_golist = self.check_white_checkmate()
                                            if len(total_golist) == 0:
                                                really_is_check = False
                                                for piece in blacklist:
                                                    if piece.x != None:
                                                        self.clear()
                                                        piece.move()
                                                        if array[kingw.x, kingw.y] == white_check:
                                                            font_win = pygame.font.SysFont("comicsansms", 30)
                                                            text_win = font_win.render("White in checkmate", True, self.white)
                                                            self.dis.blit(text_win, (self.panel_width + self.dis_width, self.dis_width / 5))
                                                            end_game = True
                                                            really_is_check = True
                                                            break
                                                if really_is_check == False:
                                                    font_draw = pygame.font.SysFont("comicsansms", 30)
                                                    text_draw = font_draw.render("White can't move.\nStalemate", True, self.white)
                                                    self.dis.blit(text_draw, (self.panel_width + self.dis_width, self.dis_width / 5))
                                                    end_game = True





            # ----- COMPUTER TURNS (WHITE) ----- #
            if white_computer == True and player == "WHITE" and setup == False and setup_delay == False and black_human_just_moved == False and end_game == False:

                #time.sleep(5)
                print("**********\n\n\nWHITE TURN:\n\n\n\n")



                random_x, random_y, random_piece = gameplay.computerplay(player, white_computer_setting)


                if random_x == "checkmate":
                    font_win = pygame.font.SysFont("comicsansms", 30)
                    text_win = font_win.render("White in checkmate", True, self.white)
                    self.dis.blit(text_win, (self.panel_width + self.dis_width, self.dis_width / 5))
                    end_game = True

                elif random_x == "stalemate" and random_y == "stalemate" and random_piece == "stalemate":
                    font_draw = pygame.font.SysFont("comicsansms", 30)
                    text_draw = font_draw.render("White can't move.\nStalemate", True, self.white)
                    self.dis.blit(text_draw, (self.panel_width + self.dis_width, self.dis_width / 5))
                    end_game = True

                else:
                    random_piece.move()
                    original_x = random_piece.x
                    original_y = random_piece.y

                    # if taking a piece, remove it from the game
                    if array[random_x, random_y] in black_taken:
                        for piece in blacklist:
                            if piece.x == random_x and piece.y == random_y:
                                piece.x = None
                                piece.y = None
                                piece.first_turn = None
                                taking = True
                                taken_list.append(piece.value)

                    # move piece if castling
                    if array[random_x, random_y] == white_castle_value:
                        computer_castle = True
                        if random_piece.y == 7:
                            array[random_piece.x, random_piece.y] = board
                            random_piece.y = 5
                            kingw.y = 6
                            array[random_x, random_y] = board
                        if random_piece.y == 0:
                            array[random_piece.x, random_piece.y] = board
                            random_piece.y = 3
                            kingw.y = 2
                            array[random_x, random_y] = board

                    # move piece if not castling
                    if computer_castle == False:
                        array[random_x, random_y] = random_piece.value
                        array[random_piece.x, random_piece.y] = board
                        random_piece.x = random_x
                        random_piece.y = random_y

                    # pawns turn to queens
                    if random_piece.type == 6:
                        if random_piece.x == 0:
                            random_piece.type = 2
                            random_piece.ranking = 9


                    self.clear()
                    self.display_init()
                    self.previous_move(original_y, original_x, random_y, random_x, taking)
                    saved_last_click_x = original_y
                    saved_last_click_y = original_x
                    saved_x = random_y
                    saved_y = random_x
                    saved_taking = taking
                    self.piece_continue()
                    player = "BLACK"
                    random_piece.first_turn = False
                    if computer_castle == True:
                        kingb.first_turn = False
                    last_click_y = random_y
                    last_click_x = random_x
                    computer_moved = True
                    delay = True

                    total_golist = self.check_black_checkmate()
                    print("length")
                    print(len(total_golist))
                    if int(len(total_golist)) == 0:
                        really_is_check = False
                        for piece in whitelist:
                            if piece.x != None:
                                self.clear()
                                piece.move()
                                if array[kingb.x, kingb.y] == black_check:
                                    font_win = pygame.font.SysFont("comicsansms", 30)
                                    text_win = font_win.render("Black in checkmate", True, self.white)
                                    self.dis.blit(text_win, (self.panel_width + self.dis_width, self.dis_width / 5))
                                    end_game = True
                                    really_is_check = True
                                    break
                        if really_is_check == False:
                            font_draw = pygame.font.SysFont("comicsansms", 30)
                            text_draw = font_draw.render("Black can't move.\nStalemate", True, self.white)
                            self.dis.blit(text_draw, (self.panel_width + self.dis_width, self.dis_width / 5))
                            end_game = True



            # ----- COMPUTER TURNS (BLACK) ----- #
            if black_computer == True and player == "BLACK" and setup == False and setup_delay == False and delay == False and end_game == False:

                print("\n\nBLACK TURN:\n\n")

                random_x, random_y, random_piece = gameplay.computerplay(player, black_computer_setting)


                if random_x == "checkmate" and random_y == "checkmate" and random_piece == "checkmate":
                    font_win = pygame.font.SysFont("comicsansms", 30)
                    text_win = font_win.render("Black in checkmate", True, self.white)
                    self.dis.blit(text_win, (self.panel_width + self.dis_width, self.dis_width / 5))
                    end_game = True

                elif random_x == "stalemate" and random_y == "stalemate" and random_piece == "stalemate":
                    font_draw = pygame.font.SysFont("comicsansms", 30)
                    text_draw = font_draw.render("Black can't move.\nStalemate", True, self.white)
                    self.dis.blit(text_draw, (self.panel_width + self.dis_width, self.dis_width / 5))
                    end_game = True


                else:
                    random_piece.move()
                    original_x = random_piece.x
                    original_y = random_piece.y

                    # if taking a piece, remove it from the game
                    if array[random_x, random_y] in white_taken:
                        for piece in whitelist:
                            if piece.x == random_x and piece.y == random_y:
                                piece.x = None
                                piece.y = None
                                piece.first_turn = None
                                taking = True
                                taken_list.append(piece.value)

                    # move piece if castling
                    if array[random_x, random_y] == black_castle_value:
                        computer_castle = True
                        if random_piece.y == 7:
                            array[random_piece.x, random_piece.y] = board
                            random_piece.y = 5
                            kingb.y = 6
                            array[random_x, random_y] = board
                        if random_piece.y == 0:
                            array[random_piece.x, random_piece.y] = board
                            random_piece.y = 3
                            kingb.y = 2
                            array[random_x, random_y] = board

                    # move piece if not castling
                    if computer_castle == False:
                        array[random_x, random_y] = random_piece.value
                        array[random_piece.x, random_piece.y] = board
                        random_piece.x = random_x
                        random_piece.y = random_y

                    # pawns turn to queens
                    if random_piece.type == 6:
                        if random_piece.x == 7:
                            random_piece.type = 2
                            random_piece.ranking = 9


                    self.clear()
                    self.display_init()
                    self.previous_move(original_y, original_x, random_y, random_x, taking)
                    saved_last_click_x = original_y
                    saved_last_click_y = original_x
                    saved_x = random_y
                    saved_y = random_x
                    saved_taking = taking
                    self.piece_continue()
                    player = "WHITE"
                    random_piece.first_turn = False
                    if computer_castle == True:
                        kingb.first_turn = False
                    last_click_y = random_y
                    last_click_x = random_x
                    computer_moved = True


            if end_game == True:
                font = pygame.font.SysFont("comicsansms", 30)
                text = font.render("Play again?", True, self.white)
                self.dis.blit(text, (30, 30))
                play_again_possible = True
                black_computer = False
                black_human = False
                white_human = False
                white_computer = False
                player = "WHITE"


            # ----- RESETS ----- #
            # originally on same indentation as if player == "BLACK" / "WHITE"
            if computer_moved == False:
                last_click_y = y
                last_click_x = x

            # ----- STALEMATE CHECKER ----- #
            if len(listall) - len(taken_list) == 2:
                font_draw = pygame.font.SysFont("comicsansms", 30)
                text_draw = font_draw.render("Stalemate", True, self.white)
                self.dis.blit(text_draw, (self.panel_width + self.dis_width, self.dis_width / 5))
                end_game = True

            # ----- TIME KEEPING ----- #

            end = time.time()

            if setup == False and end_game == False and player == "BLACK":
                timed_white = end - start
                time_white = round(timed_white, 4)
                timelist_white.append(time_white)

            if setup == False and end_game == False and player == "WHITE":
                timed_black = end - start
                time_black = round(timed_black, 4)
                timelist_black.append(time_black)


            if end_game == True:
                if int(len(timelist_white)) > 0 and int(len(timelist_black)) > 0:
                    averaged_time_white = sum(timelist_white) / len(timelist_white)
                    averaged_time_black = sum(timelist_black) / len(timelist_black)

                    average_time_white = round(averaged_time_white, 4)
                    average_time_black = round(averaged_time_black, 4)

                    fast_time_white = min(timelist_white)
                    fast_time_black = min(timelist_black)

                    slow_time_white = max(timelist_white)
                    slow_time_black = max(timelist_black)

                    font_time = pygame.font.SysFont("arial", 20)
                    font_time_title = pygame.font.SysFont("comicsansms", 30)

                    text_time = font_time_title.render("Times:", True, self.white)
                    text_time_white_av = font_time.render(f"White average time: {average_time_white} seconds", True, self.white)
                    text_time_black_av = font_time.render(f"Black average time: {average_time_black} seconds", True, self.white)
                    text_time_white_fast = font_time.render(f"White fastest: {fast_time_white} seconds", True, self.white)
                    text_time_white_slow = font_time.render(f"White slowest: {slow_time_white} seconds", True, self.white)
                    text_time_black_fast = font_time.render(f"Black fastest: {fast_time_black} seconds", True, self.white)
                    text_time_black_slow = font_time.render(f"Black slowest: {slow_time_black} seconds", True, self.white)


                    self.dis.blit(text_time, (self.panel_width + self.dis_width + 10, self.dis_width - 200))
                    self.dis.blit(text_time_white_av, (self.panel_width + self.dis_width + 10, self.dis_width - 130))
                    self.dis.blit(text_time_white_fast, (self.panel_width + self.dis_width + 10, self.dis_width - 85))
                    self.dis.blit(text_time_white_slow, (self.panel_width + self.dis_width + 10, self.dis_width - 40))

                    self.dis.blit(text_time, (10, self.dis_width - 200))
                    self.dis.blit(text_time_black_av, (10, self.dis_width - 130))
                    self.dis.blit(text_time_black_fast, (10, self.dis_width - 85))
                    self.dis.blit(text_time_black_slow, (10, self.dis_width - 40))



            # ----- DISPLAY UPDATE ----- #
            pygame.display.update()












game = chessboard()
game.run()




















# end of script
