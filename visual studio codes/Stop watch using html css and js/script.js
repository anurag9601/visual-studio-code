let stop = document.getElementById('stop');
let start = document.getElementById('start');
let reset = document.getElementById('reset');
let h1 =  document.querySelector('h1');
let hour = 0;
let minute = 0;
let second = 0;
// let minisecond = 0;

function stopWatch() {
    second++;
  if (second == 60) {
    second = 0;
    minute++;
  } else if (minute == 60) {
    minute = 0;
    hour++;
  }
  let h = hour < 10 ? '0' + hour : hour;
  let m = minute < 10 ? '0' + minute : minute;
  let s = second < 10 ? '0' + second : second;
  // let ms = minisecond < 10 ? '0' + minisecond : minisecond;
  h1.innerHTML = `${h}:${m}:${s}`;
}

start.addEventListener('click',()=>{
  a = setInterval(()=>{stopWatch()},1000);
})

stop.addEventListener('click',()=>{
  clearInterval(a);
})

reset.addEventListener('click',()=>{
  clearInterval(a);
  h1.innerHTML = `00:00:00`;
  hour = 0;
  minute = 0;
  second = 0;
})


