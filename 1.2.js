function Solve(num){
    var a = num;
    var i = 0;
    var arry = [];
    while(a > 0){
        if(a%2 == 0){
            arry[i] = 2;
            a = (a-2)/2;
            i++;
        }else{
            arry[i] = 1;
            a =(a-1)/2;
            i++;
        }
    }
    var arry2 = arry.reverse();
    var str = arry2.join('');
    print(str);
}
