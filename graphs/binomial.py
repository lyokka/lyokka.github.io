#! /usr/bin/python

import matplotlib.pyplot as plt
import os

def binomial_rv_plot(params):
    num_p = len(params)
    num_n = len(params[0])
    plt.figure(figsize=(num_p*4, num_n*4))
    for i, p1 in enumerate(params):
        for j, p2 in enumerate(p1):
            x = range(1, p2[0])
            pmf = [(1-p)**(i-1) * p2[0] for i in x]
        
        plt.subplot(1, 3, i+1)
        plt.bar(x, pmf, width=0.4)
        plt.xlabel(r'$x$')
        plt.ylabel(r'pmf $p(x)$')
        plt.title(r'Geometric Distribution($p=%.2f$)'%p)
        plt.xlim([0,16])
        plt.ylim([0,1])
        plt.subplots_adjust(top = 0.92,
                           bottom = 0.08,
                           left = 0.1,
                           right = 0.9,
                           hspace = 0.25,
                           wspace = 0.35)
    plt.show()
    if not os.path.exists('../assets/images/prob/prob5/'):
        try:
            os.makedirs('../assets/images/prob/prob5/')
        except:
            raise "can not make a directory"
            
    #plt.savefig('../assets/images/prob/prob5/geometric_rv.png')

if __name__ == '__main__':
    params = [[(n,p) for n in range(5, 15, 5)] for p in [0.1, 0.5, 0.8]]
    binomial_rv_plot(params)
