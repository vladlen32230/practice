(function() {
    let gameStarted=false;
    let timer=null;
    let interval=null;

    function createNumbersArray(count) {
        chosen=new Set();
    
        while (count>0) {
            let number=Math.round(Math.random()*899+100);
            if (!chosen.has(number)) {
                chosen.add(number);
                count--;
            }
        }
    
        return Array.from(chosen).concat(Array.from(chosen));
    }
    
    function shuffle(arr) {
        for (let index in arr) {
            let randomIndex=Math.round(Math.random()*(arr.length-1));
            if (randomIndex!==index) {
                temp=arr[index];
                arr[index]=arr[randomIndex];
                arr[randomIndex]=temp;
            }
        }
    
        return arr;
    }
    
    let cards=document.querySelector('.cards');

    let input=document.querySelector('#counter');

    let status=document.querySelector('.status');

    let remainingTime=document.querySelector('.remaining-time');

    let timerCheck=document.querySelector('.timer-check')

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
                    e.preventDefault();
                } else if (firstCard===null) {
                    firstCard=button;
                    firstCard.textContent=number;
                } else if (secondCard===null) {
                    secondCard=button;
                    if (number===parseInt(firstCard.textContent)) {
                        secondCard.textContent=number;
                        secondCard.disabled=true;
                        firstCard.disabled=true;
                        firstCard=null;
                        secondCard=null;
                        count--;
                        if (count===0) {
                            endGame(true);
                        }

                    } else {
                        secondCard.textContent=number;
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

        if (win) {
            status.textContent='Вы выиграли (:';
        } else {
            status.textContent='Вы проиграли ):';
        }
    }

    let start=document.querySelector('.start-game');
    start.addEventListener('click', startGame);
})();