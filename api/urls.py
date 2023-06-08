from api.models import CategoryResource, CourseResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')
course_resource = CourseResource()
category_resource = CategoryResource()
api.register(course_resource)
api.register(category_resource)

urlpatterns = [
    path('', include(api.urls), name='index'),

]

# api/v1/courses/       GET, POST
# api/v1/courses/1/     GET, DELETE
# api/v1/categories/    GET
# api/v1/categories/1/  GET

# For POST, DELETE add header
# Key: Authorization
# Value: ApiKey bogdan:asdhlkl2513413561
