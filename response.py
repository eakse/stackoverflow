    
for row in rows:
    print("{0} {1} {2} {3} {4}".format(row[0], row[1], row[2], row[3], row[4]))
    
    times = row[0]
    Voltage = row[1]
    Current = row[2]
    Temperature = row[3]
    id = row[4]
        
    Response = {}
    Response['times'] = times
    Response['Voltage'] = Voltage
    Response['Current'] = Current
    Response['Temperature'] = Temperature
    Response['id'] = id  
    
        
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['headers']['Cache-Control'] = 'no-store, no-cache, must-revalidate'
    responseObject['body'] = json.dumps(Response)   
    return responseObject