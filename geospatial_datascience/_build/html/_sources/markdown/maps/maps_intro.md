# Maps and Cartography

<h3>This section covers conventions for map and cartographic design. Here, you will learn about design principles and choices for making what is considered a good map. Examples include ways to organize the elements of the map, structuring data, and color and shape choices for telling different stories with the data.</h3>

<h2>Basic Principles of Graphic Design: The C.R.A.P. Principle</h2>

The abbreviation **C.R.A.P.** stands for *contrast*, *repetition*, *alignment*, and *proximity*.<sup>[1]</sup>

* **Constrast** refers to a state of things being different, for example, the colors red and green. This makes things stand out, which helps users know where to look first.

* **Repetition** refers to consistent elements, for example repeat color choices and bulleted lists when items can be naturally listed. This provides a cohesive look.

* **Alignment** refers to structuring elements into columns and ordering objects. This provides an easy-to-read profile.

* **Proximity** refers the closeness of elements that are associated and/or related.

<h6><sup>[1]</sup>https://saylordotorg.github.io/text_business-information-systems-design-an-app-for-that/s07-01-c-r-a-p-principles-of-graphic-.html

<hr>

<h2>Tuft's Principles of Graphical Excellence</h2>

1. Show the data.
2. Induce the reader to think about the substance, not the methodology, graphic design, or technology used.
3. Avoid distorting what the data says. Graphic design choices are important to conveying the story you want, but can easily disrupt the true meaning if poor choices are made.
4. Present many numbers in a small space.
5. Make large datasets coherent.
6. Encourage the eye to compare. Show enough data to make your point, but not too much as to distract the reader.
7. Stay integrated with statistical and verbal descriptions of a dataset.

<hr>

<h2>Types of Maps</h2>

These are examples of maps that you may often encounter. In the **Graphics Variables** section of this chapter, you will see how graphics are chosen and related for some of these maps.

* **Choropleth maps** consists of varying shades or patterns to depict differences in proportions of a statistic. The shapes in a choropleth map are defined not by the data, but by conventional geographic boundaries (for example, state borders in the United States). Examples of the maps depict population density or income per-capita.
    > **Important:** Choropleth maps should NOT represent raw numbers or absolute values. In a population density choropleth map, the values should be normalized proportions, not the magnitude (i.e. population count).

![Choropleth Map Example](../geospatial_datascience/images/choropleth_example.PNG)

<img src="../geospatial_datascience/images/choropleth_example.PNG" alt="Choropleth Map Example">

* **Heat maps** 

* **Line (network) maps**

* **Point maps**

* **3D and 2.5D maps**


<hr>

<h2>Basic Principles of Creating Effective Maps</h2>

<h3>Rules of Thumb for Spatial Data</sup></h3>

These are a few points regarding rules of thumb for spatial data.<sup>[2]</sup> The full list can be found [here](http://ibis.geog.ubc.ca/~brian/rules_of_thumb/).


> **Rules of thumb in cartography**
* Number of shades of gray distinguishable - 16 max
* Number of legend categories consistently recognized - 5, 7 max
* Symbol sizes should not vary when mapping qualitative data.
* Raw totals should not be mapped using a choropleth map.

> **Rules of thumb in GIS**
* To determine the approximate resolution of vector data, if the "scale" of the data is known -- take the 1000's units, divide by 2 to get the minimum mapping unit in meters (e.g., 1:20,000 - 20/2 - 10 m).
* The resolution of raster data is considered equal to the square root of the cell area.
* An heuristic is a rule of thumb, strategy, trick, simplification, or any other kind of device which drastically limits the search for solutions in large problem spaces.

<h6><sup>[2]</sup>http://ibis.geog.ubc.ca/~brian/rules_of_thumb/</h6>
<hr>

<h2>David Sinton’s Framework for Spatial Data Representation</h2>

|        Example         |         Fixed          |       Controlled       |        Measured        |
|------------------------|------------------------|------------------------|------------------------|
|     Geological Map     |          Time          |          Theme         |        Location        |
|      Census Data       |          Time          |        Location        |          Theme         |
|     Weather Report     |        Location        |          Time          |          Theme         |
|       Tide Table       |          Theme         |        Location        |          Time          |
|    Flood Hydrograph    |        Location        |          Time          |          Theme         |
|     Grid Cell Data     |          Time          |        Location        |          Theme         |
