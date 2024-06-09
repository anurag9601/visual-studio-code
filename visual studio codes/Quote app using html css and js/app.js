let quotebtn = document.querySelector('#new-quote');
let quote = document.querySelector('#quote');
let author = document.querySelector('#author-name');
let api_url = 'https://api.quotable.io/random';
async function getQuote(url){
    const response = await fetch(url);
    let data = await response.json();
    quote.innerHTML = data.content;
    author.innerHTML = data.author;
}

quotebtn.addEventListener('click',()=>{
    quote.innerHTML = 'Loading...';
    author.innerHTML = 'Loading...';
    getQuote(api_url);
})

function tweet(){
    window.open('https://twitter.com/intent/tweet?text='+ quote.innerHTML + ' ---' + author.innerHTML, 'Tweet window', 'width=600 , height=300');
}

getQuote(api_url);