# Widget Trial

from arcgis.gis import GIS

#Create a map widget like you have done many times before
gis = GIS()

webscene_search = gis.content.search(query="LA Trails *", item_type="Web Scene")
webscene_search

webscene_item = webscene_search[2]
webscene_item

from arcgis.mapping import WebScene
la_trails = WebScene(webscene_item)
la_trails





