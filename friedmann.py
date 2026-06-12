import math
from scipy import constants
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class universe:

    #define the parameters for the universe
    def __init__(self, omegaR, omegaM, omegaL, hubbleConst):
        self.omegaR = omegaR
        self.omegaM = omegaM
        self.omegaL = omegaL
        self.omegaK = 1 - (omegaR + omegaM + omegaL)
        
        self.displayHubbleConst = hubbleConst
        self.hubbleConst = hubbleConst*1000/(1e+6 * constants.parsec) #convert to SI unit

    def secondFriedmann(self, tau, y):
        #define the function that needs to be integrated
        a, v = y 
        if a <= 0:
            return [0,0]
        dadt = v
        dvdt = - self.omegaR/(a**3) - self.omegaM/(2*a**2) + self.omegaL*a

        return [dadt, dvdt]
    
    def simulate(self, max_tau, accuracy):
        a_init = 1e-5
        v_init = np.sqrt(self.omegaR/a_init**2 + self.omegaM/a_init + self.omegaL*a_init**2 + self.omegaK)
        y0 = [a_init, v_init]

        def big_crunch(tau, y):
            return y[0] - 1e-5
        big_crunch.terminal = True
        big_crunch.direction = -1

        tau_eval = np.arange(a_init, max_tau, accuracy)
        sol = solve_ivp(
            self.secondFriedmann,
            t_span=(0, max_tau),
            y0=y0,
            t_eval=tau_eval,
            events=big_crunch,
            method="DOP853",
            rtol=1e-13,
            atol=1e-13
        )

        time = sol.t
        scale_factor = sol.y[0]

        return time, scale_factor
    
    def plotResult(self, timeGyr, accuracy):

        time_sec = timeGyr * 1e9 * constants.year
        max_tau = time_sec * self.hubbleConst

        #change H0t to comprehensible human time in Gyr
        time, a = self.simulate(max_tau, accuracy)

        time_seconds = time / self.hubbleConst
        seconds_in_a_Gyr = 1e9 * constants.year
        time_Gyr = time_seconds / seconds_in_a_Gyr

        #plot on matplotlib
        plt.plot(time_Gyr, a, label=f"Ωᵣ={self.omegaR}, Ωₘ={self.omegaM}, Ωₗ={self.omegaL}, Ωₖ={self.omegaK:.12g}, H₀={self.displayHubbleConst} km/s/Mpc")
        plt.xlabel("time (Gyr)")
        plt.ylabel("scale factor")
        plt.title("Evolution of Universe: Size-Time Relation")
        plt.grid(True)
        plt.legend()
        plt.show()