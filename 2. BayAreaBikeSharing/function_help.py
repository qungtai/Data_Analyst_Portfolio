import csv
from datetime import datetime
def create_station_mapping(station_data):
	station_dict = {}
	with open(station_data, newline='' ) as file_open:
		reader = csv.DictReader(file_open)
		for row in reader:
			station_dict[row['name']] = row['landmark']
	return station_dict

def summarise_data(trip, station, trip_summarised): 
	'''
	This function takes trip and station information and outputs a new
	data file with a condensed summary of major trip information. The
	trip and station arguments will be lists of data files for
	the trip and station information, respectively, while trip_summarised
	specifies the location to which the summarized data will be written.
	'''
	'''
	what we want is
	- tripID
	- Duration from second to minute
	- start date from dateTime to 
		- date 
		- year 
		- month 
		- weekday
	- start station from place to city (land mark)
	- end station from place to city (land mark)
	- subcription_type 
	'''
	station_dict = create_station_mapping(station)
	trip_summmarise_column = ['tripID','duration','start_date','start_year','start_month','start_hour', 'weekday','start_city','end_city','subscription_type']
	with open(trip_summarised, newline='', mode ='w') as write_summary:
		writer = csv.DictWriter(write_summary, delimiter=',',fieldnames=trip_summmarise_column)
		writer.writeheader()
		with open(trip,'r') as read_trip:
			reader = csv.DictReader(read_trip)

			for row in reader:
				new_dict_to_write = {}
				new_dict_to_write['tripID'] = row['Trip ID']

				new_dict_to_write['duration'] = float(row['Duration'])/60
				
				trip_date = datetime.strptime(row["Start Date"],"%m/%d/%Y %H:%M")
				new_dict_to_write['start_date'] = trip_date.strftime('%Y-%m-%d')
				new_dict_to_write['start_year'] = trip_date.year
				new_dict_to_write['start_month'] = trip_date.month
				new_dict_to_write['start_hour'] = trip_date.hour
				new_dict_to_write['weekday'] = trip_date.strftime("%A")
				new_dict_to_write['start_city'] = station_dict[row['Start Station']]
				new_dict_to_write['end_city'] = station_dict[row['End Station']]
				new_dict_to_write['subscription_type'] = row['Subscription Type']
				writer.writerow(new_dict_to_write)
def call_summarise_func():
	summarise_data('Database/trip_data.csv','Database/station_data.csv','Database/trip_summarised.csv')


