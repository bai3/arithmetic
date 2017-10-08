function Solve(str1){
    var arr =  [];
    arr = str1.split('');
    var a = 1;
    var b = 0;
    var j = 0;    
    for(var i=0;i < arr.length;i++){
        if(i!==0){
            if(arr[i] == arr[i-1]){
                a = a+1;
                if(i == arr.length-1){
                    b = b+a;
                    j++;
                }
            }else{
                b = b+a;                                
                a = 1;
                j++;
                if(i == arr.length-1){
                    b = b+a;
                    j++;
                }
            }
        }
    } 
    return (b/j).toFixed(2);   
}
Solve("aaabbaaac");