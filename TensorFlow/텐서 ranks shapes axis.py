노드와 엣지로 구성되어있는데
노드들에는 op 연산자들이들어가고 엣지가 텐서이다 이러한것들을 그래프로 그려내고 세션에서 연산이된다. 텐서플로우다.


텐서의 ranks
0 rank scalar s=483
1 rank vector v=[1.1, 2.2, 3.3, 4.4]
2 rank matrix m=[[1,2,3],[1,2,3],[1,2,3]]
3 rank 3-tensor t=[[[1,2,3],[1,2,3],[1,2,3]]
,[[1,2,3],[1,2,3],[1,2,3]]]
n rank n-tensor ....

shapes
몇차원의 행렬 3x3 이런형태를 일컫음



####
추가적으로
Rank 는 [ 갯수를 확인하면 됨.
 ex) [[1,2,3][1,2,4]]  >> rank 2

[[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
  [[13,14,15,16],[17,18,19,20],[21,22,23,24,25]]]]
shape는 rank 4일경우  ## 결국 아래 단계마다 갯수가 확인될때 [] 괄호를 제거해 나가면된다.
        (?,?,?,?) 형태가 되며 최초 [1,2,3,4] 열의 수 4를 
        (?,?,?,4) 와 기입 그후  1~4 같은 랭크안에서 9~12까지 반복되므로 갯수3을 그 다음 열에 
        (?,?,3,4) 와 기입 그후 1~12 와 13~25까지가 같은 랭크 이므로 갯수 2
        (?,2,3,4) 와 기입 그후 1~25 같은 랭크이고 갯수가 1 이므로
        (1,2,3,4)

Axis 축 [ 갯수를 0부터 카운팅하면됨
        위의 경우는 [axis=0[axis=1[axis=2[axis=3]]]] 이와같음

Axis Reduce mean
###결국
###            
               ----> axis=1
        x=[ | [1.,2.],
            | [3.,4.] ]
            v
           axis =0
###
        
        tf.reduce_mean([1,2], axis=0).eval()
     >>>1 #interger 이므로
        x=[[1.,2.],
           [3.,4.]]
        tf.reduce_mean(x).eval()
     >>>2.5
        tf.reduce_mean(x, axis=0).eval()
     >>>array([2., 3.], dtype=float32)
        tf.reduce_mean(x, axis=1).eval()
     >>>array([1.5, 3.5], dtype=float32)
        tf.reduce_mean(x, axis=-1).eval()
     >>>array([1.5, 3.5], dtype=float32)
        
Argmax

        x=[[0,1,2],
           [2,1,0]]
        tf.arg_max(x, axis=0).eval()
     >>>array[1,0,0]
        tf.arg_max(x, axis=1).eval()
     >>>array[2,0]
        tf.arg_max(x, axis=-1).eval()
     >>>array[2,0]
        
        
        
