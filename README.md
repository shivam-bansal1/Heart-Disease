# Heart-Disease

Python is most powerful programming language having numerous libraries which is used in this project
with machine learning model. Machine learning is a subset model of artificial intelligence network in
which uses complex algorithms and deep learning neural networks. Cardio vascular disease is a
widespread disease in all over a region. This type of disease may cause due to smoking, high blood
pressure, diabetes, overweight, hyper tension, cholesterol etc that has to be accumulated because of the
fatty foods or unlimited intake of foods or non-moving to anywhere. This disease may occur by various
heart problems such as coronary-artery disease, cardio-vascular, stroke, heart failure and much more.
Chest pain (cp), resting blood pressure, cholesterol, resting electrocardiographic results, fasting blood
sugar(fbs), maximum heart achieved, exercise induced angina, ST depression induced by exercise relative
to rest, slope of the peak exercise ST segment, number of major vessels colored by fluoroscopy etc… are
the major reasons for causing heart problems but we have a attributes of individual person like height,
weight, systolic blood pressure, diastolic blood pressure, cholesterol, glucose, smoke, alcohol, active
(physically active person). Python libraries are the pre-requisites for making prediction in which SKLEARN
is basically used in machine learning predictions. From SKLEARN, we will be able to preprocess the data
by splitting the attributes and labels, test and train data, and also scale the values in the data to be values
between 0 and 1 by importing the library STANDARDSCALAR. Also SEABORN is another library used in
our prediction to correlate each and every attributes together. At last the confusion matrix decides
accuracy perfectly by importing CONFUSION MATRIX.


## Methodology And Analysis
A. Methodology
i. Data collection
Overall process of predicting heart disease carries following procedure:
We have collected data from dataset provider –Kaggle.com. the dataset which is published by
Svetlana Ulianova as in the title of Cardiovascular Disease dataset, 2019.The dataset collected
consists of 70,000 records of patients data carries 11 features and
Dataset is the information or a tool essential to do any kind of research or a project
ii. Data Preprocessing
Segregation of target data and feature data as training and test data.
Scaling the values in the data to be values between 0 and 1 in which and scale all the values before
training the Machine Learning models.
iii. Applying Algorithms
Comparing 4-machine learning algorithms such as SVM, Decision tree, Random forest classifier and
K- nearest neighbor to get the better accuracy to which highest parameter may cause disease.
For each algorithm, there is a pseudo code helpful to develop any kind of programming language. In
python, there is a simple way to establish any kind of algorithm in which simple and short code
easier to predict accuracy.
B. Machine Learning Algorithm:

The algorithms used in this project is highly helpful to predict the accurate result to detect heart disease
in which factors that cause a disease can be detected. The following algorithms have built in this project.
i. K-Nearest Neighbor algorithm:
KNN is a supervised classifier that carry-outs a observations from within a test set to predict
classification labels. KNN is one of the classification technique used whenever there is a classification. It
has a few assumptions includes dataset has little noise, labeled and it should contains relevant features.
By applying KNN in large datasets takes long time to process. The accuracy gained with this algorithm is
63.4%.
ii. Random Forest Classifier:
Random forest classifier is a powerful tool in the machine learning library. With this classifier, we will be
able to get higher accuracy and training time should be less. Initially, we have to build a model and by
splitting variables into training and test set. After splitting the data, train the dependent variables and
predict the response. By using the random forest classifier, the accuracy predicted result is of
approximately 71% but actually 71.4%.
iii. Decision tree classifier:
In this algorithm, preprocessing made initially by splitting data into training and test data .Feature scaling
can be done because of normalizing the values before prediction. Import a decision tree classifier to fit
the training sets of dependent and independent variables in which Gini-index criterion is used to predict
the accuracy or response for the test set. The accuracy gained with this algorithm is 68.4%.
iv. Support Vector Machine (SVM):
SVM is also one of the classification algorithms in machine learning in which better accuracy can be
predicted. In comparison of other algorithms, it is better for predicting accuracy in an expected way.
In our prediction, predicted highest accuracy is 72.5% using linear SVM kernel.
In our prediction, predicted highest accuracy is 86.2% using Gaussian SVM kernel.
