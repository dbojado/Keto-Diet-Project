[![Header](https://github.com/dbojado/Keto-Diet-Project/blob/main/images/The_Keto_Diet_Banner_2.png "Header")](https://www.canva.com/design/DAEPhrgPsOk/NCc1MmlWCpMdEclyl1kbWQ/view?utm_content=DAEPhrgPsOk&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton)

# The Keto Diet Project
Can we predict if a food is "Keto Friendly"?

## What is a Keto Diet?
- The Ketogenic Diet (keto) is a low carb, high fat diet. Many studies show that this type of diet can help you lose weight and improve your health.


## About the Project
- For this project I will be exploring a "Nutritional Facts" database and using machine learning clustering methodologies to predict if a food is "Keto Friendly".

## Goals
- Predict if a food is "Keto Friendly" based solely on it's macro ratios from the given nutritional facts database.
- Use a clustering model to answer the question above and find out if certain groupings exist in the data.


## Deliverables
- A well-documented Github Repo with a Final Notebook and README.
- Slide Deck Presentation suitable for an audience of data science peers that summarizes findings.
- Writeup for resume


## Data Dictionary
| Feature | Definition |
|---------------------------|--------------------------------------------------|
| Ketogenic Diet (Keto)   | A low carb, high fat diet.|  
| Nutritional Facts/Food Labels   | These labels are found on packaged foods and beverages. They are meant as a tool for making informed food choices that contribute to healthy lifelong eating habits. |  
| Macronutrients (Macros)   | Carbohydrates, fats, and proteins. They are the nutrients you use in the largest amounts, as opposed to micronutrients, such as a variety of vitamins in food. |  
| Carbohydrates   | The sugars, starches and fibers found in fruits, grains, vegetables and milk products. |  
| Fats  | Fatty acids most commonly found in meat and dairy products.|  
| Protein   | An essential nutrients at are the "building blocks" of body tissue. |  

## Project Steps
### Acquire
- Data is aquired from Kaggle [("Nutritional Values for Common Foods and Products")](https://www.kaggle.com/trolukovich/nutritional-values-for-common-foods-and-products) and https://www.nutritionvalue.org.
- Functions are stored in the acquire.py file.
- File is a reproducible component for gathering the data.

### Prepare
- Create a prepare.py file. 
- Clean dataset.
- Missing values are investigated and handled.
- Run train, validate, and test.
- File is a reproducible component that is ready for exploration.

### Explore
- Explore nutritional facts data across over 8.7k different foods.
- Find macronutrients percentage (carbohydrates, fats, and protein) patterns by creating histograms.
- Summarize takeaways and conclusions.   

### Model
- Fit different K-means clustering models. 
- Choosing k with inertia (the sum of squared distances from each point to it's assigned centroid). 
- Use elbow method to determine a good value for k.

### Conclusions
#### What was best model?
- The K-means, k=4 model, provided the best clustering.

#### How did the findings compare with what is known?
- Cluster 1 matched up very closely to a ketogenic diet that could be more balanced and substantial in the long-term. 
- This information might be great for someone who needs help making food choices that are not all just meat, cheese, and eggs.

### Future Investigations
- Can other food items be classified under certain diets (vegan, vegetarian, low-carb, etc) using similar methods?
- Could this system be used on an food tracking app to give users suggestions on what food they should be buying depending on what diet they are on? This could take out a lot of the guessing and research that comes with being on a diet and really simplify things for the user. 

## How to Reproduce
All files are reproducible and available for download and use.
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and Final_Report.ipynb files

## Contact Me 
Dani Bojado
- daniella.bojado@gmail.com 
