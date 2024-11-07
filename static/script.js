document.addEventListener('DOMContentLoaded', () => {
    const board = document.getElementById('board');
    const cells = document.querySelectorAll('.cell');
    const status = document.getElementById('status');
    const resetBtn = document.getElementById('resetBtn');
    const vsHumanBtn = document.getElementById('vsHuman');
    const vsAIBtn = document.getElementById('vsAI');

    let gameMode = 'human'; // 'human' or 'ai'

    vsHumanBtn.addEventListener('click', () => {
        gameMode = 'human';
        vsHumanBtn.classList.add('active');
        vsAIBtn.classList.remove('active');
        resetGame();
    });

    vsAIBtn.addEventListener('click', () => {
        gameMode = 'ai';
        vsAIBtn.classList.add('active');
        vsHumanBtn.classList.remove('active');
        resetGame();
    });

    const updateBoard = (boardState) => {
        cells.forEach((cell, index) => {
            cell.textContent = boardState[index];
            cell.className = 'cell' + (boardState[index] !== ' ' ? 
                ` ${boardState[index].toLowerCase()}` : '');
        });
    };

    const handleMove = async (position) => {
        try {
            const response = await fetch('/api/move', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    position: position,
                    gameMode: gameMode
                }),
            });

            const data = await response.json();
            
            if (response.ok) {
                updateBoard(data.board);
                
                if (data.winner) {
                    status.textContent = `Player ${data.winner} wins!`;
                } else if (data.isDraw) {
                    status.textContent = "It's a draw!";
                } else {
                    status.textContent = `Player ${data.currentPlayer}'s turn`;
                }
                
                if (data.gameOver) {
                    board.style.pointerEvents = 'none';
                }
            } else {
                console.error('Error:', data.error);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const resetGame = async () => {
        try {
            const response = await fetch('/api/reset', {
                method: 'POST',
            });
            
            const data = await response.json();
            
            updateBoard(data.board);
            status.textContent = `Player ${data.currentPlayer}'s turn`;
            board.style.pointerEvents = 'auto';
        } catch (error) {
            console.error('Error:', error);
        }
    };

    cells.forEach(cell => {
        cell.addEventListener('click', () => {
            const position = parseInt(cell.dataset.index);
            handleMove(position);
        });
    });

    resetBtn.addEventListener('click', resetGame);

    // Initialize the game
    resetGame();
});