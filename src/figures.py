import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

''''''''''''''''''''''''''''''''''''''''''''''''
# df = pd.read_csv('../data/model/compare.csv', skiprows=1)
# fig, ax = plt.subplots()
# ax.plot(df['Depth (nm)'], df['Load (uN)'], linewidth=0.3, color='gray', zorder=1, label='Experimental results')
# ax.plot(df['Depth0 (nm)'], df['Load0 (uN)'], linewidth=0.3, color='gray', zorder=1)
# ax.plot(df['Depth2 (nm)'], df['Load2 (uN)'], linewidth=0.3, color='gray', zorder=1)
# ax.plot(df['Depth3 (nm)'], df['Load3 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth4 (nm)'], df['Load4 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth5 (nm)'], df['Load5 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth6 (nm)'], df['Load6 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth7 (nm)'], df['Load7 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth8 (nm)'], df['Load8 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth9 (nm)'], df['Load9 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth10 (nm)'], df['Load10 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth11 (nm)'], df['Load11 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth12 (nm)'], df['Load12 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth13 (nm)'], df['Load13 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth14 (nm)'], df['Load14 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth15 (nm)'], df['Load15 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth16 (nm)'], df['Load16 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth17 (nm)'], df['Load17 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth18 (nm)'], df['Load18 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth19 (nm)'], df['Load19 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth20 (nm)'], df['Load20 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth21 (nm)'], df['Load21 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth22 (nm)'], df['Load22 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth23 (nm)'], df['Load23 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.plot(df['Depth24 (nm)'], df['Load24 (uN)'], color='gray', linewidth=0.3, zorder=1)
# ax.scatter(df['disp_y_3D']*-1e3, df['react_y_3D']*-6e3, color='blue', marker='.', zorder=2, label='3D model')
# #ax.scatter(df['hm (nm)'], df['F (uN)'], color='blue', marker='.', zorder=2, label='Old 3D model')
# #ax.scatter(df['h3D']*-1000, df['F3D'], color='green', marker='s', zorder=3, s = 10, label='New 3D model')
# ax.scatter(df['disp_y_2D']*-1e3, df['react_y_2D']*-1e3, color='red', marker='*', zorder=3, s = 10, label='2D model')
# #ax.scatter(df['Depth']*1000, df['Force'], color='red', marker='*', zorder=3, s = 10, label='Old 2D model')
# #ax.scatter(df['Depth']*1000, df['Force'], color='red', marker='*', zorder=3, s = 10, label='Old 2D model')
# #ax.set_xlabel('Indenter depth (nm)')
# ax.set_xlabel('Indenter depth (nm)', fontsize=14)
# ax.set_xlim([0, 275])
# #ax.set_ylabel('Load (μN)')
# ax.set_ylabel('Load (μN)', fontsize=14)
# ax.set_ylim([0, 11000])
# ax.grid(False)
# leg = ax.legend(fontsize=14)
# #leg = ax.legend(frameon=False)
# #plt.savefig('/Users/joe/Desktop/NN_graphs/R2comp.pdf', dpi=800, bbox_inches="tight")
# plt.savefig('/Users/joe/Desktop/R2comp.pdf', dpi=800, bbox_inches="tight")
# plt.show()

# # Old ANSYS convergence study
# Bqx = [0.5, 0.25, 0.125]
# Bqy = [4.0372711553219845e-09, 7.747377814928931e-10, 1.9368444537322373e-10]
# Blx = [0.5, 0.25, 0.125]
# Bly = [8.819859692027829e-10, 3.302762232738491e-10, 8.256905581846215e-11]
# fx = [0.01, 1.5]
# C70lx = [0.25, 0.125, 0.0625, 0.03125]
# C70lx = [0.25, 0.125, 0.0625]
# C70ly = [1.5246585249772645e-09, 4.582326181224469e-10, 1.2222572353786809e-10, 3.0556430884467364e-11]
# C70ly = [1.5246585249772645e-09, 4.582326181224469e-10, 1.2222572353786809e-10]
# C70qx = [0.25, 0.125, 0.0625]
# C70qy = [1.3124579276878138e-09, 3.5390593493538945e-10, 8.847648373384798e-11]

# def equation(x, y, eqx):
#     l = len(x) - 1
#     p = np.log10(y[l]/y[0])/np.log10(x[l]/x[0])
#     C = 0
#     for i in range(3):
#         C += (1/3)*y[i]/(x[i]**p)
#     print('C = ', C)
#     print('p = ', p)
#     eqy = [0, 0]
#     for i in range(2):
#         eqy[i] = C * eqx[i] ** p
#     return eqy
# Bfq = equation(Bqx, Bqy, fx)
# Bfl = equation(Blx, Bly, fx)
# f70l = equation(C70lx, C70ly, fx)
# f70q = equation(C70qx, C70qy, fx)

# fig, ax = plt.subplots()
# ax.scatter(Blx, Bly, color='blue', marker='s', facecolor='none', label='Linear 3D: $||e||_{L_{2}}=0.0031h^{1.71}$')
# ax.scatter(Bqx, Bqy, color='red', marker='^', facecolor='none', label='Qadratic 3D: $||e||_{L_{2}}=0.0177h^{2.19}$')
# ax.scatter(C70lx, C70ly, color='gray', marker='o', label='Linear 2D: $||e||_{L_{2}}=0.0194h^{1.82}$')
# ax.scatter(C70qx, C70qy, color='violet', marker='d', label='Qadratic 2D: $||e||_{L_{2}}=0.0197h^{1.95}$')
# ax.plot(fx, Bfl, linestyle="--", color='blue')
# ax.plot(fx, Bfq, linestyle="--", color='red')
# ax.plot(fx, f70l, linestyle="--", color='gray')
# ax.plot(fx, f70q, linestyle="--", color='violet')
# ax.plot()
# ax.set_xlabel('Element length (μm)')
# ax.set_xscale('log')
# ax.set_xlim([0.04, 0.8])
# ax.set_ylabel('L$_{2}$ error')
# ax.set_yscale('log')
# ax.set_ylim([8*10.0**-12, 0.6*10.0**-8])
# ax.grid(False)
# leg = ax.legend(loc='lower right', frameon=False)
# leg.set_title('Element order')
# plt.savefig('/Users/joe/Desktop/linqd2D.pdf', dpi=800, bbox_inches="tight")
# plt.show()

# New MOOSE convergence study
# Bqx = [0, 0, 0]
# Bqy = [0, 0, 0]
# Blx = [0, 0, 0]
# Bly = [0, 0, 0]
fx = [0.01, 1.5]
C70lx = [0.281737, 0.1534312, 0.0817]
C70ly = [0.049237246872649965, 0.01989063690102448, 0.005899134270702621]
# C70qx = [0, 0, 0]
# C70qy = [0, 0, 0]

def equation(x, y, eqx):
    l = len(x) - 1
    p = np.log10(y[l]/y[0])/np.log10(x[l]/x[0])
    C = 0
    for i in range(3):
        C += (1/3)*y[i]/(x[i]**p)
    print('C = ', C)
    print('p = ', p)
    eqy = [0, 0]
    for i in range(2):
        eqy[i] = C * eqx[i] ** p
    return eqy
# Bfq = equation(Bqx, Bqy, fx)
# Bfl = equation(Blx, Bly, fx)
f70l = equation(C70lx, C70ly, fx)
# f70q = equation(C70qx, C70qy, fx)

fig, ax = plt.subplots()
# ax.scatter(Blx, Bly, color='blue', marker='s', facecolor='none', label='Linear 3D: $||e||_{L_{2}}=0.0031h^{1.71}$')
# ax.scatter(Bqx, Bqy, color='red', marker='^', facecolor='none', label='Qadratic 3D: $||e||_{L_{2}}=0.0177h^{2.19}$')
ax.scatter(C70lx, C70ly, color='gray', marker='o', label='Linear 2D: $||e||_{L_{2}}=0.453h^{1.714}$')
# ax.scatter(C70qx, C70qy, color='violet', marker='d', label='Qadratic 2D: $||e||_{L_{2}}=0.0197h^{1.95}$')
# ax.plot(fx, Bfl, linestyle="--", color='blue')
# ax.plot(fx, Bfq, linestyle="--", color='red')
ax.plot(fx, f70l, linestyle="--", color='gray')
# ax.plot(fx, f70q, linestyle="--", color='violet')
ax.plot()
ax.set_xlabel('Element length (μm)')
ax.set_xscale('log')
ax.set_xlim([0.04, 0.8])
ax.set_ylabel('L$_{2}$ error')
ax.set_yscale('log')
ax.set_ylim([1e-4, 1e-1])
ax.grid(False)
leg = ax.legend(loc='lower right', frameon=False)
leg.set_title('Element order')
plt.savefig('/Users/joe/Desktop/linqd2D.pdf', dpi=800, bbox_inches="tight")
plt.show()

# Toy problem convergence study
fx = [0.01, 1.5]
C70lx = [1, 0.5, 0.25]
C70ly = [0.404420928, 0.20564558, 0.10859519]
C70qx = [1, 0.5, 0.25]
C70qy = [0.566705153, 0.097948254, 0.026901775]

def equation(x, y, eqx):
    l = len(x) - 1
    p = np.log10(y[l]/y[0])/np.log10(x[l]/x[0])
    C = 0
    for i in range(3):
        C += (1/3)*y[i]/(x[i]**p)
    print('C = ', C)
    print('p = ', p)
    eqy = [0, 0]
    for i in range(2):
        eqy[i] = C * eqx[i] ** p
    return eqy
f70l = equation(C70lx, C70ly, fx)
f70q = equation(C70qx, C70qy, fx)

fig, ax = plt.subplots()
ax.scatter(C70lx, C70ly, color='gray', marker='o', label='Linear 2D: $||e||_{L_{2}}=0.001h^{0.95}$')
ax.scatter(C70qx, C70qy, color='violet', marker='d', label='Qadratic 2D: $||e||_{L_{2}}=0.0004h^{2.20}$')
ax.plot(fx, f70l, linestyle="--", color='gray')
ax.plot(fx, f70q, linestyle="--", color='violet')
ax.plot()
ax.set_xlabel('Element length (μm)')
ax.set_xscale('log')
ax.set_xlim([0.1, 1.5])
ax.set_ylabel('L$_{2}$ error')
ax.set_yscale('log')
ax.set_ylim([1e-4, 7e-1])
ax.grid(False)
leg = ax.legend(loc='lower right', frameon=False)
leg.set_title('Element order')
ax.set_title('Convergence study with unevenly distributed loading (sinusoidal)')
plt.savefig('/Users/joe/Desktop/convergence.pdf', dpi=800, bbox_inches="tight")
plt.show()
# Toy problem convergence study
fx = [0.01, 1.5]
C70lx = [1, 0.5, 0.25]
C70ly = [0.372148957, 0.145814845, 0.039428335]
C70qx = [1, 0.5, 0.25]
C70qy = [0.024558453, 0.015362063, 0.004153902]

def equation(x, y, eqx):
    l = len(x) - 1
    p = np.log10(y[l]/y[0])/np.log10(x[l]/x[0])
    C = 0
    for i in range(3):
        C += (1/3)*y[i]/(x[i]**p)
    print('C = ', C)
    print('p = ', p)
    eqy = [0, 0]
    for i in range(2):
        eqy[i] = C * eqx[i] ** p
    return eqy
f70l = equation(C70lx, C70ly, fx)
f70q = equation(C70qx, C70qy, fx)

fig, ax = plt.subplots()
ax.scatter(C70lx, C70ly, color='gray', marker='o', label='Linear 2D: $||e||_{L_{2}}=0.372h^{1.62}$')
ax.scatter(C70qx, C70qy, color='violet', marker='d', label='Qadratic 2D: $||e||_{L_{2}}=0.024h^{1.28}$')
ax.plot(fx, f70l, linestyle="--", color='gray')
ax.plot(fx, f70q, linestyle="--", color='violet')
ax.plot()
ax.set_xlabel('Element length (μm)')
ax.set_xscale('log')
ax.set_xlim([0.1, 1.5])
ax.set_ylabel('L$_{2}$ error')
ax.set_yscale('log')
ax.set_ylim([1e-4, 5e-1])
ax.grid(False)
leg = ax.legend(loc='lower right', frameon=False)
leg.set_title('Element order')
ax.set_title('Convergence study with uniform loading')
plt.savefig('/Users/joe/Desktop/convergence1.pdf', dpi=800, bbox_inches="tight")
plt.show()

# # NN trained using only Exp data
# n = [2, 3, 4, 5, 6, 8, 10, 15]
# expσ = [74.99, 229.59, 41.16, 55.95, 23.93, 13.79, 5.93, 2.27]
# εexpσ = [48.20, 322.59, 18.52, 96.40, 18.64, 9.51, 3.30, 1.74]
# expE = [101.85, 69.65, 16.93, 18.11, 9.79, 4.71, 3.07, 2.56]
# εexpE = [76.39, 54.69, 9.46, 10.72, 6.12, 3.10, 2.16, 4.19]

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
# ax1.errorbar(n, expσ, yerr = εexpσ, color = 'blue', label = "NN, experimental training data")
# ax1.set_yscale('log')
# ax1.set_ylim([1, 1500])
# ax1.set_xlim([-0.5, 16])
# ax1.set_xticks([0, 5, 10, 15])
# #ax1.set_xticklabels([0, 5, 10, 15], fontsize=14)
# ax1.set_xticklabels([0, 5, 10, 15])
# ax1.set_yticks([1, 5, 20, 200, 1500])
# #ax1.set_yticklabels([1, 5, 20, 200, 2000], fontsize=14)
# ax1.set_yticklabels([1, 5, 20, 200, 1500])
# #ax1.legend(fontsize=14, frameon=False)
# ax1.legend(frameon=False)
# ax1.set_ylabel("MAPE (%)")
# ax1.set_xlabel("Experimental training data size")
# ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
#               fontsize=12, ha="center",
#               bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
# #ax1.set_ylabel("MAPE (%)", fontsize=18)
# #ax1.set_xlabel("Experimental training data", fontsize=18)
# #ax1.annotate("A: $\sigma_{y}$", xy=(0.1, 0.95), xycoords="axes fraction",
# #              fontsize=18, ha="center",
# #              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

# ax2.errorbar(n, expE, yerr = εexpE, color = 'blue')
# ax2.set_yscale('log')
# ax2.set_ylim([1, 1500])
# ax2.set_xlim([-0.5, 16])
# ax2.set_xticks([0, 5, 10, 15])
# ax2.set_xticklabels([0, 5, 10, 15])
# #ax2.set_xticklabels([0, 5, 10, 15], fontsize=14)
# ax2.set_yticks([1, 5, 20, 200, 1500])
# ax2.set_yticklabels([1, 5, 20, 200, 1500])
# #ax2.set_yticklabels([1, 5, 20, 200, 2000], fontsize=14)
# ax2.set_ylabel("MAPE (%)")
# ax2.set_xlabel("Experimental training data size")
# plt.subplots_adjust(bottom=0.180)
# fig.tight_layout()
# ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
#               fontsize=12, ha="center",
#               bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
# plt.savefig("/Users/Joe/Desktop/graphs/NN_exp.pdf", dpi=800, bbox_inches="tight")
# #ax2.set_ylabel("MAPE (%)", fontsize=18)
# #ax2.set_xlabel("Experimental training data", fontsize=18)
# #ax2.annotate("B: $E_{r}$", xy=(0.1, 0.95), xycoords="axes fraction",
# #              fontsize=18, ha="center",
# #              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
# #plt.savefig("/Users/Joe/Desktop/NN_exp.pdf", dpi=800, bbox_inches="tight")
# plt.show()

'''
# NN trained using only 3D FEM data
n = [2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [986.74, 68.14, 48.33, 62.06, 25.37, 13.41, 8.88, 3.05]
εquadσ = [2339.3, 74.76, 47.22, 100.05, 19.2, 9.73, 8.6, 1.83]
quadE = [2778.98, 29.71, 16.23, 19.93, 11.04, 2.89, 3.04, 1.54]
εquadE = [7709.45, 26.63, 11.26, 15.32, 6.96, 1.78, 2.08, 1.06]
# Linear
linσ = [266.1, 155.85, 52.86, 38.35, 35, 15.56, 11.59, 5.29]
εlinσ = [239.74, 165.01, 36.87, 15.93, 21, 8.09, 3.81, 3.58]
linE = [232.69, 99.21, 32.35, 15.87, 18.67, 7.28, 5.68, 2.97]
εlinE = [318.25, 147.57, 30.52, 10.15, 15.33, 4.46, 5.21, 3.73]
# Rough quad
rqσ = [6130.41, 93.06, 68.02, 69.92, 23.77, 15.54, 12.41, 8.9]
εrqσ = [17436.26, 102.86, 102.64, 97.61, 19.81, 7.79, 12.34, 13.79]
rqE = [444.95, 63.66, 17.07, 17.74, 8.23, 4.52, 4.15, 1.88]
εrqE = [1017.29, 76.11, 7.92, 25.78, 4.2, 2.98, 3.02, 1.51]
# Rough linear
rlσ = [331.35, 82.95, 35.96, 30.1, 21.16, 8.89, 6.3, 1.71]
εrlσ = [313.91, 91.45, 27.63, 35.86, 14.47, 7.7, 3.96, 2]
rlE = [133.23, 53.87, 19.23, 25.34, 6.98, 6.7, 4.04, 0.9]
εrlE = [155.38, 57.54, 11.61, 42.93, 3.67, 11.62, 3.23, 0.58]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "NN, quadratic 3D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "NN, linear 3D FEM")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "NN, rough quadratic 3D FEM")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "NN, rough linear 3D FEM")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 2000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 5, 20, 200, 2000])
ax1.set_yticklabels([1, 5, 20, 200, 2000])
ax1.legend(frameon=False)
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("3D FEM training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.3, 400])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 100, 400])
ax2.set_yticklabels([1, 5, 20, 100, 400])
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("3D FEM training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/NN_3D.pdf", dpi=800, bbox_inches="tight")
plt.show()


# NN trained using only 2D FEM data
n = [2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [212.94, 94.18, 45.21, 36.36, 43.48, 27.84, 30.22, 11.38]
εquadσ = [198.4, 60.71, 32.85, 25.92, 42.98, 17.2, 29.49, 22.21]
quadE = [148.56, 47.97, 24.67, 18.92, 15.01, 6.97, 5.99, 2.86]
εquadE = [225.48, 47.25, 20.73, 14.04, 10.13, 4.31, 4.14, 3.95]
# Linear
linσ = [2442.06, 123.75, 131.23, 64.36, 41.86, 48.24, 47.69, 143.44]
εlinσ = [5165.55, 121.11, 116.49, 40.47, 38.56,56.27, 98.03, 208.49]
linE = [756.26, 39.38, 42.67, 15.69, 12.98, 7.54, 5.43, 10.7]
εlinE = [1567.03, 50.9, 18.97, 14.32, 11.65, 12.1, 7.56, 14.37]
# Rough quadratic
rqσ = [413.5, 58.08, 18.11, 28.25, 11.46, 7.36, 3.89, 2.45]
εrqσ = [815.19, 79.78, 16.59, 36.32, 5.59, 3.37, 2.83, 3.53]
rqE = [257.90, 37.33, 31.51, 30.03, 8.33, 3.37, 2.55, 1.20]
εrqE = [295.82, 47.03, 62.86, 61.95, 15.46, 2.69, 3.56, 1.31]
# Rough linear
rlσ = [234.01, 27.22, 10.86, 28.07, 12.04, 5.53, 3.48, 0.78]
εrlσ = [330.48, 26.25, 7.01, 37.49, 18.06, 6.16, 7.04, 0.8]
rlE = [231.74, 103.86, 27.39, 11.12, 11.89, 3.97, 3.16, 0.82]
εrlE = [280.37, 148.34, 47.39, 17.79, 10.66, 3.4, 2.58, 0.5]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "NN, quadratic 2D FEM training data")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "NN, linear 2D FEM")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "NN, rough quadratic 2D FEM")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "NN, rough linear 2D FEM")
ax1.set_yscale('log')
ax1.set_ylim([0.3, 2000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 4, 40, 200, 2000])
ax1.set_yticklabels([1, 4, 40, 200, 2000])
ax1.legend(frameon=False)
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("2D FEM training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.2, 1000])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 200, 2000])
ax2.set_yticklabels([1, 5, 20, 100, 1000])
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("2D FEM training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/NN_2D.pdf", dpi=800, bbox_inches="tight")
plt.show()


# NN trained using 3D FEM + exp data
n = [1, 2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [1059.66, 100.98, 92.71, 30.64, 23.04, 17.84, 21.85, 15.16, 10.92]
εquadσ = [636.84, 102.66, 104.39, 19.21, 12.42, 6.85, 10.31, 9.01, 9.78]
quadE = [24.29, 23.16, 10.45, 11.09, 5.52, 5.61, 3.91, 2.93, 1.68]
εquadE = [10.07, 15.14, 9.92, 7.51, 3.91, 5.65, 3.78, 1.88, 1.21]
# Linear
linσ = [1150.53, 73.17, 33.75, 24.88, 18.33, 13.9, 16.63, 8.6, 5.7]
εlinσ = [950.8, 47.15, 17.25, 12.27, 11.61, 14.89, 4.78, 2.92, 3.84]
linE = [43.66, 35.36, 7.44, 8.62, 4.38, 2.61, 1.83, 2.22, 0.89]
εlinE = [41.87, 60.42, 3.24, 7.3, 2.85, 1.57, 0.93, 1.64, 0.48]
# Rough quadratic
rqσ = [1289.19, 241.96, 28.5, 20.11, 11.87, 10.18, 7.99, 4.65, 4.34]
εrqσ = [1046.94, 516.09, 25.18, 14.51, 6.47, 6.28, 4.94, 3.34, 2.8]
rqE = [17.2, 8.37, 2.35, 3.65, 2.54, 1.45, 1.1, 1.26, 0.58]
εrqE = [8.1, 8.44, 2.08, 2.65, 2.5, 1.53, 0.42, 0.85, 0.39]
# Rough linear
rlσ = [1675.69, 21.21, 12.83, 6.27, 5.59, 6.9, 4.63, 6.51, 1.54]
εrlσ = [804.48, 17.93, 9.39, 2.21, 3.41, 4.69, 2.35, 4.95, 0.94]
rlE = [20.15, 5.9, 4.21, 3.32, 1.78, 2.04, 1.53, 1.32, 0.41]
εrlE = [9.95, 4.12, 6.2, 2.25, 1.25, 1.95, 1.1, 1.19, 0.29]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN, quadratic 3D FEM + experiment")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MFNN, linear 3D FEM + experiment")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MFNN, rough quadratic 3D FEM + experiment")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MFNN, rough linear 3D FEM + experiment")
ax1.set_yscale('log')
ax1.set_ylim([1, 2000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 3, 20, 200, 2000])
ax1.set_yticklabels([1, 3, 20, 200, 2000])
ax1.legend(frameon=False)
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.5, 100])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 3, 10, 30, 100])
ax2.set_yticklabels([1, 3, 10, 30, 100])
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/MFNN_3Dexp.pdf", dpi=800, bbox_inches="tight")
plt.show()


# NN trained using 2D FEM + exp data
n = [1, 2, 3, 4, 5, 6, 8, 10, 15]
# Quad
quadσ = [1361.85, 863.64, 123.4, 126.98, 72.64, 60.89, 59.13, 32.84, 13.14]
εquadσ = [1111.76, 1540.86, 50.87, 65.35, 22.83, 20.09, 27.33, 21.3, 11.13]
quadE = [65.44, 34.84, 38.36, 21.29, 11.58, 8.96, 5.74, 4.96, 3.39]
εquadE = [51.47, 32.09, 69.16, 24.89, 6.36, 4.36, 2.89, 5.12, 1.63]
# Linear
linσ = [1723.27, 221, 53.92, 54.41, 83.75, 23.93, 25.42, 23.64, 13.26]
εlinσ = [1685.46, 228.88, 30.26, 25.8, 117.77, 12.7, 27.64, 14.13, 11.15]
linE = [80.47, 15.82, 7.7, 11.13, 6.26, 3.17, 2.25, 2.8, 2.89]
εlinE = [113.42, 12.53, 8.1, 12.09, 3.01, 1.69, 1.77, 2.79, 5.28]
# Rough quadratic
rqσ = [14618, 10.57, 3.33, 1.94, 1.36, 1, 1.07, 0.73, 0.66]
εrqσ = [37534.82, 13.1, 3.41, 1.87, 0.62, 0.38, 0.61, 0.31, 0.23]
rqE = [0.83, 32.76, 0.53, 0.24, 0.26, 0.23, 0.14, 0.1, 0.12]
εrqE = [0.49, 31.93, 0.59, 0.2, 0.15, 0.2, 0.11, 0.05, 0.06]
# Rough linear
rlσ = [2382.1, 2.93, 1.81, 1.12, 0.91, 0.96, 0.81, 0.73, 0.68]
εrlσ = [1759.34, 2.29, 1.25, 0.94, 0.63, 0.33, 0.44, 0.43, 0.55]
rlE = [18.97, 0.3, 0.19, 0.14, 0.16, 0.11, 0.1, 0.05, 0.06]
εrlE = [13.92, 0.23, 0.22, 0.09, 0.21, 0.06, 0.04, 0.03, 0.03]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN, quadratic 2D FEM + experiment")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MFNN, linear 2D FEM + experiment")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MFNN, rought quadratic 2D FEM + experiment")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MFNN, rough linear 2D FEM + experiment")
#ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "quadr 2D FEM + experiment")
#ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "linear 2D FEM + experiment")
#ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "rought quad 2D FEM + experiment")
#ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "rough linear 2D FEM + experiment")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 3000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_xticklabels([0, 5, 10, 15])
#ax1.set_xticklabels([0, 5, 10, 15], fontsize=12)
ax1.set_yticks([1, 5, 50, 500, 3000])
ax1.set_yticklabels([1, 5, 50, 500, 3000])
#ax1.set_yticklabels([1, 5, 50, 500, 3000], fontsize=12)
ax1.legend(frameon=False)
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
#ax1.legend(fontsize=12, frameon=False)
#ax1.set_ylabel("MAPE (%)", fontsize=18)
#ax1.set_xlabel("Experimental training data", fontsize=18)
#ax1.annotate("A: $\sigma_{y}$", xy=(0.1, 0.95), xycoords="axes fraction",
#              fontsize=18, ha="center",
#              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.5, 200])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_xticklabels([0, 5, 10, 15])
#ax2.set_xticklabels([0, 5, 10, 15], fontsize=12)
ax2.set_yticks([1, 5, 20, 50, 200])
ax2.set_yticklabels([1, 5, 20, 50, 200])
#ax2.set_yticklabels([1, 5, 20, 50, 200], fontsize=12)
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
#plt.subplots_adjust(bottom=0.180, left=0.08, right=0.95, wspace=0.18, hspace=0.5)
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
#ax2.set_ylabel("MAPE (%)", fontsize=18)
#ax2.set_xlabel("Experimental training data", fontsize=18)
#ax2.annotate("A: $\sigma_{y}$", xy=(0.1, 0.95), xycoords="axes fraction",
#              fontsize=18, ha="center",
#              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/MFNN_2Dexp.pdf", dpi=800, bbox_inches="tight")
plt.show()


# NN trained using 2D FEM + 3D FEM + exp data
n = [1, 2, 3, 4, 5, 6, 8, 10, 15]
# Quad lo
quadσ = [871.38, 263.41, 115.62, 53.59, 59.53, 21.74, 17.79, 9.61, 5.69]
εquadσ = [1226.36, 240.95, 166.55, 29.94, 45.5, 7.92, 7.32, 2.5, 1.69]
quadE = [161.76, 27.14, 35.97, 28.67, 10.65, 13.45, 3.83, 3.23, 0.84]
εquadE = [205.34, 21.01, 42.06, 55.88, 6.1, 12.5, 1.44, 1.5, 0.38]
# Linear lo
linσ = [552.3, 94.28, 58.61, 46.12, 43.19, 20.47, 16.58, 11.12, 4.86]
εlinσ = [441.62, 60.1, 39.11, 15.78, 35.69, 8.91, 7.72, 9.43, 1.86]
linE = [200.11, 138.47, 35.57, 7.11, 6.17, 5.41, 2.73, 1.92, 0.65]
εlinE = [184.05, 317.07, 56.48, 3.59, 3.72, 4.81, 1.32, 1.91, 0.57]
# Rough quadratic lo
rqσ = [213.68, 11.13, 13.18, 5.18, 3.36, 2.83, 0.92, 0.83, 0.7]
εrqσ = [314.93, 9.34, 11.19, 3.5, 1.37, 1.67, 0.29, 0.45, 0.23]
rqE = [48.12, 8.01, 3.2, 1.35, 0.75, 0.68, 0.15, 0.12, 0.09]
εrqE = [39.6, 6.53, 2.23, 0.9, 0.38, 0.52, 0.08, 0.04, 0.03]
# Rough linear lo
rlσ = [63.52, 9.18, 6.64, 1.57, 1.93, 1.57, 1.14, 0.84, 0.58]
εrlσ = [70, 7.01, 4.87, 0.58, 0.87, 1.39, 0.28, 0.35, 0.18]
rlE = [11.48, 3.26, 0.61, 0.26, 0.26, 0.18, 0.09, 0.1, 0.05]
εrlE = [4.86, 2.47, 0.61, 0.2, 0.21, 0.13, 0.05, 0.03, 0.02]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN, quadratic 2D & 3D FEM low training")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MFNN, linear FEM + experiment")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MFNN, rough quadratic FEM + experiment")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MFNN, rough linear FEM + experiment")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 1000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 5, 20, 100, 1000])
ax1.set_yticklabels([1, 5, 20, 100, 1000])
ax1.legend(frameon=False)
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.5, 500])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 5, 20, 100, 500])
ax2.set_yticklabels([1, 5, 20, 100, 500])
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/MFNN_2D3Dexp_lo.pdf", dpi=800, bbox_inches="tight")
plt.show()


# NN trained using 2D FEM + 3D FEM + exp data
n = [1, 2, 3, 4, 5, 6, 8, 10, 15]
# Quad hi
quadσ = [58114.36, 341.14, 351.02, 235.6, 175.72, 137.22, 59.99, 44.14, 21.09]
εquadσ = [149848.96, 1243.39, 258.34, 164.15, 140.49, 65.35, 21.89, 18.5, 4.31]
quadE = [176.13, 487.97, 45.47, 21.19, 14.48, 14.53, 12, 10.51, 2.17]
εquadE = [159.43, 458.61, 41.58, 13.95, 4.45, 13.54, 9.93, 12.44, 0.85]
# Linear hi
linσ = [4551.18, 2237.59, 89.47, 173.2, 60.55, 50.27, 35.49, 22.81, 6.1]
εlinσ = [10147.38, 2559.53, 61.26, 147.02, 23.91, 45.5, 38.69, 13.16, 2.14]
linE = [262.42, 831.94, 45.07, 24.43, 15.28, 10.81, 4.93, 2.12, 0.69]
εlinE = [243.41, 1505.22, 51.23, 31.87, 10.25, 15.79, 2.24, 1.41, 0.86]
# Rough quadratic hi
rqσ = [11031.18, 23.43, 8.77, 3.96, 2.75, 1.47, 2.31, 1.13, 0.56]
εrqσ = [20684.23, 18.78, 7.55, 1.88, 2.2, 0.83, 2.28, 0.15, 0.31]
rqE = [71.47, 20.03, 3.74, 3.92, 0.7, 0.73, 0.36, 0.21, 0.09]
εrqE = [104.42, 44.15, 3.68, 9, 0.69, 1.04, 0.34, 0.13, 0.02]
# Rough linear hi
rlσ = [4147.81, 48.35, 4.56, 3.83, 2.52, 2.04, 0.83, 1, 0.52]
εrlσ = [3015.84, 60.55, 2.67, 3.4, 1.27, 1.36, 0.47, 0.75, 0.32]
rlE = [149.93, 2.3, 1.86, 0.99, 0.37, 0.42, 0.24, 0.15, 0.07]
εrlE = [230.24, 2.62, 2.9, 1.54, 0.21, 0.3, 0.13, 0.05, 0.03]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'blue', label = "MFNN, quadratic FEM 2D low + 3D high training")
ax1.errorbar(n, linσ, yerr = εlinσ, color = 'darkorange', linestyle = '--', label = "MFNN, linear FEM training data")
ax1.errorbar(n, rqσ, yerr = εrqσ, color = 'red', linestyle = '-.', label = "MFNN, rough quadratic FEM training data")
ax1.errorbar(n, rlσ, yerr = εrlσ, color = 'green', linestyle = ':', label = "MFNN, rough linear FEM training data")
ax1.set_yscale('log')
ax1.set_ylim([0.5, 2000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([1, 10, 50, 200, 2000])
ax1.set_yticklabels([1, 20, 50, 200, 2000])
ax1.legend(frameon=False)
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadE, yerr = εquadE, color = 'blue')
ax2.errorbar(n, linE, yerr = εlinE, color = 'darkorange', linestyle = '--')
ax2.errorbar(n, rqE, yerr = εrqE, color = 'red', linestyle = '-.')
ax2.errorbar(n, rlE, yerr = εrlE, color = 'green', linestyle = ':')
ax2.set_yscale('log')
ax2.set_ylim([0.5, 1000])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_yticks([1, 20, 50, 200, 1000])
ax2.set_yticklabels([1, 20, 50, 200, 1000])
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/MFNN_2D3Dexp_hi.pdf", dpi=800, bbox_inches="tight")
plt.show()


# Comparison of different MFNNs
n = [1, 2, 3, 4, 5, 6, 8, 10, 15]
n_1 = [2, 3, 4, 5, 6, 8, 10, 15]
expσ = [1059.66, 100.98, 92.71, 30.64, 23.04, 17.84, 21.85, 15.16, 10.92]
εexpσ = [636.84, 102.66, 104.39, 19.21, 12.42, 6.85, 10.31, 9.01, 9.78]
expE = [24.29, 23.16, 10.45, 11.09, 5.52, 5.61, 3.91, 2.93, 1.68]
εexpE = [10.07, 15.14, 9.92, 7.51, 3.91, 5.65, 3.78, 1.88, 1.21]
# Quad 2
quad2σ = [459.25, 57.65, 37.62, 25.06, 21.03, 15.31, 10.36, 5.07]
εquad2σ = [782.72, 23.27, 20.01, 10.49, 15.46, 6.43, 5.35, 3.07]
quad2E = [252.46, 68.7, 31.93, 20.65, 10.36, 4.55, 2.33, 0.75]
εquad2E = [374.75, 82.24, 33.76, 25.67, 5.88, 3, 1.99, 0.64]
# Quad hi
quadσ = [58114.36, 341.14, 351.02, 235.6, 175.72, 137.22, 59.99, 44.14, 21.09]
εquadσ = [149848.96, 1243.39, 258.34, 164.15, 140.49, 65.35, 21.89, 18.5, 4.31]
quadE = [176.13, 487.97, 45.47, 21.19, 14.48, 14.53, 12, 10.51, 2.17]
εquadE = [159.43, 458.61, 41.58, 13.95, 4.45, 13.54, 9.93, 12.44, 0.85]
# Quad lo
quadlσ = [871.38, 263.41, 115.62, 53.59, 59.53, 21.74, 17.79, 9.61, 5.69]
εquadlσ = [1226.36, 240.95, 166.55, 29.94, 45.5, 7.92, 7.32, 2.5, 1.69]
quadlE = [161.76, 27.14, 35.97, 28.67, 10.65, 13.45, 3.83, 3.23, 0.84]
εquadlE = [205.34, 21.01, 42.06, 55.88, 6.1, 12.5, 1.44, 1.5, 0.38]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.errorbar(n, quadlσ, yerr = εquadlσ, color = 'blue', label = "MFNN, quadratic 2D & 3D FEM low training")
ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'darkorange', linestyle = '--', label = "MFNN, quadratic 2D low + 3D FEM high")
ax1.errorbar(n_1, quad2σ, yerr = εquad2σ, color = 'red', linestyle = '-.', label = "MFNN, quadratic 3D low")
ax1.errorbar(n, expσ, yerr = εexpσ, color = 'green', linestyle = ':', label = "NN, experimental data")
#ax1.errorbar(n, quadlσ, yerr = εquadlσ, color = 'blue')
#ax1.errorbar(n, quadσ, yerr = εquadσ, color = 'darkorange', linestyle = '--')
#ax1.errorbar(n_1, quad2σ, yerr = εquad2σ, color = 'red', linestyle = '-.')
#ax1.errorbar(n, expσ, yerr = εexpσ, color = 'green', linestyle = ':')
ax1.set_yscale('log')
ax1.set_ylim([0.5, 2000])
ax1.set_xlim([-0.5, 16])
ax1.set_xticks([0, 5, 10, 15])
ax1.set_xticklabels([0, 5, 10, 15])
#ax1.set_xticklabels([0, 5, 10, 15], fontsize=12)
ax1.set_yticks([1, 10, 100, 500, 2000])
ax1.set_yticklabels([1, 20, 100, 500, 2000])
#ax1.set_yticklabels([1, 20, 100, 500, 2000], fontsize=12)
ax1.legend(frameon=False)
ax1.set_ylabel("MAPE (%)")
ax1.set_xlabel("Experimental training data size")
ax1.annotate("A: $\sigma_{y}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
#ax1.set_ylabel("MAPE (%)", fontsize=18)
#ax1.set_xlabel("Experimental training data", fontsize=18)
#ax1.annotate("A: $\sigma_{y}$", xy=(0.1, 0.95), xycoords="axes fraction",
#              fontsize=18, ha="center",
#              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

ax2.errorbar(n, quadlE, yerr = εquadlE, color = 'blue', label = "quad 2D & 3D low training")
ax2.errorbar(n, quadE, yerr = εquadE, color = 'darkorange', linestyle = '--', label = "quad 2D low + 3D hi")
ax2.errorbar(n_1, quad2E, yerr = εquad2E, color = 'red', linestyle = '-.', label = "quad 3D low")
ax2.errorbar(n, expE, yerr = εexpE, color = 'green', linestyle = ':', label = "experiment only")
ax2.set_yscale('log')
ax2.set_ylim([0.5, 1000])
ax2.set_xlim([-0.5, 16])
ax2.set_xticks([0, 5, 10, 15])
ax2.set_xticklabels([0, 5, 10, 15])
#ax2.set_xticklabels([0, 5, 10, 15], fontsize=12)
ax2.set_yticks([1, 5, 20, 100, 1000])
ax2.set_yticklabels([1, 5, 20, 100, 1000])
#ax2.set_yticklabels([1, 5, 20, 100, 1000], fontsize=12)
#ax2.legend(fontsize=12)
ax2.set_ylabel("MAPE (%)")
ax2.set_xlabel("Experimental training data size")
plt.subplots_adjust(bottom=0.180)
#plt.subplots_adjust(bottom=0.180, left=0.08, right=0.95, wspace=0.18, hspace=0.5)
fig.tight_layout()
ax2.annotate("B: $E_{r}$", xy=(0.05, 0.95), xycoords="axes fraction",
              fontsize=12, ha="center",
              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
#ax2.set_ylabel("MAPE (%)", fontsize=18)
#ax2.set_xlabel("Experimental training data", fontsize=18)
#ax2.annotate("B: $E_{r}$", xy=(0.1, 0.95), xycoords="axes fraction",
#              fontsize=18, ha="center",
#              bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
plt.savefig("/Users/Joe/Desktop/NN_graphs/NN_MFNN_compare.pdf", dpi=800, bbox_inches="tight")
plt.show()
'''