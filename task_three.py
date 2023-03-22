fhand = open('cereals.csv')

# Version 1 - no RegEx

highest_cold_rating = 0
lowest_cold_rating = 1000
highest_hot_rating = 0
lowest_hot_rating = 1000
avg_cold = 0
avg_hot = 0
hot_count = 0
cold_count = 0

for line in fhand :
    
    # Find the rating of the cereal
    index_start = line.rfind(',')+1
    index_end = len(line) - 1
    rating = line[index_start:index_end]

    # Find the name of the cereal
    index_name = line.find(',')
    name = line[0:index_name]
 
    # Find the highest and lowest rated cold cereal
    if ',C,' in line :
        if float(rating) > float(highest_cold_rating) :
            highest_cold_rating = rating
            best_cold_cereal = name
        if float(rating) < float(lowest_cold_rating) :
            lowest_cold_rating = rating
            worst_cold_cereal = name
        # Update variables required for calculation of average rating
        avg_cold += float(rating)
        cold_count += 1

    # Find the highest and lowest rated hot cereal
    if ',H,' in line :
        if float(rating) > float(highest_hot_rating) :
            highest_hot_rating = rating
            best_hot_cereal = name
        if float(rating) < float(lowest_hot_rating) :
            lowest_hot_rating = rating
            worst_hot_cereal = name
        # Update variables required for calculation of average rating
        avg_hot += float(rating)
        hot_count += 1
    
# Print the results for hot cereal
print('Cereal type: Hot')
print('The lowest cereal rating value: ', lowest_hot_rating, end="")
print('   Cereal name: '+worst_hot_cereal)
print('The average cereal ratings value: ', avg_hot / hot_count)
print('The highest cereal rating value: ', highest_hot_rating, end="")
print('   Cereal name: '+best_hot_cereal)
print()

# Print the results for cold cereal
print('Cereal type: Cold')
print('The lowest cereal rating value: ', lowest_cold_rating, end="")
print('   Cereal name: '+worst_cold_cereal)
print('The average cereal ratings value: ', avg_cold / cold_count)
print('The highest cereal rating value: ', highest_cold_rating, end="")
print('   Cereal name: '+best_cold_cereal)



    

    