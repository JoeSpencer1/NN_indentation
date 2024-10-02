import numpy as np

ab = 65.27 #https://doi.org/10.1557/s43578-021-00113-9
ac = np.arctan(np.sqrt(3*np.sqrt(3)*np.tan(ab*np.pi/180)**2/np.pi))*180/np.pi #https://www.sci-hub.ren/10.1007/978-1-4419-9872-9
#ac = 70.32 Is inaccurate.
r = 0.13826
h = 1
d = 1.6#2

ab *= np.pi/180
ac *= np.pi/180

print('2D geometry:')
print('Conical angle: ', ac*180/np.pi)
r1 = r/np.cos(np.arctan(np.tan(ab)*2))
r2 = r1*np.cos(np.pi/3)+r*np.sin(np.pi/3)
Al = r2*r1*np.pi-r2**2*np.sqrt(3)*6/2
le = (1+r/np.cos(np.pi/2-ab)-r)*np.tan(ab)
A = le**2*3*np.sqrt(3)+Al
rn = np.sqrt(A/np.pi)
rc = (rn - np.tan(ac))/(np.tan(ac)*(1/np.sin(ac)-1))
print('Fillet radius: ', rc)
print('Fillet x = ', rc*np.sin(np.pi/2-ac))
print('Fillet y = ', rc*(1-np.cos(np.pi/2-ac)))
print('Edge y = ', rc*(1-np.cos(np.pi/2-ac))+(d-rc*np.sin(np.pi/2-ac))/np.tan(ac))

print('3D geometry:')
print('Second angle: ', np.arctan(np.tan(ab)*2)*180/np.pi)
ab2 = np.arctan(np.tan(ab)/np.cos(60*np.pi/180))
print('Top tip x = ', (h+r/np.sin(ab2)-r)*np.tan(ab2))
print('Bottom radius: ', r*np.cos(ab2))
print('Translate: ', r/np.sin(ab2)-r)