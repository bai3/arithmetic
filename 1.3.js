function Solve(num){
    var str1 = num.toString();
    var arr = [];
    arr = str1.split('');
    var arr1 = [];
    arr1 = str1.split('');
    var arr2 = arr.reverse();    
    var str2 = arr1.join('');
    var str3 = arr2.join('');
    var val1 = parseInt(str2);
    var val2 = parseInt(str3);
    var val3 = val1+val2;
    return val3;
}