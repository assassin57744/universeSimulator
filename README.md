# universeSimulator
This application uses solve_ivp from scipy to numerically integrate and plot the Friedmann equation, visually demonstrating the evolution of the Universe

To simulate a universe, one need at least 3 parameters: radiation parameter, matter parameter and dark energy parameter. Radiation parameter and matter parameter cannot be less than 0; dark matter parameter can take in any value.

The bottom three parameters are optional; leave them blank if you do not wish to tamper with it. The default value for Hubble's Constant is 70 km/s/Mpc; the default value for terminating time is 5.0 Gyr and the default value for sample space is 0.0005. Terminating time determines when the numerical integration will end and sample space determines how many samples are generated within the integration bounds.

To simulate a new universe, click Simulate. Altering the parameters and clicking Simulate again will plot the integrated function on the same graph. If you wish to plot it on a different graph, close the graph window, then click Simulate
