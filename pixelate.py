#!/usr/bin/python

import numpy as np

#********************************

#Script written by Nichole Barry, November 2016.

#********************************
#Module that pixelates and histograms in the range of ra_zoom (right ascention) and
#dec_zoom (declination) at the resolution of n_bins. Returns a tuple of 
#the pixel values (summed flux in that bin), the pixel centers in ra, and the pixel
#centers in dec.
def pixelate(ra_zoom, dec_zoom, n_bins, ra_total, dec_total, eyed_total, flux_total):

	#Check to see which dimension is larger so that a square in ra,dec can 
	#be returned
	if (ra_zoom[1]-ra_zoom[0]) > (dec_zoom[1]-dec_zoom[0]):
		zoom = ra_zoom
	else:
		zoom = dec_zoom

	#Find the size of the bins using the largest dimension and the num of bins
	binsize = (zoom[1]-zoom[0])/n_bins

	#Create arrays for ra and dec that give the left side of each pixel
	ra_bin_array = (range(n_bins) * binsize) + ra_zoom[0]
	dec_bin_array = (range(n_bins) * binsize) + dec_zoom[0]

	#Create an empty array of pixels to be filled in the for loops
	pixels = numpy.zeros((len(ra_bin_array),len(dec_bin_array)))

	#Histogram components into ra bins
	np.digitize(ra_total,ra_bin_array,ra_histogram)

	#Begin for loop over both dimensions of pixels, starting with ra
	for bin_i in range(len(ra_bin_array) - 2):

		#Find the indices that fall into the current ra bin slice
		ra_inds = np.where(ra_histogram == bin_i)

		#Go to next for cycle if no indices fall into current ra bin slice
		if len(ra_inds) == 0:
			continue

		#Histogram components that fall into the current ra bin slice by dec
		np.digitize(dec_total[ra_inds],dec_bin_array,dec_histogram)

		#Begin for loop by dec over ra bin slice
		for bin_j in range(len(dec_bin_array) -2):
			
			#Find the indicies that fall into the current dec bin
			dec_inds = np.where(dec_histogram == bin_j)

			#Go to next for cycle if no indices fall into current dec bin			
			if len(dec_inds) == 0:
				continue

			#Sum the flux components that fall into current ra/dec bin
			pixels[bin_i,bin_j] = np.sum(flux_total[ra_inds[dec_inds]])

	#Find the pixel centers in ra/dec for plotting purposes
	ra_pixel_centers = (range(n_bins) * binsize) + ra_zoom[0] + binsize/2.
	dec_pixel_centers = (range(n_bins) * binsize) + dec_zoom[0] + binsize/2.

	return pixels, ra_pixel_centers, dec_pixel_centers
#********************************
