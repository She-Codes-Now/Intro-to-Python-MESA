# An example of the process of data analysis using Python 3
#  Get Data,  Prepare data, Analyze Data, Present Data.

#http://pandas.pydata.org/pandas-docs/version/0.20/10min.html
import pandas
import sys
from  matplotlib import pyplot
from numpy import arange


# Plot Functions
def barplot(labels,data):
    pos=arange(len(data))
    pyplot.figure()
    pyplot.xticks(pos+0.4,labels)
    pyplot.bar(pos,data)
    pyplot.savefig('barplot')
    #pyplot.show()


def scatterplot(x,y):
    pyplot.plot(x,y,'b.')
    pyplot.xlim(min(x)-1,max(x)+1)
    pyplot.ylim(min(y)-1,max(y)+1)
    pyplot.show()

def boxplot(labels,data):
    pos=arange(len(data))
    pyplot.figure()
    data.plot.box()
    pyplot.savefig('boxplot')
    #pyplot.show()

print('Python version ' + sys.version)
print('Pandas version ' + pandas.__version__)

print ('---- Beginning of Data Acquisition ------')
ifile="degrees-that-pay-back.csv"

degreesFile = pandas.read_csv(ifile)

print ('---- End of Data Acquisition ------')
#------------------------------------------------------


print ('---- Beginning of Transformation -------')
# Transform data
print ("# of records in file: %d" % len(degreesFile))
print ( " Fields in file %s" % ifile)
print (degreesFile.dtypes) # View the fields and datatypes.

#Remove $ from fields - https://stackoverflow.com/questions/14345739/replacing-part-of-string-in-python-pandas-dataframe
#degreesFile['Starting Median Salary'] = degreesFile['Starting Median Salary'].str.replace('$','')

degreesFile['Starting Median Salary'] = degreesFile['Starting Median Salary'].str.replace('$','')
degreesFile['Starting Median Salary'] = degreesFile['Starting Median Salary'].str.replace(',','')

degreesFile['Mid-Career Median Salary'] = degreesFile['Mid-Career Median Salary'].str.replace('$','')
degreesFile['Mid-Career Median Salary'] = degreesFile['Mid-Career Median Salary'].str.replace(',','')

degreesFile['Mid-Career 10th Percentile Salary'] = degreesFile['Mid-Career 10th Percentile Salary'].str.replace('$','')
degreesFile['Mid-Career 10th Percentile Salary'] = degreesFile['Mid-Career 10th Percentile Salary'].str.replace(',','')

degreesFile['Mid-Career 25th Percentile Salary'] = degreesFile['Mid-Career 25th Percentile Salary'].str.replace('$','')
degreesFile['Mid-Career 25th Percentile Salary'] = degreesFile['Mid-Career 25th Percentile Salary'].str.replace(',','')


degreesFile['Mid-Career 75th Percentile Salary'] = degreesFile['Mid-Career 75th Percentile Salary'].str.replace('$','')
degreesFile['Mid-Career 75th Percentile Salary'] = degreesFile['Mid-Career 75th Percentile Salary'].str.replace(',','')


degreesFile['Mid-Career 90th Percentile Salary'] = degreesFile['Mid-Career 90th Percentile Salary'].str.replace('$','')
degreesFile['Mid-Career 90th Percentile Salary'] = degreesFile['Mid-Career 90th Percentile Salary'].str.replace(',','')

#Change columns to float type
degreesFile['Mid-Career 10th Percentile Salary'] = degreesFile['Mid-Career 10th Percentile Salary'].astype(float)
degreesFile['Mid-Career 25th Percentile Salary'] = degreesFile['Mid-Career 25th Percentile Salary'].astype(float)
degreesFile['Mid-Career 75th Percentile Salary'] = degreesFile['Mid-Career 75th Percentile Salary'].astype(float)
degreesFile['Mid-Career 90th Percentile Salary'] = degreesFile['Mid-Career 90th Percentile Salary'].astype(float)
degreesFile['Starting Median Salary'] = degreesFile['Starting Median Salary'].astype(float)
degreesFile['Mid-Career Median Salary'] = degreesFile['Mid-Career Median Salary'].astype(float)

print ('---- End of Transformation ------')
#-----------------------------------------
print ('---- Beginning of Analysis -------')

print (degreesFile.dtypes)

#print degreesFile['Starting Median Salary']

print ('---- End of Analysis ------')

#-----------------------------------------
print ('---- Beginning of Visualization -------')
# Visualization : Create graph

#matplotlib.use('gplot')
boxplot(degreesFile['Undergraduate Major'], degreesFile['Mid-Career Median Salary'])

print ('---- End of Visualization -------')


