int checkprime(int x){
    for(int i=2; i<x; i++){
        if(x%i==0)
            return 0;
        else
            return 1;
    }
}