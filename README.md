# NASA Solar image

This is a project that consist in a web spider that is constantly downloading 
an image from a NASA website url. It is designaned to run continuously during
and indefinited period of time. 

## Setting the enviorment
Before you run the script you have to create a file
called `config.ini` in the same folder of this project, and
paste the following text:
```
[SETTINGS]
download-minutes=6
image-folder-dir=/your-images/folder/
```
You have to be sure that the `image-folder-dir` actually exists, otherwise you will have to create it or 
you will get an error.

Also, you can modify the `download-minutes` image if you require it.

## Running the script
To run the script you only have to use this command:
```
> python3 main.py
```
And if you require it, you can leave it running in background typing `&` at the end like this:
```
> python3 main.py &
```
