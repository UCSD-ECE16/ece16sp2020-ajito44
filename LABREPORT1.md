# ECE16 Lab Report 1

## Tutorial 1: Arduino and Git

>>Q. When you open the conflicted readme, what did you get? How did you fix it?

> ![IMAGES](README.png)

>A. When I opened the conflicted readme, it just showed me the text that I put on my local file rather than the text showing up on github. This is because I saved the readme file with the new text I put, so no changes would be made to it even after I commit and try to push the new edited file. To fix this, I changed the text on my local file to match with the one on github and then followed the steps to commit and push the file. 

### Challenge 1
>In this challenge, I created my repository in the classroom github so I could submit my upcoming labs. To create my repository, I clicked on the classroom link and followed the steps to clone my repository to my local machine. I also practiced making gifs because we will be using them for lab reports.  


>> ![IMAGES](Repository.png)
>>> The image shows a picture of my classroom repository. 

>>![IMAGES](GIF.gif)
>>> This is the sample gif that I made. 

## Tutorial 2: Python

>Q. Show the code: Starting with a = “Hello World!!!”, come up with a code snippet that will give us b = “Hello” and c = “World” and 
d = “!!!. Also, in code, check if “ello” is in a. 

>A. ![IMAGES](HelloWorld.png)
  >> ![IMAGES](HelloWorldOutput.png)
    >>> To approach this question, I knew that a = "Hello World" is a string and I could easily get a substring using square brackets. To print out b = "Hello" , I used the print function and since I know that strings index always start at 0, the number's in the bracket would be [0:5]. For the number after the :, the substring with that value will not print out, so we could think of it as being from 0 to 4. The same process also goes for c = "World" and d = "!!!" but with different index values. To check if "ello" is in a, I defined another variable, f, and did an IF loop to check if the "ello" was present. 



>Q. In the following code, what is the output of the print statement? Why doesn’t original_list = ['hi','how','are','you']?

>>A. ![IMAGES](OriginalList.png)
   > ![IMAGES](OriginalListOutput.png)
    >> original_list does not = ['hi','how','are','you'] because the code never actually changed the words in the list. The code just kept creating new lists. To get the results we want, we would want to put original_list[1:3] = ['how','are'] to change the substrings. 
 

### Challenge 2
>In this challenge, I familiarized myself with Python and the Numpy package scientific computing functions. I went through each tutorial thoroughly in order to understand and be able to complete the following questions. The tutorials and examples were extremely helpful for me to complete this challenge. 

#### Numpy Array
>>Q.Show the code: Make a Numpy Array called test_array  from a list = [0,10,4,12]. Subtract 20 from the test_array, what do you get? What is the shape of the test_array?

>>>A.  ![IMAGES](NumpyArray1.png)
    > ![IMAGES](NumpyArray1Results.png)
    >> When you subtract 20 from the test_array, 20 is subtracted from each value of the array
    >>> The shape of the array is (4,)

>>Q. Show the code: Make a 2D array of test_2D_array from [0,10,4,12]
                                                         >[1,20,3,41]
>>>A. ![IMAGES](NumpyArray2.png)
      > ![IMAGES](NumpyArray2results.png)

#### Zeros and Ones

>>Q. Make a 2D array of zeros with shape of 10x20 and then print it out.

>>> A. ![IMAGES](Zeros:Ones.png)
    > ![IMAGES](Zeros:Onesresults.png)

#### hstack and vstack

>>Q. Show the code: Out of the test_array, create the following using hstack and vstack: 

>>> A. ![IMAGES](hstack:vstack.png)
    > ![IMAGES](hstack:vstackresult.png)

#### arange

>>Q.Show the code: Using arange, make an array called arange_array1 to equal [-3, 3,9,15] and arange_array2 to equal [ -7,  -9, -11, -13, -15, -17, -19]

>>> A. ![IMAGES](arange.png)
    > ![IMAGES](arangeresults.png)

#### linspace

>>Q. Make an array called linspace_array using linspace that goes from 0 to 100 with 49 steps. 

>>>A. ![IMAGES](linspace.png)
   > ![IMAGES](linspaceresults.png)

>>Q. How do linspace and arange differ? When might you use one over the other?

>>>A. linspace and arange differ because for linspace, the values and increments are random but the end value can be determined, and for arange, you can choose the values and the increments. You might use linspace when you want to make a random graph, and arange, when you want a precise graph. 

#### indexing and slicing

>>Q. What is an array of size 3x4 that would produce the following results. Show your work on how you deduced your answer on paper or some kind of graphics:
print(e[0])     >>> [12 3 1 2]
print(e[1,0])  >>> 0
print(e[:,1])   >>> [3 0 2]
print(e[2, :2])>>> [4 2]
print(e[2, 2:])>>> [3 1] 
print(e[:,2])  >>> [1 1 3]
print(e[1,3]) >>> 2

>>> A. ![IMAGES](indexing:slicinghand.JPG)

>>Q. Show your code: Now solve the problem from the section Indexing and slicing using numpy and array assignment.

>>> A. ![IMAGES](indexingandslicing.png)
    > A. ![IMAGES](indexingandslicingresults.png)

#### Setting values of array from comma-separated values

>>Q.  Using fromstring, vstack, and a for loop, create an array of 100x4 from s: [[1,2,3,4],[1,2,3,4],[1,2,3,4]…..[1,2,3,4]]. 

>>> A. ![IMAGES](SettingValuesfromComma.png)
    >A. ![IMAGES](SettingValuesFromCommaresults.png)










