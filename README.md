# Invisible Chess

This is a modified version of Chess which is a combination of Indian Poker Game and Original Chess Game\

You can find the baseline of our chess game at this link: https://github.com/marcusbuffett/command-line-chess

## Members

Jiajun Wang and Gibong Hong

## Rules for Invisible Chess

- Our new type of chess has two major differences with the original one.
- First of all, each piece have integer value which is assigned randomly. Unlike original chess where each piece can capture opponent's pieces, our new version can capture the piece of counterpart only if it has higher or same value than the opponent's one.
  - For example, if a player move pawn to the position where the rook with its value 4 is located, the pawn could capture the rook only if its value is higher than 4.
- Secondly, players are not aware of values of their own pieces, only to know values of opponent's pieces.
- Except these two aspects, other rules are same as the original one.

## Screenshots

### Initial Board State

![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/new_version.jpg)

### Heuristic Scoring Table

- We need to create the board evaluation part as Minimax algorithm is used for each step.
- The values could be set in an 8*8 matrix so that it has a higher value at favorable positions and a lower value at a non-favorable place.
- For example, in the case of Queen piece, she would like her to be placed at the center position
as she can dominate relatively more positions from the center.
- Piece square tables we used are from this link (https://medium.com/dscvitpune/lets-create-a-chess-ai-8542a12afef
). However, we modified some values as we found that AI does not move in smart way when using the original tables.

![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/table.pic.jpg)

- Consider the scoring table initialized for each piece.
- Also, we need to include the position of opponents’ pieces such that we can adjust the value of scoring table to make reasonable move: Our pieces would - - rather avoid the opponents’ pieces having higher values (6, 7, 8)
- For each turn, scoring function updates the values in the original scoring table by considering possible legal moves of all pieces and finding whether the new coordinate is occupied by the opponent’s piece.
- Rule Exception: Queen and King can be captured by any other pieces, to make the game end.

![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/scoring1.jpg)
![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/scoring2.jpg)

## Contribution

- Jiajun Wang: Implementation of Minimax Function with pruning, modification for functions including Move and undoMove, error correction, setting visualization for detailed rules in our game.
- Gibong Hong: Setting Heuristic Scoring Table, modification for scoring function in Move function.

## Technical stuff

The AI is a simple brute-force Minimax AI with pruning. The board class contains an attribute named points, if one piece moves to a certain position, the points of board will (white piece - adding, black piece - reducing) update correlative points through scoring table and opponents' value. Then it will evaluate the tree of moves and get the path that takes the greatest points.


Algorithm Time Complexity Analysis:
Since we are using the base code provided by @marcusbuffett, so we followed the overall structure of the previous code, and made some changes on rules(judging capturing which piece can win), AI(using minimax, also updated the scoring table to evaluate position score). According to the introduction of our scoring function above, our scoring can be divided to two parts. When one certain piece is going to move to a certain position, we have a original score table as the basic table, and the program will also generate another table which throught positions of opponent pieces, then getting the final points if move to that certain position. We put that process of generating another table at MakeMove() function, so the basic time complexity will be added O(k) (k represents the number of pieces of each side) every time when we call MakeMove(). 
![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/O(k).jpg)
 
In our Minimax function, the basic structure is dfs, and we need to makeMove() and undoMove() to get the score of each move, so the total time complexity will be k times the orginial dfs time complexity.

Comparsion between pruning and non-pruning:
![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/pruning.jpg)
![Image text](https://github.com/WangJiaJun515/2022Fall_projects/blob/main/img/non-pruning.jpg)

