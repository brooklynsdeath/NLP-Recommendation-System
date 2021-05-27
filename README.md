# NLP-Recommendation-System

In this we use the Machine Learning NLP based recommendation system with scikit learn library, which help us recommend the users to the user on the basis of collaborative filtering.
We have only one main .py file which can be run directly or on the command line with proper parameters. (CSV file, user id, o/p file)

1.	In first block of code, it imports the required libraries.
2.	Then the pre-processing of the dataset is done like cleaning the dataset and null values and taking the required fields for the program to recommend.
3.	Then bag of words is used in which all the interest columns are stored and creates a column with specific number of interests chosen by the users.
4.	With that bag of words columns, the matrix is made in which for specific user with interest. 
5.	Then the cosine similarity is used to recommend the user.
6.	From the last function created recommendation, which will be used to call the program.
7.	Then it will store the user id to the text file as a list.
