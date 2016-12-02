# radio-eyes
Code to analyze radio sources

**Presentation tips**<br />
* Make sure the axes and title are present and correct for every plot. It's better to have done this within the plotting code, but you can also just correct it within google slides. Things to look for: is it EoR0 or EoR1? What is the frequency range? Is the ra/dec right? <br />
* Make sure the color bar is labelled correctly. We haven't been doing this programmatically, so you might want to just do this in google slides. <br />
  * If it is on a linear scale (and you have normalized properly!), it should be roughly in janskys. Label it with Jy <br />
  * If it is on a log scale (and you have normalized properly!), it should be in log(Jy). Label it with log(Jy). <br />
  * You should probably calculate the center spot and the lobes in Jy and have it written down somewhere in case someone asks you. Let's say your log color bar says the center spot is at about 0 in log(Jy) and the lobes are at about -5 in log(Jy). Then to calculate the Jy, you need to solve for 0 = log(x) and -5 = log(y). <br />
* Tell the audience if the object has another name (NGC 253 or Fornax A). If it's one of the faint objects, say "we haven't found it in other surveys" or something to that effect.<br />
* If you want to show difference plots, show the two things you've subtracted first. This will help the audience be on the same page. <br />
* You might have edge effects due to binning on the edges of your image. They are just an artifact of how we plotted things...they are not physical. You don't have to mention this, but it's good to know about it just in case an audience member gets confused. <br />
* Try to draw conclusions about your images. <br />
  * Is the high or low band brighter?<br />
  * Is the object symmetrical or asymmetrical? <br />
  * Is it faint or bright? Anything less than 1 Jy is definitely faint. Fornax A and NGC 253 are bright. <br />
  * Is it fainter than our quoted reliability? Our survey is "reliable" (things are totally real and not a figment of our imagination/instrument) to 100 mJy (or .1 Jy). How many observations went into this image?<br />
  * Does its structure follow a typical AGN? There are symmetrical and asymmetrical types (see https://ned.ipac.caltech.edu/level5/Urry1/UrryP2.html for a brief description and two examples). You don't have to do this, but who knows, it might be fun. <br />
   * Don't be afraid to get weird. No one knows what these objects look like in our frequency band, and with the faint objects, it's very likely that no one has even seen them before! If you can come up with hypotheses based off of some of the astronomy classes you took this quarter, your professors will beam with pride.
* You'll want to briefly describe the processing before you show images. Try to keep this to about a minute or so. The points you want to hit are: <br />
  * We are taking data from the telescope (the Murchison Widefield Array). However, this data has large, bright point spread functions which make it really hard to know what is going on in the image. You know when you squint at the night sky, there are crosses on the bright points? That happens to a much greater extent in the radio! (Show dirty image). We would like to see the bright sources and compact celestial objects, and we do this using deconvolution. We find the brightest spot within the image, and subtract off a little bit of the flux along with its calculated point spread function. We do this thousands and thousands of times, until there is nothing left! (Show subtracted image) This is where Andi/Teagan and I come in. We were given deconvolved components of two regions of the sky, and told to investigate interesting sources. We took these little bits of flux, or components, and histogrammed them within a region. This creates a reconstructed image of the night sky in the radio.  <br />
  * You might want to mention resolution, at least briefly: Normally, people who look at deconvolved data will "smooth out" their components to match the resolution of the instrument. We are histogramming, which definitely helps, but is not as drastic as the resolution of the instrument. We want to see hyper-resolved objects. Really bright objects will be hyper-resolved...we statistically sample them at a finer resolution due to their brightness. We also want to look at faint objects to see how they look as well, but we show them with the caveat that we would need to think harder about what resolution to show them in. <br />
* I put some images in extra_pres_images that you might want for your presentation. Email me if you want more/variants
  * 1061316296_uniform_Dirty_XX.png: image of the radio sky for the field EoR0 for a two minute observation. This is the image that we get from the instrument. It has point spread functions in it. We use deconvolution to reduce it. <br />
  * 1061316296_uniform_Residual_XX.png: residual (as much flux taken out as possible) image of the radio sky for the field EoR0 for a two minute observation. This is what is leftover after we deconvolve thousands and thousands of times. Edges of the field look worse because we the instrument didn't see it very well. Large-scale ripple is the diffuse synchrotron emission from our own galaxy. <br />
  * MWA_EoR_fields-498 copy.jpg: locations of the EoR0 and EoR1 field on the sky. <br />
  * mwabackground.png: image of one tile from the MWA. There are 128 tiles. You have to credit <br />
  * https://www.flickr.com/photos/icrar/albums/with/72157631041722366 has some more random pictures of the MWA. <br />

**Fields** <br />
* EoR0: Really good data within dec=-10,-40, ra=340,10 (or ra=-20,10 with corrected ra)
* EoR1: Really good data within dec=-10,-40, ra=40,75

**Days** <br />
* Aug23: Field EoR0 (which includes NGC 253) in the high band (182 MHz). There are 94 observations.
* Aug27: Field EoR0 (which includes NGC 253) in the high band (182 MHz). There are 78 observations.
* Aug26: Field EoR0 (which includes NGC 253) in the low band (154 MHz). There are 104 observations.
* Oct23: Field EoR1 (which includes Fornax) in the high band (182 MHz). There are 97 observations.
* Oct24: Field EoR1 (which includes Fornax) in the low band (154 MHz). There are 101 observations.

**Cool things to look at, listed as ra_zoom, dec_zoom** <br />
* NGC 253: [11.7,12.1], [-25.45, -25.15] in EoR0
* Fornax A: [49.5,52], [-38,-39] in EoR1
* Faint double-lobed object: [8.9,9.1], [-30.3,-30.5] in EoR0
* Faint double-lobed with multiple sources nearby: [6.6,7.2], [-30.1, -30.4] in EoR0
* Bright, compact double-lobed object: [57.6,58.4], [-27.4,-28] in EoR1
* Faint double-lobed object 2: [7.4,7.8], [-33.1,-33.4] in EoR0
* Asymmetrical faint double-lobed object: [7.7,8],[-32.8,-33.1] in EoR0
* Faint double-lobed object 3: [5.9,6.1],[-30.25,-30.45] in EoR0

**Goals** <br />
1. Plot EoR0 highband components on a RA/DEC scatter plot. Pixelate and histogram as well? <br />
2. Recreate Patti's plot of NGC 253. Compare across days for stability. Investigate normalization. <br />
3. Create plots of a few bright extended sources in EoR0 <br />
4. Plot EoR0 lowband components and compare extended sources <br />
5. Plot Fornax from EoR1 highband and lowband <br />
6. Plot CasA (highband and lowband?) <br />
7. Cross-correlations <br />

## Key terms

**components**: little point-like portions of flux. Extended source models can be built using many point-like flux components. <br />

**declination**: a celestial (and therefore spherical) coordinate that descibes locations on the sky. Declination traces an arc from the North Celestial pole (+90 degrees) to the South Celestial pole (-90 degrees), or "up" to "down".<br />

**hdu**: Header Data Unit in a fits file <br />

**field of view**: the range in area of the sky that the instrument can see clearly. <br />

**fits files**: Flexible Image Transport System. <br />

**flux density**: the energy absorbed per unit area per unit time. <br />

**galactic diffuse emission**: electrons stuck in the magnetic field of the galaxy emit in the radio. This is bright and large. <br />

**observations**: two minutes worth of data collection. <br />

**right ascension**: a celestial (and therefore spherical) coordinate that descibes locations on the sky. Right ascenion traces an arc around the globe along the equator from 0 to 360 degrees, or "left" to "right".<br />

## Quick github tutorial

**pull** <br />
First, make sure you are fully up-to-date before you push any changes. Run this command in the radio-eyes directory. <br />
`git pull` <br />

**add** <br />
Add the file that you have changed to the local repository. <br />
`git add filename.py` <br />

**commit** <br />
Commit the file you have added to prepare for pushing to the remote repository. Add a little comment that describes the change. <br />
`git commit -m 'Comment'` <br />

**push** <br />
Push the commit to the remote repository. <br />
`git push` <br />

If at any point you are curious about what is in your version of radio-eyes, you can run the command `git status`.
