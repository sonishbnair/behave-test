from influxdb import InfluxDBClient, exceptions
# thehostname = '100.121.54.125'
# thehostport = 8086

#Connecting to the telegraph locally
thehostname = 'localhost'
thehostport = 8186

thedbname = 'selenium'
client = InfluxDBClient(host=thehostname, port=thehostport, database=thedbname)

def send_to_influx(message_dict):
    '''
    Input :
        Message dictionary

    Saple JSON format
     [
        {
            "measurement": "selenium",
            "tags": {
                "host": 'TESTHOST' ,
                "jobtype": "Play" ,
                "target" : "MAM"
            },
            "time": 4,
            "fields": {
                "itemsfound": 10 ,
                "loginduration": 10
            }
        }
      ]
    '''
    print('Inside influx client=================', message_dict)
    try:
        '''
        TO-DO : exception handling
        '''
        print('Influx DB - - - - -  -', client)
        response = client.write_points(message_dict)
        print('Message sent to influx............', response)
    except exceptions.InfluxDBClientError as err:
        print('InfluxDBClientError while writing to Influx...', err)
    except Exception as err:
        print('Error while writing to Influx...', err)
