# radio-eyes
Code to analyze radio sources

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
