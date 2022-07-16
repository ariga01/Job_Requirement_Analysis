# _**Data Analyst Job Requirement Analysis**_

## About This Project

Data analyst is one of the fastest growing jobs in the world. Coincidentally, I also aspire to be one as well. In order to fulfill such a needs, I did this project in order to gauge the possible factors and skills that may help me to find an internship as a data analyst.

## Objective

- Find the possible requirement for data analyst job
- Find interesting insight out of the data

## Workflow

- Webscrape the data from certain site
- Clean the data
- Process and analyze the data
- Make visualization in Tableau

## Discussion

For this project, I use data from the following location:

- Indonesia
- Singapore
- Malaysia
- Japan
- United States

I use data from the aforementioned countries because I expected that such places may offer the best and most probable chance of me being accepted. I limited the data for each countries to be 500 entities. That said, there are clear differences of job listing between the aforementioned countries. United States come as the highest with total of 400K of job listing, although the site limited the view of only 1000 job listing. That said, with total of 2500 job listing, I do think that this is enough number for generalization to be made.

The data doesn't contain too much substantial error or nan, making the cleaning a much easier process than normal. That being said, the data contain so much non-data analyst job as well, making the exclusion process as mandatory step to clean the data further. Luckily, I can use google translate package for the Japanese job title, and then use regex for all of the job listing to remove the non-data analyst job.

During the analysis process, I want to extract the hard skill and tools being needed by the employer. Initially, I want to use the google translate package, but I have to stop doing that because it returned error for having too much character in one process. In order to mitigate this, I searched for the Katakana equivalent of the desired tools, and associating that Katakana word with its english equivalent. Additionally, I need to make assumption that for job with less than or equal to 25 applications, I need to convert those value into 25 for simplicity and uniformness.

For the last part, I used some script that I found in one of the medium writings[^1]. I took some of the most likely to be important word into tableau presentation.

## Results

After analyzing the data, I concluded that:

- Indonesia is the most crowded with applications
- Only 3 out of 100 applications being accepted on average
- SQL is still the most popular tools being used
- Many employers seek an experienced data analyst
- Employers seek data analyst that can bring insight from data to their business, which may use various tools and approach
- Employers typically seek insight about their marketing operation or companies product

## Links

[^1]:[GitHub Pages](https://github.com/tcaffrey/LDA_Job_Search)
