import pandas as pd

df = pd.read_csv(r"C:\Users\main\Documents\data.csv")
person_name = df['PERSON_NAME']
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
def combined_list (Data_List1, Data_List2, Data_List3, Data_List4, Data_List5):
    Combine_List = Data_List1 + Data_List2 + Data_List3 + Data_List4 + Data_List5
    Final_Vlid_List = set(Combine_List)
    return Final_Vlid_List

def not_combined_list (Data_List1, Data_List2, Data_List3, Data_List4, Data_List5,combine_post_type):
    tot_data = 0
    if len(Data_List1) > 0:
        tot_data = tot_data+1
    tot_data
    if len(Data_List2) > 0:
        tot_data = tot_data+1
    tot_data
    if len(Data_List3) > 0:
        tot_data = tot_data+1
    tot_data
    if len(Data_List4) > 0:
        tot_data = tot_data+1
    tot_data
    if len(Data_List5) > 0:
        tot_data = tot_data+1
    if combine_post_type == "YES":

        x = []
        if len(Data_List3) or len(Data_List4) == 0:
            tot_data = tot_data-1

        post_type_list_combine = Data_List3 + Data_List4
        post_type_list_combine = set(post_type_list_combine)
        post_type_list_combine = list(post_type_list_combine)
        Combine_List = Data_List1 + Data_List2 + post_type_list_combine + Data_List5
        for i in range(max(Combine_List)):
            if Combine_List.count(i) > tot_data-1:
                x.append(i)
        Final_Vlid_List = x
        return Final_Vlid_List
    else:
        x = []
        Combine_List = Data_List1 + Data_List2 + Data_List3 + Data_List4 + Data_List5
        for i in range(max(Combine_List)):
            if Combine_List.count(i) > tot_data-1:
                x.append(i)
        Final_Vlid_List = x
        return Final_Vlid_List



Age_Valid = []
Gender_Valid = []
Recent_Post_Valid = []
Most_Post_Valid = []
Friends_Valid = []
min_age = input("Enter minimum age for the ads, if not applicable, put'na': ")
try:
    min_age = int(min_age)
except ValueError:
    min_age = -1
max_age = input("Enter maximum age for the ads, if not applicable, put'na': ")
try:
    max_age = int(max_age)
except ValueError:
    max_age = -1
Gender_input = input("Enter gender preference for the ads, if not applicable, put'na': ")
Gender_input = Gender_input.upper()
Recent_post = input("Enter user's recent post for the ads, if not applicable, put'na': ")
Recent_post = Recent_post.upper()
Most_Post = input("Enter user's most post for the ads, if not applicable, put'na': ")
Most_Post = Most_Post.upper()
print("Is the ad fine with having the user have")
print(Most_Post)
print("on either their recent or most post? Please enter yes or no: ")
combine_post_type = input()
combine_post_type = combine_post_type.upper()
min_friends = input("Enter user's minimum friends for the ads, if not applicable, put'na': ")
try:
    min_friends = int(min_friends)
except ValueError:
    min_friends = -1
max_friends = input("Enter user's maximum friends for the ads, if not applicable, put'na': ")
try:
    max_friends = int(max_friends)
except ValueError:
    max_friends = -1
print("Would you like to return users who have:")
print("1. With at least one of the above input")
print("2. All the items that were inputted")
combine_or_not = input("Please enter 1 or 2: ")

ad = [ min_age, max_age, Gender_input , Recent_post , Most_Post , min_friends, max_friends]

for i in range(6):

    if ad[i] == "ANY":
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
        if gender[i] == "FEMALE":
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

if combine_or_not == "1":
    Final_Valid = combined_list(Age_Valid, Gender_Valid, Recent_Post_Valid, Most_Post_Valid, Friends_Valid)
elif combine_or_not == "2":
    Final_Valid = not_combined_list(Age_Valid, Gender_Valid, Recent_Post_Valid, Most_Post_Valid, Friends_Valid,combine_post_type)
print("valid users:")
for i in range(len(df)+1):
    if i in Final_Valid:
        print(i,person_name[i-1])
