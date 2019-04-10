from random import randint

def game_level():
    """
    This function asks the player to choose the game difficulty
    and makes sure, that the value of the game diffiuculty has a valid value
    """
    input=raw_input("Please choose the game difficulty (easy/medium/hard):")
    while True:
        if input =="easy":
            return "easy"
        elif input =="medium":
            return "medium"
        elif input =="hard":
            return "hard"
        print input + " is not a valid input!"
        input=raw_input("Please choose the game difficulty (easy/medium/hard):")

def sentence(difficulty):
    """
    This function returns the sentence which will used to play the game, based on the
    difficulty the player chose
    """
    if difficulty=="easy":
        return "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    elif difficulty=="medium":
        return "1 4 5 6 9 10 11 14 15 16 19 20 21 24 25 26"
    elif difficulty=="hard":
        return "1 4 2 3 6 4 5 8 6 7 10 8 9 12 10 11 14 12"

def replace_random_word():
    """
    This function replaces random words in the sentence and saves the correct
    answer in a separate list
    """
    numbering_of_replaced_word=1
    total_words_to_replace=4
    max_position_sentence_list=len(sentence_list)-1
    while numbering_of_replaced_word<=total_words_to_replace:
        random_num = randint(0,max_position_sentence_list )
        if not "!" in sentence_list[random_num] and not "." in sentence_list[random_num]\
        and not "," in sentence_list[random_num] and not "," in sentence_list[random_num]\
        and not "_1_" in sentence_list[random_num] and not "_2_" in sentence_list[random_num]\
        and not "_3_" in sentence_list[random_num]:
            answers_list.append([sentence_list[random_num],random_num])
            sentence_list[random_num]="_" + str(numbering_of_replaced_word) + "_"
            numbering_of_replaced_word+=1
    return answers_list

def tries():
    """
    Aks the user to insert the number of tries he wants to have for each missing word.
    """
    while True:
        try:
            tries=int(raw_input("Insert the number of tries you will need for completing the quiz:"))
            if tries>0:
                return tries
            else:
                print tries,"is not a valid number"
        except ValueError:
            print "That is not a valid number"


def swap_word(position_answer,new_word):
    """
    swaps out the place holder in the sentence list against the correct answer
    """
    sentence_list[answers_list[position_answer][1]]=new_word

def correct_answer(position_in_answer_list,max_position_answers_list):
    print "Correct! Good job."
    position_replaced_word_in_nested_list=0
    position_replaced_words_position_in_nested_list=1
    sentence_list[answers_list[position_in_answer_list][position_replaced_words_position_in_nested_list]]=answers_list[position_in_answer_list][position_replaced_word_in_nested_list]
    if position_in_answer_list==max_position_answers_list:
        print " ".join(sentence_list) +"\nGood job. You solved the quiz!"

def play_the_game(number_of_tries):
    """
    User needs to guess the correct word. if its correct the next placeholder
    will be asked.
    """
    current_position_in_answer_list=0
    max_position_answers_list=len(answers_list)-1
    current_try_number=1
    position_replaced_word_in_nested_list=0
    while current_position_in_answer_list<=max_position_answers_list and  current_try_number <= number_of_tries:
        print " ".join(sentence_list)
        placeholder_str="_"+str(current_position_in_answer_list+1)+"_"
        if raw_input("Please insert the word, which should replace "+placeholder_str+":")== answers_list[current_position_in_answer_list][position_replaced_word_in_nested_list]:
            correct_answer(current_position_in_answer_list,max_position_answers_list)
            current_position_in_answer_list+=1
            current_try_number=1
        else:
            current_try_number+=1
            if number_of_tries < current_try_number:
                print "Unfortunately this was your last try. GAME OVER"
            else:
                print "Unfortunately the answer was not correct. This is your "+str(current_try_number)+". out of " + str(number_of_tries) +" tries!"


difficulty = game_level()
sentence_list = sentence(difficulty).split()
answers_list = []
replace_random_word()
number_of_tries=tries()
play_the_game(number_of_tries)
raw_input("Press a key to leave the game!")
