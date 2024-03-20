
This study explores the recent fluctuations in car prices, taking into account the numerous factors that shape pricing dynamics. The past decade has witnessed price escalations, resulting in uncertainty among consumers regarding future trends. Leveraging both data analysis and machine learning methods, this research will forecast future changes in car prices. These insights will help in aiding individuals to better strategize their financial planning or contemplate alternative transportation avenues.


In the past decade, we've witnessed a significant change in both new and used car prices. Several factors contribute to this shift, including material shortages during the COVID-19 shutdown, economic fluctuations, and the principles of supply and demand. The pandemic forced auto manufacturers worldwide to halt operations to safeguard their employees from the rapidly spreading virus. Consequently, the used car market took the brunt of consumer reliance, as individuals turned to pre-owned vehicles out of necessity. Despite the pandemic's gradual decline, car prices have yet to recede, indicating a lasting impact on the automotive 


In this research endeavor, data acquisition was facilitated directly through the Kaggle platform, ensuring a complete dataset. Data cleaning procedures were implemented, selectively filtering for pertinent information to enhance accuracy. Then Exploratory analysis generated visually compelling representations to display key insights. Using machine learning techniques, a predictive model was deployed to forecast future trends based on the dataset. Finally, the findings were communicated, and the efficacy of the model was evaluated, showing the credibility and applicability of the research outcomes.




This study sheds light on the upward trend in used car prices and offers insights into their projected trajectory. Given the influence of inflation, the cost of living continues to escalate, making it important for consumers to predict and plan for potential price hikes and scarcity. Using their predictions individuals can make informed decisions to adapt their lifestyles, such as opting for public transportation, carpooling, or embracing vehicle-sharing initiatives.

This research equips consumers with valuable data to devise more precise savings strategies in anticipation of rising prices. There are limitations of this study that must be noted and taken into account. There are a multitude of external factors that may impact car prices, That are not captured in this dataset. Variables such as economic recessions, material shortages, and unforeseen events can cause unpredictability.

\subsection{Data Attributes and Cleaning}
Data was found from this website: \url{https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho/discussion}. The dataset was initially obtained in CSV format, offering convenient organization and cleansing capabilities. It encompasses a diverse array of attributes pertinent to used car valuation, including but not limited to Car Name, Year, Selling Price, Present Price, Miles Driven, Fuel Type, and Transmission. The dataset comprises 301 entries, each comprising 8 fields uses a mix of numerical and categorical data.

In the data cleansing phase, redundant columns such as Seller type and owner were eliminated using Python. These exclusions were justified both by the presence of incomplete entries and their lack of relevance to the vehicle's pricing dynamics. A transformation was executed in Python to convert the 'KMS' column—representing kilometers—into 'Miles,' aligning with the prevailing measurement standard in the United States. This conversion was achieved by systematically dividing each entry by 1.609 to ensure accurate representation in miles.\cite{mogridge1967prediction}

Here are the following attribute definitions:

Car Name- Each cars specific make and model name.

Year- Year the car was sold.

Selling price- What the used car sold for

Present price- What the car sold for new

Miles driven – Miles the car had driven at time of sale

Fuel Type – Fuel the car uses

Transmission – If the car is manual or automatic.

The price is the dependent variable and the independent variables are the attributes of the car.



Exploratory Data Analysis (EDA) stands as a cornerstone in the data analysis process, offering crucial insights into the dataset. This phase is pivotal for cultivating a profound comprehension of the dataset and its attributes, mitigating the risk of misinterpretation.

In initiating the EDA, Python was used to alphabetically sort the data and display its descriptive statistics. This necessitated the creation and activation of a virtual environment to facilitate the utilization of built-in descriptive functions. The Pandas library was imported, laying the groundwork for comprehensive data exploration and analysis. Exact python code can be found at 

Histograms were used during this phase to visually represent the frequency and distribution of the data. This step was imperative to assure the depth and consistency of the dataset, while also identifying any potential outliers requiring attention. The histograms revealed a satisfactory distribution of data across the range, with the exception of a single outlier necessitating removal to uphold the integrity and reliability of the dataset.





\section{Machine Learning }
The machine learning component chosen for analysis and prediction was the Random Forest algorithm. This technique is a supervised learning algorithm, comprising multiple decision trees. Each decision tree contributes predictions, and the Random Forest aggregates these outputs to provide a final prediction, typically by averaging them. By increasing the number of trees, the algorithm's precision improves.
What sets Random Forest apart is its capability to use many features to make predictions, a crucial aspect given the diverse attributes affecting car prices. Notably, Random Forest accommodates both quantitative and qualitative attributes, making it particularly suited for this task.
Using the Random Forest in this context showed to be effective, showcasing its high accuracy and compatibility with the dataset at hand. \cite{website02}

\section{Results of Random Forest }

\begin{figure}[h!]
  \centering
\includegraphics[width=0.8\linewidth]{heatmap.png}
  \caption{ Heat Map showing the correlation of the different attributes}
  \label{fig:12}
  
\end{figure}
\begin{figure}[h!]
  \centering
\includegraphics[width=0.9\linewidth]{results1.png}
  \caption{Diagram showing how relevant each attribute is to sales price}
  \label{fig:13}
  
\end{figure}

\begin{figure}[h!]
  \centering
\includegraphics[width=0.9\linewidth]{results3.png}
  \caption{Diagram showing the accuracy of the Random Forest}
  \label{fig:15}
  
\end{figure}
 \pagebreak 
  \pagebreak 
\section{ Further Analysis and Conclusion }
In summary, numerous factors contribute to determining the price of a car. As depicted in Figure 16, the scatter plot illustrates a positively skewed trend, highlighting the influential role of the car's production year on its price. Notably, over time, as inflation has continued to escalate, car prices have seen a corresponding significant increase. This trend poses challenges for affordability, particularly as most salaries have remained stagnant. This disparity between rising car prices and stagnant incomes shows the growing difficulty for the average individual to purchase a car.

Addressing this issue is imperative to ensure fair access to transportation options. Efforts must be directed towards making cars more affordable or exploring alternative modes of transportation to alleviate the burden on citizens. Failure to address this issues risks increasing transportation issues and hindering mobility for many individuals.\cite{matas2014hedonic}
\begin{figure}[h!]
  \centering
\includegraphics[width=0.8\linewidth]{yearvsprice.png}
  \caption{Year a Car was Manufactured vs Price }
  \label{fig:16}
  
\end{figure}







\bibliographystyle{splncs04}
\bibliography{mybibliography}




\end{document}

