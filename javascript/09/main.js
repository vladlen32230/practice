(function() {
    let gameStarted=false;
    let timer=null;
    let interval=null;

    function createNumbersArray(count) {
        const chosen=new Array();
    
        for (let i = 1; i <= count; i++) {
            chosen.push(i);
        }
    
        return chosen.concat(chosen);
    }
    
    function shuffle(arr) {
        return arr.sort(() => Math.random() - 0.5);
    }
    
    const cards=document.querySelector('.cards');

    const input=document.querySelector('#counter');

    const status=document.querySelector('.status');

    const remainingTime=document.querySelector('.remaining-time');

    const timerCheck=document.querySelector('.timer-check')

    function startGame() {
        clearTimeout(timer);
        clearInterval(interval);

        remainingTime.textContent='';
        status.textContent='';

        cards.innerHTML='';
        let count=parseInt(input.value);

        cards.style.gridTemplateColumns='75px '.repeat(Math.sqrt(count*2));

        let numbers=shuffle(createNumbersArray(count));

        let firstCard=null;
        let secondCard=null;

        if (timerCheck.checked) {
            timer=setTimeout(endGame, 60000);
            remainingTime.textContent=59;
            interval=setInterval(() => remainingTime.textContent--, 1000);   
        }

        for (let number of numbers) {
            let button=document.createElement('button');
            button.classList.add('card');
            button.addEventListener('click', (e) => {
                if (firstCard===button || secondCard===button || !gameStarted) {
                    return;
                } else if (firstCard===null) {
                    firstCard=button;
                    firstCard.textContent=number;
                } else if (secondCard===null) {
                    secondCard=button;
                    secondCard.textContent=number;
                    if (number===parseInt(firstCard.textContent)) {
                        secondCard.disabled=true;
                        firstCard.disabled=true;
                        firstCard=null;
                        secondCard=null;
                        count--;
                        if (count===0) {
                            endGame(true);
                        }
                    }
                } else {
                    firstCard.textContent='';
                    firstCard=button;
                    firstCard.textContent=number;
                    secondCard.textContent='';
                    secondCard=null;
                }
            });

            cards.append(button);
        }

        gameStarted=true;
    }

    function endGame(win=false) {
        clearInterval(interval);
        clearTimeout(timer);

        gameStarted=false;

        win ? status.textContent = 'Вы выиграли (:' : status.textContent = 'Вы проиграли ):'
    }

    const start=document.querySelector('.start-game');
    start.addEventListener('click', startGame);
})();