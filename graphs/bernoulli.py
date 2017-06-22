#! /usr/bin/python

import matplotlib.pyplot as plt
import os

def bernoulli_rv_plot(prob):
    num_subfig = len(prob)
    plt.figure(figsize=(num_subfig*4, 4))
    for i, p in enumerate(prob):
        plt.subplot(1, 3, i+1)
        plt.bar([0,1], [1-p, p], width=0.2)
        plt.xlabel(r'$x$')
        plt.ylabel(r'pmf $p(x)$')
        plt.title(r'Bernoulli Distribution($p=%.2f$)'%p)
        plt.xlim([-1,2])
        plt.ylim([0,1])
        plt.subplots_adjust(top = 0.92,
                           bottom = 0.08,
                           left = 0.1,
                           right = 0.9,
                           hspace = 0.25,
                           wspace = 0.35)
    if not os.path.exists('../assets/images/prob/prob5/'):
        try:
            os.makedirs('../assets/images/prob/prob5/')
        except:
            raise "can not directory"
            
    plt.savefig('../assets/images/prob/prob5/bernoulli_rv.png')


if __name__ == '__main__':
    bernoulli_rv_plot([0.1, 0.5, 0.8])
