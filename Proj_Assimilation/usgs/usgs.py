{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f077c438-88c6-43bf-9908-9a2d3f872bef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                         Date    Flow\n",
      "0   2017-12-01 00:00:00-05:00  3355.0\n",
      "1   2017-12-01 01:00:00-05:00  3350.0\n",
      "2   2017-12-01 02:00:00-05:00  3355.0\n",
      "3   2017-12-01 03:00:00-05:00  3350.0\n",
      "4   2017-12-01 04:00:00-05:00  3355.0\n",
      "..                        ...     ...\n",
      "763 2018-01-01 19:00:00-05:00  2760.0\n",
      "764 2018-01-01 20:00:00-05:00  2785.0\n",
      "765 2018-01-01 21:00:00-05:00  2790.0\n",
      "766 2018-01-01 22:00:00-05:00  2800.0\n",
      "767 2018-01-01 23:00:00-05:00  2815.0\n",
      "\n",
      "[768 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "This code will grab USGS streamflow data for a defined period of interest \n",
    "\n",
    "'''\n",
    "\n",
    "# first import the functions for downloading data from NWIS\n",
    "import dataretrieval.nwis as nwis\n",
    "import pandas as pd\n",
    "\n",
    "# specify the USGS site code for which we want data.\n",
    "site = ['01054500']\n",
    "\n",
    "# get instantaneous values (iv)\n",
    "df = nwis.get_record(sites=site, service='iv', start='2017-12-01', end='2018-01-01')\n",
    "df.reset_index(inplace=True) #reset index to grab station date\n",
    "df_quarter = df.iloc[:,0:2] #locates every row by the columns we want (date and flow)\n",
    "df_quarter.columns = ['Date', 'Flow'] # rename column headers \n",
    "#print(df_quarter)\n",
    "\n",
    "## Make copy od dataframe to average flow every hour \n",
    "df_copy = df.copy()\n",
    "df_copy['datetime'] = pd.to_datetime(df_copy['datetime']) #convert datetime to average every hour \n",
    "#df_copy.reset_index(inplace=True) #reset indexes so can grab \"Date\" column\n",
    "#df_copy.drop(\"datetime\", axis=1, inplace=True) #drop unneccsary date column now \n",
    "df_copy.index = df_copy['datetime'] # index so can pull date time in resample\n",
    "df_avg = df_copy.resample('H').mean() # Average every hour based on datetime\n",
    "df_avg.reset_index(inplace=True) #reset index again to have datetime \n",
    "df_avgflow = df_avg.iloc[:,0:2] #locates every row by the columns we want (date and flow)\n",
    "df_avgflow.columns = ['Date', 'Flow']\n",
    "print(df_avgflow)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a37d26a-9601-48d8-b1e6-b210d436cc48",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb3dbd21-2da7-4cae-b565-d689d60e6dfc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:root] *",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
