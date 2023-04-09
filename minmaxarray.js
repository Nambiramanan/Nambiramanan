function getMinMax(arr,n){
        var min=Infinity;
        var max=-Infinity;
        for(let i=0;i<n;i++ ){
            if(arr[i]<min){
                min=arr[i];
            }
            if(arr[i]>max){
                max=arr[i];
             }
        }
        return [min,max];
    }

const arr= [3, 2, 1, 56, 10000, 167];
let n=arr.length;
x=getMinMax(arr,n);
console.log(x);