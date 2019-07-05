import pandas as pd
# ===================================================
#       Functions that I used with my analysis
# ===================================================

def check_df(df,option = None):
    if option == 1:
        for index,column in enumerate(df.columns):
            print(index,column)
    elif option==2:
        print(df.describe().T)
    else:
        for index,column in enumerate(df.columns):
            print(index,column)
        print(50*'-')
        print(df.describe().T)
# ===================================================
#       Check if two columns fro two different
#                   df are equal
# ===================================================
def compare_two_columns(column1,column2):
    if column1.any() == column2.any():
        print(f"Yes {column1.name} and {column2.name} are equal")
    else:
        print(f"No {column1.name} and {column2.name} are not equal")

# Such as: compare_two_columns(inner_joint_Int.index,Inters_type_Table.index)
# ===================================================
#       How to find Duplicate in a given column
#         default case: inner_joint_Int.index
# ===================================================
def find_duplicates(df = None):
    list_non_duplicated = []
    list_duplicated2 = []
    location_of_duplicates = []
    counter = 0
    for i in range(len(df)):
        if df[i] not in list_non_duplicated:
            list_non_duplicated.append(df[i])
        else:
            list_duplicated2.append(df[i])
            location_of_duplicates.append(i)
            counter = counter + 1
    for i in range(len(list_non_duplicated)):
        print(list_non_duplicated[i])
    print(list_duplicated2)
    print(10*"-")
    print(f"index of duplicates location \n {location_of_duplicates}")
    print(10*"-")
    print(f"No. of duplicated items = {counter}")
    print(10*"-")


def find_duplicates_with_pandas(col = None):
    # df.get_duplicates()   # is deprected
    print(col[col.duplicated()])
    # Or
    print(col[col.duplicated()].unique())
    # Or
    #print(col.groupby(level=0).filter(lambda x: len(x) > 1)['type'])

def change_to_unique_Data_frame(df):
    '''
        The solution here is used to ensure that all items in the
        index should be unqiue and rename them if they are not
        unique.
        https://stackoverflow.com/questions/43095955/rename-duplicated-index-values-pandas-dataframe
    '''
    #df.index = df.index.where(~df.index.duplicated(), df.index + '_dp')
    # If you want to remove of duplicated index to unique
    # This method is better than the non-highlighted one as
    # it return E1,E2,E3, as many as duplicates you have.
    df.index = df.index + df.groupby(level=0).cumcount().astype(str).replace('0','')



def pretty_print(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be     specified also
        print(df)


# def reset_g():
#     %reset
#     %clear
#     %run 3_Creating_Dummies_continued.py
