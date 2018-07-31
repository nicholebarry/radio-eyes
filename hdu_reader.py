#use python 3 in jupyter
import sys
!conda install --yes --prefix {sys.prefix} astropy
#import astropy and then fits
from astropy.io import fits

#***This is from 11/07/16, read in for obsids from Aug 23
#We have not yet, but plan to build strings that include obsids that point to locations of each fits file
#to be used to open fits files one by one
aug23_obsids_file = open('/astro/users/teagao/radio-eyes/Aug23_obsids.txt', 'r')
aug23 = [line.split( ) for line in aug23_obsids_file.readlines()]


#file name is hardcoded, and in windows DOS
file_name = r'C:\Users\Teagan\Desktop\Aug23_high_EoR0\1061311664_highEoR0.fits'
#header dater unit list- package from astropy to open file
hdu_list = fits.open(file_name)
#details about hdu.list
hdu_list.info()
#call name to read the header to figure out which file
header = hdu_list[1].header
#pulls out actual data from hdu
data = hdu_list[1].data
#id random interger
eyed = data[0]
#declanation random interger
dec = data[1]
#right ascension of the component
ra = data[2]
#the flux density of the component woooo
flux = data[3]

#Things from 11/07/16
#Given the array ra, execute the condition if an element is greater than 180. Reset that element to that
#element minus 360.
#This only works on numpy arrays
ra[ra>180] -= 360


#The following is the code for a scatter plot of EoR0
#dec as y, ra as x
import matplotlib.pyplot as plt
from astropy.io import ascii
#s is size, and marker type is indicated with 'marker'
plt.scatter(ra, dec,
           s = 0.5, color = 'blue', marker= '*')
#Labels for the graph
plt.xlabel('RA (degrees)',
           fontweight='bold', size=14)
plt.ylabel('Declination (degrees)',
           fontweight='bold', size=14)
#This is hardcoded right now, but we will change that at a later time
plt.title('Field: EoR0 at Frequency 182 MHz')
#These are commented out right now, but limits are here to be adjusted to see specific parts of the plot
#This is the location of NGc 253 (probably sculptor galaxy) in degrees
#plt.xlim([11.75, 12.00])
#plt.ylim([-25.2,-25.0])

plt.show()
