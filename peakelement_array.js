function peakElement(arr, n){
    var p=0;
    for(let i=0;i<(n-1);i++){
        if(i==0){
            if(arr[i]>arr[i+1]){
                p=arr[i];
            }
        }
        else if(i=arr.length-1){
            if(arr[i]>arr[i-1]){
                p=arr[i];
            }
        }    
        else if(arr[i-1]<arr[i]>arr[i+1]){
            p=arr[i];
        }  
    }
    console.log(p);
}

const arr=[1,4,3];
let n=arr.length;
peakElement(arr,n);
