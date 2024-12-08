# Data k následujícím úkolům najdete ve složce 09-arcpy/data - jedná se o liniovou vrstvu silnic a polygonovou vrstvu chráněných území

# Úkol 1
""" 
V rámci Python notebooku nejprve do vrstvy SILNICE_DALNICE vložte nový sloupec, který pojmenujete "kategorie" a který bude typu TEXT. Pokud bude mít linie vyplněný sloupec "JMENO" a délka linie bude větší než 1000, vložte do sloupce "kategorie" hodnotu "01", pokud ne, pak vložte hodnotu "00".
"""

import arcpy
arcpy.management.AddField("SILNICE_DALNICE", "kategorie", "TEXT")

with arcpy.da.UpdateCursor("SILNICE_DALNICE", ["JMENO", "Shape_Leng", "kategorie"]) as cursor:
    for row in cursor:
        if row[0] and row[1] > 1000:
            row[2] = "01"
        else:
            row[2] = "00"
        cursor.updateRow(row)




# Úkol 2
""" Vytvořte pomocí Python notebooku v ArcGISu Pro histogram z vrstvy SILNICE_DALNICE na základě sloupce Shape_Length, který vyexportujete jako svg. Histogram bude rozdělen na 7 sloupců, vytvoře název grafu, pojmenujte osy x a y a přidejte popis grafu. """

import arcpy
chart = arcpy.charts.Histogram("Shape_Leng", binCount=7)
chart.dataSource = "SILNICE_DALNICE"
chart.title = "Delka silnic"
chart.exportToSVG("histogram.svg", width=1000, height=800)




# Úkol 3
""" Vytvořte Python toolbox pro ArcGIS Pro, který bude jako první parametr přijímat vrstvu (v našem případě očekávejme polygonovou vrstvu chráněných území VELKOPLOS_ZVL_CHRAN_UZEMI) a jako druhý parametr bude možné vybrat mezi dvěma hodnotami "min" nebo "max". Na základě toho, jestli uživatel zvolí min nebo max najdete buď rozlohou nejmenší polygon nebo největší a jeho fid_zbg (jedinečný identifikátor) si uložte do proměnné. Následně vytvořte pomocí geoprocessingu ze vstupní polygonové vrstvy bodovou vrstvu (Feature To Point), v této vrstvě najděte podle fid_zbg bod nejmenšího nebo největšího polygonu a vraťte jeho souřadnice a název. 
"""

# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        #Define parameter definitions

        # First parameter
        param0 = arcpy.Parameter(
            displayName="Input Features",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        # Second parameter
        param1 = arcpy.Parameter(
            displayName="Min/Max",
            name="min_max",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        param1.filter.type = "ValueList"
        param1.filter.list = ["min", "max"]

        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        
        # vstupní parametry 
        inFeatures = parameters[0].valueAsText
        minmax = parameters[1].valueAsText
        
        # hodnoty pro porovnávání min a max
        minvalue = float('inf')
        maxvalue = 0
        
        # hodnota,do které si ukládám fid
        final_fid = ""
        
        
        with arcpy.da.SearchCursor(inFeatures, ["NAZEV", "SHAPE_Area", "FID_ZBG"]) as cursor:
            for row in cursor:
                if minmax == "max":
                    if maxvalue < row[1]:
                        maxvalue = row[1]
                        final_fid = row[2]
                elif minmax == "min":
                    if minvalue > row[1]:
                        minvalue = row[1]
                        final_fid = row[2]
                        
        
        output = "C:\\Users\\aneta.ryglova\\Documents\\ArcGIS\\Projects\\hranice\\zk1.gdb\\featuretopoint"
        
        arcpy.management.FeatureToPoint(parameters[0].valueAsText, output)
        
        with arcpy.da.SearchCursor(output, ["NAZEV", "SHAPE", "FID_ZBG"]) as cursor:
            for row in cursor:
                if final_fid == row[2]:
                    arcpy.AddMessage(f"{row[1]}, {row[0]}")
                    
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
