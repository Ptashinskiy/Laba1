function sumDigits(x) {
    return x.toString().split('').reduce(function(a,b){return +a+ +b;});
}

console.log(sumDigits(433))
console.log(sumDigits(111))
console.log(sumDigits(567))
