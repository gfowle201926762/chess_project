from chess_piece import *
import random

player = None
class chessgame:
    def __init__(self, player):
        pass

    def clear(self):
        for a in range(0, 8):
            for b in range(0, 8):
                array[a, b] = board
        for piece in listall:
            if not piece.x == None:
                array[piece.x, piece.y] = piece.value
        #for a in range(0, 8):
        #    for b in range(0, 8):
        #        if array[a, b] == white_move_only or array[a, b] == white_take_line or array[a, b] == black_move_only or array[a, b] == black_take_line or array[a, b] == white_take_only or array[a, b] == black_take_only:
        #            array[a, b] = board
        #        elif array[a, b] in white_taken or array[a, b] in black_taken:
        #            array[a, b] -= 40
        #        elif array[a, b] in white_star or array[a, b] in black_star:
        #            array[a, b] -= 80

    def clear_white_mod(self):

        #for a in range(0, 8):
        #    for b in range(0, 8):
        #        array[a, b] = board

        #for mod_piece in listall:
        #    if mod_piece.x != None:
        #        array[mod_piece.x, mod_piece.y] = mod_piece.value

        #for num in range(0, int((len(taking_black_list) / 2))):
        #    array[taking_black_list[num * 2], taking_black_list[(num * 2) + 1]] += 40


        clear_mod_list = []
        for a in range(0, 8):
            for b in range(0, 8):
                if array[a, b] in black_taken:
                    clear_mod_list.append(a)
                    clear_mod_list.append(b)
                else:
                    array[a, b] = board

        for mod_piece in listall:
            if mod_piece.x != None:
                array[mod_piece.x, mod_piece.y] = mod_piece.value

        for num in range(0, int((len(clear_mod_list) / 2))):
            array[clear_mod_list[num * 2], clear_mod_list[(num * 2) + 1]] += 40




        #for a in range(0, 8):
        #    for b in range(0, 8):
        #        if array[a, b] == white_move_only or array[a, b] == white_take_line or array[a, b] == black_move_only or array[a, b] == black_take_line or array[a, b] == white_take_only or array[a, b] == black_take_only:
        #            array[a, b] = board
        #        elif array[a, b] in white_taken:
        #            array[a, b] -= 40
        #        elif array[a, b] in white_star or array[a, b] in black_star:
        #            array[a, b] -= 80

    def clear_black_mod(self):
        clear_mod_list = []
        for a in range(0, 8):
            for b in range(0, 8):
                if array[a, b] in white_taken:
                    clear_mod_list.append(a)
                    clear_mod_list.append(b)
                else:
                    array[a, b] = board

        for mod_piece in listall:
            if mod_piece.x != None:
                array[mod_piece.x, mod_piece.y] = mod_piece.value

        for num in range(0, int((len(clear_mod_list) / 2))):
            array[clear_mod_list[num * 2], clear_mod_list[(num * 2) + 1]] += 40




        #for a in range(0, 8):
        #    for b in range(0, 8):
        #        if array[a, b] == white_move_only or array[a, b] == white_take_line or array[a, b] == black_move_only or array[a, b] == black_take_line or array[a, b] == white_take_only or array[a, b] == black_take_only:
        #            array[a, b] = board
        #        elif array[a, b] in black_taken:
        #            array[a, b] -= 40
        #        elif array[a, b] in white_star or array[a, b] in black_star:
        #            array[a, b] -= 80

    def random(self, golist):
        if int(len(golist)) != 0:
            select = random.randint(0, ((int(len(golist) / 2)) - 1))
            return int(golist[select * 2]), int(golist[(select * 2) + 1])
        elif int(len(golist)) == 0:
            return None, None

    def random_2(self, total_go_list):
        if int(len(total_go_list)) != 0:
            select = random.randint(0, (int(len(total_go_list) / 3) - 1))
            return total_go_list[select * 3], total_go_list[(select * 3) + 1], total_go_list[(select * 3) + 2]
        elif int(len(total_go_list)) == 0:
            return "checkmate", "checkmate", "checkmate"

    def holistic_white_program(self, total_ranking_list):

        #print("hello?")
        ranking_list = []
        number_list = []
        for num in range(0, int(len(total_ranking_list) / 6)):
            ranking = total_ranking_list[num * 6]
            ranking_list.append(ranking)
            number_list.append(num)


        best_ranking = min(ranking_list)
        #print(f"best_ranking {best_ranking}")
        tie_list = []
        count = 0
        for num in ranking_list:
            #print(f"num {num}")
            if num == best_ranking:
                tie_list.append(count)
            count += 1

        tied_number_list = []
        for num in tie_list:
            tied_number_list.append(number_list[num])

        the_take = False
        the_offense = False

        take_record = []
        offense_record = []
        abort_record = []
        #print("ass")
        #print(f"tie_list {tie_list}")
        #print(f"tied_number_list {tied_number_list}")
        for num in tied_number_list: # we already know they have identical rankings. Just need to make the take happen.
            abort = False
            just_gone = False
            sim_take = total_ranking_list[(num * 6) + 4]
            offense = total_ranking_list[(num * 6) + 5]

            #print(f"sim_take: {sim_take}")
            if sim_take == True:
                the_take = True
                just_gone = True

            #print(f"offense: {offense}")
            if offense != False:
                the_offense = True
                if just_gone == True:
                    abort = True
                    abort_record.append(num)

            if abort == True:
                pass

            if abort == False and the_take == True:
                take_record.append(num)

            if abort == False and the_offense == True:
                offense_record.append(num)

        if int(len(take_record)) > 0:
            if int(len(offense_record)) > 0:
                for num in offense_record:
                    total_ranking_list[num * 6] += total_ranking_list[(num * 6) + 5]
                    name = total_ranking_list[(num * 6) + 1]


        return total_ranking_list



    def checkmate_check(self, player):
        p_legal = True
        legal_count = 0
        #print("\n")
        #print(moved_piece.name)

        if player == "WHITE":
            selflist = whitelist
            opponentlist = blacklist

            selfking = kingw
            opponentking = kingb

            selfcheck = white_check
            opponentcheck = black_check

            opponenttaken = black_taken
            selfmoveonly = white_move_only
            selftakeline = white_take_line
            selfcastlevalue = white_castle_value

            selftaken = white_taken
            opponentmoveonly = black_move_only
            opponenttakeonly = black_take_only
            opponenttakeline = black_take_line

        if player == "BLACK":
            selflist = blacklist
            opponentlist = whitelist

            selfking = kingb
            opponentking = kingw

            selfcheck = black_check
            opponentcheck = white_check

            opponenttaken = white_taken
            selfmoveonly = black_move_only
            selftakeline = black_take_line
            selfcastlevalue = black_castle_value

            selftaken = black_taken
            opponentmoveonly = white_move_only
            opponenttakeonly = white_take_only
            opponenttakeline = white_take_line


        for p_piece in selflist:
            if p_piece.x != None:
                self.clear()
                p_piece.move()
                #print(array)
                #print(f"kingb.x: {kingb.x}")
                #print(f"kingb.y: {kingb.y}")
                if array[opponentking.x, opponentking.y] == opponentcheck:
                    for defend_piece in opponentlist:
                        if defend_piece.x != None:
                            #legal_count = 0
                            p_xx = defend_piece.x
                            p_yy = defend_piece.y
                            p_revive_me = None

                            self.clear()
                            defend_piece.move()
                            # no need to determine castle values - cannot castle if in check anyway.
                            defend_move_list = []
                            for a in range(0, 8):
                                for b in range(0, 8):
                                    if array[a, b] in selftaken or array[a, b] == opponentmoveonly or array[a, b] == opponenttakeline:
                                        defend_move_list.append(a)
                                        defend_move_list.append(b)

                            if player == "WHITE":
                                self.clear_black_mod()

                            if player == "BLACK":
                                self.clear_white_mod()


                            p_count = 0
                            for num in range(0, int(len(defend_move_list) / 2)):

                                p_simulate_take = False
                                if array[defend_move_list[num * 2], defend_move_list[(num * 2) + 1]] in selftaken:
                                    p_simulate_take = True
                                    for p_other_piece in selflist:
                                        if p_other_piece.x == defend_move_list[num * 2] and p_other_piece.y == defend_move_list[(num * 2) + 1]:
                                            p_other_piece.x = None
                                            p_other_piece.y = None
                                            p_revive_me = p_other_piece

                                p_previous = array[defend_move_list[num * 2], defend_move_list[(num * 2) + 1]]
                                array[defend_move_list[num * 2], defend_move_list[(num * 2) + 1]] = defend_piece.value
                                if p_count == 0:
                                    array[defend_piece.x, defend_piece.y] = board

                                defend_piece.x = defend_move_list[num * 2]
                                defend_piece.y = defend_move_list[(num * 2) + 1]

                                p_legal = True
                                for p_oppose_piece in selflist:
                                    if p_oppose_piece.x != None:
                                        p_oppose_piece.move()
                                        if array[opponentking.x, opponentking.y] == opponentcheck:
                                            p_legal = False
                                            if player == "WHITE":
                                                self.clear_black_mod()
                                            if player == "BLACK":
                                                self.clear_white_mod()
                                            break
                                        else:
                                            if player == "WHITE":
                                                self.clear_black_mod()
                                            if player == "BLACK":
                                                self.clear_white_mod()
                                #print(f"p_legal: {p_legal}")

                                array[defend_move_list[num * 2], defend_move_list[(num * 2) + 1]] = p_previous
                                if p_simulate_take == True:
                                    p_revive_me.x = defend_move_list[num * 2]
                                    p_revive_me.y = defend_move_list[(num * 2) + 1]

                                if p_legal == True:

                                    legal_count += 1
                                    #print("added!")

                                    save_black_piece = defend_piece
                                    save_x = defend_move_list[num * 2]
                                    save_y = defend_move_list[(num * 2) + 1]
                                    save_take = p_simulate_take
                                    save_other_piece = None
                                    if save_take == True:
                                        save_other_piece = p_revive_me




                                p_count += 1
                                defend_piece.x = p_xx
                                defend_piece.y = p_yy
                                array[defend_piece.x, defend_piece.y] = defend_piece.value
                                if legal_count > 1:
                                    break
                            self.clear()


                        if legal_count > 1:
                            break

                self.clear()
        if p_legal == False and legal_count == 0:
            return 2

        if legal_count == 1:
            list = (1, save_black_piece, save_x, save_y, save_take, save_other_piece)
            return list

        else: # these parameters might not work.
            return 0


    def train(self, centre_ranking, ranking_changes):

        actual_ranking = 0
        # actual_ranking = 0 if safe
        # actual_ranking = 1 if we want to append the ranking change
        # actual_ranking = 2 if we want to append the centre ranking


        redo = False
        redo_type = None
        #redo_type: a = 0, b = centre ranking, c = ranking changes[0]

        if ranking_changes[0] < 0:

            # no second ranking - SAFE
            if int(len(ranking_changes)) == 1:
                pass

            # second ranking - MAYBE NOT SAFE
            if int(len(ranking_changes)) > 1:

                # DEFINITELY NOT SAFE
                if ranking_changes[1] > abs(ranking_changes[0]):
                    # centre ranking
                    actual_ranking = 2

                # SAFE (not necessarily)
                if ranking_changes[1] <= abs(ranking_changes[0]):
                    redo = True
                    redo_type = "ab"
                    # CHOOSE BETWEEN 0 AND CENTRE RANKING. Are you sure?



        # on the first exchange we loose material. Definitely not safe
        if ranking_changes[0] > 0:

            # no second exchange - we can viably respond, so instead of centre ranking it is the first ranking change
            if int(len(ranking_changes)) == 1:
                # ranking changes
                actual_ranking = 1

            if int(len(ranking_changes)) > 1:
                if ranking_changes[1] > 0:
                    # centre ranking
                    actual_ranking = 2

                if ranking_changes[1] <= 0:
                    redo = True
                    redo_type = "bc"
                    # CHOOSE BETWEEN APPENDING CENTRE RANKING, OR RANKING CHANGES
                    # we need to go through again - determine if it is safe to respond



        if ranking_changes[0] == 0:
            if int(len(ranking_changes)) == 1:
                pass
            if int(len(ranking_changes)) > 1:
                redo = True
                redo_type = "abc"
                # we need to go through again - determine if it is safe to respond
                # CHOOSE BETWEEN 0, CENTRE RANKING, OR RANKING CHANGES

        if redo == False:
            #print(f"actual ranking in function: {actual_ranking}")
            return actual_ranking

        if redo == True:
            #print(f"REDO type: {redo_type}")
            return redo_type



    def program_white(self, simulate_take, other_piece, moved_piece, player):
        # piece has already moved to a possible legal position.
        # first, just try and always get it to move into a check mate position.
        # save the array to reset it for later. Maybe have this outside the function?
        print("\n")
        print(moved_piece.name)
        print(moved_piece.x)
        print(moved_piece.y)
        print(array)
        the_ranking = 0

        if player == "WHITE":
            selflist = whitelist
            opponentlist = blacklist

            selfking = kingw
            opponentking = kingb

            selfcheck = white_check
            opponentcheck = black_check

            opponenttaken = black_taken
            selfmoveonly = white_move_only
            selftakeline = white_take_line
            selfcastlevalue = white_castle_value

            selftaken = white_taken
            opponentmoveonly = black_move_only
            opponenttakeonly = black_take_only
            opponenttakeline = black_take_line

            selfsupport = white_support
            opponentsupport = black_support

        if player == "BLACK":
            selflist = blacklist
            opponentlist = whitelist

            selfking = kingb
            opponentking = kingw

            selfcheck = black_check
            opponentcheck = white_check

            opponenttaken = white_taken
            selfmoveonly = black_move_only
            selftakeline = black_take_line
            selfcastlevalue = black_castle_value

            selftaken = black_taken
            opponentmoveonly = white_move_only
            opponenttakeonly = white_take_only
            opponenttakeline = white_take_line

            selfsupport = black_support
            opponentsupport = white_support


        # CHECK FOR CHECK MATE MOVE... make it look for check mate in 3.
        checkmate = self.checkmate_check(player)
        if checkmate != 0 and checkmate != 2:

            save_black_piece = checkmate[1]
            save_x = checkmate[2]
            save_y = checkmate[3]
            save_take = checkmate[4]
            save_other_piece = checkmate[5]
            checkmate = checkmate[0]

            # make the move
            saved_previous_x = save_black_piece.x
            saved_previous_y = save_black_piece.y
            array[saved_previous_x, saved_previous_y] = board
            save_black_piece.x = save_x
            save_black_piece.y = save_y
            if save_take == True:
                save_revive_x = save_other_piece.x
                save_revive_y = save_other_piece.y
                save_other_piece.x = None
                save_other_piece.y = None
            array[save_x, save_y] = save_black_piece.value



            # black piece has now moved in response to the white move resulting in only one possible move for black

            # all possible white moves need to be iterated over this function.
            for piece in selflist:
                if piece.x != None:
                    possible_x = None
                    possible_y = None
                    xx = piece.x
                    yy = piece.y
                    re_move = False
                    revive_me = None
                    move_list_white = []
                    golist_white = []
                    piece.move()

                    #taking_black_list = []
                    #for a in range(0, 8):
                    #    for b in range(0, 8):
                    #        if array[a, b] in black_taken:
                    #            taking_black_list.append(a)
                    #            taking_black_list.append(b)

                    # ALL LEGAL MOVES FOR A PARTICULAR PIECE
                    for a in range(0, 8):
                        for b in range(0, 8):
                            if array[a, b] in opponenttaken or array[a, b] == selfmoveonly or array[a, b] == selftakeline:
                                move_list_white.append(a)
                                move_list_white.append(b)

                    #self.clear_white_mod() #used to be white mod clear, where black taken values are left intact.
                    if player == "WHITE":
                        self.clear_white_mod()
                    if player == "BLACK":
                        self.clear_black_mod()

                    count = 0
                    for num in range(0, int(len(move_list_white) / 2)):

                        simulate_take = False

                        # If it's moving into a taken value, remove the taken value
                        if array[move_list_white[num * 2], move_list_white[(num * 2) + 1]] in opponenttaken:
                            simulate_take = True
                            for other_piece in opponentlist:
                                if other_piece.x == move_list_white[num * 2] and other_piece.y == move_list_white[(num * 2) + 1]:
                                    other_piece.x = None
                                    other_piece.y = None
                                    revive_me = other_piece
                                    break

                        # Move the piece, and save the last value for future clearing.
                        previous = array[move_list_white[num * 2], move_list_white[(num * 2) + 1]]
                        array[move_list_white[num * 2], move_list_white[(num * 2) + 1]] = piece.value
                        if count == 0:
                            array[piece.x, piece.y] = board

                        piece.x = move_list_white[num * 2]
                        piece.y = move_list_white[(num * 2) + 1]


                        # Check for check!! If it is a legal move, append it to the golist.
                        legal = True
                        for oppose_piece in opponentlist:
                            if oppose_piece.x != None:
                                oppose_piece.move()
                                if array[selfking.x, selfking.y] == selfcheck:
                                    legal = False
                                    #self.clear_white_mod() # used to be white mod clear
                                    if player == "WHITE":
                                        self.clear_white_mod()
                                    if player == "BLACK":
                                        self.clear_black_mod()
                                    break
                                else:
                                    #self.clear_white_mod() # used to be white mod clear
                                    if player == "WHITE":
                                        self.clear_white_mod()
                                    if player == "BLACK":
                                        self.clear_black_mod()

                        if legal == True:
                            save_piece_list = []
                            for save_piece in listall:
                                save_piece_list.append(save_piece.x)
                                save_piece_list.append(save_piece.y)

                            save_list = []
                            for a in range(0, 8):
                                for b in range(0, 8):
                                    save_list.append(array[a, b])

                            checkmate = self.checkmate_check(player)


                            save_count = 0
                            for a in range(0, 8):
                                for b in range(0, 8):
                                    array[a, b] = save_list[save_count]
                                    save_count += 1

                            save_piece_count = 0
                            for save_piece in listall:
                                save_piece.x = save_piece_list[save_piece_count * 2]
                                save_piece.y = save_piece_list[(save_piece_count * 2) + 1]
                                save_piece_count += 1

                            if checkmate == 0:
                                pass

                            if checkmate == 2:
                                break

                            if checkmate != 0 and checkmate != 2:


                                # we need to do the move.
                                deep_save_black_piece = checkmate[1]
                                deep_save_x = checkmate[2]
                                deep_save_y = checkmate[3]
                                deep_save_take = checkmate[4]
                                deep_save_other_piece = checkmate[5]
                                checkmate = checkmate[0]

                                # make the move
                                deep_saved_previous_x = deep_save_black_piece.x
                                deep_saved_previous_y = deep_save_black_piece.y
                                array[deep_saved_previous_x, deep_saved_previous_y] = board
                                deep_save_black_piece.x = deep_save_x
                                deep_save_black_piece.y = deep_save_y
                                if deep_save_take == True:
                                    deep_save_revive_x = deep_save_other_piece.x
                                    deep_save_revive_y = deep_save_other_piece.y
                                    deep_save_other_piece.x = None
                                    deep_save_other_piece.y = None
                                array[deep_save_x, deep_save_y] = deep_save_black_piece.value





                                for deep_piece in selflist:
                                    if deep_piece.x != None:
                                        deep_possible_x = None
                                        deep_possible_y = None
                                        deep_xx = deep_piece.x
                                        deep_yy = deep_piece.y
                                        deep_revive_me = None
                                        deep_move_list_white = []
                                        deep_piece.move()

                                        #taking_black_list = []
                                        #for a in range(0, 8):
                                        #    for b in range(0, 8):
                                        #        if array[a, b] in black_taken:
                                        #            taking_black_list.append(a)
                                        #            taking_black_list.append(b)

                                        # ALL LEGAL MOVES FOR A PARTICULAR PIECE
                                        #print(array)
                                        for a in range(0, 8):
                                            for b in range(0, 8):
                                                if array[a, b] in opponenttaken or array[a, b] == selfmoveonly or array[a, b] == selftakeline:
                                                    deep_move_list_white.append(a)
                                                    deep_move_list_white.append(b)

                                        #self.clear_white_mod() #used to be white mod clear, where black taken values are left intact.

                                        if player == "WHITE":
                                            self.clear_white_mod()
                                        if player == "BLACK":
                                            self.clear_black_mod()
                                        deep_count = 0
                                        for deep_num in range(0, int(len(deep_move_list_white) / 2)):
                                            #print("\nAt the start of the num loop:")
                                            #print(f"kingb.x: {kingb.x}")
                                            #print(f"kingb.y: {kingb.y}")
                                            deep_simulate_take = False

                                            # If it's moving into a taken value, remove the taken value
                                            if array[deep_move_list_white[deep_num * 2], deep_move_list_white[(deep_num * 2) + 1]] in opponenttaken:
                                                deep_simulate_take = True
                                                for other_piece in opponentlist:
                                                    if other_piece.x == deep_move_list_white[deep_num * 2] and other_piece.y == deep_move_list_white[(deep_num * 2) + 1]:
                                                        other_piece.x = None
                                                        other_piece.y = None
                                                        deep_revive_me = other_piece
                                                        #print(f"deep_revive_me: {deep_revive_me.name}")
                                                        #print(f"piece moving: {deep_piece.name}")
                                                        break

                                            # Move the piece, and save the last value for future clearing.
                                            previous = array[deep_move_list_white[deep_num * 2], deep_move_list_white[(deep_num * 2) + 1]]
                                            array[deep_move_list_white[deep_num * 2], deep_move_list_white[(deep_num * 2) + 1]] = deep_piece.value
                                            if deep_count == 0:
                                                array[deep_piece.x, deep_piece.y] = board

                                            deep_piece.x = deep_move_list_white[deep_num * 2]
                                            deep_piece.y = deep_move_list_white[(deep_num * 2) + 1]


                                            # Check for check!! If it is a legal move, append it to the golist.
                                            legal = True
                                            for oppose_piece in opponentlist:
                                                if oppose_piece.x != None:
                                                    oppose_piece.move()
                                                    if array[selfking.x, selfking.y] == selfcheck:
                                                        legal = False
                                                        #self.clear_white_mod() # used to be white mod clear
                                                        if player == "WHITE":
                                                            self.clear_white_mod()
                                                        if player == "BLACK":
                                                            self.clear_black_mod()
                                                        break
                                                    else:
                                                        #self.clear_white_mod() # used to be white mod clear
                                                        if player == "WHITE":
                                                            self.clear_white_mod()
                                                        if player == "BLACK":
                                                            self.clear_black_mod()
                                            if legal == True:
                                                save_piece_list = []
                                                for save_piece in listall:
                                                    save_piece_list.append(save_piece.x)
                                                    save_piece_list.append(save_piece.y)

                                                save_list = []
                                                for a in range(0, 8):
                                                    for b in range(0, 8):
                                                        save_list.append(array[a, b])

                                                #print("\nJust before checkmate_check:")
                                                #print(f"kingb.x: {kingb.x}")
                                                #print(f"kingb.y: {kingb.y}")
                                                checkmate = self.checkmate_check(player)


                                                save_count = 0
                                                for a in range(0, 8):
                                                    for b in range(0, 8):
                                                        array[a, b] = save_list[save_count]
                                                        save_count += 1

                                                save_piece_count = 0
                                                for save_piece in listall:
                                                    save_piece.x = save_piece_list[save_piece_count * 2]
                                                    save_piece.y = save_piece_list[(save_piece_count * 2) + 1]
                                                    save_piece_count += 1

                                                if checkmate == 0:
                                                    pass

                                                if checkmate == 2:
                                                    break

                                                if checkmate != 0 and checkmate != 2:
                                                    pass




                                            # and now, reset the board to test for the next potential legal / illegal move
                                            array[deep_move_list_white[deep_num * 2], deep_move_list_white[(deep_num * 2) + 1]] = previous
                                            if deep_simulate_take == True:
                                                deep_revive_me.x = deep_move_list_white[deep_num * 2]
                                                deep_revive_me.y = deep_move_list_white[(deep_num * 2) + 1]


                                            deep_count += 1



                                        #break
                                        deep_piece.x = deep_xx
                                        deep_piece.y = deep_yy
                                        array[deep_piece.x, deep_piece.y] = deep_piece.value
                                        self.clear()
                                        if checkmate == 2:
                                            break # at this point, we have discovered that a white moves leads to only one possible black move.
                                            # then, we have made that move.
                                            # then, out of all legal white moves, can we give black only one choice again?


                                # now we need to reset.
                                deep_save_black_piece.x = deep_saved_previous_x
                                deep_save_black_piece.y = deep_saved_previous_y
                                array[deep_saved_previous_x, deep_saved_previous_y] = deep_save_black_piece.value
                                if deep_save_take == True:
                                    deep_save_other_piece.x = deep_save_revive_x
                                    deep_save_other_piece.y = deep_save_revive_y
                                    array[deep_save_revive_x, deep_save_revive_y] = deep_save_other_piece.value


                        # and now, reset the board to test for the next potential legal / illegal move
                        array[move_list_white[num * 2], move_list_white[(num * 2) + 1]] = previous
                        if simulate_take == True:
                            revive_me.x = move_list_white[num * 2]
                            revive_me.y = move_list_white[(num * 2) + 1]


                        count += 1
                        if checkmate == 2:
                            break



                    #break
                    piece.x = xx
                    piece.y = yy
                    array[piece.x, piece.y] = piece.value
                    self.clear()
                    if checkmate == 2:
                        break

            # now reset
            save_black_piece.x = saved_previous_x
            save_black_piece.y = saved_previous_y
            array[saved_previous_x, saved_previous_y] = save_black_piece.value
            if save_take == True:
                save_other_piece.x = save_revive_x
                save_other_piece.y = save_revive_y
                array[save_revive_x, save_revive_y] = save_other_piece.value


        # WHITE SUPPORTS AND THREATS
        threaten_list = []
        support_list = []
        discover_list = []
        for p_piece in selflist:
            if p_piece.x != None:
                self.clear()
                p_piece.move()

                for a in range(0, 8):
                    for b in range(0, 8):
                        if array[a, b] in opponenttaken:
                            for threatened in opponentlist:
                                if array[a, b] == (threatened.value + 40):
                                    threaten_list.append(p_piece)
                                    threaten_list.append(threatened)
                        elif array[a, b] in selfsupport:
                            for supported in selflist:
                                if array[a, b] == (supported.value + 80):
                                    support_list.append(p_piece)
                                    support_list.append(supported)

        # DISCOVERABLES FOR WHITE MOVES
        # Discover threat
        check_discover_list = []
        for num in range(0, int(len(threaten_list) / 2)):
            r_piece = threaten_list[num * 2]
            t_piece = threaten_list[(num * 2) + 1]

            if t_piece not in check_discover_list:
                check_discover_list.append(t_piece)

                r_count = 0
                r_list = []
                for p_piece in threaten_list:
                    if r_count % 2 != 0:
                        if p_piece == t_piece:
                            r_list.append(r_count)
                            r_count += 1
                        else:
                            r_count += 1
                    else:
                        r_count += 1
                # the r_list contains the locations of all the threatened pieces which are the same as the initial threatened piece.
                # now, we need to remove thier repsective threatening pieces, to see if there is a discoverable threat.
                r_piece_list = []
                for number in r_list:
                    remove_piece = threaten_list[number - 1]
                    r_piece_list.append(remove_piece)

                # the r_piece_list contains a list of all own pieces which threatens one particular black piece.
                r_save_list = []
                for p_piece in r_piece_list:
                    save_x = p_piece.x
                    save_y = p_piece.y
                    r_save_list.append(p_piece)
                    r_save_list.append(save_x)
                    r_save_list.append(save_y)
                    array[save_x, save_y] = board
                    p_piece.x = None
                    p_piece.y = None

                # Now, all these pieces have been removed. Now, see if any more own pieces threaten that same black piece.
                for p_piece in selflist:
                    if p_piece.x != None:
                        self.clear()
                        p_piece.move()
                        for a in range(0, 8):
                            for b in range(0, 8):
                                if array[a, b] == t_piece.value + 40: # found a discoverable threat:
                                    threaten_list.append(p_piece)
                                    threaten_list.append(t_piece)
                                    #print("DISCOVERABLE THREAT DETECTED")
                                    #print(p_piece.name)
                                    #print("threatens")
                                    #print(t_piece.name)

                # Now, put the removed pieces back in.
                for nums in range(0, int(len(r_save_list) / 3)):
                    p_piece = r_save_list[nums * 3]
                    x = r_save_list[(nums * 3) + 1]
                    y = r_save_list[(nums * 3) + 2]
                    p_piece.x = x
                    p_piece.y = y
                self.clear()

        # Discover support:
        check_discover_list = []
        for num in range(0, int(len(support_list) / 2)):
            r_piece = support_list[num * 2]
            s_piece = support_list[(num * 2) + 1]

            if s_piece not in check_discover_list:
                check_discover_list.append(s_piece)
                r_count = 0
                r_list = []
                for p_piece in support_list:
                    if r_count % 2 != 0:
                        if p_piece == s_piece: # NOT IN THE CORRECT SECTION!!!!!
                            r_list.append(r_count)
                            r_count += 1
                        else:
                            r_count += 1
                    else:
                        r_count += 1
                # the r_list contains the locations of all the threatened pieces which are the same as the initial threatened piece.
                # now, we need to remove thier repsective threatening pieces, to see if there is a discoverable threat.
                r_piece_list = []
                for number in r_list:
                    remove_piece = support_list[number - 1]
                    r_piece_list.append(remove_piece)


                # the r_piece_list contains a list of all own pieces which supports one particular white piece.
                r_save_list = []
                for p_piece in r_piece_list:
                    save_x = p_piece.x
                    save_y = p_piece.y
                    r_save_list.append(p_piece)
                    r_save_list.append(save_x)
                    r_save_list.append(save_y)
                    array[save_x, save_y] = board
                    p_piece.x = None
                    p_piece.y = None

                # Now, all these pieces have been removed. Now, see if any more own pieces threaten that same black piece.
                for p_piece in selflist:
                    if p_piece.x != None:
                        self.clear()
                        p_piece.move()
                        for a in range(0, 8):
                            for b in range(0, 8):
                                if array[a, b] == s_piece.value + 80: # found a discoverable support:
                                    support_list.append(p_piece)
                                    support_list.append(s_piece)


                # Now, put the removed pieces back in.
                for nums in range(0, int(len(r_save_list) / 3)):
                    p_piece = r_save_list[nums * 3]
                    x = r_save_list[(nums * 3) + 1]
                    y = r_save_list[(nums * 3) + 2]
                    p_piece.x = x
                    p_piece.y = y
                self.clear()



        # BLACK SUPPORTS AND THREATS
        oppose_threaten_list = []
        oppose_support_list = []
        for p_piece in opponentlist:
            if p_piece.x != None:
                self.clear()
                p_piece.move()

                for a in range(0, 8):
                    for b in range(0, 8):
                        if array[a, b] in selftaken:
                            for threatened in selflist:
                                if array[a, b] == (threatened.value + 40):
                                    oppose_threaten_list.append(p_piece)
                                    oppose_threaten_list.append(threatened)
                        elif array[a, b] in opponentsupport:
                            for supported in opponentlist:
                                if array[a, b] == (supported.value + 80):
                                    oppose_support_list.append(p_piece)
                                    oppose_support_list.append(supported)

        # DISCOVERABLES FOR BLACK MOVES:
        # Discover threat:
        check_discover_list = []
        for num in range(0, int(len(oppose_threaten_list) / 2)):
            r_piece = oppose_threaten_list[num * 2]
            t_piece = oppose_threaten_list[(num * 2) + 1]

            if t_piece not in check_discover_list:
                check_discover_list.append(t_piece)

                r_count = 0
                r_list = []
                for p_piece in oppose_threaten_list:
                    if r_count % 2 != 0:
                        if p_piece == t_piece:
                            r_list.append(r_count)
                            r_count += 1
                        else:
                            r_count += 1
                    else:
                        r_count += 1
                # the r_list contains the locations of all the threatened pieces which are the same as the initial threatened piece.
                # now, we need to remove thier repsective threatening pieces, to see if there is a discoverable threat.
                r_piece_list = []
                for number in r_list:
                    remove_piece = oppose_threaten_list[number - 1]
                    r_piece_list.append(remove_piece)

                # the r_piece_list contains a list of all own pieces which threatens one particular black piece.
                r_save_list = []
                for p_piece in r_piece_list:
                    save_x = p_piece.x
                    save_y = p_piece.y
                    r_save_list.append(p_piece)
                    r_save_list.append(save_x)
                    r_save_list.append(save_y)
                    array[save_x, save_y] = board
                    p_piece.x = None
                    p_piece.y = None

                # Now, all these pieces have been removed. Now, see if any more black pieces threaten that same white piece.
                for p_piece in opponentlist:
                    if p_piece.x != None:
                        self.clear()
                        p_piece.move()
                        for a in range(0, 8):
                            for b in range(0, 8):
                                if array[a, b] == t_piece.value + 40: # found a discoverable threat:
                                    oppose_threaten_list.append(p_piece)
                                    oppose_threaten_list.append(t_piece)
                                    #print("THREAT DISCOVERED:")
                                    #print(p_piece.name)
                                    #print("threatens")
                                    #print(t_piece.name)

                # Now, put the removed pieces back in.
                for nums in range(0, int(len(r_save_list) / 3)):
                    p_piece = r_save_list[nums * 3]
                    x = r_save_list[(nums * 3) + 1]
                    y = r_save_list[(nums * 3) + 2]
                    p_piece.x = x
                    p_piece.y = y
                self.clear()

        # Discover support:
        check_discover_list = []
        for num in range(0, int(len(oppose_support_list) / 2)):
            r_piece = oppose_support_list[num * 2]
            s_piece = oppose_support_list[(num * 2) + 1]

            if s_piece not in check_discover_list:
                check_discover_list.append(s_piece)

                r_count = 0
                r_list = []
                for p_piece in oppose_support_list:
                    if r_count % 2 != 0:
                        if p_piece == s_piece: # NOT IN THE CORRECT SECTION!!!!!
                            r_list.append(r_count)
                            r_count += 1
                        else:
                            r_count += 1
                    else:
                        r_count += 1
                # the r_list contains the locations of all the threatened pieces which are the same as the initial threatened piece.
                # now, we need to remove thier repsective threatening pieces, to see if there is a discoverable threat.
                r_piece_list = []
                for number in r_list:
                    remove_piece = oppose_support_list[number - 1]
                    r_piece_list.append(remove_piece)



                # the r_piece_list contains a list of all own pieces which supports one particular white piece.
                r_save_list = []
                for p_piece in r_piece_list:
                    save_x = p_piece.x
                    save_y = p_piece.y
                    r_save_list.append(p_piece)
                    r_save_list.append(save_x)
                    r_save_list.append(save_y)
                    array[save_x, save_y] = board
                    p_piece.x = None
                    p_piece.y = None

                # Now, all these pieces have been removed. Now, see if any more own pieces threaten that same black piece.
                for p_piece in opponentlist:
                    if p_piece.x != None:
                        self.clear()
                        p_piece.move()
                        for a in range(0, 8):
                            for b in range(0, 8):
                                if array[a, b] == s_piece.value + 80: # found a discoverable support:
                                    oppose_support_list.append(p_piece)
                                    oppose_support_list.append(s_piece)


                # Now, put the removed pieces back in.
                for nums in range(0, int(len(r_save_list) / 3)):
                    p_piece = r_save_list[nums * 3]
                    x = r_save_list[(nums * 3) + 1]
                    y = r_save_list[(nums * 3) + 2]
                    p_piece.x = x
                    p_piece.y = y
                self.clear()



        # DEFENSIVE RANKINGS: (own)
        aggregate_list = []
        save_threatened_list = []
        for num in range(0, int(len(oppose_threaten_list) / 2)):
            white_threatened = oppose_threaten_list[(num * 2) + 1] # the white piece being threatened
            black_threatening = oppose_threaten_list[(num * 2)]

            if white_threatened not in save_threatened_list:
                #print(f"\nwhite threatened: {white_threatened.name}")

                threatening_list = []
                threatening_list.append(black_threatening) # record the piece which is threatening own piece
                save_threatened_list.append(white_threatened)

                for number in range(0, int(len(oppose_threaten_list) / 2)): # now find all other threatening pieces in that list where the SAME piece is being threatened
                    if number != num: # BUT we cannot have duplicates - the piece cannot be put twice.
                        if white_threatened == oppose_threaten_list[(number * 2) + 1]:
                            black_threatening = oppose_threaten_list[(number * 2)]
                            threatening_list.append(black_threatening)

                # Now in the record_list, we have the location of all the opposing pieces which threaten ONE particular own piece.
                # Now, we need to find all own pieces which support that ONE particular piece.

                supporting_list = []
                for nums in range(0, int(len(support_list) / 2)):
                    if white_threatened == support_list[(nums * 2) + 1]:
                        supporter = support_list[(nums * 2)]
                        supporting_list.append(supporter)

                # Now in the supporting_list, we have all the pieces which support the ONE threatened piece.
                # Now, we need to find the difference in ranking between the threatened piece in question, and the opposing piece(s) threatening it.
                # ONE CAVEAT: we need discoverable supporting and threatening pieces.

                threatening_ranking = []
                for threatening_piece in threatening_list:
                    threatening_ranking.append(threatening_piece.ranking)

                supporting_ranking = []
                for supporting_piece in supporting_list:
                    supporting_ranking.append(supporting_piece.ranking)



                centre_ranking = white_threatened.ranking

                threatening_length = int(len(threatening_ranking))
                supporting_length = int(len(supporting_ranking))

                # Now we have a list of rankings for all the offensive and defensive pieces on ONE of your own pieces.
                # We need to record the piece at the centre of all this.
                # HIGHER RANKINGS ARE MORE VALUABLE

                threatening_ranking.sort()
                supporting_ranking.sort()
                #print(f"threatening list: {threatening_ranking}")
                #print(f"supporting list: {supporting_ranking}")

                #print("white threatened:")
                #print(white_threatened.name)
                #print("black threatening:")
                #print(black_threatening.name)


                ranking_changes = []
                stop_ranking = False

                for sequence in range(0, threatening_length):

                    # If there are supporting pieces, and it's the first take
                    if supporting_length > sequence and sequence == 0:
                        ranking_change = centre_ranking - threatening_ranking[sequence]
                        #print("first")
                        #print(ranking_change)
                        ranking_changes.append(ranking_change)

                    # no supporting pieces, and it's the first take
                    if supporting_length == sequence and sequence == 0:
                        ranking_change = centre_ranking
                        #print("second")
                        #print(ranking_change)
                        ranking_changes.append(ranking_change)

                    # if there are supporting pieces, and it's not the first take
                    if supporting_length > sequence and sequence != 0:
                        ranking_change = supporting_ranking[sequence - 1] - threatening_ranking[sequence]
                        #print("third")
                        #print(ranking_change)
                        ranking_changes.append(ranking_change)

                    # no supporting pieces, and it's not the first take
                    if supporting_length == sequence and sequence != 0:
                        ranking_change = supporting_ranking[sequence - 1]
                        #print("fourth")
                        #print(ranking_change)
                        ranking_changes.append(ranking_change)


                # on the first exchange we win material. May or may not be safe.


                save_ranking_changes = []
                for pointless in ranking_changes:
                    save_ranking_changes.append(pointless)
                actual_ranking = self.train(centre_ranking, ranking_changes)
                first_ranking_change = ranking_changes[0]
                re_doing = False

                if isinstance(actual_ranking, int) == False:
                    re_doing = True

                    # first save. if type = abc, we also need to save the next one.
                    redo_type_save = actual_ranking
                    count = 0
                    while isinstance(actual_ranking, int) == False:
                        ranking_changes.pop(0)
                        actual_ranking = self.train(centre_ranking, ranking_changes)
                        if redo_type_save == "abc" and isinstance(actual_ranking, int) == False: # is that right??
                            redo_type_save = actual_ranking
                        count += 1



                    # ranking change was 0
                    if redo_type_save == "abc":
                        if actual_ranking == 0:
                            final_ranking = 0

                        if actual_ranking == 1:
                            #print("decision branch actual ranking is one")
                            #print(f"centre ranking: {centre_ranking}")
                            #print(f"save ranking change: {save_ranking_changes[count]}")
                            # this means that the first exchange was equal, and the next exchange is bad, but can be reponded to (a viable exchange)
                            if centre_ranking > save_ranking_changes[count]:
                                #print("centre ranking greater")
                                final_ranking = save_ranking_changes[count]

                            if centre_ranking < save_ranking_changes[count]:
                                #print("centre ranking smaller")
                                final_ranking = centre_ranking

                            if centre_ranking == save_ranking_changes[count]:
                                final_ranking = centre_ranking
                                #print("centre ranking equal")



                            # what about when they are equal?

                        if actual_ranking == 2:
                            #print("decision branch actual ranking is two")
                            #print(f"centre ranking: {centre_ranking}")
                            #print(f"supporting ranking: {supporting_ranking[count]}")

                            # this means that the first exchange was equal, and the next exchange is bad and cannot be responded to (therefore, it is not a ranking change, it is a rank.)
                            # the next value in the supporting ranking efectively becomes the centre ranking
                            if centre_ranking > supporting_ranking[count]:
                                final_ranking = supporting_ranking[count]
                                #print("centre ranking greater")

                            if centre_ranking < supporting_ranking[count]:
                                final_ranking = centre_ranking
                                #print("centre ranking smaller")

                            if centre_ranking == supporting_ranking[count]:
                                final_ranking = centre_ranking
                                #print("centre ranking equal")


                    # ranking change was negative, and the next one is less than or equal to the modulus of the last change. decide between safe and centre ranking.
                    if redo_type_save == "ab":
                        if actual_ranking == 0:
                            final_ranking = 0

                        # this means it can be responded to, but still has a negative impact
                        if actual_ranking == 1 or actual_ranking == 2:
                            final_ranking = centre_ranking

                    # choose between centre ranking and ranking changes - the first ranking was positive (definitely loosing something)
                    if redo_type_save == "bc":

                        # safe for the next exchange to take place.
                        if actual_ranking == 0:
                            final_ranking = save_ranking_changes[0]
                        if actual_ranking == 1 or actual_ranking == 2:
                            final_ranking = centre_ranking



                if re_doing == False:
                    if actual_ranking == 0:
                        final_ranking = 0
                    if actual_ranking == 1:
                        final_ranking = first_ranking_change
                    if actual_ranking == 2:
                        final_ranking = centre_ranking

                save_threatened_list.append(final_ranking)
                #print(f"final ranking at end: {final_ranking}")
                aggregate_list.append(final_ranking)



        ranking_sum = sum(aggregate_list)
        #print(f"ranking sum: {ranking_sum}")
        the_ranking += ranking_sum






        # DEFENSIVE RANKINGS: (opponent's)
        aggregate_list = []
        o_save_threatened_list = []
        for num in range(0, int(len(threaten_list) / 2)):
            black_threatened = threaten_list[(num * 2) + 1] # the black piece being threatened
            white_threatening = threaten_list[(num * 2)]

            if black_threatened not in o_save_threatened_list:

                threatening_list = []
                threatening_list.append(white_threatening) # record the piece which is threatening own piece
                o_save_threatened_list.append(black_threatened)

                for number in range(0, int(len(threaten_list) / 2)): # now find all other threatening pieces in that list where the SAME piece is being threatened
                    if number != num: # BUT we cannot have duplicates - the piece cannot be put twice.
                        if black_threatened == threaten_list[(number * 2) + 1]:
                            white_threatening = threaten_list[(number * 2)]
                            threatening_list.append(white_threatening)

                # Now in the record_list, we have the location of all the opposing pieces which threaten ONE particular own piece.
                # Now, we need to find all own pieces which support that ONE particular piece.

                supporting_list = []
                for nums in range(0, int(len(oppose_support_list) / 2)):
                    if black_threatened == oppose_support_list[(nums * 2) + 1]:
                        supporter = oppose_support_list[(nums * 2)]
                        supporting_list.append(supporter)

                # Now in the supporting_list, we have all the pieces which support the ONE threatened piece.
                # Now, we need to find the difference in ranking between the threatened piece in question, and the opposing piece(s) threatening it.
                # ONE CAVEAT: we need discoverable supporting and threatening pieces.

                threatening_ranking = []
                for threatening_piece in threatening_list:
                    threatening_ranking.append(threatening_piece.ranking)

                supporting_ranking = []
                for supporting_piece in supporting_list:
                    supporting_ranking.append(supporting_piece.ranking)

                centre_ranking = black_threatened.ranking

                threatening_length = int(len(threatening_ranking))
                supporting_length = int(len(supporting_ranking))

                # Now we have a list of rankings for all the offensive and defensive pieces on ONE of your own pieces.
                # We need to record the piece at the centre of all this.
                # HIGHER RANKINGS ARE MORE VALUABLE

                threatening_ranking.sort()
                supporting_ranking.sort()

                #print("black threatened:")
                #print(black_threatened.name)
                #print("white threatening:")
                #print(white_threatening.name)


                # POSITIVE NUMBERS ARE BAD RANKING CHANGES. LOWER NUMBERS ARE BETTER.
                # Defensive ranking
                ranking_changes = []
                stop_ranking = False

                for sequence in range(0, threatening_length):
                    # If there are supporting pieces, and it's the first take
                    if supporting_length > sequence and sequence == 0:
                        ranking_change = centre_ranking - threatening_ranking[sequence]
                        #print("first")
                        #print(ranking_change)
                        ranking_changes.append(ranking_change)

                    # no supporting pieces, and it's the first take
                    if supporting_length == sequence and sequence == 0:
                        ranking_change = centre_ranking
                        #print("second")
                        #print(ranking_change)
                        ranking_changes.append(ranking_change)

                    # if there are supporting pieces, and it's not the first take
                    if supporting_length > sequence and sequence != 0:
                        ranking_change = supporting_ranking[sequence - 1] - threatening_ranking[sequence]
                        #print("third")
                        #print(ranking_change)
                        ranking_changes.append(ranking_change)

                    # no supporting pieces, and it's not the first take
                    if supporting_length == sequence and sequence != 0:
                        ranking_change = supporting_ranking[sequence - 1]
                        #print("fourth")
                        #print(ranking_change)
                        ranking_changes.append(ranking_change)


                # on the first exchange we win material. May or may not be safe.


                save_ranking_changes = []
                for pointless in ranking_changes:
                    save_ranking_changes.append(pointless)
                actual_ranking = self.train(centre_ranking, ranking_changes)
                first_ranking_change = ranking_changes[0]
                re_doing = False

                if isinstance(actual_ranking, int) == False:
                    re_doing = True

                    # first save. if type = abc, we also need to save the next one.
                    redo_type_save = actual_ranking
                    count = 0
                    while isinstance(actual_ranking, int) == False:
                        ranking_changes.pop(0)
                        actual_ranking = self.train(centre_ranking, ranking_changes)
                        if redo_type_save == "abc" and isinstance(actual_ranking, int) == False: # is that right??
                            redo_type_save = actual_ranking
                        count += 1



                    # ranking change was 0
                    if redo_type_save == "abc":
                        if actual_ranking == 0:
                            final_ranking = 0

                        if actual_ranking == 1:
                            #print("decision branch actual ranking is one")
                            #print(f"centre ranking: {centre_ranking}")
                            #print(f"save ranking change: {save_ranking_changes[count]}")
                            # this means that the first exchange was equal, and the next exchange is bad, but can be reponded to (a viable exchange)
                            if centre_ranking > save_ranking_changes[count]:
                                #print("centre ranking greater")
                                final_ranking = save_ranking_changes[count]

                            if centre_ranking < save_ranking_changes[count]:
                                #print("centre ranking smaller")
                                final_ranking = centre_ranking

                            if centre_ranking == save_ranking_changes[count]:
                                final_ranking = centre_ranking
                                #print("centre ranking equal")



                            # what about when they are equal?

                        if actual_ranking == 2:
                            #print("decision branch actual ranking is two")
                            #print(f"centre ranking: {centre_ranking}")
                            #print(f"supporting ranking: {supporting_ranking[count]}")

                            # this means that the first exchange was equal, and the next exchange is bad and cannot be responded to (therefore, it is not a ranking change, it is a rank.)
                            # the next value in the supporting ranking efectively becomes the centre ranking
                            if centre_ranking > supporting_ranking[count]:
                                final_ranking = supporting_ranking[count]
                                #print("centre ranking greater")

                            if centre_ranking < supporting_ranking[count]:
                                final_ranking = centre_ranking
                                #print("centre ranking smaller")

                            if centre_ranking == supporting_ranking[count]:
                                final_ranking = centre_ranking
                                #print("centre ranking equal")


                    # ranking change was negative, and the next one is less than or equal to the modulus of the last change. decide between safe and centre ranking.
                    if redo_type_save == "ab":
                        if actual_ranking == 0:
                            final_ranking = 0

                        # this means it can be responded to, but still has a negative impact
                        if actual_ranking == 1 or actual_ranking == 2:
                            final_ranking = centre_ranking

                    # choose between centre ranking and ranking changes - the first ranking was positive (definitely loosing something)
                    if redo_type_save == "bc":

                        # safe for the next exchange to take place.
                        if actual_ranking == 0:
                            final_ranking = save_ranking_changes[0]
                        if actual_ranking == 1 or actual_ranking == 2:
                            final_ranking = centre_ranking



                if re_doing == False:
                    if actual_ranking == 0:
                        final_ranking = 0
                    if actual_ranking == 1:
                        final_ranking = first_ranking_change
                    if actual_ranking == 2:
                        final_ranking = centre_ranking

                o_save_threatened_list.append(final_ranking)









        offensive = False
        do_offensive = True
        if do_offensive == True:
            offensive = False
            # OFFENSIVE RANKINGS:
            # Get all the black pieces which one white piece threatens.
            save_offensive_list = []
            aggregate_list = []
            save_attacking_list = []
            for num in range(0, int(len(threaten_list) / 2)):
                td_piece = threaten_list[(num * 2) + 1]
                at_piece = threaten_list[(num * 2)]
                # block it out, prevent repeats
                if at_piece not in save_attacking_list:
                    save_attacking_list.append(at_piece)
                    td_list = []
                    td_list.append(td_piece)

                    for number in range(0, int(len(threaten_list) / 2)):
                        if number != num:
                            if at_piece == threaten_list[number * 2]:
                                td_piece = threaten_list[(number * 2) + 1]
                                td_list.append(td_piece)

                    # now we have a list of all the black pieces which one white piece threatens.
                    td_ranking_list = []

                    for td_piece in td_list:
                        td_ranking_list.append(td_piece.ranking)

                    td_ranking_list.sort()
                    # TD_LIST NEEDS TO BE SORTED IN CONJUNCTION WITH THE RANKING LIST
                    td_length = int(len(td_ranking_list))
                    at_ranking = at_piece.ranking

                    #print(f"attacking piece: {at_piece.name}")
                    #print(f"threatened ranking list: {td_ranking_list}")

                    if at_piece in save_threatened_list:
                        #print(f"at_piece IS in save_threatened_list: {at_piece.name}")

                        x_count = 0
                        for x in save_threatened_list:
                            if x == at_piece:
                                break
                            else:
                                x_count += 1
                        defensive_ranking = save_threatened_list[x_count + 1]
                        #print(f"defensive ranking: {defensive_ranking}")

                        if defensive_ranking > 0: #BAD MOVE, DON'T EXECUTE:
                            pass

                        if defensive_ranking <= 0: #IT SHOULD BE OK...:

                            #if td_length > 1: # THREATENS MORE THAN ONE PIECE

                            td_df_ranking_list = []

                            for td_piece in td_list:
                                if td_piece in o_save_threatened_list: # The threatened piece is in some way defended. NO NO NO NO NO! save_threatened_list refers to black pieces being threatened. Obviously it's going to be threatened anyway.
                                    k_count = 0
                                    for k_piece in o_save_threatened_list:
                                        #if k_piece == td_list[0]:
                                        if k_piece == td_piece:
                                            break
                                        else:
                                            k_count += 1
                                    o_defensive_ranking = o_save_threatened_list[k_count + 1]
                                    #print(f"DEFENSIVE RANKING: {td_piece.name}, {o_defensive_ranking}")
                                    # positive is bad for the defending piece. The defending piece is black.
                                    # Therefore, positive is good for white.
                                    if o_defensive_ranking > 0:
                                        # black piece is not sufficiently defended...
                                        # record all the defensive ranking values if they are above 0 (it is a valid take)
                                        rank_change = o_defensive_ranking
                                        td_df_ranking_list.append(rank_change)
                                        #print(f"{td_piece.name} not defended enough!")

                                else: # The threatened black piece is not defended:
                                    rank_change = td_piece.ranking
                                    td_df_ranking_list.append(rank_change)
                                    #print(f"{td_piece.name} not defended at all!")

                            td_df_ranking_list.sort()

                            if int(len(td_df_ranking_list)) >= 2: #"GUARANTEED" UPPER HAND
                                low_rank = td_df_ranking_list[-2]
                                aggregate_list.append(low_rank)
                                #print(f"low rank: {low_rank}")
                                offensive = low_rank

                            elif int(len(td_df_ranking_list)) == 1: # SUBTLE ATTACK (only has a valid threat to one piece.)
                                subtle_rank = td_df_ranking_list[0] / 100
                                aggregate_list.append(subtle_rank)
                                #print(f"subtle rank: {subtle_rank}")



                    if at_piece not in save_threatened_list: # at_piece is not under threat from anything:
                        # only make the move substantially more valuable if it attacks two at once
                        # if only attacks once (meaningfully), add a value which is less than one.
                    #    print(f"at_piece IS NOT in save_threatened_list: {at_piece.name}")

                        td_df_ranking_list = []
                        for td_piece in td_list:
                            if td_piece in o_save_threatened_list: # The threatened piece is in some way defended.
                                k_count = 0
                                for k_piece in o_save_threatened_list:
                                    #if k_piece == td_list[0]:
                                    if k_piece == td_piece:
                                        break
                                    else:
                                        k_count += 1


                                o_defensive_ranking = o_save_threatened_list[k_count + 1]
                                example_piece = o_save_threatened_list[k_count]
                            #    print(f"threatened piece: {example_piece.name}")
                                #print(f"threatened piece defensive ranking: {o_defensive_ranking}")
                                # positive is bad for the defending piece. The defending piece is black.
                                # Therefore, positive is good for white.
                                #print(f"DEFENSIVE RANKING: {td_piece.name}, {o_defensive_ranking}")
                                if o_defensive_ranking > 0:
                                    # black piece is not sufficiently defended...
                                    # record all the defensive ranking values if they are above 0 (it is a valid take)
                                    #print(f"{td_piece.name} not defended enough.")

                                    rank_change = o_defensive_ranking
                                    td_df_ranking_list.append(rank_change)

                            else: # The threatened black piece is not defended:
                                rank_change = td_piece.ranking
                                td_df_ranking_list.append(rank_change)
                                #print(f"{td_piece.name} not defended at all.")

                        td_df_ranking_list.sort()

                        if int(len(td_df_ranking_list)) >= 2: #GUARANTEED UPPER HAND
                            low_rank = td_df_ranking_list[-2]
                            aggregate_list.append(low_rank)
                            #print(f"low rank: {low_rank}")
                            offensive = low_rank

                        elif int(len(td_df_ranking_list)) == 1: # SUBTLE ATTACK (only has a valid threat to one piece.)
                            subtle_rank = td_df_ranking_list[0] / 100
                            aggregate_list.append(subtle_rank)
                            #print(f"subtle rank: {subtle_rank}")



            #more_ranking = sum(aggregate_list)
            if int(len(aggregate_list)) > 0:
                more_ranking = max(aggregate_list)
                the_ranking -= more_ranking

            #print(f"len agg list: {len(aggregate_list)}")
            #print(f"agg list: {aggregate_list}")











        # If there is an opportunity to realise a take, do the take instead of getting into an offensive position
        # Which seemingly guarantees a taking opportunity - as that is not reliable.


        # TAKING RANKING
        if simulate_take == True:
            the_ranking -= other_piece.ranking


        # Needs to be taught about promotions
        # defensive support in general
        # pawn structure
        # opening positions
        # CASTLING
        # Not to move king or castles unless needed
        if moved_piece.type == 5 or moved_piece.type == 1:
            if moved_piece.first_turn == True:
                the_ranking += 0.1




        # Look forward to the next move the opponent will make - if bad, change decision.
        # spacial density
        # NEEDS TO LOOF FORWARD TWO IN DISCOVERY

        # SOMETHING WRONG - doesn't appreciate putting the pressure on ( / 100) as much as it is meant to.

        print(f"final ranking: {the_ranking}")

        if checkmate == 2:
            print("dios mio")
            return "checkmate_move", the_ranking, offensive

        if checkmate == 0:
            return None, the_ranking, offensive







    def computerplay(self, player, computer_setting):

        if player == "WHITE":
            selflist = whitelist
            opponentlist = blacklist

            selfking = kingw
            opponentking = kingb

            selfcheck = white_check
            opponentcheck = black_check

            opponenttaken = black_taken
            selfmoveonly = white_move_only
            selftakeline = white_take_line
            selfcastlevalue = white_castle_value

            selftaken = white_taken
            opponentmoveonly = black_move_only
            opponenttakeonly = black_take_only
            opponenttakeline = black_take_line

            selfcastlevalueone = 13
            selfcastlevaluetwo = 14




        if player == "BLACK":
            selflist = blacklist
            opponentlist = whitelist

            selfking = kingb
            opponentking = kingw

            selfcheck = black_check
            opponentcheck = white_check

            opponenttaken = white_taken
            selfmoveonly = black_move_only
            selftakeline = black_take_line
            selfcastlevalue = black_castle_value

            selftaken = black_taken
            opponentmoveonly = white_move_only
            opponenttakeonly = white_take_only
            opponenttakeline = white_take_line

            selfcastlevalueone = 33
            selfcastlevaluetwo = 34




        # this function gets legal moves for all pieces of one player

        self.clear()
        potential = None
        saved_potential = None
        other_piece = None
        total_ranking_list = []


        really_is_check = None
        total_go_list = []
        for piece in selflist:
            if piece.x != None:
                possible_x = None
                possible_y = None
                xx = piece.x
                yy = piece.y
                re_move = False
                revive_me = None
                move_list_white = []
                golist_white = []
                piece.move()

#                    taking_black_list = []
#                    for a in range(0, 8):
#                        for b in range(0, 8):
#                            if array[a, b] in black_taken:
#                                taking_black_list.append(a)
#                                taking_black_list.append(b)

                # ALL LEGAL MOVES FOR A PARTICULAR PIECE
                for a in range(0, 8):
                    for b in range(0, 8):
                        if array[a, b] in opponenttaken or array[a, b] == selfmoveonly or array[a, b] == selftakeline or array[a, b] == selfcastlevalue:
                            castle_legal_white = True

                            if array[a, b] == selfcastlevalue:
                                re_move = True
                                self.clear()

                                for oppose_piece_castle in opponentlist:
                                    if oppose_piece_castle.x != None:
                                        oppose_piece_castle.move()

                                        if piece.value == selfcastlevalueone: #hmmm....
                                            if array[selfking.x, selfking.y] == selfcheck or array[0, 2] == opponenttakeline or array[0, 2] == opponenttakeonly or array[0, 3] == opponenttakeline or array[0, 3] == opponenttakeonly:
                                                self.clear()
                                                castle_legal_white = False
                                                break
                                            else:
                                                self.clear()
                                        if piece.value == selfcastlevaluetwo:
                                            if array[selfking.x, selfking.y] == selfcheck or array[0, 5] == opponenttakeline or array[0, 5] == opponenttakeonly or array[0, 6] == opponenttakeline or array[0, 6] == opponenttakeonly:
                                                self.clear()
                                                castle_legal_white = False
                                                break
                                            else:
                                                self.clear()

                            if castle_legal_white == True:
                                move_list_white.append(a)
                                move_list_white.append(b)

                            if re_move == True:
                                piece.move()
                #self.clear_white_mod() #used to be white mod clear, where black taken values are left intact.
                #hmmm

                if player == "WHITE":
                    self.clear_white_mod()

                if player == "BLACK":
                    self.clear_black_mod()



                count = 0
                for num in range(0, int(len(move_list_white) / 2)):
                    simulate_take = False

                    # If it's moving into a taken value, remove the taken value
                    if array[move_list_white[num * 2], move_list_white[(num * 2) + 1]] in opponenttaken:
                        simulate_take = True
                        for other_piece in opponentlist:
                            if other_piece.x == move_list_white[num * 2] and other_piece.y == move_list_white[(num * 2) + 1]:
                                other_piece.x = None
                                other_piece.y = None
                                revive_me = other_piece
                                break

                    # Move the piece, and save the last value for future clearing.
                    previous = array[move_list_white[num * 2], move_list_white[(num * 2) + 1]]
                    array[move_list_white[num * 2], move_list_white[(num * 2) + 1]] = piece.value
                    if count == 0:
                        array[piece.x, piece.y] = board

                    piece.x = move_list_white[num * 2]
                    piece.y = move_list_white[(num * 2) + 1]


                    # Check for check!! If it is a legal move, append it to the golist.
                    legal = True
                    for oppose_piece in opponentlist:
                        if oppose_piece.x != None:
                            oppose_piece.move()
                            if array[selfking.x, selfking.y] == selfcheck:
                                legal = False
                                #self.clear_white_mod() # used to be white mod clear
                                if player == "WHITE":
                                    self.clear_white_mod()
                                if player == "BLACK":
                                    self.clear_black_mod()
                                break
                            else:
                                #self.clear_white_mod() # used to be white mod clear
                                if player == "WHITE":
                                    self.clear_white_mod()
                                if player == "BLACK":
                                    self.clear_black_mod()
                    if legal == True:
                        golist_white.append(move_list_white[num * 2])
                        golist_white.append(move_list_white[(num * 2) + 1])

                        if computer_setting == "PROGRAM":



                            save_piece_list = []
                            for save_piece in listall:
                                save_piece_list.append(save_piece.x)
                                save_piece_list.append(save_piece.y)

                            save_list = []
                            for a in range(0, 8):
                                for b in range(0, 8):
                                    save_list.append(array[a, b])

                            potential, the_ranking, offensive = self.program_white(simulate_take, other_piece, piece, player)

                            total_ranking_list.append(the_ranking)
                            total_ranking_list.append(piece)
                            total_ranking_list.append(move_list_white[num * 2])
                            total_ranking_list.append(move_list_white[(num * 2) + 1])
                            total_ranking_list.append(simulate_take)
                            total_ranking_list.append(offensive)


                            save_count = 0
                            for a in range(0, 8):
                                for b in range(0, 8):
                                    array[a, b] = save_list[save_count]
                                    save_count += 1

                            save_piece_count = 0
                            for save_piece in listall:
                                save_piece.x = save_piece_list[save_piece_count * 2]
                                save_piece.y = save_piece_list[(save_piece_count * 2) + 1]
                                save_piece_count += 1



                            if potential == "checkmate_move":
                                potential_x = move_list_white[num * 2]
                                potential_y = move_list_white[(num * 2) + 1]
                                potential_piece = piece
                                saved_potential = "checkmate_move"






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



                #if computer_setting == "RANDOM":
                possible_x, possible_y = self.random(golist_white)
                if possible_x != None:
                    total_go_list.append(possible_x)
                    total_go_list.append(possible_y)
                    total_go_list.append(piece)




        #if computer_setting == "RANDOM":
        print(f"total go list line 2015: {total_go_list}")
        rank_x, rank_y, rank_piece = self.random_2(total_go_list)

        if rank_x == "checkmate":
            really_is_check = False
            for piece in opponentlist:
                if piece.x != None:
                    self.clear()
                    piece.move()
                    if array[selfking.x, selfking.y] == selfcheck:
                        really_is_check = True
                        break

        self.clear()
        if really_is_check == False:
            rank_x = "stalemate"
            rank_y = "stalemate"
            rank_piece = "stalemate"

        if computer_setting == "PROGRAM":
            #total_ranking_list = self.holistic_white_program(total_ranking_list)

            for num in range(0, int(len(total_ranking_list) / 6)):
                name = total_ranking_list[(num * 6) + 1]
                #print("\n")
                #print(name.name)
                #print(total_ranking_list[(num * 6)])

            new_ranking_list = []
            for num in range(0, int(len(total_ranking_list) / 6)):
                ranking = total_ranking_list[num * 6]
                new_ranking_list.append(ranking)

            if int(len(new_ranking_list)) > 0:
                best_ranking = min(new_ranking_list)
                print("BEST RANKING:")
                print(best_ranking)



                rank_count = 0
                random_rank_list = []
                for rum in new_ranking_list:
                    if best_ranking == rum:
                        random_rank_list.append(rank_count)
                        rank_count += 1
                    else:
                        rank_count += 1

                random_rank = random.choice(random_rank_list)
                rank_piece = total_ranking_list[(random_rank * 6) + 1]
                rank_x = total_ranking_list[(random_rank * 6) + 2]
                rank_y = total_ranking_list[(random_rank * 6) + 3]




        print(saved_potential)
        if saved_potential != "checkmate_move":
            return rank_x, rank_y, rank_piece


        if saved_potential == "checkmate_move":
            print("gggg")
            return potential_x, potential_y, potential_piece







gameplay = chessgame(player)




















# end of script
