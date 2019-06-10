To deploy this proxy to apigee use the below command:

`mvn clean install -P<profile_name> -Dusername="<username>" -Dpassword="<password>"`

please understand unless there are multiple proxies to be deployed all at once the use of parent-pom is not required.
And all the functions can be moved down to child POM this helps to keep just one pom file and manage things easily.
The GOT project shows the use of parent-pom where deploying multiple proxies is required.