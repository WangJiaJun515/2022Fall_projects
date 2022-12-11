
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
![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/India_poker.jpg)


A new version of Chess

- Each piece is randomly assigned its original value and a certain piece could be capture only if it has lower value than the opponent’s one
- Each player is not aware of values of their own pieces, only to know values of opponent’s pieces.
![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/new_version.jpg)



Heuristic Scoring Table 
- We need to create the board evaluation part as Minimax algorithm is used for each step.
- Piece Square Tables by Heuristic approach
- The values could be set in an 8*8 matrix so that it has a higher value at favorable positions 
and a lower value at a non-favorable place.
- For example, in the case of Queen piece, she would like her to be placed at the center position
as she can dominate relatively more positions from the center.
![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/table.pic.jpg)

- Consider the scoring table initialized for each piece.
- Also, we need to include the position of opponents’ pieces such that we can adjust the value of scoring table to make reasonable move: Our pieces would - - rather avoid the opponents’ pieces having higher values (6, 7, 8)
- For each turn, scoring function updates the values in the original scoring table by considering possible legal moves of all pieces and finding whether the new coordinate is occupied by the opponent’s piece.
![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/scoring1.jpg)

![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/scoring2.jpg)

Rule Exception: Queen and King can be captured by any other pieces, to make the game end.



## Technical stuff

The AI is a simple brute-force AI with no pruning. It evaluates a given position by counting the value of the pieces for each side (pawn -> 1, knight/bishop -> 3, rook -> 5, queen -> 9). It will evaluate the tree of moves, and take the path that results in the greatest gain. To learn more, check out [my post on how it works](https://mbuffett.com/posts/chess-ai/).
