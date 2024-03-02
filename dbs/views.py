import json
from django.http import JsonResponse
from django.views import View
from dbs.models import Author, Book
from http import HTTPStatus
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class BookCreate(View):

    def post(self, request):
        author_instance = Author.objects.create(name="james blunt")
        book_instance = Book.objects.create(
            title="second coming", author=author_instance)
        return JsonResponse({"book": book_instance.id}, status=HTTPStatus.CREATED)

    def get(self, request):
        # retrieve all books
        books = Book.objects.all()
        # serialize the books queryset to get json string
        serialized_books = serialize('json', books)
        # convert the string to python object which in theis case is a list and
        # since list is a non ordered dict we cant pass it to jsonresponse since
        # it accepts ordered dict therefore we create a dict
        parsed_books = json.loads(serialized_books)
        # paersed books is now a list of dicts

        def getOnlyRequiredFields(data):
            reqFieldsArr = []
            for dict in data:
                reqFields = {}
                reqFields["id"] = dict["pk"]
                reqFields["title"] = dict["fields"]["title"]
                reqFields["author"] = dict["fields"]["author"]
                reqFieldsArr.append(reqFields)
            return reqFieldsArr
        return JsonResponse({"books": getOnlyRequiredFields(parsed_books)}, status=HTTPStatus.OK)
