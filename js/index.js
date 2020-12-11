function isPrime(num) {
    if (num === 2) {
        return true;
    }
    if (num <= 1 || num % 2 === 0) {
        return false
    }
    for (let div = 3; div <= Math.sqrt(num); div += 2) {
        if (num % div === 0) {
            return false;
        }
    }
    return true;
}

function main(N) {
    const st = new Date().getTime();
    for (let i = 0; i < N; i++) {
        let prime = isPrime(i);
        if (prime) {
            // console.log(i + ': ' + prime);
        }
    }
    console.log((new Date().getTime() - st) / 1000);
}

// node ./js/index.js
// 3.266
(function (){
    const N = 10_000_000;
    main(N)
})()
