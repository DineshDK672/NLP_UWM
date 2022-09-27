# NLP_UWM
Contains programs and projects I've written during my NLP course at University of Wisconsin Milwaukee.

## HW1:

      The HW1.py contains three functions.
      
        #compareWordTypes():
            This funtion has three parameters two text paragraphs and a normalization flag. 
            The function finds similar word-POS pairs or Unigrams in both the text paragraphs and returns either the probability or the number of similar unigrams based on the value of normalization flag as either "Y" or "N" respectively.
            
        #compareBigramTypes():
            This function also has the same parameters as compareWordTypes().
            This function works similar to compareWordTypes() except that this function finds and compares bigram pairs and returns either the probability or the number of similar bigrams based on the value of normalization flag as either "Y" or "N" respectively.
            
         #plagiarismDetector():
            This function takes two text paragraphs, type of comparison, normalization flag and a threshold value as parameters.
            The function calls either of the two above mentioned functions based on the value of type parameter and recieves the probability value of plagiarism from the functions.
            Then it compares the probablity value with the threshold value to determine whether the two paragraphs are plagiarised or not.
