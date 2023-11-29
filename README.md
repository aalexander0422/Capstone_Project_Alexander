# Capstone_Project_Alexander
LINK TO REPORT 
https://www.overleaf.com/read/vwbrkdgwxfmc#bddfbb
 The prices of new and used cars has changed drastically in the last decade. There are a number of reasons for this. The shortages of materials during the covid 19 shutdown, the economy and supply and demand may play a big part in car prices. During the pandemic auto manufactures everywhere had to shutdown to keep workers safe from the fast spreading virus. The used car market has suffered because consumers had no other option but to buy used. Even after the pandemic has subsided car prices have not reduced and are still affected.

For this research the data was collected directly from the Kaggle website. Data was then cleaned by filtering to only include relevant information. Data was then explored and compelling visuals were created. Then a machine learning model was use to predict future data. Data results were then communicated and effectiveness was evaluated. 

This research shows the rising used car prices and also predicts what the prices will be in the future. With inflation everything is only getting more expensive. Consumers need to know what the future may hold so that they may prepare for increases in price and low availability. Consumers may use this information to plan out their everyday lives such as choosing to use public transportation, carpooling, or even sharing vehicles. 

Consumers may also use this data to make a savings plan that is more accurate to rising prices. A limitation of this research is having so many outside factors that may affect car prices that may not be included in this data. These factors may include a recession, lack of materials, and other unpredictable disasters.

Data was found from this website: \url{ttps://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho/discussion} This data came in a CSV format. This allows for easy organization and cleaning. This data set includes a lot of different attributes about a used car that may affect its price. These attributes include: Car Name, Year, Selling Price,	Present Price, Miles Driven, Fuel Type, and Transmission. The data is structured and contains 301 entries. There are 8 fields in each record and they include numerical and categorical data. 

To start the data cleaning unneeded columns were deleted from the data using python. The columns that were deleted were Seller type and owner. These were deleted to get rid of the incomplete entries and also because these variables are not related to the vehicle price or are accounted for in the other attributes. Then in python a column named KMS which stands for kilometers was changed to miles since that is the form of measurement used in the united States. To get the correct result every entry was divided by 1.609.

Here are the following attribute definitions:

Car Name- Each cars specific make and model name.

Year- Year the car was sold.

Selling price- What the used car sold for

Present price- What the car sold for new

Miles driven – Miles the car had driven at time of sale

Fuel Type – Fuel the car uses

Transmission – If the car is manual or automatic.

The price is the dependent variable and the independent variables are the attributes of the car.

Exploratory Data Analysis is one of the most important steps. This is where the data is explored to see what story the data is trying to tell. It is important to make sure their is a deep understanding of the data and its attributes so it is not misread. 
First python was used to sort the data alphabetically and to display the descriptive statistics. To be able to use the descriptive built in function a virtual environment was created and activated. Then Pandas was imported. Exact python code can be found at \url{https://github.com/aalexander0422/Capstone_Project_Alexander}.

Histograms were also used in the step to show the frequency and range of the data. This was a required step to insure that there was a good range of data and to determine if there are any outliers that need to be addressed. The histograms showed that this is a good range of data and there is one outlier that was needed to be removed in order to keep data reliability.

Random Forest was the machine learning component chosen to analyze and predict the data. A random forest is a supervised machine learning algorithm composed of decision tree algorithms. The random forest algorithm shows the outcome based on the predictions of each of the decision trees. It predicts the outcomes by using the mean of the output from the trees. Increasing the amount of trees improves the precision of the outcome. The Random Forest is able to combine features to make predictions which is important in this case because car prices can vary based on the different attributes. The attributes in a random forest can also be quantitative and qualitative. This Random forest was shown to be very accurate and worked well with this data.

In conclusion there is a lot of different attributes that can determine a cars price. In Figure 16 the scatter-plot shows a positively skewed trend showing that the year a car is built can affect the cars price. This also shows as time has passed and inflation continued to rise car prices have also drastically rose, because of this it can be more difficult to afford a car. Car prices are rising and most salary's have remained the same meaning it will be harder for the average person to afford a car. Something needs to be done to that cars can be more affordable or other means of transportation may have to pick up the slack and provide citizens alternative ways of transportation.

References 
1. GOYAL, S.: Car price, https://www.kaggle.com/datasets/nehalbirla/vehicle-
dataset-from-cardekho/discussion, addendum =
 2. Matas, A., Raymond, J.L.: Hedonic prices for cars: an application to the spanish car
 market, 1981–2005. In: The Applied Economics of Transport, pp. 99–116. Routledge
(2014)
3. Mbaabu, O.: Car price, https://www.section.io/engineering-
education/introduction-to-random-forest-in-machine-learning/, addendum =
4. Mogridge, M.J.: The prediction of car ownership. Journal of Transport Economics
and Policy pp. 52–74 (1967)