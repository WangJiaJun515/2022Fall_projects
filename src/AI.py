from __future__ import annotations

import random

from src.Board import Board
from src.InputParser import InputParser
from src.Move import Move
from src.MoveNode import MoveNode

WHITE = True
BLACK = False


class AI:
    depth = 1
    movesAnalyzed = 0

    def __init__(self, board: Board, side: bool, depth: int):
        self.board = board
        self.side = side
        self.depth = depth
        self.parser = InputParser(self.board, self.side)

    def getRandomMove(self) -> Move:
        legalMoves = list(self.board.getAllMovesLegal(self.side))
        randomMove = random.choice(legalMoves)
        return randomMove

    def generateMoveTree(self) -> list[MoveNode]:
        moveTree = []
        for move in self.board.getAllMovesLegal(self.side):
            moveTree.append(MoveNode(move, [], None))

        for node in moveTree:
            self.board.makeMove(node.move)
            self.populateNodeChildren(node)
            self.board.undoLastMove()
        return moveTree

    def populateNodeChildren(self, node: MoveNode) -> None:
        node.pointAdvantage = self.board.getPointAdvantageOfSide(self.side)
        node.depth = node.getDepth()
        if node.depth == self.depth:
            return

        side = self.board.currentSide

        legalMoves = self.board.getAllMovesLegal(side)
        if not legalMoves:
            if self.board.isCheckmate():
                node.move.checkmate = True
                return
            elif self.board.isStalemate():
                node.move.stalemate = True
                node.pointAdvantage = 0
                return
            raise Exception()

        for move in legalMoves:
            self.movesAnalyzed += 1
            node.children.append(MoveNode(move, [], node))
            self.board.makeMove(move)
            self.populateNodeChildren(node.children[-1])
            self.board.undoLastMove()

    def getOptimalPointAdvantageForNode(self, node: MoveNode) -> int:
        if node.children:
            for child in node.children:
                child.pointAdvantage = self.getOptimalPointAdvantageForNode(
                    child
                )

            # If the depth is divisible by 2,
            # it's a move for the AI's side, so return max
            if node.children[0].depth % 2 == 1:
                return max(node.children).pointAdvantage
            else:
                return min(node.children).pointAdvantage
        else:
            return node.pointAdvantage

    def getBestMove(self) -> Move:
        '''moveTree = self.generateMoveTree()
        bestMoves = self.bestMovesWithMoveTree(moveTree)
        randomBestMove = random.choice(bestMoves)'''
        move,score = self.minimax(self.depth, False,-10000,10000)
        print(score)
        move.notation = self.parser.notationForMove(move)
        return move

    def makeBestMove(self) -> None:
        self.board.makeMove(self.getBestMove())

    def bestMovesWithMoveTree(self, moveTree: list[MoveNode]) -> list[Move]:
        bestMoveNodes: list[MoveNode] = []
        for moveNode in moveTree:
            moveNode.pointAdvantage = self.getOptimalPointAdvantageForNode(
                moveNode
            )
            if not bestMoveNodes:
                bestMoveNodes.append(moveNode)
            elif moveNode > bestMoveNodes[0]:
                bestMoveNodes = []
                bestMoveNodes.append(moveNode)
            elif moveNode == bestMoveNodes[0]:
                bestMoveNodes.append(moveNode)

        return [node.move for node in bestMoveNodes]

    def minimax(self, depth, maximizing, max, min):
        if depth == 0:
            return None, self.board.points
        currentSide = self.board.currentSide
        moves = self.board.getAllMovesLegal(currentSide)
        res = None
        if maximizing:
            score = -1000
        else: score = 1000
        max1 = - 10000
        min1 = 10000
        for move in moves:
            self.board.makeMove(move)
            temp,point = self.minimax(depth-1, not maximizing, max1, min1)

            if maximizing and point > score:
                res = move
                score = point
            elif not maximizing and point < score:
                res = move
                score = point
            if point < min1:
                min1 = point
            if point > max1:
                max1 = point
            self.board.undoLastMove()
            if (maximizing and point >= min) or (not maximizing and point <= max):
                return temp,point
        return res, score



if __name__ == '__main__':
    mainBoard = Board()
    ai = AI(mainBoard, True, 3)
    print(mainBoard)
    ai.makeBestMove()
    print(mainBoard)
    print(ai.movesAnalyzed)
    print(mainBoard.movesMade)
