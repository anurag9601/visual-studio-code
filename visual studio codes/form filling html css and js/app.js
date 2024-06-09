let name = document.getElementById('name');
let phoneNo = document.getElementById('phone');
let email = document.getElementById('email');
let message = document.getElementById('message');
let nameError = document.querySelector('.name-error');
let boxError= document.querySelector('.box-error');
let phoneError = document.querySelector('.phone-error');
let emailError = document.querySelector('.email-error');
let messageError = document.querySelector('.message-error');

function nameValid(){
    let n = name.value
    if(n.length == 0){
        nameError.innerHTML = 'Name is required';
        return false;
    }
    if(!n.match(/^[A-Za-z]*\s{1}[A-Za-z]*$/)){
    nameError.innerHTML = 'Write full name';
    return false
    }
    nameError.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
    return true;
}

function phoneValid(){
    let p = phoneNo.value;
    if(p.length == 0){
        phoneError.innerHTML = 'Phone number is required';
        return false;
    }else if(!p.match(/^[0-9]{10}$/)){
        phoneError.innerHTML = 'Enter valid Phone No';
        return false;
    }
    phoneError.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
    return true;
}

function mailValid(){
    let m = email.value;
    if(m.length==0){
        emailError.innerHTML = 'Mail is required';
        return false;
    }else if(!m.match(/^[A-Za-z\._\-[0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)){
        emailError.innerHTML = 'Enter vaild mail'
        return false
    }
    emailError.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
    return true;
}


function messageValid(){
    let t = message.value;
    let required = 30;
    let left = required - t.length
    if (left > 0){
        messageError.innerHTML = left + 'more characters required';
        return false;
    }
    messageError.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
    return true;

}

function submit() {
    if (!nameValid() || !phoneValid() || !mailValid() || !messageValid()) {
        boxError.style.display = 'block';
        boxError.innerHTML = 'Please fix errors to submit';
        setTimeout(() => {
            boxError.style.display = 'none';
        }, 3000);
        return false;
    }
    return true;
}
