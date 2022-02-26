const closeBtn = document.querySelector('.close-pop-btn');
const popup = document.querySelector('.popup')

closeBtn.addEventListener('click', ()=>{
    popup.classList.remove('active')
});