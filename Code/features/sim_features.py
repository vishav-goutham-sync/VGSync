import numpy as np
class similarity_features:
    def dice_coefficient(self ,x,y):
        x=np.diff(x)
        y=np.diff(y)
        num=2*abs(np.dot(x,y))
        denom=abs(np.dot(x,x))+abs(np.dot(y,y))
        dc=np.divide(num,denom)
        return dc
    def chebyshev_distance(self,x,y):
        return np.max(np.abs(x-y))
    def manhattan_distance(self,x,y):
        return np.sum(np.abs(x-y))
    def euclidean_distance(self, x, y):
        return np.sqrt(np.sum((x-y)**2))
    def minkowski_distance(self,x,y,p):
        return np.sum((np.abs(x-y)**p))**(1/p)
    def canberra_distance(self, x, y):
        num=np.abs(x-y)
        denom=np.abs(x)+np.abs(y)
        return np.sum(np.divide(num+1,denom+1))
    def cosine_distance(self, x, y):
        num=np.dot(x,y)
        denom=np.dot(x,x)*np.dot(y,y)
        return 1-(np.divide(num,denom))
		
    def pearson_correlation_coefficient(self,x,y):
        return np.correlate(x,y)[0]
    def root_mean_square_difference(self, x, y):
        return np.sqrt(((x - y) ** 2).mean())
