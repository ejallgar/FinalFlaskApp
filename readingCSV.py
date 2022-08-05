import pandas as pd
from datetime import datetime

class ReadingCSV:

  """Constructor Method"""
  def __init__(self):

    #GET DATA FROM CSV FILE (READ)
    #Converts the timestamp to a panda date format
    #Splits date and time into seperate columns
    self.df = pd.read_csv("data/weatherdata.csv")
    self.df['Date'] = pd.to_datetime(self.df['timestamp']).dt.date
    self.df['Time'] = pd.to_datetime(self.df['timestamp']).dt.time

  """Testing PRINT OUT ALL DATA"""
  def printAll(self):
    print(self.df)

  """Method to fillter csv by start and end time"""
  def filterbytime (self, start,end):
    # Filter data by date
    #date = datetime.strptime('2022-07-24', '%Y-%m-%d').date()
    #filtered_dates = self.df.loc[self.df["Date"] <= date]
    #Filter by time
    start_time = datetime.strptime(start, '%H:%M:%S').time()
    end_time = datetime.strptime(end, '%H:%M:%S').time()

    after_start_time = self.df["Time"] >= start_time
    before_end_time = self.df["Time"] <= end_time
    between_two_times = after_start_time & before_end_time
    filtered_times = self.df.loc[between_two_times,["timestamp","humidity","temp"]]
    
    #filtered_dates = self.df.loc[self.df["Time"] <= end_time]

    return filtered_times

if __name__ == '__main__':
  data = ReadingCSV()
  #data.printAll()
  print(data.filterbytime())
    