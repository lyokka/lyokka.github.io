#! /usr/bin/python

import matplotlib.pyplot as plt
import os

def geometric_rv_plot(prob):
    num_subfig = len(prob)
    plt.figure(figsize=(num_subfig*4, 4))
    for i, p in enumerate(prob):

        x = range(1, 15)
        pmf = [(1-p)**(i-1) * p for i in x]
        
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
    #plt.show()
    if not os.path.exists('../assets/images/prob/prob5/'):
        try:
            os.makedirs('../assets/images/prob/prob5/')
        except:
            raise "can not make a directory"
            
    plt.savefig('../assets/images/prob/prob5/geometric_rv.png')


if __name__ == '__main__':
    geometric_rv_plot([0.1, 0.5, 0.8])
