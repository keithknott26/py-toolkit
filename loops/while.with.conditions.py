# Use of the "While" loop: Run a process repeatedly while certain conditions hold.
# Example here: repeat until raster output has stabilized or maximum iterations reached

# Import required libraries
import arcpy, os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

inRaster = # Reference to your input raster goes here

i = 1 # initialize an iteration counter
NumCells = 1 # initialize a raster cell counter
PreRaster = inRaster # Input raster is designated as the pre-processing raster    
MaxIter = 10 # Maximum number of iterations to run; change number as desired

while NumCells > 0 and i <= MaxIter:
   # Do processing in the loop while there are still cells meeting the condition
   PostRaster = # Your function producing PostRaster goes here
   
   # Save the output, keeping track of iteration number
   # You may or may not want to do this. If there are many iterations you could clog up your disk.
   OutRaster = [path] + os.sep + "Iter" + str(i) 
   PostRaster.save(OutRaster)
   
   # Make a binary raster where changed cells are coded 1, unchanged cells coded 0
   BinRaster = (Raster(PreRaster) != Raster(PostRaster))
   
   # Determine the number of cells that have changed
   rows = arcpy.SearchCursor (BinRaster, "Value = 1", "", "Count", "")
   row = rows.next()
   if row:
      NumCells = row.getValue("Count")
   else:
      NumCells = 0

   # Get set for next iteration
   i += 1 # increment the iteration counter by 1
   PreRaster = PostRaster # the post-processing raster becomes the pre-processing raster for next iteration
   
else: 
   # Go on to the next step
   
# The "else" part is optional; see here: https://stackoverflow.com/questions/3295938/else-clause-on-python-while-statement
