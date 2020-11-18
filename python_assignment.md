# 11/17 to 1/4 Assignment:
##In Django and ReactJS
###Specification:
1. The system should have a home page file named "index.html". The pages displays should show a banner. The home page should have a left sidebar that has buttons linking to the following two pages: About and Search. Choose an appropriate font. Leave the whitespace on the right side of the page for descriptions of what this project will be, use Bootstrap 4 for layout.

2. In the About page, named "about.html", there should be 4 different pictures of UBC listed, in a 2 by 2 matrix with invisible margins, not dotted or concrete lines for the matrix.

3. When the user starts the system, there should be a session associated with the user. If you don't know what a session is, google it. Each session should have a session.json file with its session ID listed in it.

4. The Search page, named "run.html", is the first page of a process of finding a certain element in a database. This page however only has three buttons here: Upload, Download, Search. There are 3 pages associated: "upload.html", "download.html", "search.html". Use the white space to explain what these three buttons do.

5. Before you continue, in your backend, you should connect to a database, the database should be NoSQL, not mySQL. Add synthetic data into the database. The database should only have three columns: "Sample_Name", "Description",  "Time".

6. In the upload page, the user is able to view the current database and add new data to the database. The user cannot delete data. It's up to you how to create the layout.

7. In the download page, the user is able to download the entire database down in a CSV file. It's up to you how to create the layout.

8. Lastly, in the search page, the page should have a search function that queries the database. You must write the search function in python. The page should ask the user what sample they are looking for. The user can input in a small text box. 

9. Once the user inputs, it will list all the samples that match the text inputted. Use regular expressions here if needed. 

10. The user can select the items wanted. All the records will be saved into the session.json file. It can be downloaded by the user in the search function page.