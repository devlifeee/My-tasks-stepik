// В этом задании вам нужно вычислить сумму всех четных чисел, встречающихся в ряду
// от 1 до числа (включительно), передаваемого в нашу функцию (переменная "а").
function sumToN(n) {
    var sum = 0;
    var i = 1;                
    while (i <= n) {        
        sum = sum + i;                                  
        i = i + 1;                  
    }
    return sum;
}
