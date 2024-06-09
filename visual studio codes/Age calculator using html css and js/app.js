let inputdate = document.querySelector('#input-date');
let button = document.querySelector('button');
let result = document.querySelector('#result');

inputdate.max = new Date().toISOString().split('T')[0];

function calculateAge(){
    let yourDate = new Date(inputdate.value);
    let d1 = yourDate.getDate();
    let m1 = yourDate.getMonth() + 1;
    let y1 = yourDate.getFullYear();
    
    let todayDate = new Date();
    let d2 = todayDate.getDate();
    let m2 = todayDate.getMonth() + 1;
    let y2 = todayDate.getFullYear();

    let d3 , m3 , y3,l;
    
    y3 = y2 - y1;

    if(m2 >= m1){
        m3 = m2 - m1
    }else{
        y3--;
        m3 = (12 + m2) - m1;
    }
    if (d2 >= d1){
        d3 = d2 - d1;
    }else{
        m3--;
        d3 = getDaysInMonth(m3,y3) + d2 - d1;
    }
    result.innerHTML = `You are <span>${y3}</span> years , <span>${m3}</span> months and <span>${d3} </span> days old`
}

function getDaysInMonth(month,year){
    return new Date(year,month,0).getDate();
}

button.addEventListener('click',()=>{
    calculateAge();
});