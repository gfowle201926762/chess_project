import numpy

# ----- VALUES ----- #
board = 0
white_values = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] #(king, queen, castle, bishop, knight, pawn)
white_move_only = 2
white_take_line = 6
white_take_only = 8
white_taken = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66] #white_values + 40
white_support = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106] #white_values + 80

black_values = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46] #(king, queen, castle, bishop, knight, pawn)
black_move_only = 3
black_take_line = 7
black_take_only = 9
black_taken = [71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86] #black_values + 40
black_support = [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126] #black_values + 80

check_values = [51, 71]
white_check = 51
black_check = 71

king_values = [11, 31]
castle_values = [211, 231]
white_castle_value = 211
black_castle_value = 231

only_values = [2, 8, 3, 9]

class piece:

    def __init__(self, x, y, type, player, value, first_turn, ranking, name):
        self.x = x
        self.y = y
        self.type = type
        self.player = player
        self.value = value
        self.first_turn = first_turn
        self.ranking = ranking
        self.name = name



    def move_updown(self):
        count = 0
        for num in range(self.x + 1, 8): #scanning down:
            if num >= 0 and num <= 7:
                if array[num, self.y] != board: # and array[num, self.y] not in only_values:
                    count += 1
                self.fill_move(num, self.y)
                if count >= 1:
                    break

        count = 0
        for num in reversed(range(0, self.x)): #scanning up:
            if num >= 0 and num <= 7:
                if array[num, self.y] != board: # and array[num, self.y] not in only_values:
                    count += 1
                self.fill_move(num, self.y)
                if count >= 1:
                    break

        count = 0
        for num in range(self.y + 1, 8): # scanning right:
            if num >= 0 and num <= 7:
                if array[self.x, num] != board: # and array[num, self.x] not in only_values:
                    count += 1
                self.fill_move(self.x, num)
                if count >= 1:
                    break

        count = 0
        for num in reversed(range(0, self.y)): # scanning left:
            if num >= 0 and num <= 7:
                if array[self.x, num] != board: # and array[num, self.x] not in only_values:
                    count += 1
                self.fill_move(self.x, num)
                if count >= 1:
                    break

    def move_diagonal(self):

        count = 0
        dummy = self.y + 1
        for numx in range(self.x + 1, 8): # scanning down-right
            if dummy < 8:
                if count >= 1:
                    break
                if array[numx, dummy] == board: # or array[numx, dummy] in only_values:
                    self.fill_move(numx, dummy)
                    dummy += 1
                elif array[numx, dummy] != board: # and array[numx, dummy] not in only_values:
                    self.fill_move(numx, dummy)
                    count += 1

        count = 0
        dummy = self.y + 1
        for numx in reversed(range(0, self.x)): # scanning up-right
            if dummy < 8:
                if count >= 1:
                    break
                if array[numx, dummy] == board: # or array[numx, dummy] in only_values:
                    self.fill_move(numx, dummy)
                    dummy += 1
                elif array[numx, dummy] != board: # and array[numx, dummy] not in only_values:
                    self.fill_move(numx, dummy)
                    count += 1

        count = 0
        dummy = self.y - 1
        for numx in range(self.x + 1, 8): # scanning down-left
            if dummy >= 0:
                if count >= 1:
                    break
                if array[numx, dummy] == board: # or array[numx, dummy] in only_values:
                    self.fill_move(numx, dummy)
                    dummy -= 1
                elif array[numx, dummy] != board: #in white_values or array[numx, dummy] in black_values:
                    self.fill_move(numx, dummy)
                    count += 1

        count = 0
        dummy = self.y - 1
        for numx in reversed(range(0, self.x)): # scanning up-left
            if dummy >= 0:
                if count >= 1:
                    break
                if array[numx, dummy] == board: # or array[numx, dummy] in only_values:
                    self.fill_move(numx, dummy)
                    dummy -= 1
                elif array[numx, dummy] != board: # and array[numx, dummy] not in only_values:
                    self.fill_move(numx, dummy)
                    count += 1

    def fill_move(self, numx, numy):

        if numx >= 0 and numx <= 7 and numy >= 0 and numy <= 7:

            if self.player == "white": #white
                if array[numx, numy] == board:
                    array[numx, numy] = white_take_line
                if array[numx, numy] in black_values: # black pieces which can be taken
                    array[numx, numy] += 40
                #if array[numx, numy] in white_values:
                #    array[numx, numy] += 80
                #if array[numx, numy] == black_castle_value:
                #    array[numx, numy] = black_check
                castle_cancel = False
                if self.type == 5:
                    if self.first_turn == True:
                        if array[numx, numy] in white_values:
                            for piece in listall:
                                if piece.type == 1:
                                    if piece.x == numx and piece.y == numy:
                                        if piece.first_turn == True:
                                            array[numx, numy] += 200
                                            castle_cancel = True

                if array[numx, numy] in white_values and castle_cancel == False:
                    array[numx, numy] += 80

            elif self.player == "black": #black
                if array[numx, numy] == board:
                    array[numx, numy] = black_take_line
                if array[numx, numy] in white_values:
                    array[numx, numy] += 40
                #if array[numx, numy] in black_values:
                #    array[numx, numy] += 80
                #if array[numx, numy] == white_castle_value:
                #    array[numx, numy] = white_check
                castle_cancel = False
                if self.type == 5:
                    if self.first_turn == True:
                        if array[numx, numy] in black_values:
                            for piece in listall:
                                if piece.type == 1:
                                    if piece.x == numx and piece.y == numy:
                                        if piece.first_turn == True:
                                            array[numx, numy] += 200
                                            castle_cancel = True
                if array[numx, numy] in black_values and castle_cancel == False:
                    array[numx, numy] += 80

    def move(self):
        move_list = []
        take_list = []
        if self.type == 1: #king
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    if not (a == 0 and b == 0):
                        numx = self.x + a
                        numy = self.y + b
                        self.fill_move(numx, numy)
        #    print(f"\n\nKING POSSIBLE MOVES:\n{array}")

        if self.type == 2: #queen:
            self.move_updown()
            self.move_diagonal()
        #    print(f"\n\nQUEEN POSSIBLE MOVES:\n{array}")

        if self.type == 3: #bishop
            self.move_diagonal()
        #    print(f"\n\nBISHOP POSSIBLE MOVES:\n{array}")

        if self.type == 4: #knight:
            for a in [-2, -1, 1, 2]:
                if abs(a) == 1:
                    for b in [2, -2]:
                        self.fill_move(self.x + a, self.y + b)
                if abs(a) == 2:
                    for b in [1, -1]:
                        self.fill_move(self.x + a, self.y + b)
        #    print(f"\n\nKNIGHT POSSIBLE MOVES:\n{array}")

        if self.type == 5: #castle
            self.move_updown()
        #    print(f"\n\nCASTLE POSSIBLE MOVES:\n{array}")

        if self.type == 6: #pawn:
            second = False
            if self.player == "white": #white
                if self.x - 1 >= 0 and self.x - 1 <= 7: #taking possibility
                    if self.y - 1 >= 0 and self.y - 1 <= 7:
                        if array[self.x - 1, self.y - 1] == board:
                            array[self.x - 1, self.y - 1] = white_take_only
                        elif array[self.x - 1, self.y - 1] in black_values:
                            array[self.x - 1, self.y - 1] += 40
                        elif array[self.x - 1, self.y - 1] in white_values:
                            array[self.x - 1, self.y - 1] += 80
                    if self.y + 1 >= 0 and self.y + 1 <= 7:
                        if array[self.x - 1, self.y + 1] == board:
                            array[self.x - 1, self.y + 1] = white_take_only
                        elif array[self.x - 1, self.y + 1] in black_values:
                            array[self.x - 1, self.y + 1] += 40
                        elif array[self.x - 1, self.y + 1] in white_values:
                            array[self.x - 1, self.y + 1] += 80
                if self.x == 6:
                    numx = self.x - 1
                    if array[numx, self.y] == board:
                        array[numx, self.y] = white_move_only
                        second = True
                    if second == True:
                        numx = self.x - 2
                        if array[numx, self.y] == board:
                            array[numx, self.y] = white_move_only
                if self.x != 6:
                    numx = self.x - 1
                    if self.x - 1 >= 0 and self.x - 1 <= 7:
                        if array[numx, self.y] == board:
                            array[numx, self.y] = white_move_only
            #    print(f"\n\nPAWN white POSSIBLE MOVES:\n{array}")
            if self.player == "black": #black:
                if self.x + 1 >= 0 and self.x + 1 <= 7:
                    if self.y - 1 >= 0 and self.y - 1 <= 7:
                        if array[self.x + 1, self.y - 1] == board:
                            array[self.x + 1, self.y - 1] = black_take_only
                        elif array[self.x + 1, self.y - 1] in white_values:
                            array[self.x + 1, self.y - 1] += 40
                        elif array[self.x + 1, self.y - 1] in black_values:
                            array[self.x + 1, self.y - 1] += 80

                    if self.y + 1 >= 0 and self.y + 1 <= 7:
                        if array[self.x + 1, self.y + 1] == board:
                            array[self.x + 1, self.y + 1] = black_take_only
                        elif array[self.x + 1, self.y + 1] in white_values:
                            array[self.x + 1, self.y + 1] += 40
                        elif array[self.x + 1, self.y + 1] in black_values:
                            array[self.x + 1, self.y + 1] += 80

                if self.x == 1:
                    numx = self.x + 1
                    if array[numx, self.y] == board:
                        array[numx, self.y] = black_move_only
                        second = True
                    if second == True:
                        numx = self.x + 2
                        if array[numx, self.y] == board:
                            array[numx, self.y] = black_move_only
                if self.x != 1:
                    numx = self.x + 1
                    if self.x + 1 >= 0 and self.x + 1 <= 7:
                        if array[numx, self.y] == board:
                            array[numx, self.y] = black_move_only
            #    print(f"\n\nPAWN black POSSIBLE MOVES:\n{array}")

    def reset(self):
        if self.value == 11:
            self.first_turn = True
            self.x = 7
            self.y = 4
        if self.value == 12:
            self.first_turn = True
            self.x = 7
            self.y = 3
        if self.value == 13:
            self.first_turn = True
            self.x = 7
            self.y = 0
        if self.value == 14:
            self.first_turn = True
            self.x = 7
            self.y = 7
        if self.value == 15:
            self.first_turn = True
            self.x = 7
            self.y = 2
        if self.value == 16:
            self.first_turn = True
            self.x = 7
            self.y = 5
        if self.value == 17:
            self.first_turn = True
            self.x = 7
            self.y = 1
        if self.value == 18:
            self.first_turn = True
            self.x = 7
            self.y = 6
        if self.value == 19:
            self.first_turn = True
            self.type = 6
            self.x = 6
            self.y = 0
        if self.value == 20:
            self.first_turn = True
            self.type = 6
            self.x = 6
            self.y = 1
        if self.value == 21:
            self.first_turn = True
            self.type = 6
            self.x = 6
            self.y = 2
        if self.value == 22:
            self.first_turn = True
            self.type = 6
            self.x = 6
            self.y = 3
        if self.value == 23:
            self.first_turn = True
            self.type = 6
            self.x = 6
            self.y = 4
        if self.value == 24:
            self.first_turn = True
            self.type = 6
            self.x = 6
            self.y = 5
        if self.value == 25:
            self.first_turn = True
            self.type = 6
            self.x = 6
            self.y = 6
        if self.value == 26:
            self.first_turn = True
            self.type = 6
            self.x = 6
            self.y = 7
        if self.value == 31:
            self.first_turn = True
            self.x = 0
            self.y = 4
        if self.value == 32:
            self.first_turn = True
            self.x = 0
            self.y = 3
        if self.value == 33:
            self.first_turn = True
            self.x = 0
            self.y = 0
        if self.value == 34:
            self.first_turn = True
            self.x = 0
            self.y = 7
        if self.value == 35:
            self.first_turn = True
            self.x = 0
            self.y = 2
        if self.value == 36:
            self.first_turn = True
            self.x = 0
            self.y = 5
        if self.value == 37:
            self.first_turn = True
            self.x = 0
            self.y = 1
        if self.value == 38:
            self.first_turn = True
            self.x = 0
            self.y = 6
        if self.value == 39:
            self.first_turn = True
            self.type = 6
            self.x = 1
            self.y = 0
        if self.value == 40:
            self.first_turn = True
            self.type = 6
            self.x = 1
            self.y = 1
        if self.value == 41:
            self.first_turn = True
            self.type = 6
            self.x = 1
            self.y = 2
        if self.value == 42:
            self.first_turn = True
            self.type = 6
            self.x = 1
            self.y = 3
        if self.value == 43:
            self.first_turn = True
            self.type = 6
            self.x = 1
            self.y = 4
        if self.value == 44:
            self.first_turn = True
            self.type = 6
            self.x = 1
            self.y = 5
        if self.value == 45:
            self.first_turn = True
            self.type = 6
            self.x = 1
            self.y = 6
        if self.value == 46:
            self.first_turn = True
            self.type = 6
            self.x = 1
            self.y = 7




# ----- STARTING POSITIONS ----- #
# these cannot be inside their own class - they are instances of the class.

#coordinate values need to be unique letters which can be changed.

kingw = piece(7, 4, 1, "white", white_values[0], True, 9.8, "white king")

queenw = piece(7, 3, 2, "white", white_values[1], True, 9, "white queen")

bishop1w = piece(7, 2, 3, "white", white_values[4], True, 3, "white bishop 1")
bishop2w = piece(7, 5, 3, "white", white_values[5], True, 3, "white bishop 2")

knight1w = piece(7, 1, 4, "white", white_values[6], True, 3, "white knight 1")
knight2w = piece(7, 6, 4, "white", white_values[7], True, 3, "white knight 2")

castle1w = piece(7, 0, 5, "white", white_values[2], True, 5, "white castle 1")
castle2w = piece(7, 7, 5, "white", white_values[3], True, 5, "white castle 2")

pawn1w = piece(6, 0, 6, "white", white_values[8], True, 1, "white pawn 1")
pawn2w = piece(6, 1, 6, "white", white_values[9], True, 1, "white pawn 2")
pawn3w = piece(6, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
pawn4w = piece(6, 3, 6, "white", white_values[11], True, 1, "white pawn 4")
pawn5w = piece(6, 4, 6, "white", white_values[12], True, 1, "white pawn 5")
pawn6w = piece(6, 5, 6, "white", white_values[13], True, 1, "white pawn 6")
pawn7w = piece(6, 6, 6, "white", white_values[14], True, 1, "white pawn 7")
pawn8w = piece(6, 7, 6, "white", white_values[15], True, 1, "white pawn 8")


kingb = piece(0, 4, 1, "black", black_values[0], True, 9.8, "black king")

queenb = piece(0, 3, 2, "black", black_values[1], True, 9, "black queen")


bishop1b = piece(0, 2, 3, "black", black_values[4], True, 3, "black bishop 1")
bishop2b = piece(0, 5, 3, "black", black_values[5], True, 3, "black bishop 2")

knight1b = piece(0, 1, 4, "black", black_values[6], True, 3, "black knight 1")
knight2b = piece(0, 6, 4, "black", black_values[7], True, 3, "black knight 2")

castle1b = piece(0, 0, 5, "black", black_values[2], True, 5, "black castle 1")
castle2b = piece(0, 7, 5, "black", black_values[3], True, 5, "black castle 2")

pawn1b = piece(1, 0, 6, "black", black_values[8], True, 1, "black pawn 1")
pawn2b = piece(1, 1, 6, "black", black_values[9], True, 1, "black pawn 2")
pawn3b = piece(1, 2, 6, "black", black_values[10], True, 1, "black pawn 3")
pawn4b = piece(1, 3, 6, "black", black_values[11], True, 1, "black pawn 4")
pawn5b = piece(1, 4, 6, "black", black_values[12], True, 1, "black pawn 5")
pawn6b = piece(1, 5, 6, "black", black_values[13], True, 1, "black pawn 6")
pawn7b = piece(1, 6, 6, "black", black_values[14], True, 1, "black pawn 7")
pawn8b = piece(1, 7, 6, "black", black_values[15], True, 1, "black pawn 8")

dummy_piece = piece(None, None, None, None, None, None, None, None)


array = numpy.full((8, 8), board)


listall = [kingw, queenw, bishop1w, bishop2w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn6w, pawn7w, pawn8w,
kingb, queenb, bishop1b, bishop2b, knight1b, knight2b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn5b, pawn6b, pawn7b, pawn8b]

whitelist = [kingw, queenw, bishop1w, bishop2w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn6w, pawn7w, pawn8w]

blacklist = [kingb, queenb, bishop1b, bishop2b, knight1b, knight2b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn5b, pawn6b, pawn7b, pawn8b]



# ---- TEST LISTS ----- #

# black in checkmate:
#castle2w = piece(1, 7, 5, "white", white_values[3], True, 5, "white castle 2")
#queenb = piece(7, 3, 2, "black", black_values[1], True, 9, "black queen")
#pawn1w = piece(6, 3, 6, "white", white_values[8], True, 1, "white pawn 1")
#whitelist = [castle1w, castle2w, pawn1w]
#blacklist = [kingb, queenb]
#listall = [kingb, castle1w, castle2w, queenb, pawn1w]

# white in checkmate:
#castle1b = piece(6, 0, 5, "black", black_values[2], True, 5, "black castle 1")
#whitelist = [kingw]
#blacklist = [castle1b, castle2b]
#listall = [kingw, castle1b, castle2b]

# black castling:
#whitelist = [castle1w]
#blacklist = [kingb, castle2b, pawn8b]
#listall = [castle1w, kingb, castle2b, pawn8b]

# white castling:
#whitelist = [kingw, castle2w, pawn8w]
#blacklist = [kingb]
#listall = [kingw, castle2w, pawn8w, kingb]

# checkmate messup
#kingw = piece(6, 7, 1, "white", white_values[0], True, 9.8, "white king")
#pawn1w = piece(5, 2, 6, "white", white_values[8], True, 1, "white pawn")
#whitelist = [kingw, pawn1w]
#queen2b = piece(4, 4, 2, "black", black_values[4], True, 9, "black queen")
#queenb = piece(5, 4, 2, "black", black_values[1], True, 9, "black queen")
#blacklist = [queenb, queen2b]
#listall = [kingw, pawn1w, queenb, queen2b]

# new list
#whitelist = [kingw, pawn5w, pawn6w]
#blacklist = [kingb, pawn5b, pawn6b]
#listall = [kingw, pawn5w, pawn6w, kingb, pawn5b, pawn6b]

# train list
#bishop1w = piece(7, 7, 3, "white", white_values[4], True, 3, "white bishop 1")
#pawn1b = piece(3, 3, 6, "black", black_values[8], True, 1, "black pawn 1")
#pawn1w = piece(5, 4, 6, "white", white_values[8], True, 1, "white pawn 1")
#bishop1b = piece(0, 0, 3, "black", black_values[4], True, 3, "black bishop")
#whitelist = [bishop1w, pawn1w]
#blacklist = [pawn1b, bishop1b]
#listall = [bishop1w, pawn1w, pawn1b, bishop1b]

# train list 2
#bishop1b = piece(1, 4, 3, "black", black_values[4], True, 3, "black bishop")
#queenb = piece(0, 3, 2, "black", black_values[1], True, 9, "black queen")
#pawn1w = piece(4, 7, 6, "white", white_values[8], True, 1, "white pawn 1")
#knight1w = piece(5, 5, 4, "white", white_values[6], True, 3, "white knight 1")
#pawn2w = piece(6, 1, 6, "white", white_values[9], True, 1, "white pawn 2")
#pawn3w = piece(6, 4, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn4w = piece(6, 3, 6, "white", white_values[11], True, 1, "white pawn 4")
#whitelist = [pawn1w, pawn3w, pawn4w, knight1w]
#blacklist = [queenb, bishop1b]
#listall = [pawn1w, pawn3w, pawn4w, knight1w, queenb, bishop1b]

# WEIRD EXAMPLE
#kingw = piece(7, 4, 1, "white", white_values[0], True, 9.8, "white king")
#queenw = piece(7, 3, 2, "white", white_values[1], True, 9, "white queen")
#bishop1w = piece(7, 2, 3, "white", white_values[4], True, 3, "white bishop 1")
#bishop2w = piece(7, 5, 3, "white", white_values[5], True, 3, "white bishop 2")
#knight1w = piece(7, 1, 4, "white", white_values[6], True, 3, "white knight 1")
#knight2w = piece(5, 5, 4, "white", white_values[7], True, 3, "white knight 2")
#castle1w = piece(7, 0, 5, "white", white_values[2], True, 5, "white castle 1")
#castle2w = piece(7, 7, 5, "white", white_values[3], True, 5, "white castle 2")
#pawn1w = piece(6, 0, 6, "white", white_values[8], True, 1, "white pawn 1")
#pawn2w = piece(6, 1, 6, "white", white_values[9], True, 1, "white pawn 2")
#pawn3w = piece(5, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn4w = piece(6, 3, 6, "white", white_values[11], True, 1, "white pawn 4")
#pawn5w = piece(6, 4, 6, "white", white_values[12], True, 1, "white pawn 5")
#pawn6w = piece(6, 5, 6, "white", white_values[13], True, 1, "white pawn 6")
#pawn7w = piece(6, 6, 6, "white", white_values[14], True, 1, "white pawn 7")
#pawn8w = piece(4, 7, 6, "white", white_values[15], True, 1, "white pawn 8")
#kingb = piece(0, 4, 1, "black", black_values[0], True, 9.8, "black king")
#queenb = piece(0, 3, 2, "black", black_values[1], True, 9, "black queen")
#bishop1b = piece(4, 6, 3, "black", black_values[4], True, 3, "black bishop 1")
#bishop2b = piece(0, 5, 3, "black", black_values[5], True, 3, "black bishop 2")
#knight1b = piece(0, 1, 4, "black", black_values[6], True, 3, "black knight 1")
#knight2b = piece(0, 6, 4, "black", black_values[7], True, 3, "black knight 2")
#castle1b = piece(0, 0, 5, "black", black_values[2], True, 5, "black castle 1")
#castle2b = piece(0, 7, 5, "black", black_values[3], True, 5, "black castle 2")
#pawn1b = piece(1, 0, 6, "black", black_values[8], True, 1, "black pawn 1")
#pawn2b = piece(1, 1, 6, "black", black_values[9], True, 1, "black pawn 2")
#pawn3b = piece(1, 2, 6, "black", black_values[10], True, 1, "black pawn 3")
#pawn4b = piece(3, 3, 6, "black", black_values[11], True, 1, "black pawn 4")
#pawn5b = piece(3, 4, 6, "black", black_values[12], True, 1, "black pawn 5")
#pawn6b = piece(1, 5, 6, "black", black_values[13], True, 1, "black pawn 6")
#pawn7b = piece(1, 6, 6, "black", black_values[14], True, 1, "black pawn 7")
#pawn8b = piece(1, 7, 6, "black", black_values[15], True, 1, "black pawn 8")
#listall = [kingw, queenw, bishop1w, bishop2w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn6w, pawn7w, pawn8w,
#kingb, queenb, bishop1b, bishop2b, knight1b, knight2b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn5b, pawn6b, pawn7b, pawn8b]
#whitelist = [kingw, queenw, bishop1w, bishop2w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn6w, pawn7w, pawn8w]
#blacklist = [kingb, queenb, bishop1b, bishop2b, knight1b, knight2b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn5b, pawn6b, pawn7b, pawn8b]



# CHECK MATE messUP
#kingw = piece(7, 4, 1, "white", white_values[0], True, 9.8, "white king")
#queenw = piece(5, 5, 2, "white", white_values[1], True, 9, "white queen")
#bishop1w = piece(7, 2, 3, "white", white_values[4], True, 3, "white bishop 1")
#bishop2w = piece(7, 5, 3, "white", white_values[5], True, 3, "white bishop 2")
#knight1w = piece(7, 1, 4, "white", white_values[6], True, 3, "white knight 1")
#knight2w = piece(3, 4, 4, "white", white_values[7], True, 3, "white knight 2")
#castle1w = piece(7, 0, 5, "white", white_values[2], True, 5, "white castle 1")
#castle2w = piece(7, 7, 5, "white", white_values[3], True, 5, "white castle 2")
#pawn1w = piece(6, 0, 6, "white", white_values[8], True, 1, "white pawn 1")
#pawn2w = piece(6, 1, 6, "white", white_values[9], True, 1, "white pawn 2")
#pawn3w = piece(4, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn4w = piece(6, 3, 6, "white", white_values[11], True, 1, "white pawn 4")
#pawn5w = piece(6, 4, 6, "white", white_values[12], True, 1, "white pawn 5")
#pawn6w = piece(6, 5, 6, "white", white_values[13], True, 1, "white pawn 6")
#pawn7w = piece(6, 6, 6, "white", white_values[14], True, 1, "white pawn 7")
#pawn8w = piece(4, 7, 6, "white", white_values[15], True, 1, "white pawn 8")
#kingb = piece(0, 4, 1, "black", black_values[0], True, 9.8, "black king")
#queenb = piece(0, 3, 2, "black", black_values[1], True, 9, "black queen")
#bishop1b = piece(0, 2, 3, "black", black_values[4], True, 3, "black bishop 1")
#bishop2b = piece(0, 5, 3, "black", black_values[5], True, 3, "black bishop 2")
#knight1b = piece(0, 1, 4, "black", black_values[6], True, 3, "black knight 1")
#knight2b = piece(0, 6, 4, "black", black_values[7], True, 3, "black knight 2")
#castle1b = piece(0, 0, 5, "black", black_values[2], True, 5, "black castle 1")
#castle2b = piece(0, 7, 5, "black", black_values[3], True, 5, "black castle 2")
#pawn1b = piece(1, 0, 6, "black", black_values[8], True, 1, "black pawn 1")
#pawn2b = piece(2, 1, 6, "black", black_values[9], True, 1, "black pawn 2")
#pawn3b = piece(2, 2, 6, "black", black_values[10], True, 1, "black pawn 3")
#pawn4b = piece(3, 3, 6, "black", black_values[11], True, 1, "black pawn 4")
#pawn5b = piece(None, None, 6, "black", black_values[12], True, 1, "black pawn 5")
#pawn6b = piece(1, 5, 6, "black", black_values[13], True, 1, "black pawn 6")
#pawn7b = piece(1, 6, 6, "black", black_values[14], True, 1, "black pawn 7")
#pawn8b = piece(1, 7, 6, "black", black_values[15], True, 1, "black pawn 8")
#dummy_piece = piece(None, None, None, None, None, None, None, None)
#listall = [kingw, queenw, bishop1w, bishop2w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn6w, pawn7w, pawn8w,
#kingb, queenb, bishop1b, bishop2b, knight1b, knight2b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn5b, pawn6b, pawn7b, pawn8b]
#whitelist = [kingw, queenw, bishop1w, bishop2w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn6w, pawn7w, pawn8w]
#blacklist = [kingb, queenb, bishop1b, bishop2b, knight1b, knight2b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn5b, pawn6b, pawn7b, pawn8b]


# CHECK MATE MESS UP #2
#kingw = piece(5, 7, 1, "white", white_values[0], True, 9.8, "white king")
#queenw = piece(5, 6, 2, "white", white_values[1], True, 9, "white queen")
#pawn7w = piece(1, 6, 2, "white", white_values[14], True, 1, "white pawn 7")
#knight1w = piece(2, 5, 4, "white", white_values[6], True, 3, "white knight 1")
#pawn1w = piece(1, 0, 6, "white", white_values[8], True, 1, "white pawn 1")
#pawn2w = piece(3, 1, 6, "white", white_values[9], True, 1, "white pawn 2")
#pawn3w = piece(3, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn8w = piece(2, 6, 6, "white", white_values[15], True, 1, "white pawn 8")
#castle1w = piece(1, 3, 5, "white", white_values[2], True, 5, "white castle 1")
#castle2w = piece(7, 4, 5, "white", white_values[3], True, 5, "white castle 2")
#kingb = piece(2, 4, 1, "black", black_values[0], True, 9.8, "black king")
#knight1b = piece(3, 4, 4, "black", black_values[6], True, 3, "black knight 1")
#queenb = piece(2, 6, 2, "black", black_values[1], True, 9, "black queen")
#whitelist = [pawn1w, pawn2w, pawn3w, pawn7w, pawn8w, castle1w, castle2w, kingw, queenw, knight1w]
#blacklist = [kingb, queenb, knight1b]
#listall = [pawn1w, pawn2w, pawn3w, pawn7w, pawn8w, castle1w, castle2w, kingw, queenw, knight1w, kingb, knight1b]


# CHECK MATE IN 2 MOVES:
#kingw = piece(7, 7, 1, "white", white_values[0], True, 9.8, "white king")
#bishop1w = piece(6, 2, 3, "white", white_values[4], True, 3, "white bishop 1")
#knight1w = piece(3, 6, 4, "white", white_values[6], True, 3, "white knight 1")
#knight2w = piece(4, 6, 4, "white", white_values[7], True, 3, "white knight 2")
#castle1w = piece(1, 7, 5, "white", white_values[2], True, 5, "white castle 1")
#pawn1w = piece(6, 0, 6, "white", white_values[8], True, 1, "white pawn 1")
#pawn2w = piece(6, 1, 6, "white", white_values[9], True, 1, "white pawn 2")
#pawn3w = piece(5, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn4w = piece(4, 3, 6, "white", white_values[11], True, 1, "white pawn 4")
#pawn5w = piece(3, 4, 6, "white", white_values[12], True, 1, "white pawn 5")
#pawn8w = piece(6, 7, 6, "white", white_values[15], True, 1, "white pawn 8")
#kingb = piece(0, 6, 1, "black", black_values[0], True, 9.8, "black king")
#bishop1b = piece(0, 4, 3, "black", black_values[4], True, 3, "black bishop 1")
#knight1b = piece(2, 0, 4, "black", black_values[6], True, 3, "black knight 1")
#knight2b = piece(1, 3, 4, "black", black_values[7], True, 3, "black knight 2")
#castle1b = piece(4, 5, 5, "black", black_values[2], True, 5, "black castle 1")
#pawn1b = piece(3, 0, 6, "black", black_values[8], True, 1, "black pawn 1")
#pawn2b = piece(3, 1, 6, "black", black_values[9], True, 1, "black pawn 2")
#pawn3b = piece(4, 2, 6, "black", black_values[10], True, 1, "black pawn 3")
#pawn4b = piece(3, 3, 6, "black", black_values[11], True, 1, "black pawn 4")
#pawn5b = piece(2, 2, 6, "black", black_values[12], True, 1, "black pawn 5")
#pawn7b = piece(2, 6, 6, "black", black_values[14], True, 1, "black pawn 7")
#listall = [kingw, bishop1w, knight1w, knight2w, castle1w, pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn8w,
#kingb, bishop1b, knight1b, knight2b, castle1b, pawn1b, pawn2b, pawn3b, pawn4b, pawn5b, pawn7b]
#whitelist = [kingw, bishop1w, knight1w, knight2w, castle1w,  pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn8w]
#blacklist = [kingb, bishop1b, knight1b, knight2b, castle1b, pawn1b, pawn2b, pawn3b, pawn4b, pawn5b, pawn7b]


# CHECKMATE IN 2 MOVES:
#kingw = piece(6, 3, 1, "white", white_values[0], True, 9.8, "white king")
#queenw = piece(5, 7, 2, "white", white_values[1], True, 9, "white queen")
#castle1w = piece(5, 3, 5, "white", white_values[2], True, 5, "white castle 1")
#castle2w = piece(6, 6, 5, "white", white_values[3], True, 5, "white castle 2")
#pawn3w = piece(6, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn5w = piece(3, 4, 6, "white", white_values[12], True, 1, "white pawn 5")
#pawn6w = piece(4, 5, 6, "white", white_values[13], True, 1, "white pawn 6")
#pawn8w = piece(6, 7, 6, "white", white_values[15], True, 1, "white pawn 8")
#kingb = piece(0, 7, 1, "black", black_values[0], True, 9.8, "black king")
#queenb = piece(0, 3, 2, "black", black_values[1], True, 9, "black queen")
#castle1b = piece(0, 0, 5, "black", black_values[2], True, 5, "black castle 1")
#castle2b = piece(0, 5, 5, "black", black_values[3], True, 5, "black castle 2")
#pawn1b = piece(4, 0, 6, "black", black_values[8], True, 1, "black pawn 1")
#pawn4b = piece(3, 3, 6, "black", black_values[11], True, 1, "black pawn 4")
#pawn5b = piece(2, 4, 6, "black", black_values[12], True, 1, "black pawn 5")
#pawn6b = piece(2, 5, 6, "black", black_values[13], True, 1, "black pawn 6")
#pawn8b = piece(1, 7, 6, "black", black_values[15], True, 1, "black pawn 8")
#whitelist = [kingw, queenw, castle1w, castle2w, pawn3w, pawn5w, pawn6w, pawn8w]
#blacklist = [kingb, queenb, castle1b, castle2b, pawn1b, pawn4b, pawn5b, pawn6b, pawn8b]
#listall = [kingw, queenw, castle1w, castle2w, pawn3w, pawn5w, pawn6w, pawn8w, kingb, queenb, castle1b, castle2b, pawn1b, pawn4b, pawn5b, pawn6b, pawn8b]


# CHECKMATE IN 3 MOVES:
#kingw = piece(7, 6, 1, "white", white_values[0], True, 9.8, "white king")
#queenw = piece(2, 7, 2, "white", white_values[1], True, 9, "white queen")
#castle1w = piece(7, 5, 5, "white", white_values[2], True, 5, "white castle 1")
#castle2w = piece(5, 5, 5, "white", white_values[3], True, 5, "white castle 2")
#pawn1w = piece(6, 0, 6, "white", white_values[8], True, 1, "white pawn 1")
#pawn2w = piece(6, 1, 6, "white", white_values[9], True, 1, "white pawn 2")
#pawn3w = piece(6, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn4w = piece(4, 3, 6, "white", white_values[11], True, 1, "white pawn 4")
#pawn5w = piece(4, 4, 6, "white", white_values[12], True, 1, "white pawn 5")
#pawn7w = piece(6, 6, 6, "white", white_values[14], True, 1, "white pawn 7")
#kingb = piece(0, 6, 1, "black", black_values[0], True, 9.8, "black king")
#queenb = piece(0, 4, 2, "black", black_values[1], True, 9, "black queen")
#castle1b = piece(0, 0, 5, "black", black_values[2], True, 5, "black castle 1")
#castle2b = piece(0, 7, 5, "black", black_values[3], True, 5, "black castle 2")
#pawn1b = piece(1, 0, 6, "black", black_values[8], True, 1, "black pawn 1")
#pawn2b = piece(1, 1, 6, "black", black_values[9], True, 1, "black pawn 2")
#pawn3b = piece(1, 2, 6, "black", black_values[10], True, 1, "black pawn 3")
#pawn4b = piece(2, 3, 6, "black", black_values[11], True, 1, "black pawn 4")
#pawn7b = piece(2, 6, 6, "black", black_values[14], True, 1, "black pawn 7")
#whitelist = [kingw, queenw, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn7w]
#blacklist = [kingb, queenb, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn7b]
#listall = [kingw, queenw, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn7w, kingb, queenb, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn7b]



# CHECKMATE IN 3 MOVES #2
#kingw = piece(7, 6, 1, "white", white_values[0], True, 9.8, "white king")
#castle1w = piece(1, 1, 5, "white", white_values[2], True, 5, "white castle 1")
#bishop1w = piece(4, 3, 3, "white", white_values[4], True, 3, "white bishop 1")
#pawn1w = piece(5, 0, 6, "white", white_values[8], True, 1, "white pawn 1")
#pawn2w = piece(4, 1, 6, "white", white_values[9], True, 1, "white pawn 2")
#pawn3w = piece(2, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn6w = piece(3, 5, 6, "white", white_values[13], True, 1, "white pawn 6")
#pawn7w = piece(6, 6, 6, "white", white_values[14], True, 1, "white pawn 7")
#pawn8w = piece(5, 7, 6, "white", white_values[15], True, 1, "white pawn 8")
#kingb = piece(0, 3, 1, "black", black_values[0], True, 9.8, "black king")
#castle1b = piece(2, 0, 5, "black", black_values[2], True, 5, "black castle 1")
#knight1b = piece(1, 2, 4, "black", black_values[6], True, 3, "black knight 1")
#pawn1b = piece(3, 0, 6, "black", black_values[8], True, 1, "black pawn 1")
#pawn2b = piece(3, 1, 6, "black", black_values[9], True, 1, "black pawn 2")
#pawn6b = piece(2, 5, 6, "black", black_values[13], True, 1, "black pawn 6")
#pawn7b = piece(1, 6, 6, "black", black_values[14], True, 1, "black pawn 7")
#pawn8b = piece(1, 7, 6, "black", black_values[15], True, 1, "black pawn 8")
#whitelist = [kingw, castle1w, bishop1w, pawn1w, pawn2w, pawn3w, pawn6w, pawn7w, pawn8w]
#blacklist = [kingb, castle1b, knight1b, pawn1b, pawn2b, pawn6b, pawn7b, pawn8b]
#listall = [kingw, castle1w, bishop1w, pawn1w, pawn2w, pawn3w, pawn6w, pawn7w, pawn8w, kingb, castle1b, knight1b, pawn1b, pawn2b, pawn6b, pawn7b, pawn8b]



# CHECK MATE IN 3 MOVES
#kingw = piece(7, 4, 1, "white", white_values[0], True, 9.8, "white king")
#queenw = piece(4, 5, 2, "white", white_values[1], True, 9, "white queen")
#bishop1w = piece(6, 3, 3, "white", white_values[4], True, 3, "white bishop 1")
#bishop2w = piece(7, 5, 3, "white", white_values[5], True, 3, "white bishop 2")
#knight1w = piece(2, 3, 4, "white", white_values[6], True, 3, "white knight 1")
#knight2w = piece(7, 6, 4, "white", white_values[7], True, 3, "white knight 2")
#castle1w = piece(7, 0, 5, "white", white_values[2], True, 5, "white castle 1")
#castle2w = piece(7, 7, 5, "white", white_values[3], True, 5, "white castle 2")
#pawn1w = piece(6, 0, 6, "white", white_values[8], True, 1, "white pawn 1")
#pawn2w = piece(4, 1, 6, "white", white_values[9], True, 1, "white pawn 2")
#pawn3w = piece(6, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn5w = piece(2, 5, 6, "white", white_values[12], True, 1, "white pawn 5")
#pawn6w = piece(6, 5, 6, "white", white_values[13], True, 1, "white pawn 6")
#pawn7w = piece(6, 6, 6, "white", white_values[14], True, 1, "white pawn 7")
#pawn8w = piece(6, 7, 6, "white", white_values[15], True, 1, "white pawn 8")
#kingb = piece(0, 5, 1, "black", black_values[0], True, 9.8, "black king")
#queenb = piece(0, 3, 2, "black", black_values[1], True, 9, "black queen")
#bishop1b = piece(0, 2, 3, "black", black_values[4], True, 3, "black bishop 1")
#bishop2b = piece(1, 2, 3, "black", black_values[5], True, 3, "black bishop 2")
#knight1b = piece(0, 1, 4, "black", black_values[6], True, 3, "black knight 1")
#knight2b = piece(0, 6, 4, "black", black_values[7], True, 3, "black knight 2")
#castle1b = piece(0, 0, 5, "black", black_values[2], True, 5, "black castle 1")
#castle2b = piece(0, 7, 5, "black", black_values[3], True, 5, "black castle 2")
#pawn1b = piece(1, 0, 6, "black", black_values[8], True, 1, "black pawn 1")
#pawn2b = piece(1, 1, 6, "black", black_values[9], True, 1, "black pawn 2")
#pawn3b = piece(3, 3, 6, "black", black_values[10], True, 1, "black pawn 3")
#pawn4b = piece(4, 3, 6, "black", black_values[11], True, 1, "black pawn 4")
#pawn5b = piece(2, 4, 6, "black", black_values[12], True, 1, "black pawn 5")
#pawn7b = piece(2, 6, 6, "black", black_values[14], True, 1, "black pawn 7")
#pawn8b = piece(1, 7, 6, "black", black_values[15], True, 1, "black pawn 8")
#listall = [kingw, queenw, bishop1w, bishop2w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn5w, pawn6w, pawn7w, pawn8w,
#kingb, queenb, bishop1b, bishop2b, knight1b, knight2b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn5b, pawn7b, pawn8b]
#whitelist = [kingw, queenw, bishop1w, bishop2w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn5w, pawn6w, pawn7w, pawn8w]
#blacklist = [kingb, queenb, bishop1b, bishop2b, knight1b, knight2b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn5b, pawn7b, pawn8b]


# OFFENSIVE MESSUP
#kingw = piece(7, 4, 1, "white", white_values[0], True, 9.8, "white king")
#queenw = piece(5, 7, 2, "white", white_values[1], True, 9, "white queen")
#bishop1w = piece(6, 1, 3, "white", white_values[4], False, 3, "white bishop 1")
#knight1w = piece(7, 1, 4, "white", white_values[6], True, 3, "white knight 1")
#knight2w = piece(5, 6, 4, "white", white_values[7], True, 3, "white knight 2")
#castle1w = piece(7, 0, 5, "white", white_values[2], True, 5, "white castle 1")
#castle2w = piece(7, 7, 5, "white", white_values[3], True, 5, "white castle 2")
#pawn1w = piece(5, 0, 6, "white", white_values[8], True, 1, "white pawn 1")
#pawn2w = piece(3, 1, 6, "white", white_values[9], False, 1, "white pawn 2")
#pawn3w = piece(6, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn4w = piece(4, 3, 6, "white", white_values[11], True, 1, "white pawn 4")
#pawn5w = piece(5, 4, 6, "white", white_values[12], True, 1, "white pawn 5")
#pawn8w = piece(4, 7, 6, "white", white_values[15], True, 1, "white pawn 8")
#kingb = piece(0, 6, 1, "black", black_values[0], True, 9.8, "black king")
#queenb = piece(1, 7, 2, "black", black_values[1], True, 9, "black queen")
#bishop1b = piece(2, 3, 3, "black", black_values[4], False, 3, "black bishop 1")
#knight1b = piece(3, 2, 4, "black", black_values[6], True, 3, "black knight 1")
#castle1b = piece(0, 0, 5, "black", black_values[2], True, 5, "black castle 1")
#castle2b = piece(0, 5, 5, "black", black_values[3], True, 5, "black castle 2")
#pawn1b = piece(1, 0, 6, "black", black_values[8], True, 1, "black pawn 1")
#pawn2b = piece(2, 1, 6, "black", black_values[9], True, 1, "black pawn 2")
#pawn3b = piece(1, 2, 6, "black", black_values[10], True, 1, "black pawn 3")
#pawn4b = piece(3, 3, 6, "black", black_values[11], False, 1, "black pawn 4")
#pawn7b = piece(1, 6, 6, "black", black_values[14], True, 1, "black pawn 7")
#pawn8b = piece(2, 7, 6, "black", black_values[15], True, 1, "black pawn 8")
#listall = [kingw, queenw, bishop1w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn8w,
#kingb, queenb, bishop1b, knight1b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn7b, pawn8b]
#whitelist = [kingw, queenw, bishop1w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn4w, pawn5w, pawn8w]
#blacklist = [kingb, queenb, bishop1b, knight1b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn7b, pawn8b]




# SPECIFIC DEFENSIVE RANKING TEST
#kingw = piece(7, 4, 1, "white", white_values[0], True, 9.8, "white king")
#queenw = piece(5, 7, 2, "white", white_values[1], True, 9, "white queen")
#bishop1w = piece(4, 3, 3, "white", white_values[4], False, 3, "white bishop 1")
#knight1w = piece(7, 1, 4, "white", white_values[6], True, 3, "white knight 1")
#knight2w = piece(5, 6, 4, "white", white_values[7], True, 3, "white knight 2")
#castle1w = piece(7, 0, 5, "white", white_values[2], True, 5, "white castle 1")
#castle2w = piece(7, 6, 5, "white", white_values[3], True, 5, "white castle 2")
#pawn1w = piece(5, 0, 6, "white", white_values[8], True, 1, "white pawn 1")
#pawn2w = piece(3, 1, 6, "white", white_values[9], False, 1, "white pawn 2")
#pawn3w = piece(5, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn5w = piece(5, 4, 6, "white", white_values[12], True, 1, "white pawn 5")
#pawn8w = piece(4, 7, 6, "white", white_values[15], True, 1, "white pawn 8")
#kingb = piece(0, 6, 1, "black", black_values[0], True, 9.8, "black king")
#queenb = piece(2, 6, 2, "black", black_values[1], True, 9, "black queen")
#bishop1b = piece(3, 2, 3, "black", black_values[4], False, 3, "black bishop 1")
#castle1b = piece(4, 6, 5, "black", black_values[2], True, 5, "black castle 1")
#castle2b = piece(5, 5, 5, "black", black_values[3], True, 5, "black castle 2")
#pawn1b = piece(1, 0, 6, "black", black_values[8], True, 1, "black pawn 1")
#pawn2b = piece(2, 1, 6, "black", black_values[9], True, 1, "black pawn 2")
#pawn3b = piece(1, 2, 6, "black", black_values[10], True, 1, "black pawn 3")
#pawn4b = piece(3, 3, 6, "black", black_values[11], False, 1, "black pawn 4")
#pawn7b = piece(1, 6, 6, "black", black_values[14], True, 1, "black pawn 7")
#pawn8b = piece(2, 7, 6, "black", black_values[15], True, 1, "black pawn 8")
#listall = [kingw, queenw, bishop1w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn5w, pawn8w,
#kingb, queenb, bishop1b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn7b, pawn8b]
#whitelist = [kingw, queenw, bishop1w, knight1w, knight2w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn5w, pawn8w]
#blacklist = [kingb, queenb, bishop1b, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn7b, pawn8b]


# SPECIFIC DEFENSIVE RANKING TEST
#kingw = piece(7, 4, 1, "white", white_values[0], True, 9.8, "white king")
#queenw = piece(6, 7, 2, "white", white_values[1], True, 9, "white queen")
#knight1w = piece(7, 1, 4, "white", white_values[6], True, 3, "white knight 1")
#castle1w = piece(7, 0, 5, "white", white_values[2], True, 5, "white castle 1")
#castle2w = piece(6, 6, 5, "white", white_values[3], True, 5, "white castle 2")
#pawn1w = piece(4, 0, 6, "white", white_values[8], True, 1, "white pawn 1")
#pawn2w = piece(3, 1, 6, "white", white_values[9], False, 1, "white pawn 2")
#pawn3w = piece(5, 2, 6, "white", white_values[10], True, 1, "white pawn 3")
#pawn8w = piece(3, 7, 6, "white", white_values[15], True, 1, "white pawn 8")
#kingb = piece(0, 6, 1, "black", black_values[0], True, 9.8, "black king")
#queenb = piece(3, 6, 2, "black", black_values[1], True, 9, "black queen")
#castle1b = piece(4, 6, 5, "black", black_values[2], True, 5, "black castle 1")
#castle2b = piece(5, 6, 5, "black", black_values[3], True, 5, "black castle 2")
#pawn1b = piece(1, 0, 6, "black", black_values[8], True, 1, "black pawn 1")
#pawn2b = piece(2, 1, 6, "black", black_values[9], True, 1, "black pawn 2")
#pawn3b = piece(1, 2, 6, "black", black_values[10], True, 1, "black pawn 3")
#pawn4b = piece(3, 3, 6, "black", black_values[11], False, 1, "black pawn 4")
#pawn7b = piece(1, 6, 6, "black", black_values[14], True, 1, "black pawn 7")
#pawn8b = piece(2, 7, 6, "black", black_values[15], True, 1, "black pawn 8")
#listall = [kingw, queenw, knight1w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn8w,
#kingb, queenb, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn7b, pawn8b]
#whitelist = [kingw, queenw, knight1w, castle1w, castle2w, pawn1w, pawn2w, pawn3w, pawn8w]
#blacklist = [kingb, queenb, castle1b, castle2b, pawn1b, pawn2b, pawn3b, pawn4b, pawn7b, pawn8b]











# end of script
