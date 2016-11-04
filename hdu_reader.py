#import astropy and then fits
from astropy.io import fits
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
