# nested dictionaries
dictionary1 = {
    "java" : "OOPS",
    "python " : "machine learning", 
    "Studentsdata" : {
        "name" : "SOhail khan",
        "Age"  : "220",                 #nested dictionary
         90      :    "experience"   
    }
}

# printing the complete dictionaries 
print(dictionary1)

# printing the dictionary which is presetn within dictionary
print(dictionary1["Studentsdata"]) 

# printing the value inside nested dictionary
print(dictionary1["Studentsdata"]["name"])