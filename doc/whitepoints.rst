.. _cie-whiteref:

==================================================
Appendix: CIE Standard Illuminants
==================================================

The CIE standard illuminants are used when converting from the CIE-XYZ system
to CIE L*a*b.


Illuminants Definitions
=========================

Illuminant A
--------------

This is intended to represent typical, domestic, tungsten-filament lighting.
Its relative spectral power distribution is that of a Planckian radiator at
a temperature of approximately 2 856 K.

CIE standard illuminant A should be used in all applications of colorimetry
involving the use of incandescent lighting, unless there are specific reasons
for using a different illuminant.

Illuminants B and C
---------------------

Illuminants B and C are daylight simulators. They are derived from Illuminant A
by using a liquid filters.
B served as a representative of noon sunlight, with a correlated color
temperature (CCT) of 4874 K, while C represented average day light with a CCT
of 6774 K.
They are poor approximations of any common light source and deprecated in favor
of the D series.

Illuminants D
---------------

Derived by Judd, MacAdam, and Wyszecki, the D series of illuminants are
constructed to represent natural daylight.
They are difficult to produce artificially, but are easy to characterize
mathematically.

Illuminant E
--------------

Illuminant E is an equal-energy radiator; it has a constant SPD inside the
visible spectrum. It is useful as a theoretical reference; an illuminant that
gives equal weight to all wavelengths, presenting an even color.
It also has equal CIE XYZ tristimulus values, thus its chromaticity coordinates
are (x,y)=(1/3,1/3).

Illuminant E is not a black body, so it does not have a color temperature,
but it can be approximated by a D series illuminant with a CCT of 5455 K.
(Of the canonical illuminants, D55 is the closest.)

Illuminants F
---------------

The F series of illuminants represent various types of fluorescent lighting.

F1–F6 "standard" fluorescent lamps consist of two semi-broadband emissions of
antimony and manganese activations in calcium halophosphate phosphor.
F4 is of particular interest since it was used for calibrating the CIE Color
Rendering Index (the CRI formula was chosen such that F4 would have a CRI of 51).
F7–F9 are "broadband" (full-spectrum light) fluorescent lamps with multiple
phosphors, and higher CRIs.
Finally, F10–F12 are narrow triband illuminants consisting of three "narrowband"
emissions (caused by ternary compositions of rare-earth phosphors) in the R,G,B
regions of the visible spectrum.

White points
==============

CIE Chromaticity coorinates (x, y)
------------------------------------

The standardized illuminants CIE chromaticity coordinates (x,y) of a perfect
reflecting (or transmitting) diffuser, and their correlated color temperatures
(CCTs) are given below.

The CIE chromaticity coordinates are given for both the 2 degree field of view
(1931) and the 10 degree field of view (1964).

+------+-------------------+---------------------+---------+--------------------------------------------+
|Name  |CIE 1931           |CIE 1964             |CCT      |Note                                        |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|      |x2        |y2      |x10       |y10       |         |                                            |
+======+==========+========+==========+==========+=========+============================================+
|A     |0.44757   |0.40745 |0.45117   |0.40594   |2856 K   |Incandescent tungsten                       |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|B     |0.34842   |0.35161 |0.3498    |0.3527    |4874 K   |Obsolete, direct sunlight at noon           |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|C     |0.31006   |0.31616 |0.31039   |0.31905   |6774 K   |Obsolete, north sky daylight                |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|D50   |0.34567   |0.35850 |0.34773   |0.35952   |5003 K   |ICC Profile PCS. Horizon light.             |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|D55   |0.33242   |0.34743 |0.33411   |0.34877   |5503 K   |Compromise between incandescent and daylight|
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|D65   |0.31271   |0.32902 |0.31382   |0.33100   |6504 K   |Daylight, sRGB color space                  |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|D75   |0.29902   |0.31485 |0.29968   |0.31740   |7504 K   |North sky day light                         |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|E     |1/3       |1/3     |1/3       |1/3       |5454 K   |Equal energy                                |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F1    |0.31310   |0.33727 |0.31811   |0.33559   |6430 K   |Daylight Fluorescent                        |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F2    |0.37208   |0.37529 |0.37925   |0.36733   |4230 K   |Cool White Fluorescent                      |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F3    |0.40910   |0.39430 |0.41761   |0.38324   |3450 K   |White Fluorescent                           |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F4    |0.44018   |0.40329 |0.44920   |0.39074   |2940 K   |Warm White Fluorescent                      |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F5    |0.31379   |0.34531 |0.31975   |0.34246   |6350 K   |Daylight Fluorescent                        |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F6    |0.37790   |0.38835 |0.38660   |0.37847   |4150 K   |Lite White Fluorescent                      |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F7    |0.31292   |0.32933 |0.31569   |0.32960   |6500 K   |D65 simulator, day light simulator          |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F8    |0.34588   |0.35875 |0.34902   |0.35939   |5000 K   |D50 simulator, Sylvania F40 Design          |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F9    |0.37417   |0.37281 |0.37829   |0.37045   |4150 K   |Cool White Deluxe Fluorescent               |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F10   |0.34609   |0.35986 |0.35090   |0.35444   |5000 K   |Philips TL85, Ultralume 50                  |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F11   |0.38052   |0.37713 |0.38541   |0.37123   |4000 K   |Philips TL84, Ultralume 40                  |
+------+----------+--------+----------+----------+---------+--------------------------------------------+
|F12   |0.43695   |0.40441 |0.44256   |0.39717   |3000 K   |Philips TL83, Ultralume 30                  |
+------+----------+--------+----------+----------+---------+--------------------------------------------+


Reference Whitepoints
-----------------------

The reference whitepoints calculated from the values above.

CIE 1931 (*2° Standard Observer*)
...................................

========== ======= ======= ======= ======= =======
Illuminant    x       y       Xn      Yn      Zn
========== ======= ======= ======= ======= =======
A          0,44757 0,40745 1,09847 1,00000 0,35582
B          0,34842 0,35161 0,99093 1,00000 0,85313
C          0,31006 0,31616 0,98071 1,00000 1,18225
D50        0,34567 0,3585  0,96421 1,00000 0,82519
D55        0,33242 0,34743 0,95680 1,00000 0,92148
D65        0,31271 0,32902 0,95043 1,00000 1,08890
D75        0,29902 0,31485 0,94972 1,00000 1,22639
E          0,33333 0,33333 1,00000 1,00000 1,00000
F1         0,3131  0,33727 0,92834 1,00000 1,03665
F2         0,37208 0,37529 0,99145 1,00000 0,67316
F3         0,4091  0,3943  1,03753 1,00000 0,49861
F4         0,44018 0,40329 1,09147 1,00000 0,38813
F5         0,31379 0,34531 0,90872 1,00000 0,98723
F6         0,3779  0,38835 0,97309 1,00000 0,60191
F7         0,31292 0,32933 0,95017 1,00000 1,08630
F8         0,34588 0,35875 0,96413 1,00000 0,82333
F9         0,37417 0,37281 1,00365 1,00000 0,67868
F10        0,34609 0,35986 0,96174 1,00000 0,81712
F11        0,38052 0,37713 1,00899 1,00000 0,64262
F12        0,43695 0,40441 1,08046 1,00000 0,39228
========== ======= ======= ======= ======= =======

CIE 1964 (*10° Observer*)
...........................

========== ======= ======= ======= ======= =======
Illuminant    x       y       Xn      Yn      Zn
========== ======= ======= ======= ======= =======
A          0,45117 0,40594 1,11142 1,00000 0,35200
B          0,3498  0,3527  0,99178 1,00000 0,84349
C          0,31039 0,31905 0,97286 1,00000 1,16145
D50        0,34773 0,35952 0,96721 1,00000 0,81428
D55        0,33411 0,34877 0,95797 1,00000 0,90925
D65        0,31382 0,331   0,94810 1,00000 1,07305
D75        0,29968 0,3174  0,94417 1,00000 1,20643
E          0,33333 0,33333 1,00000 1,00000 1,00000
F1         0,31811 0,33559 0,94791 1,00000 1,03191
F2         0,37925 0,36733 1,03245 1,00000 0,68990
F3         0,41761 0,38324 1,08968 1,00000 0,51965
F4         0,4492  0,39074 1,14961 1,00000 0,40963
F5         0,31975 0,34246 0,93369 1,00000 0,98636
F6         0,3866  0,37847 1,02148 1,00000 0,62074
F7         0,31569 0,3296  0,95780 1,00000 1,07618
F8         0,34902 0,35939 0,97115 1,00000 0,81135
F9         0,37829 0,37045 1,02116 1,00000 0,67826
F10        0,3509  0,35444 0,99001 1,00000 0,83134
F11        0,38541 0,37123 1,03820 1,00000 0,65555
F12        0,44256 0,39717 1,11428 1,00000 0,40353
========== ======= ======= ======= ======= =======
