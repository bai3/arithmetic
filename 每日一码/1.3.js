function Fibonacci(n)
{
    // write code here
    if(n == 0 || n ==1){
        return n;
    }
    else if(n == 2){
        return 1
    }
    else{
        var c = 1
        var b = 1
        for(var i = 3;i<=n;i++){
            c = c + b;
            b = c - b;
        }
        return c
    }
}