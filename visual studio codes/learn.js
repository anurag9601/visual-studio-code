//hoisting in javascript
//now what is meaning of hoisting:= so hoisting is when you are trying to prind or use a variable without
//defined it for example 
// console.log(a):
// let a = 5;

//our second topic is what is mainly differance between var let const in js
//so ya var is a part of old javascript that is es5
//let const is include in new javascript that is es6
// so it means that now we can't use var in new js no that is also exist in new javascript but now mainly people 
// like to use let and const now let know what is reason behind it 
// var is function scoped 
//and let and const are function braces scoped
//let's understand what is function scoped and what is function braces scoped
// function scoped means we can use the variable any where in a function
// and function braces scoped means that we can only use define variable in a braces of a function after that
// we can not use the variable 
//and the third difference is var stored in winodw object(browser) this is dangerous it can leak your data
//but let and const can not visible in window 
// that is the main difference between var let and const 

//now execution context is simply it contain where the function code is executed it created whenever function is called 
// it contain three things variable , function and lexicul environment 
// in execution context there is a lexicul invironment who conduct us that we can not use this variable or function now we can not use
// that how will we know then let's see in example there is variable a and b so can we use b by function abc() the answer is no  
// we can not use it reason is variable in function can only use by there parent function and that is def()
// let's understand by example 
// function abc(){
//     let a = 5;
//     function def(){
//         let b = 7;
//     }
// }

//spred operator in javascript very importent topic that i am sure not all people know's
// let a = [1,2,3,4,5]
// let b = [...a]
// console.log(a)
// console.log(b)
//now how to copy object
// let obj = {name:"avinash"}
// let copyobj = {...obj}
// console.log(obj)
// console.log(copyboj)

//truthy and falsy value in javascript
// now what is truthy and falsy 
// falsy values are := 0 false null undefined NaN document.all 
// exept this all are truthy values 
// for example of truthy 
// if(7){
//     console.log("hiee")
// }
// else{
//     console.log("hello")
// }
// it will return hie why because 7 is turthy value 
// now example of flasy vlaue 
// if(0){
//     console.log("hiee")
// }
// else{
//     console.log("hello")
// }

//in asynchronic js there is callback function
// so callback function is when you are using setTimeout and what ever function is in setTimeout is callback function 
// setTimeout(function(){
//     console.log("this print's after 2 second")
// },2000)

//first class function this is also called as call back function
// now what is first class function first class functions are where we are storing the function in a variable is called first class function 
// function abc(a){
//     a();
// }
// abc(function(){console.log("hey barbe")})
// one more way to write a function is a or we can say morden method 
// let b = ()=>{
//     console.log("hey")
// }
// console.log(b)