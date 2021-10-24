import pandas as pd

df = pd.read_csv(r"C:\Users\main\Documents\data2.csv")

gender = df['GENDER']
age = df['AGE']
recent_genre = df['RECENT_POST_TYPE']
most_genre = df['MOST_POST_TYPE']
friends = df['FRIENDS_AMOUNT']
# what to do
# ads will need to be filtered. What ads suit best
# ads will have preference for certain type of people. It can distinguish between gender, popular post, recent post, age, and #of friends. This project will determine the best person for a certain ad to be distributed to, and can continue to add more and more distinguish traits.
# First we will need to know what we need to filter. An ad should be published to everyone who have at least one trait on the ad.
# An ad will be put through with its category.
# read in the person who will fit the category, go through all categories.
# ad attribuite. ad = [int,int, "Any_gender","Recent_Post_Type", "Most_Post_Type", int, int, Age low, age high, Gender, Recent_Post_Type, Most_Post_Type, Friends_Amounts


#Find if the user age is in the list that was given.
def numlist_vs_num(numlow, numhigh, user_num):
    length = len(user_num)
    valid = []
    for i in range (length):
        if user_num[i]>= numlow and user_num[i] <= numhigh:
            valid.append(i+1)

    return valid
def Calculate_Valid (Data_List1, Data_List2, Data_List3, Data_List4, Data_List5):
    Comine_List = Data_List1 + Data_List2 + Data_List3 + Data_List4 + Data_List5
    Final_Vlid_List = set(Comine_List)
    return Final_Vlid_List




Age_Valid = []
Gender_Valid = []
Recent_Post_Valid = []
Most_Post_Valid = []
Friends_Valid = []

ad = [ 15, 30, "Not_Applicable", "Not_Applicable", "Not_Applicable", 50, 400]
post = False
for i in range(6):

    if ad[i] == "Any":
        All_Valid = []
        for i in range (len(df)):
            All_Valid.append(i+1)
        print(All_Valid)

if isinstance(ad[0],int):

    Age_Valid = numlist_vs_num(ad[0], ad[1], age)


if ad[2] == "MALE":

    for i in range (len(df)):
        if gender[i] == "MALE":
            Gender_Valid.append(i+1)

if ad[2] == "FEMALE":

    for i in range (len(df)):
        if gender[i] == "MALE":
            Gender_Valid.append(i+1)


#Passing for all kinds of genre for recent posts

if ad[3] == "GAME":

    for i in range (len(df)):
        if recent_genre[i] == "GAME":
            Recent_Post_Valid.append(i+1)

if ad[3] == "FASHION":

    for i in range (len(df)):
        if recent_genre[i] == "FASHION":
            Recent_Post_Valid.append(i+1)

if ad[3] == "MEDIA":

    for i in range (len(df)):
        if recent_genre[i] == "MEDIA":
            Recent_Post_Valid.append(i+1)

if ad[3] == "COMEDY":

    for i in range (len(df)):
        if recent_genre[i] == "COMEDY":
            Recent_Post_Valid.append(i+1)

if ad[3] == "NEWS":

    for i in range (len(df)):
        if recent_genre[i] == "NEWS":
            Recent_Post_Valid.append(i+1)

#Passing for all kinds of genre for most posts
if ad[4] == "GAME":

    for i in range (len(df)):
        if most_genre[i] == "GAME":
            Most_Post_Valid.append(i+1)

if ad[4] == "FASHION":

    for i in range (len(df)):
        if most_genre[i] == "FASHION":
            Most_Post_Valid.append(i+1)

if ad[4] == "MEDIA":

    for i in range (len(df)):
        if most_genre[i] == "MEDIA":
            Most_Post_Valid.append(i+1)

if ad[4] == "COMEDY":

    for i in range (len(df)):
        if most_genre[i] == "COMEDY":
            Most_Post_Valid.append(i+1)

if ad[4] == "NEWS":

    for i in range (len(df)):
        if most_genre[i] == "NEWS":
            Most_Post_Valid.append(i+1)

#for friends amounts
if isinstance(ad[5],int):
    Friends_Valid = numlist_vs_num(ad[5], ad[6], friends)


Final_Valid = Calculate_Valid(Age_Valid, Gender_Valid, Recent_Post_Valid, Most_Post_Valid, Friends_Valid)
print(Final_Valid)
