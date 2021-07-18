void combination(int[] arr, boolean[] visited, int start, int r) {
        int sum=0;
        
        if (r==0){
            for(int i=0; i<arr.length; i++){
                if(visited[i]){
                    sum+=arr[i];
                }
            }
            list.add(sum);
            return;
        }

        for(int i=start; i<arr.length; i++){
            visited[i] = true;
            combination(arr, visited, i+1, r-1);
            visited[i] = false;
        }
        return;
    }
