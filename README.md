# drf-uploadfile
Upload file using django basics of drf 


# Instructions
* Execute the docker build using ```docker build . -t drf:v2```
* Run docker using ```docker run -d --name drf -p 8000:8000 drf:v2 ```
* Upload file using curl or drf apis on page `http://0.0.0.0:8000/upload/api/v1/`
* You can delete the file by name using : `curl -XDELETE -L http://0.0.0.0:8000/upload/api/v1/develop/ -vv`
* TODO: Finish the file checksum for reuse, not done yet... 