# Anomaly detection

* [Home](https://supaerodatascience.github.io/machine-learning/)
* [Github repository](https://github.com/SupaeroDataScience/machine-learning/)

This class introduces the problem framing and methodology of Anomaly Detection. It illustrates why classical supervised ML algorithms are not suitable for such problems, and provides new approaches with outlier detection and novelty detection. You will discover, by alternating theory and practice exercises, the major algorithms, principles and warning signs for such tasks, including One-Class SVMs, Local Outlier Factor or Isolation Forest. You will also discover semi-supervised approaches where the error of supervised learning models can turn into anomaly scores.
At the end, a practical use case with anonymized aircraft sensor data is proposed, where you will have to develop the whole methodology without guidance. It will help you reflect on the main stakes and warning points of such tasks, to prepare you to address customers in your professional life.

[Lecture notes](https://github.com/SupaeroDataScience/machine-learning/blob/main/13%20-%20Anomaly%20Detection/anomaly_detection_class.pdf)  
[Notebook for class exercises](https://github.com/SupaeroDataScience/machine-learning/blob/main/13%20-%20Anomaly%20Detection/anomaly_detection_class-empty.ipynb) ([colab](https://colab.research.google.com/github/SupaeroDataScience/machine-learning/blob/main/13%20-%20Anomaly%20Detection/anomaly_detection_class-empty.ipynb))  
[Solutions](https://github.com/SupaeroDataScience/machine-learning/blob/main/13%20-%20Anomaly%20Detection/anomaly_detection_class.ipynb) ([colab](https://colab.research.google.com/github/SupaeroDataScience/machine-learning/blob/main/13%20-%20Anomaly%20Detection/anomaly_detection_class.ipynb))

[Practical use case instructions](https://github.com/SupaeroDataScience/machine-learning/blob/main/13%20-%20Anomaly%20Detection/anomaly_detection_exercise.pdf)  
[Data for use case](https://github.com/SupaeroDataScience/machine-learning/blob/main/13%20-%20Anomaly%20Detection/data/dataset.csv)

## Requirements for local installation

To setup the Anaconda environment with required dependencies, execute the following instructions in Anaconda prompt or Linux shell.

```shell
# Clone this github repository on your machine
git clone https://github.com/jfabrice/ml-class-anomaly-detection.git

# Change working directory inside the repo
cd ml-class-anomaly-detection

# Create a new virtual environment
conda create -n anomalydetectionenv python==3.6

# Activate the environment
## For Linux / MAC
source activate anomalydetectionenv
## For Windows
activate anomalydetectionenv

# Install the requirements
pip install -r requirements.txt
```
