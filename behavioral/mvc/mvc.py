'''
Whenever we need to process some request and return response accordingly, this pattern is considered. Many frameworks like django implements it too.

In this pattern, we need to receive request, as soon as we get the request, we pass it to an object which controls the flow of data and dispatches the response. These are called controllers which are often class or function. We define these controller functions or classes to contol the flow the request data.

Then we need to interact with data in the control flow, for which we define models which interact with data base and functions relating to that kind are defined in the class too and controller functions can be encapsulated here. In django, models.py file generally contains the models to interact with db and serializers often have the controller functions.

Since, we need to send response data to the user, for which we use views, functions or classes, to interact with user. These are objects which recieve requests from user and send the response data accordingly.
'''