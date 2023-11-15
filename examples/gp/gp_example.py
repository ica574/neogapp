"""
This is an example how to use the gp module of GaPP.
You can run it with 'python gp_example.py'.
"""


from gapp import gp
import numpy as np
import os


if __name__ == "__main__":
    # load the data from inputdata.txt
    file_path = os.path.abspath("2d-inputdata.txt")
    X = np.loadtxt(file_path, usecols=(0, 1))
    (Y, Sigma) = np.loadtxt(file_path, usecols=(2, 3), unpack="True")

    # nstar*nstar points of the function will be reconstructed
    # on a grid between (xmin, xmin) and (xmax, xmax)
    xmin = 0.0
    xmax = 10.0
    nstar = 40

    # initial values of the hyperparameters
    initheta = [2.0, 2.0]

    # initialization of the Gaussian Process
    g = gp.GaussianProcess(X, Y, Sigma, cXstar=(xmin, xmax, nstar))

    # training of the hyperparameters and reconstruction of the function
    (rec, theta) = g.gp(theta=initheta)

    # save the output
    np.savetxt("f.txt", rec)

    # test if matplotlib is installed
    try:
        import matplotlib.pyplot
    except:
        print("matplotlib not installed. no plots will be produced.")
        exit
    # create plot
    import plot

    plot.plot(X[:, 0], X[:, 1], Y, Sigma, rec[:, 0], rec[:, 1], rec[:, 2])
