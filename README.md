###################
###################
# TDLOG_One_Ton_Cup
###################
###################


###########
# WARNING #
###########

So as to run the code, you need to install the custom packages "Helmsman", "Foilsman" and "Wingsman" which contain the menus and widgets for each Crewmate.
For this purpose, you have to enter the following command : 

"pip install -e ."  (don't forget the dot)

in your (anaconda or device) console when located in the folder "Helmsman" (respectively "Foilsman" and "Wingsman"), containing the file "setup.py"
for the Helmsman package (respectively the Foilsman and Wingsman packages).


###################################
# Main caracteristics of the code #
###################################

Origin of the data:
###################

The current version of the code is based on a dataset provided by the .csv file "Random_data_x", where "x" indicates the number of figures given 
for each kind of data. Most of the data contained in this file are unused but can serve as examples for an additional displayed data to one of the crewmates.

Using a .csv file leads to a specific managment of the data. Basically, any function or method which identifier contains "from_pandas" is dedicated 
to this, but there always exists a generic method (typically for constructors) that does not depend on the origin of the data. Nonetheless, these functions/
methods should be written again according to the container of the data used.

Similarly, the class UdpatingValue should be written again in an other context because it assumes that we can only read a limited number of figures for each kind of data.
The methods "widgets_display_and_update" may also be written again, because they assume that we need to visit each line of a file so as to read the new coming data
whereas it's more likely that the new coming data are written in the first line so that we just have to read the first line for update. 


Structure of the view :
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤







######################################
# Necessary improvements of the code #
######################################


Quality of the display :
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤

Windows are shown when a widget is selected (clicking on the corresponding button), whereas a more apropriate view would consist in using the QStackWidget


