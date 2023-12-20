import matplotlib.pyplot as plt
from scipy import stats

# with open("oily_bright.txt") as f:
#         x= []
#         for i in f:
#             x.append(float(i.strip('\n')))
# f.close()
# with open("oily_img_bright.txt") as f:
#         y= []
#         for i in f:
#             y.append(float(i.strip('\n')))
# f.close()
x=[4415,1596.166667,1617.333333,186.6666667,351,2755.666667,657.3333333,601.6666667,4268.6,108.2,1095,131,294,1216,984,2181,2222,489,2155,98]
y=[57,44.925,42.225,20.3,39.35,38.4,45.4875,46.17,35.13,33.78,39,46,48,55,35.8,37.3,44,42.5,50.7,56]
# print(x,y)
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()
