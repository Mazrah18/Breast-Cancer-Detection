# Breast-Cancer-Detection-using-Multilayer-Perceptron\
The code contains the original ipython file where the code was written along with the equivalent .py file./

1.	Precise Input settings:
a.	For the method-2 implementation of the breast cancer detection dataset using the deep learning method of MultiLayer Perceptron model, the existing model of sklearn has been utilized. Some input parameters have been modified, while others have remained unchanged. The input settings used for this implementation are as follows:

(A) The Maximum number of iterations is set to 500.
(B) The size of the mini-batches used is 100(batch_Size=100)
(C) Hidden layer Sizes for this implementation is (12,8)
(D) The Activation Function used is the logistic sigmoid function.
(E) The Strength of the L2 regularization term is set to 0.001(Alpha=0.01)

The rest of the parameters are set to default.

2.	Potential modifications to the existing dataset and task: “Nothing To Report”

3.	Preprocessing: Pre-processing was required as in the dataset when examining the mean row of the second table, the difference between the columns is quite large. Therefore, we can conclude that standardization is a must for this dataset and processed. Although there was no NaN/Null values in the dataset but we had to drop 2 columns that were Unnamed: 32 and id which were not useful also we renamed diagnosis to target and converted categorical variables in to numeric. Also there is no need for downsamplinig or upsampling as this data is not imbalancede. For feature selection, we tried to use PCA and correlation matrix to work on reduced dimensions, however it seemed to reduce the accuracy on both the test and the training set as the data did not seem linearly separable.
4.	 Experimental Setting:

a.	The stratified K-fold sampling was used in order to slice the dataset into 10 different datasets. The Multilayer Perceptron was implemented on all the new datasets using the same parameters provided earlier. The performance of the implemented MultiLayer perceptron model was evaluated with the help of a ‘confusion matrix’ which helped provide the overall accuracy of the model. The confusion matrix was also used to get the precision, recall, and miss rate which helped understand the model better. Furthermore, using the precision and recall obtained from the confusion matrix, the f1 score was calculated. The ROC graph is plotted using the calculated AUC value.



5.	Results: The MultiLayer Perceptron model gives an average test accuracy of 94.79%. The precision, recall and f1 scores are 0.93,0.99, and 0.96 respectively. The miss rate obtained is approximately 6.8%.

 

 






