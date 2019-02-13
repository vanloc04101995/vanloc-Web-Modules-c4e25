
import mlab
from new_bike import New_bike

mlab.connect()

# Create
# 1.1. create a food data
info = New_bike(model = "honda", dailyFee="100000",image="https://auto.ndtvimg.com/bike-images/medium/honda/cbr-250r/honda-cbr-250r.jpg?v=22",year="2013" )
#1.2 save it 
info.save()