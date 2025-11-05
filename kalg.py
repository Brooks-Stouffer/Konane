#Brooks Stouffer
#Konane 
#Dr. Hogg
#CSMC 450
#Due: 10-28-2025


from konane import *

class MinimaxPlayer(Konane, Player):

    def __init__(self, size, depthLimit):
        Konane.__init__(self, size)
        self.limit = depthLimit

    def initialize(self, side):
        #complete this
        self.side = side
        self.name = "Minimax_Player"

    def minimax(self, board, depth, isMaximizing, alpha, beta):
        if depth == 0:
            return self.eval(board)

        if isMaximizing:
            moves = self.generateMoves(board, self.side)
            if len(moves) == 0:
                return float('-inf')
            bestMove = float('-inf')
            for move in moves:
                nextBoard = self.nextBoard(board, self.side, move)

                value = self.minimax(nextBoard, depth - 1, False, alpha, beta)
                alpha = max(alpha, value)
                bestMove = max(bestMove, value)
                if beta <= alpha:
                    break
            return bestMove
        
        else:
            moves = self.generateMoves(board, self.opponent(self.side))
            if len(moves) == 0:
                return float('inf')
            minV = float('inf')
            for move in moves:
                nextBoard = self.nextBoard(board, self.opponent(self.side), move)
                value = self.minimax(nextBoard, depth - 1, True, alpha, beta)
                minV = min(minV, value)
                beta = min(beta, value)


                if alpha >=  beta:
                    break
            return minV


            

    def getMove(self, board):
        #complete this
        moves = self.generateMoves(board, self.side)
        bestMove = None
        bestValue = float('-inf') 
        alpha = float('-inf')
        beta = float('inf')

        if len(moves) == 0:
            return []
        else:
           
            for move in moves:
                nextBoard = self.nextBoard(board, self.side, move)
                value = self.minimax(nextBoard, self.limit - 1, False, alpha, beta)

                if value >= bestValue:
                    bestValue = value
                    bestMove  = move
                alpha = max(alpha, value)

            return bestMove
        

    def eval(self, board):
        #complete this – this will be your evaluation function.
        #High values should be good for max.
        myPieces = self.countSymbol(board, self.side)
        opPieces = self.countSymbol(board, self.opponent(self.side))
        myMoves = len(self.generateMoves(board, self.side))
        opMoves = len(self.generateMoves(board, self.opponent(self.side)))
        return (myPieces - opPieces) * 100 + (myMoves - opMoves) * 50


class SimplePlayer(Konane, Player):
    """
    Always chooses the first move from the set of possible moves.
    """
    def initialize(self, side):
        self.side = side
        self.name = "SimplePlayer"
    def getMove(self, board):
        moves = self.generateMoves(board, self.side)
        n = len(moves)
        if n == 0:
            return []
        else:
            return moves[0]


if __name__ == "__main__":
    game = Konane(8)
    game.playNGames(10, MinimaxPlayer(8, 4), RandomPlayer(8), False)
