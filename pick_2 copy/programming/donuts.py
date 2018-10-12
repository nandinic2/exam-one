scores = [99,51,62,78,88,70,82]
# The scores of the students
def score(arr):
    for x in arr:
        average = (sum(arr))/len(arr)
        # Says that to calculate average one has to take the sum of all the values in the arr and divide it by the number of values.
        if average >= 90:
            donut = len(arr)
            # The number of donuts equals to the number of students.
            return donut
        elif 82 <= average <= 90 :
            donut = len(arr)/2
            # The number of donuts equals to half the number of students because each student gets half a donut.
            return donut
        elif 81 <= average <= 77:
            donut = len(arr)/3
            # The number of donuts equals to one-third of the number of students because each student gets one-third of a donut.
            return donut
        else:
            donut = len(arr)/2
            # The number of donuts equals to half the number of students because each student will only give Mr. James half a donut.
            return donut

print(score(scores))
# This calls the function.
