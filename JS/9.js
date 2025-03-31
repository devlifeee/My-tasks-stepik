//Найдите сумму  всех целых чисел от 1 до n включительно и верните из функции результат.
function testCycle(n) {
    var x;
    var i = 0;
    while (i <= n) {
        if (x % 2 == 0) {
            x = x + i
        }
        x = x + 1
    }
    return x;
}