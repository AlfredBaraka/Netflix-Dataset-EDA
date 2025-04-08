import pandas as pd
import matplotlib.pyplot as plt

import os
import matplotlib.pyplot as plt

colors = {'movie':'#ff9999','show':'#66b3ff', 'both':'#404040'}
def pie_movie_show_dist(df):
    data = df['type'].value_counts()
    explode = (0.05, 0.05)

    # Title for the chart
    title = "Distribution of Movies and TV Shows on Netflix"

    # Create the plot
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', colors=[colors['movie'], colors['show']], explode=explode, startangle=140)
    plt.title(title)
    plt.tight_layout()

    # Format the filename
    safe_title = title.lower().replace(" ", "_").replace(":", "").replace(".", "").replace(",", "")
    path = os.path.join('../reports/figure', f"{safe_title}.png")

    # Save the image
    os.makedirs(os.path.dirname(path), exist_ok=True)
    plt.savefig(path)
    print(f"Pie chart saved at: {path}")

    # Show the chart
    plt.show()


def plot_content_added_per_year(df):
    df = df.dropna(subset=['date_added'])

    # Convert 'date_added' to datetime
    df['date_added'] = pd.to_datetime(df['date_added'])

    # Extract year
    df['date_year'] = df['date_added'].dt.year

    # Group by year and type
    grouped = df.groupby(['date_year', 'type']).size().unstack().fillna(0)
    
    # Plot
    ax = grouped.plot(kind='bar', figsize=(12, 6), color=[colors['movie'], colors['show']])
    plt.title('Number of Movies and TV Shows Added Per Year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save to file
    path = '../reports/figure/content_added_per_year.png'
    plt.savefig(path)
    print(f"Chart saved at: {path}")

    plt.show()

    plt.show()    

def plot_top_10_countries(df, part='general'):
    # Drop rows with NaN in 'country' column
    df = df.dropna(subset=['country'])

    # Drop all data which country is not specified
    df = df[df['country'] != 'Not Specified']

    # Split 'country' entries by commas (for multiple countries) and explode the list into separate rows
    countries = df['country'].str.split(',').explode().str.strip()

    # Count occurrences of each country
    country_counts = countries.value_counts().head(10)
    
    # title
    if part == 'general':
        title = "Distribution of Movies and TV Shows on Netflix"
        color = colors['both']
    elif part == 'movie':
        title = "Distribution of Movies on Netflix"
        color = colors['movie']
    elif part == 'show':
        title = "Distribution of TV Shows on Netflix"
        color = colors['show']
    else:
        raise ValueError("Invalid part. Expected 'general', 'movie', or 'show'.")
    # Plot the top 10 countries
    plt.figure(figsize=(10, 6))
    country_counts.plot(kind='barh', color=color)
    plt.title(title)
    plt.xlabel('Number of Titles')
    plt.ylabel('Country')
    plt.tight_layout()

    # Save the plot
    safe_title = title.lower().replace(" ", "_").replace(":", "").replace(".", "").replace(",", "")
    path = os.path.join('../reports/figure', f"{safe_title}.png")
    plt.savefig(path)
    print(f" Chart saved at: {path}")

    plt.show()
def plot_movie_duration_distribution(df):
    # Drop rows where 'duration' is NaN or missing
    df = df.dropna(subset=['duration'])

    # Extract the numeric part from 'duration' column (e.g. "45 minutes" -> 45)
    df['duration_minutes'] = df['duration'].str.extract('(\d+)').astype(int)

    # Keep only durations that are multiples of 10
    df = df[df['duration_minutes'] % 10 == 0]

    # Count the most frequent durations
    duration_counts = df['duration_minutes'].value_counts().sort_index()

    # Plot the distribution of movie durations
    plt.figure(figsize=(10, 6))
    duration_counts.plot(kind='bar', color=colors['movie'])
    plt.title('Most Frequent Movie Durations on Netflix')
    plt.xlabel('Duration (Minutes)')
    plt.ylabel('Count of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    path = '../reports/figure/movie_duration_distribution.png'
    plt.savefig(path)
    print(f"Chart saved at: {path}")

    plt.show()

def plot_content_rating_distribution(df):
    # Drop rows with missing content ratings
    df = df.dropna(subset=['rating'])

    # Count the frequency of each rating
    rating_counts = df['rating'].value_counts()

    # Plot
    plt.figure(figsize=(10, 6))
    rating_counts.plot(kind='bar', color=colors['both'], edgecolor='black')
    plt.title('Frequency of Different Content Ratings on Netflix')
    plt.xlabel('Content Rating')
    plt.ylabel('Number of Titles')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    path = '../reports/figure/content_rating_distribution.png'
    plt.savefig(path)
    print(f"Chart saved at: {path}")

    plt.show()

def plot_netflix_releases(df):
    # Extract the release year from the 'date_added' column
    df['release_year'] = pd.to_datetime(df['date_added']).dt.year
    yearly_releases = df.groupby('release_year').size()

    # Plot
    plt.figure(figsize=(10, 6))
    yearly_releases.plot(kind='line', marker='o', color=colors['both'])

    # Title and labels
    plt.title("Netflix Content Releases Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Titles")
    plt.grid(True)

    # Save the plot
    path = '../reports/figure/netflix_content_releases_over_the_years.png'
    plt.tight_layout()
    plt.savefig(path)
    print(f"Chart saved at: {path}")

    # Show the plot
    plt.show()



def plot_us_vs_non_us_content(df):
    # Create a column that identifies whether the content is from the US or not
    df['is_non_us'] = df['country'] != 'United States'

    # Group by release year and whether the content is from the US or not
    local_vs_us = df.groupby(['release_year', 'is_non_us']).size().unstack().fillna(0)

    # Plot
    plt.figure(figsize=(10, 6))
    local_vs_us.plot(kind='line', marker='o')

    # Title and labels
    plt.title("US vs Non-US Content Over Time")
    plt.ylabel("Number of Titles")
    plt.xlabel("Year")
    plt.grid(True)

    # Save the plot
    path = '../reports/figure/us_vs_non_us_content_over_time.png'
    plt.tight_layout()
    plt.savefig(path)
    print(f"Chart saved at: {path}")

    # Show the plot
    plt.show()


