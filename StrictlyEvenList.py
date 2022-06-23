class StrictlyEvenList:

    internal_list = []

    def __init__(self):
        self.internal_list = []

    def add_number(self, x):
        if x % 2 == 0:
            self.internal_list.append(x)
            return True
        else:
            return False

    def even_sum(self):
        counter = 0

        for i in self.internal_list:
            counter += i
        return counter

    def square_everything(self):
        for i in range(len(self.internal_list)):
            self.internal_list[i] = self.internal_list[i] ** 2


def is_word_in_board(board, word):
    result = False
    word_counter = 0
    if(len(word) > len(board[0])):
        result = False
        print("word =", word)
        print("result =", result)
        return result

    if(len(board) == 1):
        for i in range(len(board)):
            if word_counter == len(word):
                result = True
                print("word =", word)
                print("result =", result)
                return result
            if board[i] == word[word_counter]:
                word_counter += 1
            elif word_counter > 0 and board[i] != word[word_counter]:
                result = False
                print("word =", word)
                print("result =", result)
                return result

    for i in range(len(board)):
        for j in range(len(board[i])):
            if word_counter == len(word):
                result = True
                print("word =", word)
                print("result =", result)
                return result
            elif board[i][j] == word[word_counter]:
                word_counter += 1
            elif word_counter > 0 and board[i][j] != word[word_counter]:
                result = False
                print("word =", word)
                print("result =", result)
                return result
    result = False
    print("word =", word)
    print("result =", result)
    return result

def func2(lis):
    for i in range(len(lis)):
        if isinstance(lis[i], int):
            return (lis[i], i)



if __name__ == '__main__':
    board = [['d', 'o', 'g']]

    is_word_in_board(board, "dog")


