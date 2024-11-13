import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize Kaggle API and authenticate
api = KaggleApi()
api.authenticate()

# Create data directory
output_dir = "../data"
os.makedirs(output_dir, exist_ok=True)


#File paths for datasets
mass_shooting_path = os.path.join(output_dir, 'History_of_Mass_Shootings_in_the_USA.csv')
us_crime_path = os.path.join(output_dir, 'US_Crime_Data.csv')

# # Use for removing in output directory
file_csv_paths = [mass_shooting_path, us_crime_path]
    



def download_datasets():
    #Download datasets and save them in the data directory."""
    # for downloading us crime data
    api.dataset_download_files('johnybhiduri/us-crime-data', path=output_dir, unzip=True)
    # for downloading the mass shooting
    api.dataset_download_files('rprkh15/history-of-mass-shootings-in-the-usa' , path=output_dir , unzip=True)
    print("yes done")
    # # Download CO2 Emissions dataset (from CSV file download API)
    # response = requests.get(co2_emissions_url)
    # if response.status_code == 200:
    #     with open(co2_emissions_path, 'wb') as f:
    #         f.write(response.content)
    #     print("CO2 Emissions dataset downloaded successfully.")
    # else:
    #     print(f"Failed to download CO2 Emissions dataset. Status code: {response.status_code}")

def remove_download_csv(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            if file_path.endswith('.csv'):  # Ensure only CSV files are targeted
                os.remove(file_path)
                print(f"{file_path} has been removed.")
            else:
                print(f"{file_path} is not a CSV file.")
        else:
            print(f"{file_path} does not exist.")
def preprocess_mass_shooting_data(df):
    mass_shooting_df = pd.read_csv(df)
    drop_mass_shooting = mass_shooting_df.drop('Description', axis=1)
    clean_mass_shooting_df = drop_mass_shooting.dropna()
    return clean_mass_shooting_df


def preprocess_crime_data(df):
    crime_data_df = pd.read_csv(df)
    # removing the unecessary columns 
    drop_crime_data = crime_data_df.drop(['Date' , 'Organization','State','URL','Keyword','Summary'], axis=1)
    clean_crime_df = drop_crime_data.dropna()
    return clean_crime_df


def merge_data(df1 , df2):
    print("in merge data section")
    merged_df = pd.merge(df1, df2, on='City', how='inner')
    return merged_df

def save_dataframe_to_csv(df,filename):
    directory_path = '/Users/muhammadgulfamtahir/Desktop/FAU/5th Semester/Major/Methods of the Advanced Data Engineering/made-template-2024/data'
    # Save the DataFrame to a CSV file in the specified directory
    file_path = directory_path + '/'+filename+'.csv'
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    # downloading the datasets
    download_datasets()

    # setting the path of the download datasets
    mass_shooting_data= '/Users/muhammadgulfamtahir/Desktop/FAU/5th Semester/Major/Methods of the Advanced Data Engineering/made-template-2024/data/History_of_Mass_Shootings_in_the_USA.csv'
    us_crime_data = "/Users/muhammadgulfamtahir/Desktop/FAU/5th Semester/Major/Methods of the Advanced Data Engineering/made-template-2024/data/US_Crime_Data.csv"
    
    # preprocessing the data
    filter_shooting_df = preprocess_mass_shooting_data(mass_shooting_data)
    filter_crime_df = preprocess_crime_data(us_crime_data)

    #merging the data
    final_df = merge_data(filter_shooting_df, filter_crime_df)

    print("Final Merge Data" , final_df)
    
    #removing the previous saved CSV files with the filtered 
    remove_download_csv(file_csv_paths)

    # saving all the files
    save_dataframe_to_csv(filter_shooting_df, 'Filtered_USA_Mass_Shootings_History')
    save_dataframe_to_csv(filter_crime_df , 'Filtered_USA_Crime_Data')
    save_dataframe_to_csv(final_df, 'final_merge_data')

    print("Pipeline completed successfully.")
