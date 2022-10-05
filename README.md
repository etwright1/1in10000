# 1 in 10,000 casualty area threshold plot

This is the github repository for the code used to make the 1 in 10,000 casualty area threshold plot used in:

Byers, M., Wright, E., Boley, A., Byers, C. (2022). Unnecessary risks created by uncontrolled rocket reentries.  23rd Advanced Maui Optical and Space Surveillance Technologies (AMOS) Conference, Maui, Hawaii.

It is based on a plot by S. Lemmens, Q. Funke, H. Krag, and S. Frey of the European Space Agency [1].

## Plot

<img width="886" alt="image" src="https://user-images.githubusercontent.com/91041692/194122250-f037671c-2eea-48cf-bbc8-e65640533e73.png">

## Method

The code calculates the casualty expectation per spacecraft inclination angle using a method outlined in [2] and our previous work [3], using population data from GPWv4 [4]. 

The casualty expectation per inclination angle is then converted to a critical casualty area to adhere to the 1 in 10,000 risk threshold. 

Using growth rates from the UN World Population Prospects 2022 [5], the population is then increased/decreased and the corresponding critical casualty areas calculated, across the files make_future_data.py and make_historical_data.py. The resulting data is combined into combined_data.csv, which is used by plot_final_heatmap.py to make the plot.

The contours on the colorbar were added in a photo editor.

## References

[1] Lemmens, S, Funke, Q., Krag, H., Frey, S., Order of Magnitude Analysis for On-ground Risk from Uncontrolled Re-entries. ESA Clean Space Industrial Days presentation, 2016; https://indico.esa.int/event/128/attachments/736/896/01_CSID_2016-05-25_ROM_Risk_Unontrolled_Reentries_
SLemmens.pdf.

[2] Patera, R. Hazard analysis for uncontrolled space vehicle reentry. J. Spacecr. Rockets 45, 1031–1041 (2008).

[3] Byers, M., Wright, E., Boley, A. et al. Unnecessary risks created by uncontrolled rocket reentries. Nat Astron 6, 1093–1097 (2022). https://doi.org/10.1038/s41550-022-01718-8

[4] Gridded Population of the World, Version 4.11 (GPWv4): UN WPP-Adjusted Population Count (Center for International Earth Science Information Network—CIESIN, 2022); https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-density-rev11

[5] United Nations, Department of Economic and Social Affairs, Population Division (2022). World Population Prospects 2022, Online Edition.
