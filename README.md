
A modified version of Chess

Gibong Hong, Jiajun Wang

Original Chess Game
- 8*8 Table
- Pieces having their own move: Pawns, Rooks, Knights, Bishops, Queen, and King
- Two player game
- Special Rules: En Passant, Promotion, Castling
- Checkmate to win the game
- To make strategic move, we need to consider the potential value of each piece
ex) King > Queen > Rook > Bishop = Knight > Pawn
- Lots of players follow this logic when they try to capture, exchange, or make other moves.
  
![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/chess_board.jpg)


A new version of Chess

Indian Poker Game + Original Chess -> A New Version of Chess

- With a deck of cards, every player has one card each, they will stick it on their forehead without seeing their cards.
- Objective: Have the highest card in play to win
- ”Reversed Poker”: As opponents are unaware of their cards, we need to give them impression that they have a high one.
![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/India_poker.pic.jpg)





## Technical stuff

The AI is a simple brute-force AI with no pruning. It evaluates a given position by counting the value of the pieces for each side (pawn -> 1, knight/bishop -> 3, rook -> 5, queen -> 9). It will evaluate the tree of moves, and take the path that results in the greatest gain. To learn more, check out [my post on how it works](https://mbuffett.com/posts/chess-ai/).
