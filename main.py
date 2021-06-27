import json
from lat_long_finder import get_lat_long
from location_finder import loc_find
from dist_calc import dist_calc
from report_new_loc import report_new_loc
from search_loc import search_loc

if __name__ == '__main__':
	print("1 for report\n2 for search")
	n=int(input())
	if(n==1):
		report_new_loc()
	elif(n==2):
		print(search_loc())