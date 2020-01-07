#!/usr/bin/env python
# coding: utf-8

# In[1]:


#path(x) -> The numbers on the path we are going to follow
#mid -> Max value comparison
#n(x) -> Possible path(x) array
# start-> path3 -> path2 -> mid -> path1 -> path0 -> finish


square = [[ 9 , 2 , 6 , 3 ],
          [ 1 , 4 , 5 , 7 ],
          [ 7 , 3 , 2 , 5 ],
          [ 2 , 8 , 4 , 1 ]]


start = square[3][0]
finish = square[0][3]

mid = [square[1][1], square[1][2], square[2][1], square[2][2]]

path1 = max(mid)

if max(mid) == square[2][1]:
    type = 0
    nmid = max(mid)
    n2 = [square[2][0], square[3][1]]
    path2 = max(n2)

    n1 = [square[0][1], square[1][2]]
    path1 = max(n1)

    if path1 == square[1][2]:
        n0 = [square[0][2], square[1][3]]
        path0 = max(n0)
    else:
        path0 = square[0][2]

if max(mid) == square[2][2]:
    type = 0
    nmid = max(mid)
    n2 = [square[2][1], square[3][2]]
    path2 = max(n2)

    if path2 == square[2][1]:
        n3 = [square[2][0], square[3][1]]
        path3 = max(n3)
    else:
        path3 = square[3][1]

    n1 = [square[1][2], square[2][3]]
    path1 = max(n1)

    if path1 == square[1][2]:
        n0 = [square[0][2], square[1][3]]
        path0 = max(n0)
    else:
        path0 = square[1][3]

if max(mid) == square[1][1]:
    type = 0
    nmid = max(mid)
    n2 = [square[1][0], square[2][1]]
    path2 = max(n2)

    if path2 == square[2][1]:
        n3 = [square[2][0], square[3][1]]
        path3 = max(n3)
    else:
        path3 = square[2][0]

    n1 = [square[0][1], square[1][2]]
    path1 = max(n1)

    if path1 == square[1][2]:
        n0 = [square[0][2], square[1][3]]
        path0 = max(n0)
    else:
        path0 = square[0][2]

if max(mid) == square[1][2]:
    type = 1
    nmid = max(mid)

    n0 = [square[0][2], square[1][3]]
    path0 = max(n0)

    n1 = [square[1][1], square[2][2]]
    path1 = max(n1)

    if path1 == square[1][1]:
        n2 = [square[1][0], square[2][1]]
        path2 = max(n2)

        if path2 == square[2][1]:
            n3 = [square[2][0], square[3][1]]
            path3 = max(n3)
        else:
            path3 = square[2][0]

if type == 0:
    print("The path which will give the maximum value of addition =>", start,"-",path3,"-", path2,"-", nmid,"-", path1,"-", path0,"-", finish)
else:
    print("The path which will give the maximum value of addition =>", start,"-",path3,"-", path2,"-", path1,"-", nmid,"-", path0,"-", finish)


print("Maximum value of addition =>", start+path3+path2+nmid+path1+path0+finish)


# In[ ]:
