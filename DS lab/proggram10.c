#include<stdio.h>
int a,b,u,v,n,i,j,ne=1;
int visited[10]={0},min,mincost=0,cost[10][10];
int main(){
   printf("\n Enter the number of nodes:");
   scanf("%d",&n);
   printf("\n Enter the cost adjaceny matrix:\n");
   for(i=0;i<n;i++){
   for(j=0;j<n;j++){
   scanf("%d",&cost[i][j]);
   if(cost[i][j]==0)
   cost[i][j]=999;
     }
    }

    visited[0]=1;
    printf("\n The edges of the Minimum cost Spanning tree are:\n");

    while(ne<n){
     min = 999; 
     for(i=0;i<n;i++){
     for(j=0;j<n;j++){
     if(cost[i][j] < min){
     if(visited[i] && !visited[j]){  
     min = cost[i][j];
      a = u = i;
      b = v = j;
        }
     }
         }
        }


     if(!visited[v]){
        printf("\n Edge %d:(%d->%d)\tCost:%d",ne++,a,b,min);
         { 
            mincost +=min;
           visited[v]=1;
            }
     cost[a][b]=cost[b][a]=999;
     }
 }
printf("\n\n Minimum Cost= %d\n",mincost);
 return 0;
}

