import numpy as np
import pandas as pd
from scipy import optimize

def Pi1(Er_sigma33):
    x = np.log(Er_sigma33)
    return -1.131 * x ** 3 + 13.635 * x ** 2 - 30.594 * x + 29.267


def Pi2(Er_sigma33, n):
    x = np.log(Er_sigma33)
    return (
        (-1.40557 * n ** 3 + 0.77526 * n ** 2 + 0.1583 * n - 0.06831) * x ** 3
        + (17.93006 * n ** 3 - 9.22091 * n ** 2 - 2.37733 * n + 0.86295) * x ** 2
        + (-79.99715 * n ** 3 + 40.5562 * n ** 2 + 9.00157 * n - 2.54543) * x
        + 122.65069 * n ** 3
        - 63.88418 * n ** 2
        - 9.58936 * n
        + 6.20045
    )

def Pi4(hrhm):
    return 0.268536 * (0.9952495 - hrhm) ** 1.1142735

def Pitheta(theta, Er_sigma):
    Ersig = np.log(Er_sigma)
    t1 = (-2.3985e-5 * theta ** 3 + 6.0446e-4 * theta ** 2 +0.13243 * theta - 5.0950)
    t2 = (0.0014741 * theta ** 3 - 0.21502 * theta ** 2 + 10.4415 * theta - 169.8767)
    t3 = (-3.9124e-3 * theta ** 3 + 0.53332 * theta ** 2 - 23.2834 * theta + 329.7724)
    t4 = (2.6981e-3 * theta ** 3 - 0.29197 * theta ** 2 + 7.5761 * theta + 2.0165)
    return t1 * Ersig ** 3 + t2 * Ersig ** 2 + t3 * Ersig + t4

def epsilon_r(theta):
    return 2.397e-5 * theta ** 2 - 5.311e-3 * theta + 0.2884

def model_dao(C, dPdh, nu, Er, hm, hr, nu_i=0.0691, E_i=1143):
    C *= 1e9
    hm *= 1e-6
    hr *= 1e-6
    E_i *= 1e9
    Er *= 1e9
    sigma_33 = optimize.brentq(lambda x: Pi1(Er / x) - C / x, 1e8, 1e11)
    E = (1 - nu ** 2) / (1 / Er - (1 - nu_i ** 2) / E_i)
    try:
        n = optimize.brentq(
            lambda x: Pi2(Er / sigma_33, x) - dPdh / Er / hm, 0, 0.5
        )
    except ValueError:
        n = 0
    if n > 0:
        sigma_y = optimize.brentq(
            lambda x: (1 + E / x * 0.033) ** n - sigma_33 / x, 1e7, 1e10
        )
    else:
        sigma_y = sigma_33
    return sigma_y/1e9, n

def model_swa(C, dPdh, nu, Er, hm, hr, theta=70.3, nu_i=0.0691, E_i=1143, typ='b'):
    # This model is only valid with θ=70.3˚. Please refer to Chollacoop et al for more information.
    C *= 1e9
    E_i *= 1e9
    Er *= 1e9
    hm *= 1e-6
    hr *= 1e-6
    
    if typ == 'c':
        cstar = 1.1957  # Conical
    if typ == 'b':
        cstar = 1.2370  # Berkovich
    Pm = C * hm ** 2
    Am = (Pm * cstar / dPdh / Pi4(hr / hm)) ** 2
    Er = dPdh / cstar / Am ** 0.5
    sigma_33 = optimize.brentq(lambda x: Pi1(Er / x) - C / x, 1e7, 1e10)
    for l, r in [[1e7, 1e9], [1e9, 5e9], [5e9, 1e10]]:
        if (Pitheta(theta, Er / l) - C / l) * (
            Pitheta(theta, Er / r) - C / r
        ) < 0:
            sigma_r = optimize.brentq(
                lambda x: Pitheta(theta, Er / x) - C / x, l, r
            )
            break
    else:
        raise ValueError
    epsilon = epsilon_r(theta)
    E = (1 - nu ** 2) / (1 / Er - (1 - nu_i ** 2) / E_i)
    print(epsilon, ' ', sigma_33 - sigma_r)
    if (epsilon > 0.033 and sigma_33 < sigma_r) or (
        epsilon < 0.033 and sigma_33 > sigma_r
    ):
        sigma_y = optimize.brentq(
            lambda x: np.log(sigma_33 / x) / np.log(sigma_r / x)
            - np.log(1 + E / x * 0.033) / np.log(1 + E / x * epsilon),
            1e7,
            min(sigma_33, sigma_r),
        )
        n = np.log(sigma_33 / sigma_y) / np.log(1 + E / sigma_y * 0.033)
    else:
        n = 0
        sigma_y = (sigma_33 + sigma_r) / 2
    return E/1e9,Er/1e9, sigma_y/1e9, n




#print(model_old(204.8761345, 188141.7926, 0.25, 151, 0.220941158, 0.025171))
#print(model_new(204.8761345, 0.25, 151, 0.220941158))
#filename = '../data/TI33_25.csv'
filename = '../data/B3090.csv'
df = pd.read_csv(filename)
print('New')
for i in range(len(df)):
    if i not in [0, 23]: # Remove 2 indices that do not converge
        print(model_swa(df['C (GPa)'][i], df['dP/dh (N/m)'][i], df['nu'][i], df['E* (GPa)'][i], df['hmax(um)'][i], df['hr(um)'][i]))
print('Old')
for i in range(len(df)):
    if i not in [25]: # Remove 1 indices that do not converge
        print(i, model_dao(df['C (GPa)'][i], df['dP/dh (N/m)'][i], df['nu'][i], df['E* (GPa)'][i], df['hmax(um)'][i], df['hr(um)'][i]))