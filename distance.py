## Functions for distance UF


def calculate_distance_sphere(lat1, long1, lat2, long2, unit='miles'):
    '''
    Calculates the distance on a sphere between any two latitudes and longitudes, in either miles or km.
    Miles is the default.

    Usage: calculate_distance_sphere(lat1, long1, lat2, long2)
    Returns: distance (number)

    Notice latitude and longitude have to be given in absolute numbers: for instance,
    Boston coordinates, for instance, are: (42.3601, -71.057083).

    If they are given as (42.3601 N, 71.057083 W), the letter has to be removed and changed according to
    the definition that says that N and E are positive, and S and W are negative

    '''


    #correction from angles to radians
    import math

    lat1 = lat1*math.pi/180
    long1 = long1*math.pi/180

    lat2 = lat2*math.pi/180
    long2 = long2*math.pi/180
    ######################

    # unit for Earth radius
    if unit == 'miles':
        r_Earth = 3.959e3
        #print('Distance in miles')
    elif unit == 'km':
        r_Earth = 6.356e3
        #print('Distance in km')
    else:
        r_Earth = 1
        #print('Distance in units of Earth radius')

    ## actual formula -> see https://en.wikipedia.org/wiki/Haversine_formula
    angles = (np.sin((lat2-lat1)/2))**2 + np.cos(lat1)*np.cos(lat2)*(np.sin((long2-long1)/2))**2
    dist = 2*r_Earth*np.arcsin(np.sqrt(angles))

    return dist


def assign_distances_single_dataframe(df, col_name, col_lat, col_long, unit='miles'):
    '''
    Calculates the distance between points on a dataframe

    Usage: calculate_distances_single_dataframe(df, col_name, col_lat, col_long)
    Returns: dataframe with distances between any two pairs of locations in the dataframe

    Reads a dataframe with a single column of specific locations `col_name` (e.g., HospName),
    their latitudes (`col_lat`), and longitudes (`col_long`). The default is distance in
    miles, but can also use 'km'.

    '''
    # Number of Hospitals == length of dataframe
    n = len(df)
    print('Total number of hospitals: %s \n' % n)
    print('The final dataframe should have len=%s (number of pairs of locations) \n' % int(n*(n-1)/2))

    # These lists will be used for the final dataframe. If one wants
    # the final dataframe to also have latitudes and longitudes,
    # just to make sure the function is working, one needs to
    # uncomment all the pieces below concerning lat1, long1, lat2, and long2

#     lat1=[]
#     lat2 =[]
#     long1=[]
#     long2 =[]
    loc1=[]
    loc2 =[]
    distance =[]

    for i in range(0, n):

        for j in range(i+1, n):

#             # if wants Latitude and Longitude in the datframe, uncomment these too.
#             lat1.append(df_cities.iloc[i][col_lat])
#             long1.append(df_cities.iloc[i][col_long])
#             lat2.append(df_cities.iloc[j][col_lat])
#             long2.append(df_cities.iloc[j][col_long])

            #Define locations (e.g., HospName) 1 and 2 and append to list that will be used to create dataframe below
            loc1.append(df_cities.iloc[i][col_name])
            loc2.append(df_cities.iloc[j][col_name])

            #uses function of distance sphere to calculate distance
            dist_temp = round(calculate_distance_sphere(df_cities.iloc[i][col_lat], df_cities.iloc[i][col_long],
                                                            df_cities.iloc[j][col_lat], df_cities.iloc[j][col_long],
                                                            unit),1)

            #assign distance to list that will be used to create dataframe below
            distance.append(dist_temp)

            print('Distance between %s and %s is %s %s' % (df_cities.iloc[i][col_name],
                                                            df_cities.iloc[j][col_name],
                                                            round(dist_temp,1), unit))


#     # if wants Latitude and Longitude in the datframe, uncomment the one below  and comment the second one.
#     df_distance = {col_name+'_1':city1, col_name+'_2':city2, 'Lat1':lat1, 'Long1':long1, 'Lat2':lat2, 'Long2':long2,
#                    'Distance_'+unit: distance}
    df_distance = {col_name+'_1':loc1, col_name+'_2':loc2,'Distance_'+unit: distance}


    df_distance = pd.DataFrame(data=df_distance)

    print('\n The final dataframe has len=%s \n' % len(df_distance))

    return df_distance





def assign_distances_two_dataframes(df1, df2, col_name1, col_lat1, col_long1, col_name2, col_lat2, col_long2, unit='miles'):
    '''
    Calculates the distance between points on two separate dataframes

    Usage: assign_distances_two_dataframes(df1, df2, col_name1, col_lat1, col_long1, col_name2, col_lat2, col_long2, unit='miles')
    Returns: dataframe with distances between any two pairs of locations in the dataframe

    Reads two dataframe with a single column of specific locations `col_name1` and col_name2 (e.g., HospName),
    their latitudes (`col_lat1` and `col_lat2`), and longitudes (`col_long1` and `col_long2`). The default is distance in
    miles, but can also use 'km'.

    '''
    # Number of Hospitals == length of dataframe
    n1 = len(df1)
    n2 = len(df2)
    print('Total number of 1: %s \n' % n1)
    print('Total number of 2: %s \n' % n2)
    print('The final dataframe should have len=%s (number of pairs of locations) \n' % int(n1*n2))

    # These lists will be used for the final dataframe. If one wants
    # the final dataframe to also have latitudes and longitudes,
    # just to make sure the function is working, one needs to
    # uncomment all the pieces below concerning lat1, long1, lat2, and long2

#     lat1=[]
#     lat2 =[]
#     long1=[]
#     long2 =[]
    loc1=[]
    loc2 =[]
    distance =[]

    for i in range(0, n1):

        for j in range(0, n2):

#             # if wants Latitude and Longitude in the datframe, uncomment these too.
#             lat1.append(df_cities.iloc[i][col_lat])
#             long1.append(df_cities.iloc[i][col_long])
#             lat2.append(df_cities.iloc[j][col_lat])
#             long2.append(df_cities.iloc[j][col_long])

            #Define locations (e.g., HospName) 1 and 2 and append to list that will be used to create dataframe below
            loc1.append(df1.iloc[i][col_name1])
            loc2.append(df2.iloc[j][col_name2])

            #uses function of distance sphere to calculate distance
            dist_temp = round(calculate_distance_sphere(df1.iloc[i][col_lat1], df1.iloc[i][col_long1],
                                                        df2.iloc[j][col_lat2], df2.iloc[j][col_long2],
                                                        unit),1)

            #assign distance to list that will be used to create dataframe below
            distance.append(dist_temp)

            print('Distance between %s and %s is %s %s' % (df1.iloc[i][col_name1],
                                                           df2.iloc[j][col_name2],
                                                           round(dist_temp,1), unit))


#     # if wants Latitude and Longitude in the datframe, uncomment the one below  and comment the second one.
#     df_distance = {col_name+'_1':city1, col_name+'_2':city2, 'Lat1':lat1, 'Long1':long1, 'Lat2':lat2, 'Long2':long2,
#                    'Distance_'+unit: distance}
    df_distance = {col_name1+'_1':loc1, col_name2+'_2':loc2,'Distance_'+unit: distance}


    df_distance = pd.DataFrame(data=df_distance)

    print('\n The final dataframe has len=%s \n' % len(df_distance))

    return df_distance
