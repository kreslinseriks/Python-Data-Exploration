# Version 2 - with RegEx
import re

fhand = open('cereals.csv')

# Definition of variables for further operations
highest_cold_rating = 0
lowest_cold_rating = 1000
highest_hot_rating = 0
lowest_hot_rating = 1000
avg_cold = 0
avg_hot = 0
hot_count = 0
cold_count = 0

for line in fhand :

    # Get name of cereal, remove unnecessary characters
    name = str(re.findall('^(.+?),',line))
    name = name[2:len(name) - 2]

    # Get rating of cereal, remove unnecessary characters
    rating = str(re.findall('.*,(.+?)$',line))
    rating = rating[2:len(rating) - 2]

    # Loop through cold cereal
    if re.search('^.*,C,',line) :
        # Update the variables for highest and lowest rated cold cereals
        if float(rating) > float(highest_cold_rating) :
            highest_cold_rating = rating
            best_cold_ceral = name
        if float(rating) < float(lowest_cold_rating) :
            lowest_cold_rating = rating
            worst_cold_cereal = name
        # Update variables for calculation of average rating
        avg_cold += float(rating)
        cold_count += 1
        
    # Loop through hot cereal
    if re.search('^.*,H,',line) :
        # Update the variables for highest and lowest rated hot cereals
        if float(rating) > float(highest_hot_rating) :
            highest_hot_rating = rating
            best_hot_cereal = name
        if float(rating) < float(lowest_hot_rating) :
            lowest_hot_rating = rating
            worst_hot_cereal = name
        # Update variables for calculation of average rating
        avg_hot += float(rating)
        hot_count += 1
    
# Print the results for hot cereal
print('Cereal type: Hot')
print('The lowest cereal rating value: ', lowest_hot_rating, end="")
print('   Cereal name: '+worst_hot_cereal)
print('The average cereal ratings value: ', avg_hot / hot_count)
print('The highest cereal rating value: ', highest_hot_rating, end="")
print('   Cereal name: '+best_hot_cereal+'\n')

# Print the results for cold cereal
print('Cereal type: Cold')
print('The lowest cereal rating value: ', lowest_cold_rating, end="")
print('   Cereal name: '+worst_cold_cereal)
print('The average cereal ratings value: ', avg_cold / cold_count)
print('The highest cereal rating value: ', highest_cold_rating, end="")
print('   Cereal name: '+best_cold_ceral)
